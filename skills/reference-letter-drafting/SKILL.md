---
name: reference-letter-drafting
description: Select relevant supporting documents and draft Independent Expert Opinion Letters and Direct Support (Witness) Reference Letters for O-1A, O-1B, and EB-1A visa petitions via the WeVisa API and MCP server.
---

# Reference Letter Drafting Skill (Expert Opinion & Direct Support Letters)

Use this skill when preparing testimonial letters (`Expert Opinion` or `Direct Support`) for **O-1A**, **O-1B**, or **EB-1A** petitions.

## Two Distinct Testimonial Archetypes

1. **Independent Expert Opinion Letter (`letter_variant="expert"`)**:
   - **Who**: An independent industry or academic authority who has not worked directly with or supervised the beneficiary, but who is qualified to evaluate the beneficiary's work against field-wide standards.
   - **Legal Purpose**: Establishes the prior state of the art, what the beneficiary originated, how the expert knows of the work (through publications, open-source/industry adoption, products, or public recognition), and why the work is of major significance (`o1a_contribution` / `eb1a_contribution`) or recognized distinction (`o1b_reputation`).
2. **Direct Support / Witness Letter (`letter_variant="support"`)**:
   - **Who**: A supervisor, C-suite executive, co-founder, collaborator, client, investor, or event organizer with direct personal knowledge of the beneficiary's work.
   - **Legal Purpose**: Provides first-hand factual testimony verifying the beneficiary's specific responsibilities, decision-making authority, individual attribution (separating the beneficiary's work from team/company results), and quantified outcomes (`o1a_role` / `o1b_role` / `eb1a_role` and `o1a_contribution` / `eb1a_contribution`).

## Core Drafting Rules Enforced by This Skill
- **No Prohibited Openings**: Never begin with *"I am writing to..."*, *"It is with great pleasure..."*, *"I am honored to..."*, or *"I offer my strongest recommendation..."*. Open directly with the recommender's authority and credentials.
- **No Prohibited Closings**: Avoid restating legal boilerplate or phrases like *"without reservation"* or *"wholeheartedly"*.
- **No Unbacked Superlatives**: Avoid *"unprecedented"*, *"world-class"*, *"visionary"*, *"genius"*, or *"one of a kind"*.
- **Nine-Part Narrative Arc**:
  1. Recommender's credentials and standing in the field
  2. Basis of knowledge / relationship to the beneficiary's work
  3. Concrete analysis of 1–3 specific projects/achievements
  4. Field-level impact or organizational outcome attribution
  5. Qualitative peer comparison
  6. Closing endorsement & contact signature block

---

## How to Use via MCP Tools or REST API

### 1. Suggest Supporting Documents for a Recommender
- **MCP Tool**:
  ```json
  {
    "visa_type": "eb1-a",
    "beneficiary_name": "Dr. Jane Doe",
    "reference_name": "Prof. Alan Turing",
    "letter_variant": "expert",
    "documents": [
      {"id": 1, "title": "SparseFlow Paper", "description": "Nature Machine Intelligence paper"},
      {"id": 2, "title": "GitHub Adoption Stats", "description": "4,500 stars and third-party PRs"}
    ]
  }
  ```
  Call `tool_suggest_reference_letter_documents`.
- **REST API**: `POST /api/v1/skills/reference-letters/suggest-documents`

### 2. Draft the Reference Letter
- **MCP Tool**: Call `tool_draft_reference_letter` with:
  - `visa_type`: `"o1-a"`, `"o1-b"`, or `"eb1-a"`
  - `beneficiary_name`, `reference_name`, `letter_variant` (`"expert"` or `"support"`)
  - `recommender_title`, `recommender_organization`, `recommender_credentials`, `recommender_credibility`
  - `relationship`, `how_expert_knows_work`, `observed_projects`, `points`
  - `documents`: List of selected supporting documents
- **REST API**: `POST /api/v1/skills/reference-letters/draft`

### 3. Review or Export the Reference Letter
- Audit the draft for prohibited openings/superlatives with `tool_give_draft_feedback(draft_text=..., section_type="reference_letter", visa_type=...)` (`POST /api/v1/skills/review/feedback`).
- Export to Word (`.docx`) or PDF with `tool_export_draft_to_docx` / `tool_export_draft_to_pdf` (`POST /api/v1/skills/export/docx` or `/pdf`).
