# WeVisa Agent Plugin & Skills (O-1A, O-1B & EB-1A Immigration Petitions)

Open **Agent Plugin** and **Agent Skills (`SKILL.md`)** package for preparing **O-1A**, **O-1B (Arts & MPTV)**, and **EB-1A** extraordinary ability visa petitions with **Claude Code**, **OpenAI Codex**, **Gemini CLI**, **Cursor**, **Windsurf**, and **Antigravity (`agy`)** via the WeVisa MCP server (`https://wevisa.ai/mcp`).

---

## Quick Installation

### 1. Claude Code (`/plugin install`)
Inside an interactive `claude` session, run:
```text
/plugin marketplace add wevisa-ai/plugin
/plugin install wevisa@wevisa
```

### 2. Gemini CLI (`gemini extensions install`)
```bash
gemini extensions install https://github.com/wevisa-ai/plugin
```

### 3. Universal Installer (Claude, Codex, Gemini, Cursor, Windsurf, Antigravity)
Clone this repository and run `install.py` once:
```bash
git clone https://github.com/wevisa-ai/plugin.git
cd plugin
python install.py
```

---

## Included Modular Agent Skills (`skills/*/SKILL.md`)

1. **[`prepare-o1-eb1-application`](skills/prepare-o1-eb1-application/SKILL.md)** — End-to-end meta-skill orchestrating O-1A, O-1B, and EB-1A case preparation from raw client files to a filing-ready USCIS package.
2. **[`document-review-and-draft-feedback`](skills/document-review-and-draft-feedback/SKILL.md)** — Document extraction, categorization, alphanumeric exhibit numbering (`Exhibit A.1`, `Exhibit B.1`), rubric evaluation, draft critique, and pre-filing case readiness audits.
3. **[`o1a-criteria-drafting-and-review`](skills/o1a-criteria-drafting-and-review/SKILL.md)** — O-1A Extraordinary Ability (`8 C.F.R. § 214.2(o)(3)(iii)`) criteria drafting, Petitioner, Beneficiary, and Itinerary sections.
4. **[`o1b-criteria-drafting-and-review`](skills/o1b-criteria-drafting-and-review/SKILL.md)** — O-1B Arts (`8 C.F.R. § 214.2(o)(3)(iv)`) & Motion Picture/Television (`8 C.F.R. § 214.2(o)(3)(v)`) criteria drafting and evaluation.
5. **[`eb1a-criteria-and-final-merits`](skills/eb1a-criteria-and-final-merits/SKILL.md)** — EB-1A Extraordinary Ability (`8 C.F.R. § 204.5(h)`) Step One criteria, Part 2 Final Merits Determination (*Kazarian* Step Two), and Continuation of Work sections.
6. **[`reference-letter-drafting`](skills/reference-letter-drafting/SKILL.md)** — Independent Expert Opinion (`letter_variant="expert"`) and Direct Support (`letter_variant="support"`) testimonial letter drafting.
7. **[`forms-and-package-export`](skills/forms-and-package-export/SKILL.md)** — USCIS Form I-129 / I-907 schema inspection, auto-filling from client documents, PDF generation, and Word (`.docx`) / PDF export.

---

## Usage From Any Client Packet Folder

Open a terminal inside any folder containing a client's visa documents (CV, patents, scholar citations, press articles, contracts, passport/I-94) and start your agent:

```bash
cd /path/to/client_visa_packet
claude   # or: codex / gemini
```

Example prompt:
> *"Categorize the documents in this folder for an EB-1A petition for Dr. Jane Doe (`field_of_endeavor='Computational Biology'`), evaluate each criterion against the official rubrics, run a case readiness audit, and draft the Original Contributions and Judging sections using our firm style rule: `custom_prompt='Use formal third-person legal prose and bold all Exhibit citations.'`"*
