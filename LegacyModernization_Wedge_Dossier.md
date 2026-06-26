# Agentic Wedge Dossier — Legacy-IT Modernization Tools (NL → SAP / COBOL)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — vivid, high-stakes pain: "software archaeology… manual, soul-crushing"; a retailer's 20M lines of COBOL maintained by 2 engineers, one retiring.

## 1. Target SaaS & Use Case
- **Agent Type:** Code
- **Use Case:** Legacy-IT modernization (natural-language interface over SAP/mainframe/COBOL)
- **SaaS in the crosshairs:** Modernization consulting / tools (manual-audit "archaeology")
- **Taxonomy Verdict:** KEEP (pure enrichment — agent unlocks the legacy system; system of record becomes more valuable)
- **Deployed proof points:** Suzano, Deutsche Telekom (Gemini NL over 40-year-old SAP/mainframe/COBOL)

## 2. OSINT Source Map & Methodology
Mined SAP/COBOL modernization analyses, an "AI saves COBOL" essay, and institutional-knowledge risk reports.

| # | Source | URL |
|---|--------|-----|
| 1 | Replay — Mainframe Modernization: Decoding the COBOL Logic Gap | https://www.replay.build/blog/mainframe-modernization-decoding-the-cobol-logic-gap-without-manual-audits |
| 2 | Exodus2026 — If AI Can Modernize COBOL, We Don't Need To | https://exodus2026.substack.com/p/if-ai-can-modernize-cobol-then-we |
| 3 | Devsu — The COBOL Cliff Is an Institutional Knowledge Problem | https://devsu.com/resources-center/the-cobol-cliff-is-not-a-talent-problem.-its-an-institutional-knowledge-problem |
| 4 | Codingscape — Modernize COBOL before your engineers retire | https://codingscape.com/blog/modernize-cobol-before-your-engineers-retire-ai-changed-the-math |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **Software archaeology.** Replay: *"we are currently spending billions on 'software archaeology'—the manual, soul-crushing process of hiring consultants to read 40-year-old COBOL lines to understand business rules that were never documented."* *"70% of legacy rewrites fail… 67% of legacy systems lack any form of accurate documentation… Manual audits take an average of 40 hours per screen."* (Source 1)
- **The experts have left.** Exodus2026: *"COBOL is impossible to support because nobody wants to learn COBOL. Universities don't teach it. The people who knew it have ridden off into the sunset. The documentation is bad. The business rules are arcane and incomprehensible. Nobody really knows how it all works."* (Source 2)
- **The worst version of a legacy system.** Devsu: when maintainers leave, *"what remains is the worst version of a legacy system: code that runs in production, that nobody fully understands, that cannot be modified without significant risk."* The cited example: *"a major US retailer discovered that its 2,500 store locations all ran on COBOL programs totaling approximately 20 million lines of code, maintained by two engineers — one of whom was retiring."* (Source 3)
- **The clock is the threat.** Codingscape: *"Your senior COBOL engineer just gave notice. When they leave, decades of institutional knowledge walk out with them… which 'temporary' patches from 2003 are now load-bearing. Syntax is teachable. That isn't."* COBOL expertise *"costs 2–3x market rates."* (Source 4)

## 4. User Psychographics
- **Roles:** Enterprise architects, CIOs/CTOs at banks/insurers/retailers, the last 2–3 engineers holding a core system in their heads.
- **Emotional state:** Quiet dread — a load-bearing system depends on people about to retire; "Big Bang" rewrites terrify them (70% fail), but doing nothing is a time bomb.
- **The acute bottleneck:** The "Logic Gap" — undocumented business rules + dead code paths that manual audits (40 hrs/screen) can't economically map before the experts leave.

## 5. The Agentic Wedge
**Wedge name:** "Living-System Translator Agent (Behavior-Grounded)"

**How it works:** An agent that lets non-technical staff query 40-year-old SAP/COBOL in natural language, and that captures institutional knowledge by grounding on *runtime behavior* (not just stale code/docs) — extracting business rules into modernization-ready form while the experts are still in the building.

**Why it wins:** It targets the proven, dread-inducing pain (tribal knowledge walking out, "archaeology" consulting spend) without the 70%-failure Big-Bang rewrite. This is pure enrichment (KEEP) — the agent makes the legacy system *more* valuable and sustainable; modernization-consulting spend shifts to the agent layer.

**Buyer trigger:** A senior COBOL/ABAP engineer giving notice.
