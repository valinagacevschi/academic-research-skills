# Evidence data

Each JSON file in this directory uses `{"schema_version":"ro-overlay-evidence-rows/1.0","rows":[...]}`. Every row follows `../schemas/evidence_row.schema.json` and records one encoded value with its source, evidence tag, verification date, edition when applicable, and review window. Only primary evidence may drive a fact check; secondary evidence is advisory, and recalled or unreachable values cannot be encoded. Values become advisory after their review window expires. S2 adds the verified data rows.
