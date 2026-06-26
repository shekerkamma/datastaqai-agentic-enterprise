# DataStaqAI — Positioning & Pitch Cards (25 Agentic Use Cases)

**Purpose:** Not a prospect list. This is how DataStaqAI (done-for-you AI engineering team — OpenHands + subagents + MCPs, managed ~$2–5k/mo) **positions and pitches itself** against the 25 agentic use cases the market is already pursuing. Each card = filled copy you can lift into outreach, a deck, or a discovery call.

**How to read the pattern tag on each card:**
- **REPLACE** → the agent collapses a per-seat layer. Position: "we make the seat obsolete." (10 cards)
- **RENEGOTIATE** → strip the bolt-on module, keep the system of record. Position: "keep your SoR, drop the seats." (9 cards)
- **KEEP** → enrichment that compounds the incumbent's data moat. Position: "make the investment you already made finally pay off." (6 cards)
- **Build-vs-partner** → our delivery posture: **BUILD** (custom engineering = our core), **INTEGRATE+WORKFLOW** (wire an existing agent in + own the client workflow), **DEPLOY+TUNE** (stand up + tune a mature tool).

**Portfolio POV (the one-liner across all 25):** *"Every one of these is a use case where a general agent now does work a SaaS seat used to charge for. The incumbents won't cannibalize their own seats — so someone has to deliver the agent layer on top of your systems. That's us: we build and wire the agent, you keep your systems of record."*

---

## CUSTOMER agent

### 1. Conversational Support (Zendesk-class) · REPLACE · INTEGRATE+WORKFLOW
- **Market:** Mercedes MBUX, Wendy's FreshAI, Home Depot "Magic Apron" run live tier-1 agents resolving the bulk of routine contacts.
- **Pain:** Zendesk = 1.7/5 Trustpilot; teams leave because it's "a system that requires constant maintenance"; AI add-ons run 2–3× the base bill, priced per resolution.
- **Position:** "We make the rules engine obsolete, not easier — an agent that resolves ~80% of tier-1 off your existing ticket history, billed per ticket not per seat."
- **Offer:** Resolution-first tier-1 agent wired to your helpdesk + KB; we own the deflection logic; you keep the ticketing SoR.
- **Pitch:** *"You're paying per seat AND per AI resolution to maintain a trigger graph nobody understands. We deploy an agent that resolves 80% natively and kills the macro library."*
- **Why us:** vs Zendesk AI add-ons → no cold-start, no per-resolution surprise; vs DIY → you don't have the agent-eng team.

### 2. In-Product Owner Assistant (FAQ / KB / deflection) · RENEGOTIATE · INTEGRATE+WORKFLOW
- **Market:** VW myVW (camera-at-dashboard answers), GM OnStar embed support into the product itself.
- **Pain:** "Maintaining the documentation is a bigger problem than creating it" (59% of CX teams, unprompted); stale KB silently poisons any AI you bolt on.
- **Position:** "The bottleneck isn't writing — it's change detection. We deploy a self-healing knowledge agent that rewrites the exact articles each release breaks and answers from the source, not stale prose."
- **Offer:** Change-detection agent wired to your product release signals + KB; keep the KB SoR, drop standalone deflection seats.
- **Pitch:** *"Your help center describes a product that no longer exists, and your AI is hallucinating from it. We make the docs heal themselves."*
- **Why us:** vs more writers → doesn't fix change-detection; vs DIY → we wire the release-to-article signal.

### 3. AI Shopping / Sales Consultant (Guided-selling / CPQ) · REPLACE · INTEGRATE+WORKFLOW
- **Market:** Mercedes smart-sales assistant, Mobiauto Shopping Consultant (Gemini+BigQuery), Best Buy guided selection.
- **Pain:** Reps abandon CPQ to Excel ("hours or days vs minutes"); record-by-record quote lines; Salesforce CPQ is end-of-sale.
- **Position:** "A catalog-grounded agent builds the compliant quote from a natural-language brief — at conversation speed, no record-by-record grid."
- **Offer:** Conversational quote agent on your catalog/pricing/inventory; keep the commerce SoR; we own the quote-assembly + approval flow.
- **Pitch:** *"Your reps quote in spreadsheets because CPQ is too slow — and Salesforce just deprecated it. We give them a quote agent that's faster than the 40-year-old spreadsheet."*
- **Why us:** vs Revenue Cloud rebuild ($200/seat, 12–18mo) → weeks; vs DIY → we ground it in your catalog.

### 4. Travel & Booking Planner (Booking / itinerary tools) · REPLACE · INTEGRATE+WORKFLOW
- **Market:** Agoda AI Vacation Planner, LATAM "Cosmos," Virgin Voyages "Rovey" own the plan-and-book loop.
- **Pain:** SABRE is "basically a MS-DOS system"; agents buy "errors insurance" (a typo cancels a ticket); 20-min reprices; exchanges fail ~50–100% to manual queue.
- **Position:** "We target the least-automated, most-catastrophic slice — mid-trip exchange/reissue — with a fare-rule-native agent that auto-prices the lowest valid fare."
- **Offer:** Exchange/rebook agent over live inventory + IATA rules; keep the GDS/reservation SoR.
- **Pitch:** *"One mistyped exchange costs your client thousands. We give your agents an exchange agent that handles irrops and partially-used tickets without the 20-minute reprice."*
- **Why us:** vs ripping out SABRE → impossible; vs DIY → we encode the fare-rule logic + audit trail.

### 5. Messaging-Channel Chatbot (Chatbot builders / CCaaS bots) · REPLACE · INTEGRATE+WORKFLOW
- **Market:** LUXGEN (LINE, −30% workload), Banglalink REN, Deutsche Telekom MINDR run high-throughput deflection agents.
- **Pain:** Operators: "customers hated every single one. Not disliked. Hated"; 40+ hrs to build brittle trees; proprietary-JSON lock-in = 200–400 hrs to migrate.
- **Position:** "Tree-free: point the agent at your help center + history; it interprets free-form questions with a clean human handoff — no branches to babysit."
- **Offer:** Resolution agent replacing the decision-tree builder; keep the contact-center platform.
- **Pitch:** *"Your bot is a phone tree but worse, and the flows are a 300-hour hostage in proprietary JSON. We replace the tree with an agent customers don't hate."*
- **Why us:** vs Intercom/Drift renewal → no per-flow upkeep; vs DIY → we wire the handoff + grounding.

---

## EMPLOYEE agent

### 6. Enterprise Knowledge Search · RENEGOTIATE · DEPLOY+TUNE
- **Market:** Geotab (Gemini across HR+eng), Bosch "AskBosch," Glean — proven category.
- **Pain:** "Glean is $40k/yr minimum for my 60-person company"; 10% internal first-attempt success (9.5× worse than Google); answers waver → people fall back to Slack.
- **Position:** "ACL-respecting agent over your stack that returns inline-cited answers (not a doc list), trial-able on your own corpus, at SMB pricing — not a $40k floor."
- **Offer:** Deployed knowledge agent over Notion/Drive/Slack/Confluence; your corpus stays the moat.
- **Pitch:** *"You're priced out of Glean and your team DMs coworkers instead of searching. We deploy a knowledge agent you can test on your own docs before you sign."*
- **Why us:** vs Glean → SMB price + trial-first; vs DIY → ACL + grounding done right.

### 7. Doc Summarization & Drafting · REPLACE · INTEGRATE+WORKFLOW
- **Market:** KPMG, PwC, Deloitte run drafting agents across engagements.
- **Pain:** Knowledge workers spend "40% of the week producing first drafts"; 40-page report → 1-page summary drops from 2 hrs to 4 min.
- **Position:** "An agent that ingests raw inputs once and outputs the structured deliverable per audience — human keeps every judgment call; office suite stays."
- **Offer:** Deliverable agent wired to your transcripts/Slack/Jira; replaces per-seat productivity add-ons.
- **Pitch:** *"Your team spends 40% of the week on packaging, not thinking. We automate the translation step from raw notes to finished deliverable."*
- **Why us:** vs ChatGPT-by-hand → no per-task prompt re-engineering; vs add-on seats → outcome, not a tool.

### 8. Contact-Center Agent Assist · RENEGOTIATE · INTEGRATE+WORKFLOW
- **Market:** Humana Agent Assist (next-best-action to live reps), Vodafone.
- **Pain:** A real audit: agents use the push-assist tool "about 1% of the time"; 45% actively avoid it; stateless copilots misread sentiment and destroy credibility.
- **Position:** "Pull, not push. A full-context agent the rep summons — grounded in the whole relationship, silent otherwise — so it's used, not resented."
- **Offer:** On-demand assist agent over CRM+history; keep the CCaaS SoR, displace the push add-on.
- **Pitch:** *"You bought an assist tool agents touch 1% of the time. We replace the pop-up spam with an agent they actually invoke."*
- **Why us:** vs the push add-on → relevance on demand; vs DIY → full-relationship context wiring.

### 9. Legal Research & Drafting (Westlaw / Lexis / CLM) · REPLACE · INTEGRATE+WORKFLOW
- **Market:** Harvey, Legora, Thomson Reuters CoCounsel, DB Lumina — all 40 firms >500 attys now use legal AI.
- **Pain:** "My $20 ChatGPT beats my $270 LexisNexis"; lawyers spend 5–15 hrs/wk on research, 25–30% unbillable; duopoly contract traps (mailed cancellation, $100+ per-doc surprises).
- **Position:** "A lookup-and-draft agent with citations grounded to official reporters + a citator-verification pass — the hallucination guardrail incumbents got sanctioned for missing."
- **Offer:** Research/draft/redline agent for mid-size firms + AI-use-policy governance; corpus stays valuable.
- **Pitch:** *"A $20 tool now matches your $270/seat output — but one hallucinated cite gets you sanctioned. We deploy a citator-verified agent with the governance to stay safe."*
- **Why us:** vs Harvey ($1,200–2,000/seat) → mid-firm fit; vs DIY → verification + governance.

### 10. HR / Onboarding Agent (HR workflow SaaS) · RENEGOTIATE · INTEGRATE+WORKFLOW
- **Market:** Grupo Ruiz (Gemini Enterprise workflows), employee-agent onboarding deployments.
- **Pain:** r/HR: "onboarding is sucking the soul out of me"; HR as "human router"; a 75-person co burned 312 hrs/mo + $125k/yr; 60% of HR time on data entry.
- **Position:** "The HRIS is a great database but a terrible action-taker. We deploy a zero-touch orchestrator that *executes* the downstream chain off the new-hire trigger."
- **Offer:** Onboarding orchestration agent (raises IT tickets, collects manager needs via Slack, monitors background checks, updates HRIS); keep the HRIS SoR.
- **Pitch:** *"Day 5 and the new hire still has no laptop — and HR gets blamed. We turn HR from human router into approver with an agent that does the chasing."*
- **Why us:** vs HRIS workflow modules → they store, don't act; vs DIY → cross-system orchestration.

---

## CREATIVE agent

### 11. Ad & Creative Generation at Scale (production seats) · REPLACE · INTEGRATE+WORKFLOW
- **Market:** WPP, Authentic Brands (thousands of variants in hours), PODS billboard (6,000 headlines/29 hrs).
- **Pain:** Resizing eats 26–70% of designer time; two designers quit "no time to do actual creative work"; platforms demand 3–5 fresh variants/week the team can't sustain.
- **Position:** "A brand-locked variant factory takes one approved concept and generates the full platform matrix — humans get the 30% that's judgment, not the 70% that's reformatting."
- **Offer:** Variant-generation agent on locked brand rules + ad-platform push; brand/DAM stays.
- **Pitch:** *"Your designers are quitting because they spend 70% of the day resizing. We hand the reformatting to an agent and give them the creative work back."*
- **Why us:** vs hiring → automation problem, not headcount; vs DIY → brand-lock + platform wiring.

### 12. Video Generation / Editing · RENEGOTIATE · INTEGRATE+WORKFLOW
- **Market:** Veo deployments, Adobe gen-video — agent drafts, editor finishes.
- **Pain:** "The '30-second video' is a lie — it's a 3–4 hr production job in a trench coat"; mechanical tasks (clip/silence/caption/reframe) = 60–80% of time.
- **Position:** "First-pass editor agent does the mechanical layer; human owns the creative last mile — the exact RENEGOTIATE split."
- **Offer:** Clip→caption→reframe→batch-export agent feeding a staged timeline (no auto-publish).
- **Pitch:** *"Four hours for thirty seconds isn't sustainable at daily cadence. We automate the Timeline Black Hole so your editors do the creative cut, not the grunt work."*
- **Why us:** vs point tools (5 separate apps) → one wired workflow; vs DIY → pipeline + handoff.

### 13. Personalized Marketing Content (content tools) · REPLACE · INTEGRATE+WORKFLOW
- **Market:** Adobe gen workflows, ElevenLabs voice — variant copy/voice/assets on demand.
- **Pain:** The "content treadmill" — "launch, spike, tank, repeat… running on caffeine and chaos"; 63% cite iteration speed as #1 blocker; 80% of time on tactical execution.
- **Position:** "Brief-to-variants agent breaks the linear 'double the content = double the effort' model — modular, on-brand, audience-tuned."
- **Offer:** Content agent on brand voice + martech push; campaign platform stays, content seats go.
- **Pitch:** *"Your team works weekends to feed the algorithm and it still underperforms. We break the treadmill with a brief-to-variants agent so they curate instead of type."*
- **Why us:** vs per-seat content tools → outcome; vs DIY → brand-voice + channel wiring.

### 14. Brand / 3D Asset Generation (DAM tooling) · KEEP · INTEGRATE+WORKFLOW
- **Market:** BMW Group SORDI.ai generates synthetic 3D + brand assets feeding a managed pipeline.
- **Pain:** "Why can nobody find anything?"; trust collapses on untagged/duplicate libraries; the hidden DAM-admin who tags/re-tags manually; "<30 sec to find or they stop using it."
- **Position:** "An always-on curation agent auto-tags, dedupes, retires stale versions, and answers 'what do I need?' — it *feeds* the DAM, compounding the moat."
- **Offer:** Curation/tagging agent inside the DAM; the asset SoR stays and grows in value.
- **Pitch:** *"Your DAM is a graveyard nobody trusts because tagging never happens. We deploy an agent that keeps it curated so people actually use it."*
- **Why us:** vs more DAM admin → the buried line item; vs DIY → visual+contextual tagging.

---

## CODE agent

### 15. AI Code Assistant / Review (IDE / code-review add-ons) · RENEGOTIATE · DEPLOY+TUNE
- **Market:** Valeo, Broadcom run Gemini Code Assist across engineering.
- **Pain:** "AI Code Review Is Mostly Noise"; r/ExperiencedDevs: "PRs are basically rubber stamps"; AI PRs carry 1.7× more issues, incidents/PR +24%, review capacity flat.
- **Position:** "A codebase-indexed agent that runs at commit time (before the PR), focused on real risk — contract drift, security, async paths — silent on lint noise."
- **Offer:** Context-aware review agent indexed on the client's repo + conventions; consumption, not per-seat add-ons.
- **Pitch:** *"Your review bot fires 8 noisy comments a PR and trained your team to rubber-stamp. We give you a codebase-aware reviewer that only flags what's actually risky."*
- **Why us:** vs diff-only bots → full-repo context; vs DIY → indexing + commit-time gating.

### 16. Legacy-IT Modernization (NL→SAP / COBOL) · KEEP · BUILD
- **Market:** Suzano, Deutsche Telekom put NL interfaces over 40-year-old SAP/mainframe/COBOL.
- **Pain:** "The people who knew COBOL have ridden off into the sunset"; a retailer ran 20M lines on 2 engineers (one retiring); "software archaeology" at 40 hrs/screen; 70% of rewrites fail.
- **Position:** "A living-system translator: query the legacy system in plain English AND capture institutional knowledge from runtime behavior — while the experts are still here."
- **Offer:** Behavior-grounded knowledge-extraction + NL-over-legacy build; the SoR becomes *more* valuable.
- **Pitch:** *"Your senior COBOL engineer just gave notice — decades of undocumented logic walks out with them. We capture it from the running system before they go, no Big-Bang rewrite."*
- **Why us:** vs Big-Bang rewrite → 70% fail; vs consulting "archaeology" → grounded in runtime, our core build strength.

### 17. App Build / Migration Automation (low-code & migration tooling) · RENEGOTIATE · BUILD ← *sharpest build play*
- **Market:** Code-agent deployments scaffold apps + automate migrations specialists used to own.
- **Pain:** "$50K pilot → $1.2M annual bill"; logic locked in proprietary XML; "no senior engineer wants to touch it"; one team faced "200% more for 50% less."
- **Position:** "Lock-in escape: reverse-engineer the low-code estate into owned, git-native code in months — not the 18-month manual rewrite — plus the AI layer the cage blocked."
- **Offer:** Discovery → reverse-engineer → owned React/Node/Postgres, migrated incrementally; client keeps the code.
- **Pitch:** *"Your low-code bill now exceeds your eng payroll and you can't add AI inside the cage. We get you out — into code you own — in a quarter."*
- **Why us:** vs staying → compounding bill + blocked roadmap; vs DIY rewrite → 70% fail; **this is our core competency.**

---

## DATA agent

### 18. NL Analytics / Text-to-SQL (BI dashboards, Looker-class) · RENEGOTIATE · INTEGRATE+WORKFLOW
- **Market:** Spotify, Etsy let teams ask BigQuery questions in natural language.
- **Pain:** "We deleted 1,200 dashboards, no one noticed"; dashboards are 5% of actual data usage (Excel 45%, Slack 20%); analyst quit over "40+ ad-hoc requests/week."
- **Position:** "Ask-the-warehouse agent answers 'why did leads drop?' with context + a citation to the metric definition — collapses the BI interface into an answer."
- **Offer:** NL→verified-SQL agent over the warehouse + a thin trust/verification layer; warehouse stays SoR.
- **Pitch:** *"Nobody opens your dashboards — they Slack the analyst anyway. We give stakeholders an agent that answers directly, with the metric definition attached."*
- **Why us:** vs Looker seats → answer not interface; vs DIY → semantic layer + verification.

### 19. Document AI / Extraction (IDP / OCR SaaS) · REPLACE · INTEGRATE+WORKFLOW
- **Market:** Document AI deployments parse invoices/forms/contracts at scale.
- **Pain:** Built-in OCR "chokes on half our invoices" (every vendor formats differently); 8–12 min/invoice = 3.3–5 FTE just typing; many went back to manual after a failed rollout.
- **Position:** "Read-like-a-human VLM agent — no templates — that also does the other 90%: 3-way match, ERP posting, approval, audit. We rescue the failed OCR project."
- **Offer:** Invoice/doc agent wired into Dynamics/SAP/Oracle; downstream SoR stays, capture seats + clerk role go.
- **Pitch:** *"You tried OCR, it choked on half your formats, you went back to manual. We wire a no-template agent into your ERP — starting with the vendors that broke your last system."*
- **Why us:** vs SaaS OCR → outcome + integration; vs more clerks → that's the FTE you're escaping.

### 20. Forecasting / Predictive Ops (predictive-analytics SaaS) · KEEP · DEPLOY+TUNE
- **Market:** Honeywell, Geotab run predictive maintenance/fleet forecasting on proprietary sensor data.
- **Pain:** "The boy who cried wolf" — $1.8M deployment, 87k alerts/mo, missed a real failure for 11 days ($340k); 70% of programs fail; false positives = 40% of wrench time.
- **Position:** "Trustworthy triage agent fuses multi-sensor signals, applies operating context, and emits a CMMS work order — not an alert. Rides your sensor data (the moat)."
- **Offer:** Triage/work-order agent layered on the existing PdM platform; makes the investment finally pay off.
- **Pitch:** *"Your team stopped trusting the alerts after one too many false alarms — then a real failure cost $340k. We make the alerts trustworthy and turn them into work orders."*
- **Why us:** vs rip-and-replace → keep the data moat; vs DIY → sensor-fusion + CMMS wiring.

### 21. Research & Insight Agent (market-research tooling) · RENEGOTIATE · INTEGRATE+WORKFLOW
- **Market:** MLB "Scout Insights," NotebookLM-style agents synthesize corpora into briefings.
- **Pain:** "Wrapped 12 interviews and spent an entire week synthesizing"; 60.3% cite manual synthesis as #1 pain; 6–8-wk cycles deliver "after the decision was already made."
- **Position:** "Continuous insight agent compresses recruit→transcribe→synthesize to hours, with a growing queryable evidence base — research that arrives while options are open."
- **Offer:** Synthesis-on-demand agent over your research inputs; proprietary sources keep value, synthesis seats go.
- **Pitch:** *"Your research lands after the roadmap decision it was meant to inform. We compress the week of synthesis to hours so insight shapes the call, not documents it."*
- **Why us:** vs research-tool seats → on-demand; vs DIY → synthesis + evidence-base wiring.

---

## SECURITY agent

### 22. Threat Detection / SecOps (SIEM tier-1) · KEEP · DEPLOY+TUNE
- **Market:** Google Security Operations deployments correlate signals and surface threats.
- **Pain:** r/cybersecurity: "L1 SOC analyst here—drowning in false positives" (90%+ FP); 4,400 alerts/day, only 37% investigated; 70% burnout, tenure <3 yrs.
- **Position:** "Autonomous investigation agent investigates 100% of alerts end-to-end — analysts validate instead of build — riding the SIEM's incident history (the moat). Often pays for itself by letting you cut SIEM ingest."
- **Offer:** Investigation agent on the existing SIEM + cross-tool correlation; SIEM stays SoR, L1 seat compresses.
- **Pitch:** *"You're hiring L1 analysts to triage 4,400 alerts a day and investigating a third. We deploy an agent that investigates all of them — and often cuts your SIEM bill doing it."*
- **Why us:** vs hiring (4.8M-role gap) → math doesn't work; vs DIY → tuning + correlation across the stack.

### 23. Agentic Auto-Remediation (SOAR / runbooks) · REPLACE · INTEGRATE+WORKFLOW
- **Market:** Security-agent deployments write detection rules, isolate workloads, deploy honeytokens within policy.
- **Pain:** Playbooks "break at 3 AM because a vendor changed their JSON schema"; connector repair = 4–6 weeks; "coverage = playbooks = code = needs an owner"; architect leaves, knowledge walks.
- **Position:** "Playbook-free response agent reasons per-alert and triggers deterministic actions — with self-healing integrations that auto-correct API drift. No static asset to maintain."
- **Offer:** Migration off legacy SOAR (Phantom/XSOAR/Swimlane) + agent response within policy; SoR stays for audit, authoring seats go.
- **Pitch:** *"Your SOAR coverage depends on one engineer maintaining 200 playbooks — when they leave, you're exposed. We migrate you to an agent with no playbooks to break."*
- **Why us:** vs legacy SOAR → no maintenance tax; vs DIY → migration + policy-safe action wiring.

### 24. Fraud & Risk Detection (fraud / risk add-ons) · KEEP · INTEGRATE+WORKFLOW
- **Market:** Citi, Wells Fargo (risk/fraud analysis), Commerzbank "Bene."
- **Pain:** A merchant *abandoned* its fraud tool after false positives spiked — ended up reviewing 20% of orders, +15 staff, 19%/mo declines; FP = 80–95% of alerts in banking; declined good customers "just leave."
- **Position:** "Case-file agent enriches each flag with cross-system context, auto-prioritizes, compiles an evidence packet, and routes — humans judge only the ambiguous. Augments the bank's data + models (the moat)."
- **Offer:** Triage/case-file agent on the existing fraud stack; being wrong is expensive, so humans stay in the loop.
- **Pitch:** *"Your false-positive rate is forcing review headcount and declining good customers. We give analysts pre-built case files so they judge fraud, not noise."*
- **Why us:** vs rip-and-replace → keep the model moat; vs DIY → cross-system enrichment + evidence packaging.

### 25. Compliance & Audit Agent (GRC tooling) · KEEP · INTEGRATE+WORKFLOW
- **Market:** U.S. FDA and regulated bodies use agents to draft/review compliance docs (human signs off).
- **Pain:** r/cybersecurity: "why does SOC 2 feel like security theater?" — the evidence grind; 58% burn >2,000 hrs/yr on evidence collection; the #1 GRC tool is still a spreadsheet; "automated" tools are often just organized manual work that breaks silently.
- **Position:** "Continuous evidence agent pulls system-generated proof from source systems with real provenance, detects silent integration breaks before the auditor does, and drafts the judgment docs for sign-off."
- **Offer:** Source-grounded evidence agent feeding the GRC tool; GRC stays SoR (audit/regulatory), the 2,000-hour grind goes.
- **Pitch:** *"Audit season is a fire drill of dated screenshots across a dozen tools — and one missing month restarts your observation period. We make evidence collect itself, with provenance auditors trust."*
- **Why us:** vs GRC point tools → real provenance, not organized storage; vs DIY → source-system wiring + drift detection.

---

## Cross-pattern cheat sheet (how to lead the pitch by pattern)
- **REPLACE cards (1,3,4,5,7,9,11,13,19,23):** lead with *"the seat is obsolete"* + a hard cost number (FTE, per-resolution, hours/week).
- **RENEGOTIATE cards (2,6,8,10,12,15,17,18,21):** lead with *"keep your system of record, drop the bolt-on seats"* — reassures the buyer their core platform survives.
- **KEEP cards (14,16,20,22,24,25):** lead with *"make the investment you already made finally pay off"* — enrichment that compounds their data moat; safest for regulated/risk-averse buyers.
- **The two BUILD plays (16, 17)** are where DataStaqAI sells *delivery you can't buy off the shelf* — lead with these when the buyer wants an outcome they own, not another subscription.
