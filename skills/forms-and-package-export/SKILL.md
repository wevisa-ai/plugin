---
name: forms-and-package-export
description: Inspect USCIS form schemas (I-129, I-907, G-1450), auto-fill form questionnaire answers from supporting documents, generate filled USCIS PDF forms, and export drafted petition letters and reference letters to Word (.docx) and PDF.
---

# USCIS Forms & Filing Package Export Skill

Use this skill to inspect and auto-fill USCIS forms (`Form I-129`, `Form I-907`, `Form G-1450`) from client documents and to export finalized attorney petition letters, criterion sections, and reference letters to Microsoft Word (`.docx`) and styled PDF files.

## 1. USCIS Form Inspection, Auto-Filling & PDF Generation

### Supported Forms
- **`i-129`**: Form I-129, Petition for a Nonimmigrant Worker (including the O and P Classifications Supplement) for O-1A and O-1B petitions.
- **`i-907`**: Form I-907, Request for Premium Processing Service.
- **`g-1450`**: Form G-1450, Authorization for Credit Card Transactions.

### Step-by-Step Form Workflow
1. **List Supported Forms**:
   - **MCP**: `tool_list_uscis_forms()`
   - **REST API**: `GET /api/v1/skills/forms`
2. **Inspect Questionnaire Fields or Raw PDF AcroForm Schema**:
   - **Questionnaire Questions** (`Preliminaries`, `Petitioner`, `Beneficiary`, `Petition`, `Position`):
     - **MCP**: `tool_get_uscis_form_questions(form_name="i-129", section="Beneficiary")`
     - **REST API**: `GET /api/v1/skills/forms/i-129/questions?section=Beneficiary`
   - **PDF Field Schema**:
     - **MCP**: `tool_get_uscis_form_schema(form_name="i-129")`
     - **REST API**: `GET /api/v1/skills/forms/i-129/schema`
3. **Auto-Fill Form Data from Supporting Documents**:
   - **MCP**: `tool_autofill_uscis_form(documents=[...], existing_data={...}, sections=["Preliminaries", "Petitioner", "Beneficiary", "Petition", "Position"])`
   - **REST API**: `POST /api/v1/skills/forms/autofill`
   - Extracts answers directly from the client's passport, I-94, visa stamps, CV, employer letter, and corporate documents without fabricating missing values.
4. **Generate Filled Form PDF (`I-129` + optional `I-907`)**:
   - **MCP**: `tool_fill_uscis_form_pdf(form_data={...}, include_i907=True, output_path="...", return_base64=False)`
   - **REST API**: `POST /api/v1/skills/forms/fill-pdf`
   - Populates the official AcroForm fields, extracts the relevant I-129 base and O/P Supplement pages, optionally appends filled Form I-907 when Premium Processing (`include_i907=True` or `preliminaries_q2="yes"`) is requested, and returns `download_url` (`https://wevisa.ai/api/v1/skills/files/download/{filename}`), `curl_download_command`, and optional `file_base64` so the agent can save the PDF directly into the local working directory.

---

## 2. Exporting Drafts to Word (`.docx`) and Styled PDF

- **Export Markdown to Microsoft Word (`.docx`)**:
  - **MCP**: `tool_export_draft_to_docx(markdown_text="...", output_path="...", title="EB-1A Petition Letter", return_base64=False)`
  - **REST API**: `POST /api/v1/skills/export/docx`
  - Returns `download_url`, `curl_download_command`, and optional `file_base64` to save the `.docx` locally.
- **Export Markdown to Styled PDF**:
  - **MCP**: `tool_export_draft_to_pdf(markdown_text="...", output_path="...", return_base64=False)`
  - **REST API**: `POST /api/v1/skills/export/pdf`
  - Returns `download_url`, `curl_download_command`, and optional `file_base64` to save the `.pdf` locally.
