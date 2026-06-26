# Agentic Wedge Dossier — BI Dashboards / Looker-class (NL Analytics, Text-to-SQL)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — "dashboard graveyard" is an industry-wide trauma; one team "deleted 1,200 dashboards, no one noticed"; an analyst quit over "40+ ad-hoc requests per week."

## 1. Target SaaS & Use Case
- **Agent Type:** Data
- **Use Case:** NL analytics (text-to-SQL)
- **SaaS in the crosshairs:** BI dashboards (Looker / Tableau-class)
- **Taxonomy Verdict:** RENEGOTIATE (warehouse stays as SoR; trim BI seats; keep a verification layer)
- **Deployed proof points:** Spotify, Etsy (NL questions over BigQuery)

## 2. OSINT Source Map & Methodology
Mined analyst-burnout essays, a "delete 1,200 dashboards" post-mortem, and dashboard-graveyard analyses (with usage breakdowns).

| # | Source | URL |
|---|--------|-----|
| 1 | Databox — Dashboard Graveyards | https://databox.com/dashboard-graveyard |
| 2 | Valiotti — Your Analyst Is Drowning in Ad Hoc | https://valiotti.com/your-analyst-is-drowning-and-its-not-their-fault/ |
| 3 | Reliable Data Engineering (Medium) — We Deleted 1,200 Dashboards | https://medium.com/@reliabledataengineering/i-deleted-1-200-dashboards-no-one-noticed-c559ff5d3d85 |
| 4 | Data Engineer Things — Nobody Is Making Decisions With Your Dashboards | https://blog.dataengineerthings.org/nobody-is-making-decisions-with-your-dashboards-06849015f28b |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **The graveyard, defined by lived experience.** Databox: *"The stakeholder who requested it just sent a Slack message asking if you could 'pull together a quick breakdown' of data. The same data that has been sitting in a dashboard with her name in the title for the past month."* Diagnostic: *"zero opens by a non-builder in 90 days."* (Source 1)
- **It makes people quit.** Valiotti: *"She quit because she was fielding 40+ ad-hoc requests per week from executives who couldn't self-serve… The analyst is building the airplane while flying it while also serving drinks to the passengers."* (Source 2)
- **Nobody noticed the deletion — and the real usage data.** Reliable Data Engineering: after deleting 1,200 dashboards, *"Nobody noticed because nobody was looking at them in the first place."* Actual data sources: *"Excel exports (45%), Direct database queries (20%), Asking analysts in Slack (20%)… Dashboards (5%)."* And the recurring boardroom death: *"'But Steve's spreadsheet shows $5.2M.' … 'Then this dashboard is wrong.' Analyst: Dies inside."* (Source 3)
- **Architecturally destructive.** Data Engineer Things: *"Every dashboard built without a clear owner accumulates as technical debt. Pipelines feeding reports nobody uses still need to be maintained… dashboards that do refresh automatically — on a schedule, consuming compute, every single day — and nobody could tell you why they exist."* (Source 4)

## 4. User Psychographics
- **Roles:** Data analysts, analytics engineers, BI developers reporting into execs who can't self-serve.
- **Emotional state:** Drowning and demoralized — Slack DMs look like a support queue, deep work impossible, blamed for being "slow," watching beautiful dashboards go unopened.
- **The acute bottleneck:** Every data question routes through a human because dashboards aren't true self-serve; stakeholders bypass to Excel/Slack anyway.

## 5. The Agentic Wedge
**Wedge name:** "Ask-the-Warehouse Agent (NL → Verified SQL)"

**How it works:** An agent that answers "why did leads drop last week?" in natural language directly over the warehouse — writing the query, returning the number *with context and a citation to the metric definition* — so the Slack pings stop and the basic-question dashboards become unnecessary. A thin verification/governance layer stays for trust.

**Why it wins:** It kills the proven pain (graveyard dashboards + the analyst-as-bottleneck) by collapsing the BI interface into an answer. The warehouse stays the system of record (RENEGOTIATE); per-seat dashboard licenses compress toward consumption.

**Buyer trigger:** A dashboard-usage audit (or an analyst's resignation letter citing ad-hoc overload).
