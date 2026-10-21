# WeVisa O-1A, O-1B & EB-1A Immigration Petition Plugin Rules

When preparing, reviewing, or auditing an **O-1A**, **O-1B (Arts or MPTV)**, or **EB-1A** extraordinary ability visa application in any folder:

1. **Use the `wevisa` MCP Server Tools**:
   - Read local client files (`.pdf`, `.docx`, `.txt`, images) either using your local file tools or by passing `file_base64` and `filename` to `tool_extract_document` (or `POST https://wevisa.ai/api/v1/skills/documents/upload-extract`).
   - Categorize and group documents with `tool_analyze_document`, `tool_suggest_documents_for_criterion`, and `tool_auto_categorize_documents`.
   - Assign sequential exhibit numbers (`Exhibit A.1`, `Exhibit B.1`, ...) with `tool_assign_exhibit_numbers`.
   - When generating `.docx` or `.pdf` files (`tool_fill_uscis_form_pdf`, `tool_export_draft_to_docx`, `tool_export_draft_to_pdf`), use the returned `download_url` / `curl_download_command` (or `return_base64=True`) to save the generated file into the user's local working directory.
2. **Evaluate Evidence Before Drafting**:
   - Always evaluate candidate criteria using `tool_evaluate_criterion_evidence` and audit holistic case readiness using `tool_evaluate_case_readiness`.
   - Never fabricate metrics, citations, or exhibits not present in the source documents.
3. **Maintain Strict Separation Between Filing Text and Internal Review**:
   - All USCIS-facing narrative outputs (`section_text`, `intro_text`, `conclusion_text`, `full_letter_markdown`, `reference_letter_text`) must be 100% supportive legal advocacy without negative self-assessments or internal flags.
   - Keep all gap analysis, RFE warnings, and missing document requests inside `evidence_review` or internal evaluation reports.
4. **Custom Prompt & Skill Injection**:
   - Pass `custom_prompt` (string) or `additional_prompts` (list of strings) into any evaluation, drafting, feedback, or form-autofill tool to inject firm-specific style guides, attorney instructions, or extra skill rules into the server-side execution context.
