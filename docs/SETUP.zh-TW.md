# ARS 安裝設定

ARS 只支援 Codex。若要在多個專案使用，建議安裝 Codex plugin；也可將單一 skill 連結到專案或使用者層級的 skills 目錄。核心提示不需要 Python；選用的腳本檢查才需要。

## 最小設定

1. 安裝 Codex 並登入。
2. 使用下列其中一種方式安裝 ARS。
3. 啟動 Codex，指定 ARS skill 與模式。

## 安裝 Codex plugin

在 Codex CLI 執行：

```sh
codex plugin marketplace add valinagacevschi/academic-research-skills
codex plugin add academic-research-skills@ars
```

Codex 桌面版可在 plugin 目錄加入 `ars` marketplace，再安裝 Academic Research Skills。Plugin cache 會包含 skills 與共用參考資料，因此可從其他專案使用。

## 專案層級 skills symlink

Clone repository 後，將五個 skill 連結到專案的 `.agents/skills/`：

```sh
mkdir -p .agents/skills
for skill in deep-research academic-paper academic-paper-reviewer academic-pipeline sr-screener; do
  ln -s /path/to/academic-research-skills/$skill .agents/skills/$skill
done
```

## 使用者層級 skills symlink

使用相同連結方式，將目的目錄改成 `~/.agents/skills/`，即可在自己的多個專案使用。

## 選用 Python 工具

提示式工作流程不需要 Python。若要執行本 repository 的本機驗證腳本或選用的腳本功能，請安裝 Python 3.10 以上版本。

## 文件輸出

Markdown 不需額外軟體。DOCX 轉換需要 Pandoc；PDF 另需 Tectonic 等 LaTeX engine，請參閱 [安裝說明](https://tectonic-typesetting.github.io/en-US/install.html)。

## 專案偏好

將專案特定的常設偏好放在該專案的 `AGENTS.md`。ARS 不讀取全域偏好檔；把搜尋與納入條件放在專案中，審查時較容易確認。

## 跨模型驗證（選用）

跨模型驗證預設關閉，需明確啟用並提供非 GPT 服務的 API key。Provider 與資料流詳見[跨模型驗證說明](../shared/cross_model_verification.md)。

## 控制可用性

Plugin 與 project/user skills 的可用控制不同。依賴控制前，請先閱讀[控制可用性](CONTROL_AVAILABILITY.md)。
