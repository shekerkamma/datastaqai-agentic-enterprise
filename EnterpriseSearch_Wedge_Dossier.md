# Agentic Wedge Dossier — Enterprise Search SaaS (Enterprise Knowledge Search)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — quantified, vivid pain: 10% internal first-attempt success (9.5× worse than Google), and an explicit Reddit cost revolt against Glean.

## 1. Target SaaS & Use Case
- **Agent Type:** Employee
- **Use Case:** Enterprise knowledge search
- **SaaS in the crosshairs:** Enterprise search SaaS (Glean / Coveo / Dashworks-class)
- **Taxonomy Verdict:** RENEGOTIATE (agent over your data; trim search seats)
- **Deployed proof points:** Geotab (Gemini across HR + engineering), Bosch "AskBosch," Glean

## 2. OSINT Source Map & Methodology
Mined a problem-validation board sourcing Reddit quotes, an enterprise-search survey, and operator reviews of Glean.

| # | Source | URL |
|---|--------|-----|
| 1 | Real Problem AI — "search across my company's docs" still bad (Reddit quote) | https://www.realproblem.ai/idea/why-is-search-across-my-company-s-docs-still-bad-in-2026 |
| 2 | Slite — Enterprise Search Survey 2026 (10 findings) | https://slite.com/learn/enterprise-search-survey-findings |
| 3 | eesel AI — Glean reviews | https://www.eesel.ai/blog/glean-reviews |
| 4 | Slite — Glean review (trust erosion) | https://slite.com/learn/glean-ai-review |
| 5 | IT-Online — hidden productivity crisis | https://it-online.co.za/2026/06/22/the-hidden-productivity-crisis-costing-businesses-hours-every-week/ |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **The cost revolt.** Reddit quote curated by Real Problem AI: *"Glean is $40k/yr minimum. I just want decent search for my 60-person company."* Problem severity scored **9/10**, market signal **9/10**. The status quo: *"Notion/Confluence/Drive/Slack search returns garbage; people DM coworkers instead."* (Source 1)
- **The 9.5× gap.** Slite survey: *"while Google achieves 95% first-page accuracy, internal enterprise searches have only a 10% first-attempt success rate, creating a 9.5x performance gap."* Workers waste *"3.2 hours each week"* and *"nearly three-quarters of workers express dissatisfaction with their search setup."* (Source 2)
- **It finds, but doesn't act — and the answers waver.** Slite's Glean review: it can be *"slow to provide answers and inconsistent when asked the same prompt across different occasions… trust erodes and product adoption drops. Instead of using the tool, teams fall back on Slack, teammates, or manual search."* (Source 4)
- **Garbage in, garbage out.** eesel: *"Glean's search can be hit-or-miss, especially when dealing with older or poorly-tagged documents. This is a classic 'garbage in, garbage out' problem."* And you *"cannot test Glean against their own sources before signing a contract,"* so you buy on trust. (Source 3)
- **A full day a week, gone.** IT-Online cites research: *"Employees spend as much as 8.8 hours every week searching for information they need to do their jobs… more than an entire working day lost every week."* (Source 5)

## 4. User Psychographics
- **Roles:** Knowledge workers, ops leads, and IT buyers at 50–500-person companies priced out of Glean's $40k floor.
- **Emotional state:** Frustrated by "digital scavenger hunts," distrustful of a search tool that gives different answers to the same question, resentful of enterprise pricing + two-week implementations they can't trial first.
- **The acute bottleneck:** Answers depend on stale, poorly-tagged source docs and ACL complexity; people give up and DM a coworker (the "ask a human" tax).

## 5. The Agentic Wedge
**Wedge name:** "SMB Knowledge Agent (Trial-First, ACL-Native)"

**How it works:** An ACL-respecting RAG agent over Notion/Drive/Slack/Confluence/GitHub that returns **inline-cited** answers (not a list of docs to read), flags stale/deprecated sources, and — crucially — lets buyers test it against *their own* corpus before signing. SMB pricing, not a $40k enterprise floor.

**Why it wins:** It attacks the two loudest, most-quoted pains — price ("$40k for 60 people") and answer-trust ("inconsistent → fall back to Slack"). Your proprietary corpus stays the moat (RENEGOTIATE), but the standalone enterprise-search seats compress toward an agent that actually answers.

**Buyer trigger:** A Glean renewal quote landing on a sub-200-person company's desk.
