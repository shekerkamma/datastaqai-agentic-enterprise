# Competitive Landscape & Opportunity Map — Agentic Use Cases (DataStaqAI Pitch Deck Source)

**What this is:** A market-research competitive analysis across the 25 agentic use cases — who the players are, how they compete, where the gaps are, and where DataStaqAI positions to win. Structured as a deck outline (each `##` = a slide section). All vendors named are real and appeared in cited sources (see end).

---

## SLIDE 1 — The Thesis (the one slide that sells the deck)
**Every category has split into two camps — and both leave the same hole.**
- **Incumbents** (Zendesk, Salesforce, Westlaw/Lexis, Splunk, Workday, Bynder, OutSystems, Looker…) bolt AI onto the seat they're defending. They won't cannibalize their own seat revenue.
- **AI-native point solutions** (Sierra, Decagon, Harvey, Torq, Prophet, Rossum, Vanta, Feedzai, Databricks Genie…) build great agents — but **enterprise-first, expensive, and sold as products you must integrate, tune, own, and maintain yourself.**
- **The hole both leave:** the **mid-market** that (a) can't afford $95K–$590K enterprise contracts, (b) has no engineering bandwidth to integrate and maintain an agent across its systems, and (c) doesn't want yet another siloed subscription.
- **DataStaqAI's wedge:** be the **delivery layer for the agent era** — done-for-you: we build/wire the agent into your systems of record, own the client-specific workflow + governance, and run it. Outcome, not a subscription.

> Proof the white space is real: **Crescendo** is winning by being the *fully-managed* CX agent ("100% covered, minimal engineering bandwidth, budget-friendly") against Sierra/Decagon's build-it-yourself model. **Twig** explicitly markets that "the mid-market is underserved… teams with 5–50 agents have been left to stitch together prompts and plugins on their own." **RegScale's 2026 survey:** 80%+ of orgs still can't fully automate evidence collection — "integration challenges (23%)" and "lack of skilled staff (23%)" are the top blockers, not appetite.

---

## SLIDE 2 — How the market competes (the patterns that repeat in every category)
1. **Pricing is bifurcating, not converging:** enterprise annual contracts (Sierra $150K–$350K+, Decagon $95K–$590K, Kore.ai $300K+, Looker ~$150K, Harvey $1,200–2,000/seat, GRC $25–55K) vs. usage/outcome (Intercom Fin $0.99/resolution, Twig $5/ticket, Julius $37/mo). **The pricing model you pick determines your unit economics for years.**
2. **AI-natives sit *on top of* the incumbent's system of record** (Ada/Decagon/Sierra require a separate helpdesk; Cortex/Genie only read their own warehouse). Integration cost + a second tool is the hidden TCO.
3. **The model is no longer the moat — the governed context is.** Text-to-SQL scores 87% on toy data but ~10% on real enterprise schemas (Spider 2.0); accuracy comes from the *semantic layer*, not the model. Same pattern everywhere: the agent only works once wired into the client's data/rules.
4. **"Automated" often means "organized manual work."** GRC tools mark a manually-uploaded screenshot as "evidence"; the integration breaks silently and the dashboard stays green. Real automation = source-grounded with provenance.
5. **Build-vs-buy is unresolved for the buyer** — incumbents win on distribution/compliance, AI-natives win on agent quality, 58% of buyers run both. Nobody is selling the *delivery* of the combination.

---

## SLIDE 3 — The five recurring GAPS (this is the white space)
| # | Gap | Evidence across categories | DataStaqAI opening |
|---|-----|----------------------------|---------------------|
| G1 | **Mid-market is underserved** | CX (Twig), GRC ("59% of practitioners commercially unaddressed" — RegScale), CPQ (Revenue Cloud $200/seat "out of reach for mid-market" — Prodly) | Package agent delivery at $2–5k/mo, not 6-figure ACVs |
| G2 | **No engineering bandwidth to integrate/own** | Sierra/Decagon "build on your own, high eng bandwidth"; GRC blockers = integration + skills | We *are* the eng team; done-for-you wiring |
| G3 | **Point solutions don't span the buyer's systems** | Cortex/Genie can't cross warehouse boundaries; AI-natives need a separate helpdesk | We integrate across SoRs + own the cross-system workflow |
| G4 | **Products, not outcomes** | Crescendo's managed model out-positioning Sierra; "neither platform replaces a security program" (GRC) | Sell the realized outcome + ongoing operation |
| G5 | **Governed context / provenance is the real work, and it's unglamorous** | semantic layer drives text-to-SQL accuracy; "automated evidence" is often organized storage | We build + maintain the context layer the agents depend on |

---

## SLIDE 4 — Competitive snapshot: CUSTOMER agent
- **Conversational support / chatbot:** AI-natives **Sierra** (~$4.5B val, $150K+/yr, separate helpdesk), **Decagon** ($95K–$590K), **Ada** ($100–400K), **Forethought**; incumbents **Zendesk AI** (14.6% share), **Intercom Fin** ($0.99/res, highest resolution rate), **Salesforce Agentforce**, **Freshdesk Freddy** (SMB); managed hybrid **Crescendo** (PartnerHero), usage-priced **Twig** ($5/ticket), SMB challenger **Orki**.
- **How they compete:** resolution rate vs. distribution; pricing model is the real battleground; compliance + vertical-SaaS integration decide regulated deals.
- **Gap:** mid-market (5–50 agents) "left to stitch together prompts and plugins"; AI-natives need a separate helpdesk = integration tax.
- **DataStaqAI opening:** deliver the agent **wired to the client's existing helpdesk + back-end actions**, managed, at mid-market price — the Crescendo model but as an engineering agency, not a BPO.
- (CPQ, booking, FAQ-deflection covered in POSITIONING.md cards 2–4.)

## SLIDE 5 — Competitive snapshot: EMPLOYEE agent
- **Enterprise search:** **Glean** ($40K/yr floor), **Coveo**, **Dashworks**, **Guru**, **Onyx** (OSS), **Slite/Super**. Gap: SMB pricing + trial-on-your-own-corpus + answer-trust.
- **Legal research:** AI-natives **Harvey** ($1,200–2,000/seat, $11B val), **Legora**, **Spellbook** ($350M val, contract precedent moat); incumbents rebuilding — **Thomson Reuters CoCounsel** (1.9B Westlaw docs), **Lexis+ Protégé**; **Anthropic Claude** plugins triggered a ~$285B incumbent selloff. Gap: mid-size firms (45–250 attys) priced out of Harvey; hallucination/citator-verification + governance.
- **Doc drafting / HR / agent-assist:** mostly horizontal LLM + incumbent add-ons; gap = the cross-system *workflow* (drafting→audience, HRIS→IT provisioning, pull-not-push assist).
- **DataStaqAI opening:** mid-firm/mid-market deployment + governance + cross-system workflow the point tools skip.

## SLIDE 6 — Competitive snapshot: CREATIVE agent
- **Players:** ad/creative — **Bannerbear, Tadka, Canva, Viewst**; video — **Reap, Descript, Cutsio, Veo, Adobe**; marketing content — **Copy.ai, Starti, Roster (UGC)**; DAM — **Bynder, Brandfolder, Uplifted (performance DAM)**.
- **How they compete:** volume/throughput + brand-lock; mostly self-serve SaaS tools.
- **Gap:** the *workflow + brand-system wiring* (strategy-fed variant generation, clip→caption→reframe pipeline, brief→variants on brand voice, always-on DAM curation) — tools generate, but the operator still stitches the pipeline.
- **DataStaqAI opening:** deliver the wired pipeline + brand-lock, not a generation tool the team must operate.

## SLIDE 7 — Competitive snapshot: CODE agent
- **AI code review:** **CodeRabbit** ($24/mo), **Greptile** (indexes the repo), **Qodo** (low-noise), **Sourcery**, **GitHub Copilot** (diff-only, weakest). Gap: context-blind noise; commit-time gating.
- **Legacy modernization & low-code escape:** **Replay** (visual reverse-engineering, 40hr→4hr/screen); incumbents = the legacy/low-code platforms themselves (OutSystems/Mendix/SAP). Gap: this is a **BUILD** category — the deliverable is owned code, the tool only assists the reverse-engineering.
- **DataStaqAI opening:** **Code is the cluster where we sell delivery you can't buy off the shelf.** Low-code escape (#17) + legacy modernization (#16) = our sharpest plays: outcome = owned code + AI layer, not a subscription.

## SLIDE 8 — Competitive snapshot: DATA agent
- **Text-to-SQL / analytics:** warehouse-native **Snowflake Cortex Analyst**, **Databricks Genie** (both locked to their own platform, ≤25–30 tables/space, nondeterministic), **Looker+Gemini** (~$150K, dev-heavy), search-first **ThoughtSpot**, notebook **Hex**, no-code **Julius** ($37/mo); context layers **dbt/Cube/Dawiso**.
- **How they compete:** accuracy via semantic layer (90% Cortex vs 10% raw on real schemas); single-platform lock-in.
- **Gap:** **cross-platform questions have no home** (margin in Snowflake + telemetry in Databricks + ref data in Postgres); semantic layer is the unglamorous real work; "they retrieve, they don't analyze" (no driver ranking/root cause).
- **IDP/OCR:** **Rossum, OpenEnvoy, Esker, MetaViewer, Peakflo** — mature, template-free VLM tools. Gap: ERP integration + 3-way-match + rescuing failed OCR rollouts.
- **DataStaqAI opening:** build the **cross-system semantic/context layer + the analysis workflow** (Data) and **ERP-wired document agents** (IDP) — the integration the products don't do.

## SLIDE 9 — Competitive snapshot: SECURITY agent
- **SIEM/SOC investigation:** **Prophet AI** (investigate-every-alert; JB Poindexter, Cabinetworks), **Torq HyperSOC** (Check Point, Carvana, Valvoline), **D3 Morpheus** (self-healing). 
- **SOAR replacement:** **Torq, Tines** (Mars: 200 Phantom→50 Tines), **Swimlane, BlinkOps, Simbian**; incumbents **Splunk Phantom, Palo Alto XSOAR** (declared "obsolete" by Gartner).
- **Fraud:** **Feedzai** (enterprise banking, 73% fewer FPs), **Sardine** (fintech, device+behavior, "11 vendors → 1"), **Unit21** (no-code RiskOps), **Sift** (marketplaces). Gap: mid-market issuers; ops/case-file layer.
- **GRC:** **Vanta** ($10K start, 400+ integrations, hourly, FedRAMP), **Drata** ($7.5K, depth), **Secureframe, Sprinto, Scrut** (Scrut Teammates = AI agents that *act*, not just alert). Gap: "neither replaces a security program"; 80% still can't fully automate; integration + skills.
- **DataStaqAI opening:** these are mostly **DEPLOY+TUNE / INTEGRATE** — we stand up + tune + wire to the client's stack (and the SIEM-cost-reduction business case is a strong door-opener). Security buyers are regulated/risk-averse → lead with KEEP/enrichment framing.

## SLIDE 10 — Where DataStaqAI wins (positioning synthesis)
- **Who we are:** the **done-for-you AI engineering team** — the systems integrator / delivery layer for the agent era. OpenHands + subagents + MCPs; managed ~$2–5k/mo.
- **Who we're NOT:** not another point-solution subscription; not an enterprise-only 6-figure platform.
- **Three plays, ranked by fit:**
  1. **BUILD plays (sharpest):** Low-code escape (#17), Legacy modernization (#16) — outcome = owned code the client keeps; no off-the-shelf substitute.
  2. **INTEGRATE+WORKFLOW plays (broadest):** wire a best-of-breed agent into the client's SoR + own the client-specific workflow + governance (CPQ, IDP, support, legal, fraud, GRC…).
  3. **DEPLOY+TUNE plays (fastest):** stand up + tune a mature tool the client can't operate alone (SIEM, predictive ops, enterprise search).
- **The one-line pitch:** *"The agent tools are real — but they're products you have to integrate, tune, own, and operate. We deliver the outcome: the agent wired into your systems, the workflow built, the thing running. You keep your systems of record; we run the agent layer on top."*

## SLIDE 11 — Recommended go-to-market sequence
- **Lead with the BUILD plays** for credibility (delivery you can't buy) → land **INTEGRATE** plays for volume → attach **DEPLOY+TUNE** for fast wins.
- **Best entry signals (from the prospect work):** SOC-analyst hiring posts (SIEM), legal "which-tools" re-evaluations, Salesforce CPQ End-of-Sale, low-code license re-pricing, failed-OCR AP rollouts.
- **Differentiator to repeat in every deal:** mid-market price + done-for-you integration + you own the outcome (vs. enterprise ACV + DIY integration + another silo).

---

## Sources (real, from Exa research — representative)
- CX landscape: fin.ai, twig.so, crescendo.ai, callsphere.ai, viewpointanalysis.com, presenc.ai
- GRC: securitycomplianceguide.com, scrut.io, decryptiondigest.com, stackscout.net, truvocyber.com, regscale.com
- Fraud: fluxforce.ai, decodethefuture.org, feedzai.com, sardine.ai
- Data/text-to-SQL: tellius.com, colrows.com, thenewaiorder.substack.com, promethium.ai, dawiso.com
- SOAR/SIEM: torq.io, tines.com, d3security.com, swimlane.com, bleepingcomputer.com, techtarget.com
- Legal: law.com, lexisnexis.com, theapplied.co, microsoft.com, aivortex.io
- CPQ / low-code / IDP: dealhub.io, servicepath.co, cpq-integrations.com, apparound.com, replay.build, doddledesign.co.uk, mendix.com, rossum.ai, openenvoy.com, esker
- (Full per-claim URLs live in the 25 dossiers + prospects.csv in this folder.)
