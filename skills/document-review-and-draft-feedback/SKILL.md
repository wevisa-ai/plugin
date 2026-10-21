---
name: document-review-and-draft-feedback
description: Extract, categorize, and assign exhibit numbers to case documents; evaluate criterion evidence against official USCIS rubrics; critique and refine petition and reference letter drafts; and run pre-filing case readiness audits for O-1A, O-1B, and EB-1A petitions.
---

# Document Review, Rubric Evaluation & Draft Feedback Skill

Use this skill to ingest client documents, organize exhibit indices, audit evidence against the official USCIS evaluation rubrics, give line-level legal feedback on drafts, and assess overall case readiness before filing.

## Capabilities & Modular Functions

### 1. Document Extraction, Categorization & Exhibit Numbering
- **Extract Document Text**:
  - **MCP**: `tool_extract_document(file_base64="...", filename="...", use_ocr=False)` (or `file_path="..."` when local)
  - **REST API**: `POST /api/v1/skills/documents/extract` or multipart `POST /api/v1/skills/documents/upload-extract` (`curl -sSL -X POST https://wevisa.ai/api/v1/skills/documents/upload-extract -F "file=@document.pdf"`)
  - Supports `.pdf`, `.docx`, `.txt`, `.md`, `.csv`, `.html`, and images (`.png`, `.jpg`).
- **Analyze & Categorize Single Document**:
  - **MCP**: `tool_analyze_document(text="...", filename="...", visa_type="eb1-a")`
  - **REST API**: `POST /api/v1/skills/documents/analyze`
  - Generates a clean document title, summary description, and suggested `criterion_key`.
- **Map Documents Across Criteria & Subsections**:
  - **MCP**: `tool_suggest_documents_for_criterion(criterion_key="...", documents=[...])` or `tool_auto_categorize_documents(visa_type="...", documents=[...])`
  - **REST API**: `POST /api/v1/skills/documents/suggest-for-criterion` or `POST /api/v1/skills/documents/auto-categorize`
- **Assign Exhibit Numbers & Generate Exhibit Index**:
  - **MCP**: `tool_assign_exhibit_numbers(documents=[...], visa_type="eb1-a")`
  - **REST API**: `POST /api/v1/skills/documents/assign-exhibits`
  - Produces sequential alphanumeric exhibit tags (`A.1`, `A.2`, `B.1`, ...) ordered by canonical petition sections (`Petitioner`, `Beneficiary`, then numbered criteria) and a Markdown Exhibit Index.

### 2. Rubric-Based Criterion Evidence Review
- **Evaluate Documents for a Criterion**:
  - **MCP**: `tool_evaluate_criterion_evidence(criterion_key="...", beneficiary_name="...", documents=[...], evidence_title="...")`
  - **REST API**: `POST /api/v1/skills/review/evaluate-criterion`
  - Evaluates the evidence against the server-side legal rubric (`O-1A`, `O-1B`, or `EB-1A`) and returns:
    - `overall_rating`: `"STRONG"`, `"MEDIUM"`, `"WEAK"`, or `"DO_NOT_CLAIM"`
    - `element_findings`: Element-by-element assessment (`SUPPORTED`, `PARTIALLY_SUPPORTED`, `MISSING`) with exhibit citations
    - `claim_to_evidence_table`: Structured proposition-to-exhibit traceability matrix
    - `rfe_and_denial_risks`: Specific RFE triggers identified in the record
    - `missing_evidence`: Prioritized documentary requests for the client/counsel
    - `review_markdown`: Full attorney audit memo

### 3. Legal & Editorial Feedback on Drafts
- **Critique Any Draft Section**:
  - **MCP**: `tool_give_draft_feedback(draft_text="...", section_type="criterion_section", visa_type="eb1-a", criterion_key="eb1a_contribution", documents=[...], instructions="...")`
  - **REST API**: `POST /api/v1/skills/review/feedback`
  - Audits the draft for legal element coverage, supportive advocacy tone, prohibited marketing hyperbole (*"groundbreaking"*, *"world-renowned"*), exhibit citation accuracy, and Step One vs. Step Two separation.
  - Returns `overall_assessment` (`FILING_READY`, `NEEDS_MINOR_REVISION`, `NEEDS_MAJOR_REVISION`), `compliance_issues`, `unsupported_or_hyperbolic_claims`, and `suggested_edits`.
- **Apply Targeted Instruction-Based Edits or Harmonize Sections**:
  - **MCP**: `tool_edit_draft_with_instruction(highlighted_text="...", instruction="...", context="...")` and `tool_harmonize_letter_section(...)`
  - **REST API**: `POST /api/v1/skills/draft/edit-text` and `POST /api/v1/skills/draft/harmonize-section`

### 4. Holistic Pre-Filing Case Readiness Audit
- **Evaluate Case Readiness**:
  - **MCP**: `tool_evaluate_case_readiness(visa_type="eb1-a", beneficiary_name="...", criteria_evaluations=[...], field_of_endeavor="...")`
  - **REST API**: `POST /api/v1/skills/review/case-readiness`
  - Evaluates whether the case meets the 3-criterion threshold, recommends which criteria to lead with vs. drop/corroborate, assesses *Kazarian* Step Two / Totality outlook, and lists top RFE risks and priority action items.
