# Agentic Wedge Dossier — GRC Tooling (Compliance & Audit Agent)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — r/cybersecurity "why does SOC 2 feel like security theater?" (the evidence grind); 58% burn >2,000 person-hours/year on evidence collection; #1 GRC tool is still the spreadsheet. **Enrichment** wedge (KEEP).

## 1. Target SaaS & Use Case
- **Agent Type:** Security
- **Use Case:** Compliance & audit agent
- **SaaS in the crosshairs:** GRC tooling
- **Taxonomy Verdict:** KEEP (GRC stays system of record due to audit/regulatory requirements; agent drafts/collects and accelerates)
- **Deployed proof points:** U.S. FDA and regulated bodies using agents to draft/review compliance documentation (human signs off)

## 2. OSINT Source Map & Methodology
Mined a r/cybersecurity-sourced SOC 2 busywork essay, a 748/800-practitioner GRC state report, an evidence-automation reality check, and an automation guide citing Reddit.

| # | Source | URL |
|---|--------|-----|
| 1 | Amit Kothari — The busywork of SOC 2 evidence collection (r/cybersecurity) | https://amitkoth.com/soc-2-evidence-collection-busywork/ |
| 2 | RegScale — Why Spreadsheets Still Dominate GRC in 2026 | https://regscale.com/blog/grc-spreadsheets-problem-symptom/ |
| 3 | Scrut — Automated evidence collection: where it fails | https://www.scrut.io/post/how-automated-evidence-collection-works |
| 4 | CyberSierra — How to Automate SOC 2 & ISO 27001 Evidence (Reddit horror story) | https://cybersierra.co/blog/soc-2-iso-27001-automation-tips/ |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **Security theater = the evidence grind.** Amit Kothari: *"A sprawling r/cybersecurity thread with hundreds of comments asked bluntly: why does SOC 2 feel like security theater? Most answers pointed straight at the evidence grind."* The reality: *"123 evidence items. Four different collection frequencies. Dozens of source systems… multiply those small tasks by 123 items… and you have lost a week."* And: *"60% of GRC users still manage compliance manually with spreadsheets."* (Source 1)
- **The #1 GRC tool is still a spreadsheet.** RegScale, citing the 2026 State of GRC Report (748 practitioners): the most widely used GRC tool is the spreadsheet (18% primary). *"58% are burning through more than 2,000 person-hours every year on evidence collection alone, a.k.a. one full-time employee doing nothing but gathering screenshots and compiling documentation, year-round."* (Source 2)
- **The audit-season dread + restart horror.** CyberSierra: traditional collection *"becomes an all-consuming nightmare"*; a Reddit user shared *"a horror story about having to restart their entire observation period because they couldn't produce evidence that a specific control had been continuously operating—even though it had been."* (Source 4)
- **"Automated" evidence is often just organized manual work.** Scrut: *"A significant portion of what is marketed as automated evidence collection… turns out to be organized storage… A token expires… The platform stops receiving valid data, but the dashboard stays green. The first sign of trouble is an auditor asking why no evidence exists for a four-week period."* (Source 3)

## 4. User Psychographics
- **Roles:** GRC analysts, compliance managers, security engineers conscripted into audit prep, vCISOs.
- **Emotional state:** Dread and resentment — audit season as a "fire drill," productivity nosedive, taking dated screenshots across a dozen tools, terrified of a restarted observation period.
- **The acute bottleneck:** Mechanical, recurring evidence collection (150+ artifacts, multiple frequencies, a dozen source systems) with provenance that breaks silently — and tools that "organize" manual work rather than truly generate evidence.

## 5. The Agentic Wedge
**Wedge name:** "Continuous Evidence Agent (Source-Grounded, Provenance-First)"

**How it works:** An agent that continuously pulls system-generated evidence *directly from source systems* (with collection timestamp, population, and tamper-evident log), maps it to controls, detects silent integration breaks before the auditor does, and drafts the human-judgment documentation for sign-off — turning audit prep from a fire drill into a background process.

**Why it wins:** It kills the proven pain (the 2,000-hour evidence grind, spreadsheet trackers, restart horror, "green dashboard / no evidence" gaps) while keeping GRC as the audit/regulatory system of record. KEEP: the agent drafts and accelerates with verifiable provenance; a human still signs off.

**Buyer trigger:** A SOC 2 kickoff invite (stomach-drop) — or a near-miss observation-period restart.
