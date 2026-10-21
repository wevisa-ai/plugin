---
name: o1a-criteria-drafting-and-review
description: Evaluate supporting evidence and draft O-1A Extraordinary Ability (Sciences, Education, Business, Athletics) criterion subsections, introductions, conclusions, petitioner/beneficiary sections, and itineraries using the official O-1A Criteria Prompts and Rubrics via the WeVisa API and MCP server.
---

# O-1A Criteria Drafting & Evidence Review Skill

Use this skill when preparing or auditing an **O-1A Nonimmigrant Petition** under `INA § 101(a)(15)(O)(i)` and `8 C.F.R. § 214.2(o)(3)(iii)` (Sciences, Education, Business, or Athletics).

## Governing Legal Framework
- **Threshold**: Receipt of a major, internationally recognized award (`8 C.F.R. § 214.2(o)(3)(iii)(A)`) **OR** satisfaction of at least **three (3) of the eight (8)** regulatory criteria (`8 C.F.R. § 214.2(o)(3)(iii)(B)(1)-(8)`).
- **Totality / High Standard**: Sustained national or international acclaim and placement among the small percentage who have risen to the very top of the field of endeavor.
- **Additional Required Sections**:
  - **Petitioner (`o1a_petitioner`)**: Information about the U.S. petitioner/employer or agent and the proposed role.
  - **Beneficiary (`o1a_beneficiary`)**: Educational background, career trajectory, and overview of extraordinary ability.
  - **Itinerary (`o1a_itinerary`)**: Explanation of the nature of events/activities, beginning and ending dates, and copy of itinerary under `8 C.F.R. § 214.2(o)(2)(ii)(C)`.

---

## O-1A Criterion Keys & Governing Tests

| Criterion Key | Regulatory Citation | Governing Test & Required Elements |
| :--- | :--- | :--- |
| `o1a_award` | `8 C.F.R. § 214.2(o)(3)(iii)(B)(1)` | **Nationally or Internationally Recognized Prizes or Awards**: Prove personal receipt, field nexus, awarding body reputation, award criteria, eligibility/competitiveness/selection process, and national/international significance. |
| `o1a_membership` | `8 C.F.R. § 214.2(o)(3)(iii)(B)(2)` | **Membership in Associations Requiring Outstanding Achievements**: Prove membership in a field association where admission requires outstanding achievements judged by recognized national or international experts (exclude fee-based, degree-based, or mandatory union memberships). |
| `o1a_media` | `8 C.F.R. § 214.2(o)(3)(iii)(B)(3)` | **Published Material in Professional/Major Trade Publications or Major Media**: Prove the article/broadcast is *about* the beneficiary and their work in the field, include title/date/author/translations, prove editorial independence (not paid PR), and prove outlet qualification via circulation/readership. |
| `o1a_judging` | `8 C.F.R. § 214.2(o)(3)(iii)(B)(4)` | **Participation as a Judge of the Work of Others**: Pair invitation/appointment with proof of *completed* participation (e.g., peer review logs, editor thank-you, competition judging records) in the same or an allied field. |
| `o1a_contribution` | `8 C.F.R. § 214.2(o)(3)(iii)(B)(5)` | **Original Scientific, Scholarly, or Business-Related Contributions of Major Significance**: Prove both (1) originality and personal attribution, and (2) major significance in the field beyond a single employer (widespread adoption, citations, licensing, commercial/industry impact, corroborated by independent expert letters). |
| `o1a_publication` | `8 C.F.R. § 214.2(o)(3)(iii)(B)(6)` | **Authorship of Scholarly Articles**: Prove authorship of scholarly articles reporting original research or written for learned persons in the field, published in peer-reviewed journals, major trade publications, or other major media prior to filing. |
| `o1a_role` | `8 C.F.R. § 214.2(o)(3)(iii)(B)(7)` | **Employment in a Critical or Essential Capacity for Distinguished Organizations**: Prove (1) the role was critical (significant importance to organizational outcomes) or leading/essential, and (2) the exact organization or establishment has a distinguished reputation supported by independent evidence. |
| `o1a_salary` | `8 C.F.R. § 214.2(o)(3)(iii)(B)(8)` | **High Salary or Other Remuneration**: Prove past or credible prospective compensation for services via contracts/W-2s/tax records, and compare apples-to-apples (base-to-base or total-to-total) against matched SOC code, geography, and period wage benchmarks (e.g., BLS OEWS / FLC Level IV 90th percentile). |

---

## How to Use via MCP Tools or REST API

All tools and endpoints accept optional `custom_prompt` (`str`) and `additional_prompts` (`str | List[str]`) to inject firm-specific or case-specific instructions into the server-side context.

### 1. List O-1A Criteria
- **MCP Tool**: `tool_list_criteria(visa_type="o1-a")`
- **REST API**: `GET /api/v1/skills/criteria?visa_type=o1-a`

### 2. Evaluate Documents Against the Official Rubric
- **MCP Tool**: `tool_evaluate_criterion_evidence(criterion_key="o1a_contribution", beneficiary_name="...", documents=[...], evidence_title="...", custom_prompt=..., additional_prompts=...)`
- **REST API**: `POST /api/v1/skills/review/evaluate-criterion`
- **Returns**: `overall_rating` (`STRONG`, `MEDIUM`, `WEAK`, `DO_NOT_CLAIM`), `element_findings`, `claim_to_evidence_table`, `rfe_and_denial_risks`, `missing_evidence`, and `review_markdown`.

### 3. Draft a Single Accomplishment Subsection or Full Criterion Section
- **Draft Single Subsection**:
  - **MCP Tool**: `tool_draft_evidence_subsection(criterion_key="o1a_role", beneficiary_name="...", evidence_title="...", documents=[...], custom_prompt=..., additional_prompts=...)`
  - **REST API**: `POST /api/v1/skills/draft/subsection`
  - Returns `section_text` (100% supportive USCIS-ready legal prose) and `evidence_review` (internal attorney audit).
- **Draft Complete Criterion Section (Intro + Subsections + Conclusion)**:
  - **MCP Tool**: `tool_draft_criterion_section(criterion_key="o1a_role", beneficiary_name="...", evidence_items=[{"title": "...", "documents": [...]}], custom_prompt=..., additional_prompts=...)`
  - **REST API**: `POST /api/v1/skills/draft/criterion-section`
- **Draft Petitioner, Beneficiary, or Itinerary Sections**:
  - **MCP Tools**: `tool_draft_petitioner_section`, `tool_draft_beneficiary_section`, `tool_draft_itinerary_section`
  - **REST API**: `POST /api/v1/skills/draft/petitioner`, `POST /api/v1/skills/draft/beneficiary`, `POST /api/v1/skills/draft/itinerary`
