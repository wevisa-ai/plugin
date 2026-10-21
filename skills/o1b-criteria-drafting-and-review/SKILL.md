---
name: o1b-criteria-drafting-and-review
description: Evaluate supporting evidence and draft O-1B Extraordinary Ability in the Arts and Extraordinary Achievement in Motion Picture or Television (MPTV) criterion sections using the official O-1B Criteria Prompts and Rubrics via the WeVisa API and MCP server.
---

# O-1B Criteria Drafting & Evidence Review Skill (Arts & MPTV)

Use this skill when preparing or auditing an **O-1B Nonimmigrant Petition** under `INA § 101(a)(15)(O)(i)` and `8 C.F.R. § 214.2(o)(3)(iv)` (Arts) or `8 C.F.R. § 214.2(o)(3)(v)` (Motion Picture or Television — MPTV).

## Governing Legal Framework
- **O-1B Arts Standard**: "Distinction" — a high level of achievement in the field of arts evidenced by a degree of skill and recognition substantially above that ordinarily encountered to the extent that a person described as prominent is renowned, leading, or well-known in the field of arts. Comparable evidence (`8 C.F.R. § 214.2(o)(3)(iv)(C)`) is available for O-1B Arts only when a criterion does not readily apply.
- **O-1B MPTV Standard**: "A demonstrated record of extraordinary achievement" in motion picture and/or television productions such that the beneficiary is recognized as having a high level of accomplishment significantly above that ordinarily encountered. **Important**: Comparable evidence is **not** available for MPTV petitions.
- **Threshold**: Nomination for or receipt of a significant national or international award (`o1b_award`, e.g., Academy Award, Emmy, Grammy, Director's Guild Award) **OR** satisfaction of at least **three (3) of the six (6)** regulatory criteria.

---

## O-1B Criterion Keys & Governing Tests

| Criterion Key | Regulatory Citation | Governing Test & Required Elements |
| :--- | :--- | :--- |
| `o1b_award` | `8 C.F.R. § 214.2(o)(3)(iv)(A) / (v)(A)` | **Significant National or Internationally Recognized Prize or Award (or Nomination)**: Alternative one-time eligibility route. Prove personal receipt or nomination, category stature comparable to an Oscar/Emmy/Grammy/DGA Award, and national/international significance. |
| `o1b_contribution` | `8 C.F.R. § 214.2(o)(3)(iv)(B)(1) / (v)(B)(1)` | **Lead or Starring Participant in Distinguished Productions or Events**: Prove *both* past and upcoming/prospective lead or starring services in productions or events that have a distinguished reputation (evidenced by critical reviews, advertisements, publicity releases, contracts, or endorsements). Keep productions/events distinct from organizations. |
| `o1b_media` | `8 C.F.R. § 214.2(o)(3)(iv)(B)(2) / (v)(B)(2)` | **National or International Recognition for Achievements Through Critical Reviews or Published Material**: Prove published material by or about the beneficiary in major newspapers, trade journals, magazines, or other publications showing national/international recognition of achievements. |
| `o1b_role` | `8 C.F.R. § 214.2(o)(3)(iv)(B)(3) / (v)(B)(3)` | **Lead, Starring, or Critical Role for Distinguished Organizations and Establishments**: Prove *both* past and upcoming/prospective lead, starring, or critical roles for organizations or establishments that have a distinguished reputation. |
| `o1b_commercial_success` | `8 C.F.R. § 214.2(o)(3)(iv)(B)(4) / (v)(B)(4)` | **Record of Major Commercial or Critically Acclaimed Successes**: Prove commercial or critical success through box office receipts, motion picture/television ratings, chart standings, or other occupational achievements reported in trade journals or major newspapers. |
| `o1b_reputation` | `8 C.F.R. § 214.2(o)(3)(iv)(B)(5) / (v)(B)(5)` | **Significant Recognition for Achievements from Organizations, Critics, Government Agencies, or Recognized Experts**: Prove substantive recognition through detailed testimonials that clearly establish the author's authority, expertise, and basis of knowledge of the beneficiary's achievements. |
| `o1b_salary` | `8 C.F.R. § 214.2(o)(3)(iv)(B)(6) / (v)(B)(6)` | **High Salary or Other Substantial Remuneration**: Prove past or contracted future high salary or substantial remuneration in relation to others in the field using contracts, deal memos, pay records, and matched guild/industry/geographic wage comparators. |

---

## How to Use via MCP Tools or REST API

All tools and endpoints accept optional `custom_prompt` (`str`) and `additional_prompts` (`str | List[str]`) to inject firm-specific or case-specific instructions into the server-side context.

1. **Inspect O-1B Criteria**:
   - **MCP**: `tool_list_criteria(visa_type="o1-b")`
   - **REST API**: `GET /api/v1/skills/criteria?visa_type=o1-b`
2. **Evaluate Evidence Against O-1B Rubrics**:
   - **MCP**: `tool_evaluate_criterion_evidence(criterion_key="o1b_contribution", beneficiary_name="...", documents=[...], custom_prompt=..., additional_prompts=...)`
   - **REST API**: `POST /api/v1/skills/review/evaluate-criterion`
3. **Draft O-1B Subsections, Criteria Sections, Itinerary & Full Letter**:
   - **MCP**: `tool_draft_evidence_subsection`, `tool_draft_criterion_section`, `tool_draft_itinerary_section`, `tool_draft_full_attorney_letter`
   - **REST API**: `POST /api/v1/skills/draft/subsection`, `POST /api/v1/skills/draft/criterion-section`, `POST /api/v1/skills/draft/itinerary`, `POST /api/v1/skills/draft/full-letter`
