---
name: eb1a-criteria-and-final-merits
description: Evaluate supporting evidence and draft EB-1A Extraordinary Ability (Form I-140) Step One criteria sections, Part 2 Final Merits Determination (Kazarian Step Two), and statutory Continuation of Work / Prospective Benefit sections using the official EB-1A Criteria Prompts and Rubrics via the WeVisa API and MCP server.
---

# EB-1A Criteria & Final Merits Determination Skill (*Kazarian* Two-Step Framework)

Use this skill when preparing or auditing an **EB-1A Immigrant Petition for Alien Worker of Extraordinary Ability (Form I-140)** under `INA § 203(b)(1)(A)`, `8 C.F.R. § 204.5(h)`, *Kazarian v. USCIS*, 596 F.3d 1115 (9th Cir. 2010), and `USCIS Policy Manual, Vol. 6, Pt. F, Ch. 2`.

## Governing Two-Step Adjudication Framework & Statutory Prongs
1. **Step One — Threshold Evidentiary Criteria (`8 C.F.R. § 204.5(h)(3)`)**:
   - Demonstrate either a **One-Time Achievement** (a major, internationally recognized award such as a Nobel Prize, Oscar, or Olympic Medal) **OR** satisfy the plain regulatory text of at least **three (3) of the ten (10)** criteria at `8 C.F.R. § 204.5(h)(3)(i)-(x)` (or comparable evidence under `8 C.F.R. § 204.5(h)(4)` when a criterion does not readily apply to the beneficiary's occupation).
   - **Rule**: Keep Step One strictly focused on the plain regulatory elements of each criterion; do not import Step Two totality requirements into Step One, and reserve comparative elite-standing analysis for Step Two.
2. **Step Two — Final Merits Determination (`eb1a_final_merits`)**:
   - Evaluate the totality of the evidence under the preponderance of the evidence standard (*Matter of Chawathe*, 25 I&N Dec. 369 (AAO 2010)) to prove:
     - **Sustained national or international acclaim** maintained over time up to the filing snapshot;
     - **Achievements recognized in the field through extensive documentation**; and
     - **Placement among the small percentage who have risen to the very top of the defined field**.
3. **Statutory Continuation of Work & Substantial Prospective Benefit (`eb1a_petitioner`)**:
   - Under `INA § 203(b)(1)(A)(ii)-(iii)` and `8 C.F.R. § 204.5(h)(5)`, prove through contracts, employer letters, or a detailed personal statement that the beneficiary seeks to enter the United States to continue work in the area of extraordinary ability and that their entry will substantially benefit prospectively the United States.

---

## EB-1A Criterion Keys & Governing Tests

| Criterion Key | Regulatory Citation | Governing Test & Required Elements |
| :--- | :--- | :--- |
| `eb1a_one_time_achievement` | `8 C.F.R. § 204.5(h)(3)` | **One-Time Major Internationally Recognized Award**: Personal receipt of a pinnacle international award (Nobel, Pulitzer, Academy Award, Olympic Medal). Comparable evidence cannot substitute for this route. |
| `eb1a_award` | `8 C.F.R. § 204.5(h)(3)(i)` | **Lesser Nationally or Internationally Recognized Prizes or Awards**: Prove recipient status, award for excellence in the field, candidate pool/selectivity, and national/international recognition of the award itself. |
| `eb1a_membership` | `8 C.F.R. § 204.5(h)(3)(ii)` | **Membership in Associations Requiring Outstanding Achievements**: Prove membership tier requires outstanding achievements as judged by recognized national or international experts at the time of admission. |
| `eb1a_media` | `8 C.F.R. § 204.5(h)(3)(iii)` | **Published Material About the Alien in Professional/Major Trade Publications or Other Major Media**: Prove the material is *about* the self-petitioner and relates to their work in the field, includes title/date/author/translations, is independent editorial coverage, and appeared in a qualifying publication/media outlet. |
| `eb1a_judging` | `8 C.F.R. § 204.5(h)(3)(iv)` | **Participation as a Judge of the Work of Others**: Prove *actual completed participation* (individually or on a panel) evaluating the substantive work of others in the same or an allied field. |
| `eb1a_contribution` | `8 C.F.R. § 204.5(h)(3)(v)` | **Original Scientific, Scholarly, Artistic, Athletic, or Business-Related Contributions of Major Significance**: Prove (1) discrete contribution & personal attribution, (2) originality relative to prior state of the art, and (3) major significance in the field beyond one employer. |
| `eb1a_publication` | `8 C.F.R. § 204.5(h)(3)(vi)` | **Authorship of Scholarly Articles**: Prove named authorship of scholarly articles in the field published on or before filing in professional or major trade publications or other major media. |
| `eb1a_artistic_display` | `8 C.F.R. § 204.5(h)(3)(vii)` | **Display of Work at Artistic Exhibitions or Showcases**: Prove public physical or virtual display of the self-petitioner's own artistic work at a venue/event whose purpose was to exhibit art. |
| `eb1a_role` | `8 C.F.R. § 204.5(h)(3)(viii)` | **Leading or Critical Role for Distinguished Organizations**: Prove completed leading role (hierarchy, decision authority) or critical role (significant importance to organizational outcomes) for an exact organization, establishment, or division with a proven distinguished reputation. |
| `eb1a_salary` | `8 C.F.R. § 204.5(h)(3)(ix)` | **High Salary or Significantly High Remuneration**: Prove remuneration for services via tax/pay/contract records and establish a significantly high position relative to peers using matched occupational, seniority, and geographic wage comparators. |
| `eb1a_commercial_success` | `8 C.F.R. § 204.5(h)(3)(x)` | **Commercial Successes in the Performing Arts**: Prove high box-office receipts or record/cassette/CD/video sales attributable to the self-petitioner relative to similar performing-arts pursuits. |
| `eb1a_final_merits` | `8 C.F.R. § 204.5(h)(2)-(3)` | **Part 2: Final Merits Determination (*Kazarian* Step Two)**: Independent totality synthesis establishing field definition, peer universe, placement among the small percentage at the very top, dated chronology of sustained national/international acclaim, and cross-evidence convergence. |
| `eb1a_petitioner` | `INA § 203(b)(1)(A)(ii)-(iii)` | **Continuation of Work & Substantial Prospective Benefit**: Clear evidence of prearranged commitments, employment, or detailed personal plan to continue work in the area of extraordinary ability and benefit the U.S. prospectively. |

---

## How to Use via MCP Tools or REST API

All tools and endpoints accept optional `custom_prompt` (`str`) and `additional_prompts` (`str | List[str]`) to inject firm-specific or case-specific instructions into the server-side context.

1. **List EB-1A Criteria**:
   - **MCP**: `tool_list_criteria(visa_type="eb1-a")`
   - **REST API**: `GET /api/v1/skills/criteria?visa_type=eb1-a`
2. **Evaluate Documents for Step One Criteria**:
   - **MCP**: `tool_evaluate_criterion_evidence(criterion_key="eb1a_contribution", beneficiary_name="...", documents=[...], custom_prompt=..., additional_prompts=...)`
   - **REST API**: `POST /api/v1/skills/review/evaluate-criterion`
3. **Draft Step One Subsections & Full Criterion Sections**:
   - **MCP**: `tool_draft_evidence_subsection` or `tool_draft_criterion_section` (accepts `custom_prompt` and `additional_prompts`)
   - **REST API**: `POST /api/v1/skills/draft/subsection` or `POST /api/v1/skills/draft/criterion-section`
4. **Draft Part 2: Final Merits Determination (*Kazarian* Step Two)**:
   - **MCP**: `tool_draft_eb1a_final_merits(beneficiary_name="...", criteria_summaries=[...], context="...", custom_prompt=..., additional_prompts=...)`
   - **REST API**: `POST /api/v1/skills/draft/eb1a-final-merits`
5. **Draft Continuation of Work & Full EB-1A Petition Letter**:
   - **MCP**: `tool_draft_petitioner_section(visa_type="eb1-a", ...)` and `tool_draft_full_attorney_letter(visa_type="eb1-a", include_final_merits=True, custom_prompt=..., additional_prompts=..., ...)`
   - **REST API**: `POST /api/v1/skills/draft/petitioner` and `POST /api/v1/skills/draft/full-letter`
