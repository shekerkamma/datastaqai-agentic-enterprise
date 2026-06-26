# Agentic Wedge Dossier — Market-Research Tooling (Research & Insight Agent)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — UX researcher: "wrapped 12 interviews and spent an entire week synthesizing"; 60.3% of 300 practitioners cite manual synthesis as their #1 pain.

## 1. Target SaaS & Use Case
- **Agent Type:** Data
- **Use Case:** Research & insight agent
- **SaaS in the crosshairs:** Market-research tooling (panels, survey tools, synthesis seats)
- **Taxonomy Verdict:** RENEGOTIATE (proprietary data sources retain value; research-tool seats displaced)
- **Deployed proof points:** MLB "Scout Insights," NotebookLM-style synthesis agents

## 2. OSINT Source Map & Methodology
Mined a UX Stack Exchange practitioner question, a 300-practitioner synthesis survey, and panel/agentic-research cost-time comparisons.

| # | Source | URL |
|---|--------|-----|
| 1 | UX Stack Exchange — How do you synthesize interview data faster? | https://ux.stackexchange.com/questions/153641/ux-researchers-how-do-you-synthesize-your-interview-data-faster |
| 2 | Lyssna — Research Synthesis Challenges (300 practitioners) | https://www.lyssna.com/blog/research-synthesis-challenges/ |
| 3 | UserIntuition — Why Traditional Panel Providers Slow Research | https://www.userintuition.ai/posts/why-traditional-research-panel-providers-slow-down-qualitative-research/ |
| 4 | Listen Labs — AI vs Traditional Market Research 2026 | https://listenlabs.ai/articles/ai-vs-traditional-market-research/ |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **A week lost to synthesis.** UX Stack Exchange, user198905: *"I just wrapped 12 user interviews and spent an entire week synthesizing notes. Love the process of talking to users, but capturing the notes + re-reading and synthesizing them always take a long time."* (Source 1)
- **The #1 pain, measured.** Lyssna's survey of 300 practitioners: *"60.3% cite time-consuming manual work as their biggest synthesis frustration… It's not just a minor inconvenience – it's the top barrier."* A participant: *"I tested with too many users and ended up with more data than [I could handle]… took several days to [synthesize] everything."* (Source 2)
- **Insights arrive after the decision.** UserIntuition: *"A traditional panel-to-insight cycle that takes six to eight weeks may deliver research after the decision it was commissioned to inform has already been made."* Total workflow cost is *"2-3x the original panel quote"* once scheduling, moderation, transcripts, and analyst time are counted. (Source 3)
- **The timing mismatch, named.** Listen Labs: *"For UX teams running two-week sprints, traditional research timelines mean findings arrive after decisions have already been made, so research documents choices instead of shaping them."* Traditional: 4–6 weeks, $15k–27k; AI-moderated: sub-24-hour. (Source 4)

## 4. User Psychographics
- **Roles:** UX researchers, market/customer-insights professionals, product researchers, designers doing double-duty research.
- **Emotional state:** Frustrated — love the interviews, dread the week of manual synthesis; insights teams demoralized when findings land too late to matter and stakeholders assume "the research doesn't exist."
- **The acute bottleneck:** Manual synthesis of transcripts/open-ends + fragmented panel→schedule→moderate→transcribe→analyze handoffs that take weeks and cost 2–3× the panel quote.

## 5. The Agentic Wedge
**Wedge name:** "Continuous Insight Agent (Synthesize-on-Demand)"

**How it works:** An agent that compresses the lifecycle — auto-recruit/transcribe, AI-moderated concurrent interviews, and structured synthesis with theme/sentiment tagging — returning a usable insight package in hours, while keeping the human for final interpretation and a growing, queryable evidence base across waves.

**Why it wins:** It collapses the proven pains (a week of manual synthesis; 6–8-week cycles that miss the decision window; 2–3× hidden cost) into an on-demand answer that arrives while options are open. Proprietary data sources keep value (RENEGOTIATE); standalone research-tool/synthesis seats are displaced.

**Buyer trigger:** Research landing *after* the roadmap decision it was meant to inform.
