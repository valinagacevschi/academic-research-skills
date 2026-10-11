#!/usr/bin/env python3
"""Run the overlay plugin evals with the Codex CLI.

Each case runs in an empty workspace with the ARS plugin installed from this
repository (local marketplace), exactly as a user installs it. The respiratory
layer is on by default, so the prompts do not mention it. `codex exec` answers
the case prompt in a read-only sandbox. Graders:

- regex: evaluated in code against the final reply;
- tool_used (activation): a shell command in the agent run read the
  installed plugin's ACTIVATE.md and its output contains the file's first
  heading;
- llm: majority of independent `codex exec` judge votes (default 3).

Every Codex call runs with an isolated CODEX_HOME holding only a symlink to
the user's auth.json, so user config, hooks, global AGENTS.md, agent roles and
MCP servers do not leak in. Model and reasoning effort are pinned and web
search is disabled. Results go to results/codex-<UTC timestamp>/ (gitignored).

Usage (from the repository root):
    uv run --no-project --python 3.12 --with pyyaml python \
        overlays/ro-respiratory-medicine/plugin-evals/run_codex.py
"""
import argparse
import concurrent.futures as cf
import datetime as dt
import glob
import json
import os
import re
import shutil
import subprocess
import tempfile

import yaml

SUITE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(SUITE, "..", "..", ".."))
ACTIVATE_HEADING = "# Romanian respiratory-medicine overlay instructions"
JUDGE = """You are grading an AI assistant's reply against one criterion. You have no tools; judge only the text below.

<criterion>
{c}
</criterion>

<user_prompt>
{p}
</user_prompt>

<assistant_reply>
{r}
</assistant_reply>

Reason briefly, quoting evidence, then end with exactly one final line: VERDICT: PASS or VERDICT: FAIL"""


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if m is None:
        raise SystemExit(f"{path}: missing frontmatter")
    return yaml.safe_load(m.group(1)), m.group(2).strip()


class Runner:
    def __init__(self, args, out):
        self.args, self.out = args, out
        self.auth = os.path.join(os.environ.get("CODEX_HOME", os.path.expanduser("~/.codex")), "auth.json")
        if not os.path.exists(self.auth):
            raise SystemExit(f"Codex is not logged in: {self.auth} not found")

    def install_plugin(self, home):
        env = {**os.environ, "CODEX_HOME": home}
        for cmd in (["codex", "plugin", "marketplace", "add", REPO],
                    ["codex", "plugin", "add", "academic-research-skills@ars"]):
            subprocess.run(cmd, check=True, capture_output=True, text=True, env=env,
                           stdin=subprocess.DEVNULL, timeout=120)

    def codex(self, prompt, cwd, tag, plugin=False):
        home = tempfile.mkdtemp(prefix="codex-home-")
        os.symlink(self.auth, os.path.join(home, "auth.json"))
        if plugin:
            self.install_plugin(home)
        last = os.path.join(self.out, f"{tag}.last.md")
        try:
            p = subprocess.run(
                ["codex", "exec", "--json", "--ephemeral", "--skip-git-repo-check",
                 "-m", self.args.model, "-c", f'model_reasoning_effort="{self.args.effort}"',
                 "-c", 'web_search="disabled"', "-s", "read-only", "-C", cwd, "-o", last, prompt],
                capture_output=True, text=True, timeout=900, stdin=subprocess.DEVNULL,
                env={**os.environ, "CODEX_HOME": home})
        finally:
            shutil.rmtree(home, ignore_errors=True)
        with open(os.path.join(self.out, f"{tag}.events.jsonl"), "w", encoding="utf-8") as f:
            f.write(p.stdout)
        if p.returncode:
            with open(os.path.join(self.out, f"{tag}.stderr"), "w", encoding="utf-8") as f:
                f.write(p.stderr)
        reply = open(last, encoding="utf-8").read() if os.path.exists(last) else ""
        return p.returncode, reply, p.stdout

    def judge(self, criteria, prompt, reply, tag):
        cwd = tempfile.mkdtemp(prefix="judge-")
        try:
            _, out, _ = self.codex(JUDGE.format(c=criteria, p=prompt, r=reply), cwd, tag)
        finally:
            shutil.rmtree(cwd, ignore_errors=True)
        verdicts = re.findall(r"VERDICT:\s*\**\s*(PASS|FAIL)", out)
        return (verdicts[-1] == "PASS") if verdicts else None

    def run_case(self, case_dir):
        name = os.path.basename(case_dir.rstrip("/"))
        case = yaml.safe_load(open(os.path.join(case_dir, "case.yaml"), encoding="utf-8"))
        prompt = case["execution"]["prompt"]
        ws = tempfile.mkdtemp(prefix=f"ws-{name}-")
        try:
            code, reply, events = self.codex(prompt, ws, f"{name}.agent", plugin=True)
        finally:
            shutil.rmtree(ws, ignore_errors=True)
        graders, pending = [], []
        with cf.ThreadPoolExecutor(6) as ex:
            for path in sorted(glob.glob(os.path.join(case_dir, "graders", "*.md"))):
                meta, body = frontmatter(path)
                gname = os.path.basename(path)[:-3]
                kind = meta["type"]
                if kind == "regex":
                    flags = re.I if "i" in str(meta.get("flags", "")) else 0
                    hit = re.search(body, reply, flags) is not None
                    graders.append({"grader": gname, "type": kind,
                                    "passed": hit if meta["match"] == "contains" else not hit})
                elif kind == "tool_used":
                    graders.append({"grader": gname, "type": kind, "passed": activation_read(events)})
                elif kind == "llm":
                    votes = [ex.submit(self.judge, body, prompt, reply, f"{name}.{gname}.v{i}")
                             for i in range(self.args.votes)]
                    pending.append((gname, votes))
                else:
                    raise SystemExit(f"{name}/{gname}: unsupported grader type {kind!r}")
            for gname, votes in pending:
                v = [f.result() for f in votes]
                graders.append({"grader": gname, "type": "llm", "votes": v,
                                "passed": sum(x is True for x in v) * 2 > len(v)})
        ok = sum(g["passed"] for g in graders)
        return {"case": name, "agent_exit": code, "score": ok / len(graders),
                "passed": ok == len(graders) and code == 0, "graders": graders}


def activation_read(events):
    for line in events.splitlines():
        try:
            e = json.loads(line)
        except ValueError:
            continue
        item = e.get("item") or {}
        if (e.get("type") == "item.completed" and item.get("type") == "command_execution"
                and "ro-respiratory-medicine/ACTIVATE.md" in item.get("command", "")
                and ACTIVATE_HEADING in item.get("aggregated_output", "")):
            return True
    return False


def main():
    ap = argparse.ArgumentParser(description="Run the overlay plugin evals with the Codex CLI.")
    ap.add_argument("--model", default="gpt-6-luna")
    ap.add_argument("--effort", default="medium")
    ap.add_argument("--votes", type=int, default=3)
    ap.add_argument("--case", default="", help="substring filter on case directory names")
    ap.add_argument("-j", "--concurrency", type=int, default=3)
    args = ap.parse_args()
    started = dt.datetime.now(dt.timezone.utc)
    out = os.path.join(SUITE, "results", "codex-" + started.strftime("%Y-%m-%dT%H-%M-%SZ"))
    os.makedirs(out)
    cases = [c for c in sorted(glob.glob(os.path.join(SUITE, "[0-9]*/"))) if args.case in c]
    runner = Runner(args, out)
    with cf.ThreadPoolExecutor(args.concurrency) as ex:
        results = list(ex.map(runner.run_case, cases))
    version = subprocess.run(["codex", "--version"], capture_output=True, text=True).stdout.strip()
    summary = {"started_at": started.isoformat(), "codex_version": version, "model": args.model,
               "reasoning_effort": args.effort, "judge_votes": args.votes, "web_search": "disabled",
               "cases_passed": sum(r["passed"] for r in results), "cases_total": len(results),
               "cases": results}
    with open(os.path.join(out, "results.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=1, ensure_ascii=False)
    print(f"{version} model={args.model} effort={args.effort} votes={args.votes} -> {out}")
    for r in results:
        print(f"== {r['case']} score={r['score']:.2f} passed={r['passed']} {r.get('error', '')}")
        for g in r.get("graders", []):
            extra = f" votes={g['votes']}" if "votes" in g else ""
            print(f"   {'PASS' if g['passed'] else 'FAIL'} {g['grader']}{extra}")
    print(f"{summary['cases_passed']}/{summary['cases_total']} cases passed")
    raise SystemExit(0 if summary["cases_passed"] == summary["cases_total"] else 1)


if __name__ == "__main__":
    main()
