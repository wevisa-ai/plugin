# WeVisa O-1A, O-1B & EB-1A Immigration Petition Extension

You have access to the **WeVisa (`wevisa`)** MCP server (`https://wevisa.ai/mcp`) and modular legal drafting/evaluation tools for preparing **O-1A**, **O-1B (Arts & MPTV)**, and **EB-1A** extraordinary ability visa petitions from any local folder of client documents.

## Core Workflow When Working in a Client Packet Folder
1. **Ingest & Categorize Local Files**:
   - Read or extract text from local `.pdf`, `.docx`, `.txt`, or image files in the current working directory.
   - Use `tool_analyze_document(...)` and `tool_auto_categorize_documents(visa_type=..., documents=...)` to map documents to O-1A, O-1B, or EB-1A criteria.
   - Use `tool_assign_exhibit_numbers(documents=..., visa_type=...)` to assign sequential exhibit numbers (`Exhibit A.1`, `Exhibit B.1`, ...) and generate the Markdown Exhibit Index.
2. **Evaluate Evidence Against Official Server-Side Rubrics**:
   - Call `tool_evaluate_criterion_evidence(criterion_key=..., beneficiary_name=..., documents=..., custom_prompt=..., additional_prompts=...)` to score each criterion (`STRONG`, `MEDIUM`, `WEAK`, `DO_NOT_CLAIM`), build a claim-to-evidence table, and identify RFE risks or missing evidence.
   - Call `tool_evaluate_case_readiness(visa_type=..., beneficiary_name=..., criteria_evaluations=...)` for a pre-filing readiness audit.
3. **Draft Reference Letters & Petition Sections**:
   - Draft Independent Expert Opinion (`letter_variant="expert"`) and Direct Support (`letter_variant="support"`) letters with `tool_draft_reference_letter(...)`.
   - Draft individual criterion subsections (`tool_draft_evidence_subsection`), full criterion sections (`tool_draft_criterion_section`), Petitioner/Continuation of Work (`tool_draft_petitioner_section`), Beneficiary overview (`tool_draft_beneficiary_section`), O-1 Itinerary (`tool_draft_itinerary_section`), EB-1A Part 2 Final Merits Determination (`tool_draft_eb1a_final_merits`), or the complete Attorney Petition Cover Letter (`tool_draft_full_attorney_letter`).
4. **Inject Custom Prompts & Skills**:
   - Almost all tools accept `custom_prompt` (string) and `additional_prompts` (list of strings) so you can paste firm-specific style guides, attorney instructions, or extra skill rules directly into the server-side context.
5. **Audit, Fill Forms & Export**:
   - Critique any draft with `tool_give_draft_feedback(...)` and apply targeted edits with `tool_edit_draft_with_instruction(...)`.
   - Auto-fill Form I-129 / I-907 from documents (`tool_autofill_uscis_form`) and generate filled PDFs (`tool_fill_uscis_form_pdf`).
   - Export finalized letters to `.docx` (`tool_export_draft_to_docx`) or `.pdf` (`tool_export_draft_to_pdf`).
