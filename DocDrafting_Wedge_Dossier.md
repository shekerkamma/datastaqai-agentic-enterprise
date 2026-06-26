# Agentic Wedge Dossier — Doc / Productivity Add-ons (Doc Summarization & Drafting)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — knowledge workers self-report 40% of the week is "just drafting," with itemized hour counts and a vivid board-reporting venting corpus.

## 1. Target SaaS & Use Case
- **Agent Type:** Employee
- **Use Case:** Doc summarization & drafting
- **SaaS in the crosshairs:** Doc / productivity add-ons (per-seat summarize/draft bolt-ons)
- **Taxonomy Verdict:** REPLACE (office suite stays; bolt-on drafting seats go)
- **Deployed proof points:** KPMG, PwC, Deloitte engagement-drafting agents

## 2. OSINT Source Map & Methodology
Mined first-person knowledge-worker experiments, a Reddit/LinkedIn board-reporting venting study, and a real-world-problems issue tracker.

| # | Source | URL |
|---|--------|-----|
| 1 | Sandeep Bhan (Medium) — I Gave AI My Job for 30 Days | https://sandeepbhan.medium.com/i-gave-ai-my-job-for-30-days-here-is-what-it-actually-did-6521c81b8365 |
| 2 | Erik van Dijk (Medium) — I asked 50,000 people about board reporting | https://medium.com/@erikvand/i-spent-3-days-asking-50-000-people-about-board-reporting-7cf8b38ce363 |
| 3 | RealWorldProblems #386 — rewriting status updates per audience | https://github.com/muaddibco/RealWorldProblems/issues/386 |
| 4 | The Leverage Years — Consultant's Friday Deliverable Machine | https://www.theleveragedyears.com/briefing-consultant-friday-deliverable-machine |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **40% of the week is packaging, not thinking.** Sandeep Bhan: *"I had been spending roughly 40% of my week producing first drafts of things. Not thinking. Not strategizing. Just drafting."* Itemized: *"Summarizing a 40-page internal report into a 1-page executive summary — my time: 2 hours. AI: 4 minutes."* and *"Drafting a formal proposal — my time: 3 hours. AI first draft that I edited: 35 minutes."* (Source 1)
- **The board still wants a PDF — and that person is me.** Board-reporting venting (Reddit/LinkedIn): *"Someone still has to translate a sea of charts into a coherent story and a clear ask. That person is me. Every single month."* And: *"C-level still demands flat PPT. Dashboards are for the analysts."* (Source 2)
- **The dashboards didn't save anyone.** *"The reporting specialist didn't disappear. They got a new tool to maintain on top of the old workflow. The board still wants a PDF. The PDF still takes three hours to produce."* From r/excel: *"It's super finicky. Sometimes I have to manually rechoose the file. The whole thing is a mess of linked data and broken references."* (Source 2)
- **Status reporting as a recurring 2–4 hour tax.** RealWorldProblems: *"Status reporting consumes 2–4 hours per week that should be spent on actual work… current workaround: maintaining a 'master' status doc and manually rewriting for each audience."* (Source 3)
- **The Friday-afternoon dread.** Leverage Years: *"a week of valuable client work… and somehow the status report, the exec summary, the stakeholder update, and the recommendation memo are all still in rough draft form. The work happened. The thinking happened. The output didn't."* (Source 4)

## 4. User Psychographics
- **Roles:** Consultants, PMs, analysts, account managers, finance/reporting specialists.
- **Emotional state:** Quietly demoralized — career built on judgment, but 40–60% of time spent on "packaging"; resentful that self-service dashboards added a tool to maintain instead of removing the manual PDF.
- **The acute bottleneck:** The manual "translation step" between raw inputs (notes, transcripts, threads, data) and structured, audience-specific output.

## 5. The Agentic Wedge
**Wedge name:** "Deliverable Agent (Inputs-Once, Audience-Many)"

**How it works:** An agent that ingests raw inputs (meeting transcripts, Slack threads, data outputs) once, then generates the structured deliverable — status report, exec summary, board PDF, per-audience updates — with the human retaining every judgment call. Pulls facts from Jira/Linear so input is "review and confirm," not re-typing.

**Why it wins:** It eliminates the proven manual translation tax (2–4 hrs/week status reporting; 3 hrs/PDF) that per-seat productivity add-ons never solved. The office suite stays; the bolt-on drafting/summarization seats lose their reason to exist. REPLACE at the add-on layer.

**Buyer trigger:** The 1 AM Friday deliverable scramble — recurring, universal, hated.
