#!/usr/bin/env python3
"""PART III — Business Use Cases (slides 9–18). One workflow slide per function:
WORKFLOW TODAY mini-flow + 4 cards (Current vendors / AI disruption / Opportunity / DataStaqAI position).
Renders branded .pptx with speaker notes + companion spec. Validated on save."""
import sys
sys.path.insert(0, "/home/shekerk/.claude/skills/branded-pptx-deck/scripts")
from pptxkit import Deck, Inches, Pt, PP_ALIGN, MSO_ANCHOR
from pathlib import Path

H = Path("/mnt/d/New folder/Antigravity-test/antigravity-skills/wedge_dossiers/book")
d = Deck(footer="DataStaqAI · The Agentic Enterprise · Chapter 3: Business Use Cases")
b = d.b
def notes(s,t): s.notes_slide.notes_text_frame.text=t

CHX=[Inches(0.6),Inches(3.5),Inches(6.4),Inches(9.3)]; CHW=Inches(2.7)   # workflow chips
CX=[Inches(0.6),Inches(3.63),Inches(6.66),Inches(9.69)]; CW=Inches(2.85) # cards

def build(fn, page):
    s=d.slide(fill=b.WHITE)
    d.header(s, fn["headline"], fn["sub"])
    d.text(s,"WORKFLOW TODAY", d.M, Inches(1.62), Inches(4), Inches(0.3), size=11, color=b.MUTED, bold=True)
    for i,(x,step) in enumerate(zip(CHX, fn["workflow"])):
        d.rect(s,x,Inches(1.95),CHW,Inches(0.62),b.NAVY,radius=0.06)
        d.text(s,step,x+Inches(0.1),Inches(1.95),CHW-Inches(0.2),Inches(0.62),size=10.5,color=b.WHITE,
               align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE,shrink=True)
        if i<3:
            d.text(s,"→",x+CHW,Inches(1.95),Inches(0.2),Inches(0.62),size=20,color=b.TEAL,bold=True,
                   align=PP_ALIGN.CENTER,anchor=MSO_ANCHOR.MIDDLE)
    cards=[("CURRENT VENDORS",fn["vendors"],b.SOFT,b.NAVY,b.INK),
           ("AI DISRUPTION",fn["disruption"],b.SOFT,b.NAVY,b.INK),
           ("OPPORTUNITY",fn["opportunity"],b.SOFT,b.NAVY,b.INK),
           ("DATASTAQAI POSITION",fn["positioning"],b.NAVY,b.TEAL,b.LIGHT_TEAL)]
    for (x,(title,lines,fl,tc,bc)) in zip(CX,cards):
        d.rect(s,x,Inches(2.95),CW,Inches(3.55),fl,radius=0.05,shadow=True)
        d.text(s,title,x+Inches(0.18),Inches(3.1),CW-Inches(0.36),Inches(0.35),size=11.5,color=tc,bold=True)
        d.text(s,[{"text":t,"bullet":True,"space_before":7,"size":10.5,"color":bc} for t in lines],
               x+Inches(0.18),Inches(3.55),CW-Inches(0.36),Inches(2.85),shrink=True,ls=1.06)
    d.footer(s,page,46)
    notes(s,fn["notes"])

FN=[
{"name":"Customer Operations",
 "headline":"Customer Operations is the first function to cross from software-assisted to AI-orchestrated at scale",
 "sub":"Tier-1 resolution is being automated end-to-end; the seat count collapses, the system of record survives",
 "workflow":["Ticket arrives","Read KB + history","Human macro reply","Escalate or close"],
 "vendors":["Incumbents: Zendesk, Salesforce, Intercom, Freshdesk","AI-native: Sierra ($15.8B), Decagon ($4.5B), Ada, Intercom Fin"],
 "disruption":["Agents resolve ~80% of tier-1 natively; per-resolution pricing $0.40–1.50","Seat count collapses; 'managed' tiers prove buyers can't run it alone"],
 "opportunity":["Mid-market priced out of $50–150K floors + dedicated agent engineers","Wire a resolution agent to the existing helpdesk + back-end actions"],
 "positioning":["INTEGRATE+WORKFLOW: resolution-first agent on your helpdesk","Per-ticket, bootstrapped off your history; you keep the ticketing SoR"],
 "notes":("Customer Operations leads Chapter 3 because it is the function furthest along the transition and therefore the "
  "clearest proof of the thesis in production. Walk the current workflow: a ticket arrives, a human reads the knowledge "
  "base and customer history, applies a macro or drafts a reply, and either closes or escalates — a per-seat motion where "
  "cost scales with volume. The vendor landscape has split exactly as the thesis predicts: incumbents (Zendesk, "
  "Salesforce, Intercom, Freshdesk) defend the seat and bolt AI on, while AI-natives (Sierra at $15.8B, Decagon at "
  "$4.5B, Ada, Intercom Fin) sell the agent. The disruption is that grounded agents now resolve roughly 80% of tier-1 "
  "natively and bill per resolution at $0.40–1.50, so the seat count — not the system of record — is what collapses. "
  "The tell that the white space is real is that the AI-natives have bolted on managed and forward-deployed services "
  "because mid-market buyers cannot operate the agents alone. That is the opportunity: companies priced out of $50–150K "
  "platform floors and unable to staff agent engineers. DataStaqAI's position is INTEGRATE+WORKFLOW — wire a "
  "resolution-first agent into the helpdesk the customer already runs, bootstrap it off their ticket history so there is "
  "no cold-start, price it per ticket, and leave the ticketing system as the untouched system of record. The buyer keeps "
  "what they trust and gets the outcome — resolved tickets — without buying a second platform or a 1,000-ticket cold "
  "start. Use this slide to set the template the next nine follow: workflow today, who plays, what the agent changes, "
  "where the mid-market gap is, and how we deliver into it.")},
{"name":"Sales",
 "headline":"Sales is splitting in two: agents take prospecting and quoting, humans keep the relationship",
 "sub":"The SDR seat and the CPQ grid are both being automated; the closer is not",
 "workflow":["Build list + enrich","Research + personalize","Sequence + follow up","Quote + close"],
 "vendors":["Incumbents: Salesforce, HubSpot, Outreach, Salesloft, Gong; CPQ: Revenue Cloud, DealHub","AI-native: 11x ($74M, Alice/Julian), Artisan (Ava), Regie.ai, Clay ($46M)"],
 "disruption":["Autonomous SDRs research, email & book with no human; the ~$80K SDR seat reallocated","Conversational quoting replaces the record-by-record CPQ grid (CPQ End-of-Sale)"],
 "opportunity":["Mid-market wants pipeline, not another silo'd SDR tool + data + warm-up stack","Wire SDR + quoting agents into the CRM; own the play + governance"],
 "positioning":["INTEGRATE+WORKFLOW: agentic prospecting + quoting on your CRM","Deliverable = pipeline & compliant quotes, not a tool to operate"],
 "notes":("Sales is the cleanest example of a function splitting along a human/agent line. Today the motion is: build and "
  "enrich a list, research and personalize, run a sequence and follow up, then quote and close. The first three steps are "
  "SDR work; the last is closer work. The vendor split: incumbents Salesforce, HubSpot, Outreach, Salesloft and Gong own "
  "the sequencer and CRM, while AI-natives attack the SDR seat — 11x (Alice the outbound SDR, Julian the phone agent; "
  "~$74M raised from Benchmark, a16z and HubSpot Ventures at a reported $350M valuation, customers like Xerox and Sage), "
  "Artisan's 'Ava,' Regie.ai, and Clay (~$46M) as the research layer. The disruption is that autonomous SDRs research, "
  "write, and book meetings without a human, reallocating the largest GTM line item — the ~$80K fully-loaded SDR seat — "
  "while on the quoting side conversational agents replace the record-by-record CPQ grid that reps abandon to Excel, made "
  "urgent by Salesforce CPQ's End-of-Sale. The opportunity is that the mid-market wants pipeline and quotes as an "
  "outcome, not a sprawling stack of an SDR tool plus a data vendor plus a warm-up tool that they must assemble and "
  "operate. DataStaqAI's position is INTEGRATE+WORKFLOW: wire prospecting and quoting agents into the CRM the company "
  "already runs, own the play design and the governance, and deliver pipeline and compliant quotes rather than another "
  "seat. Emphasize the boundary the slide draws — agents take the repeatable prospecting and quoting work; the human "
  "keeps the relationship and the close — because that boundary is what makes the pitch credible to a sales leader who "
  "fears being sold a robot that replaces their team.")},
{"name":"HR",
 "headline":"HR's system of record is a database that can't act — onboarding is the agent wedge",
 "sub":"The HRIS stores the new hire; an agent executes the cross-functional chain",
 "workflow":["Offer accepted","Email IT / Finance / mgr","Chase tasks + links","Provision + org update"],
 "vendors":["Incumbents: Workday (~$48K/yr), Rippling, BambooHR","Provisioning: Okta / Entra (SCIM), Zluri"],
 "disruption":["Event-driven provisioning: 5–8 hrs/hire & 15–25% error → minutes","HR shifts from 'human router' (60% of time on data entry) to approver"],
 "opportunity":["HRIS workflow modules store data but don't act across systems","Zero-touch onboarding orchestrator fired off the new-hire trigger"],
 "positioning":["INTEGRATE+WORKFLOW: orchestrate HR↔IT↔Finance; keep the HRIS SoR","Drop the per-seat workflow modules; we own the orchestration"],
 "notes":("HR makes the 'system of record vs system of action' distinction concrete. The onboarding workflow today is a "
  "human router problem: an offer is accepted, HR emails IT, Finance and the hiring manager, then spends days chasing "
  "tasks and links before the hire is provisioned and the org chart updated. Incumbents — Workday (around $48K/yr "
  "median), Rippling, BambooHR — are excellent databases but, as the research repeatedly shows, terrible action-takers; "
  "the provisioning layer (Okta/Entra via SCIM, Zluri) only partly closes the gap. The disruption is event-driven "
  "orchestration: an agent fired off the new-hire trigger turns a 5–8-hour, 15–25%-error manual process into minutes, and "
  "shifts HR from spending up to 60% of its time on data entry and 'professional nagging' to simply approving. The "
  "opportunity is precise: HRIS workflow modules store the record but do not execute across IT, Finance and the manager, "
  "and the mid-market feels this most acutely in the 'tooling chasm' between spreadsheets and a full Workday. DataStaqAI's "
  "position is INTEGRATE+WORKFLOW — a zero-touch onboarding orchestrator that raises IT provisioning tickets, collects "
  "hardware and software needs conversationally, monitors background checks, and updates the HRIS — while leaving the "
  "HRIS as the untouchable system of record and dropping the per-seat workflow modules that never actually took the "
  "action. The emotional hook for the buyer is the Day-5 new hire still without a laptop, and the HR person blamed for a "
  "broken cross-functional process they do not control; the agent removes the blame by doing the chasing. This is a "
  "RENEGOTIATE pattern: keep the system of record, strip the workflow seats, own the orchestration in between.")},
{"name":"Finance",
 "headline":"Finance back-office is a headcount problem agents convert into a software problem",
 "sub":"AP keying and the month-end close are the clearest agent ROI in the office",
 "workflow":["Invoice / txn arrives","Manual code → ERP","3-way match + approve","Reconcile + close"],
 "vendors":["Incumbents: NetSuite, SAP, Oracle, QuickBooks, Bill.com","AI-native: Ramp ($44B, Accounting Agent), Maximor (audit-ready close), Rossum, OpenEnvoy"],
 "disruption":["Auto-coding + real-time close: 'clean books 3x faster, 40+ hrs/mo saved' (Ramp)","Maximor: close 11→3 days, audit issues −90%; AP keying = 3.3–5 FTE today"],
 "opportunity":["Off-suite mid-market (Dynamics/Sage) pays the whole-suite consolidation tax","Wire a no-template AP + reconciliation agent into the existing ERP"],
 "positioning":["INTEGRATE+WORKFLOW: ERP-wired AP + close agent; rescue failed OCR","ERP stays SoR; we own the 3-way match, approval + audit trail"],
 "notes":("Finance is where the agent ROI is easiest to underwrite because the pain is measured in headcount. The workflow "
  "today: an invoice or transaction arrives, a clerk manually codes and keys it into the ERP, performs a three-way match "
  "and routes for approval, then reconciles and closes. Incumbents NetSuite, SAP, Oracle, QuickBooks and Bill.com own the "
  "ledger; AI-natives are attacking the manual layer on top of it. Ramp — now at a $44B valuation with over $1.5B "
  "run-rate revenue and an Accounting Agent that auto-codes transactions for real-time close — reports clean books three "
  "times faster and 40-plus hours saved per month; Maximor's audit-ready close agents cut one customer's close from 11 "
  "days to 3 with audit issues down over 90%; Rossum and OpenEnvoy attack template-free AP. The disruption framing is "
  "that AP keying, which today consumes the equivalent of 3.3–5 full-time staff at 2,000 invoices a month, becomes a "
  "software function. Crucially for our positioning, the leading agents layer on top of the ERP rather than replacing it "
  "(Maximor explicitly: 'no rip-and-replace'). The opportunity is the off-suite mid-market — companies on Dynamics, Sage "
  "or Intacct with diverse vendor formats who pay a consolidation tax to adopt a whole suite. DataStaqAI's position is "
  "INTEGRATE+WORKFLOW: wire a no-template AP and reconciliation agent into the existing ERP, explicitly positioned to "
  "rescue the failed OCR rollout, owning the three-way match, approval routing and audit trail while the ERP stays the "
  "system of record. Land the line from the research: AP should stop being a hiring problem.")},
{"name":"Procurement",
 "headline":"Procurement's intake-to-pay friction is the back office's clearest agent ROI",
 "sub":"The 'messy middle' of approvals across legal, finance and risk is being orchestrated by agents",
 "workflow":["Employee request (intake)","Route legal / finance / risk","Source + qualify supplier","PO + approve + pay"],
 "vendors":["Incumbents: Coupa (Navi, $9.5T data), SAP Ariba (Joule, ~29% share), Ivalua","AI-native: Zip ($371M, 50+ agents), ORO Labs ($100M), Levelpath, Opstream"],
 "disruption":["Agentic intake-to-procure automates up to 80% of manual review cycles (ORO)","58% of procurement now using/piloting AI (Ardent); Zip has unlocked ~$6B savings"],
 "opportunity":["Mid-market wants the orchestration layer without a Coupa/Ariba rip-replace","Wire an intake → approval → sourcing agent across existing systems"],
 "positioning":["INTEGRATE+WORKFLOW: intake-to-pay agent over your stack","Own the approval orchestration + policy guardrails; SoR stays"],
 "notes":("Procurement is a back-office function with unusually clean agent ROI because its pain is the 'messy middle' — the "
  "approval choreography across legal, finance and risk that sits between an employee request and a paid invoice. The "
  "workflow today: intake a request, route it through legal/finance/risk, source and qualify a supplier, then issue a PO "
  "and pay. The vendor landscape has split sharply: incumbents Coupa (Navi agents on a $9.5T spend dataset), SAP Ariba "
  "(Joule, ~29% share) and Ivalua defend the suite, while a wave of orchestration-native players — Zip ($371M raised, 50+ "
  "AI agents, customers including T-Mobile and OpenAI, ~$6B savings unlocked) and ORO Labs ($100M, founded by ex-SAP "
  "Ariba executives, customers like Coca-Cola, automating up to 80% of manual review cycles) plus Levelpath and Opstream "
  "— rebuild procurement as an agentic orchestration layer. Ardent's survey shows 58% of procurement is now using or "
  "piloting AI, so the 'wait and see' era is over. The opportunity for DataStaqAI is the mid-market that wants this "
  "orchestration without ripping out Coupa or Ariba or buying a new suite. Our position is INTEGRATE+WORKFLOW: wire an "
  "intake-to-pay agent across the systems the company already runs, own the approval orchestration and the policy "
  "guardrails (every action logged and auditable), and leave the spend system of record in place. The strategic point to "
  "make is that even the AI-native orchestrators are enterprise-first and configuration-heavy; the mid-market needs the "
  "outcome delivered, which is the integrator's job, not another platform to administer.")},
{"name":"Security",
 "headline":"SecOps is hiring to triage alerts it can't keep up with — the strongest deploy-an-agent signal",
 "sub":"Tier-1 investigation is being automated; the SIEM stays, the L1 seat compresses",
 "workflow":["Alert fires (~4,400/day)","L1 triage + context","Investigate / escalate","Remediate"],
 "vendors":["Incumbents: Splunk, Microsoft Sentinel, Google SecOps, QRadar","AI-native: Prophet, Torq HyperSOC, Dropzone ($57M), Radiant; SOAR: Tines ($1.1B)"],
 "disruption":["Agents investigate 100% of alerts end-to-end; analysts validate (90%+ FP today)","Often self-funds via SIEM-ingest reduction; legacy SOAR playbooks obsolete"],
 "opportunity":["Mid-market + MSSPs can't run a Prophet/Torq deployment alone","Deploy + tune an investigation agent on the existing SIEM"],
 "positioning":["DEPLOY+TUNE: stand up + tune the agent + cross-tool correlation","KEEP framing: the SIEM stays SoR; we make it finally keep up"],
 "notes":("Security has the single strongest 'deploy an agent now' signal in the portfolio, because the buyers broadcast "
  "their pain by posting jobs. The workflow today: an alert fires — a typical SOC sees ~4,400 a day — an L1 analyst "
  "triages and gathers context, investigates or escalates, and remediates, with over 90% of alerts proving to be false "
  "positives and analysts investigating only a third. Incumbents Splunk, Microsoft Sentinel, Google SecOps and QRadar own "
  "the SIEM; AI-natives Prophet, Torq HyperSOC, Dropzone ($57M raised) and Radiant investigate autonomously, while Tines "
  "($1.1B valuation) leads the SOAR-replacement motion as legacy playbooks are declared obsolete. The disruption is that "
  "agents investigate 100% of alerts end-to-end and analysts shift to validating completed investigations; notably the "
  "deployment often self-funds by letting teams cut SIEM ingest costs. The opportunity is that mid-market security teams "
  "and MSSPs cannot stand up and tune a Prophet or Torq deployment alone, and they are regulated and risk-averse. "
  "DataStaqAI's position is DEPLOY+TUNE: stand up and tune an investigation agent on the customer's existing SIEM, wire "
  "the cross-tool correlation, and frame it as KEEP/enrichment — the SIEM remains the system of record and the agent "
  "makes it finally keep up. The go-to-market instruction is to treat L1/Tier-1 SOC-analyst job postings as the lead "
  "list: every posting is an account drowning in alerts. And the business case writes itself twice — analyst time "
  "recovered plus a SIEM-ingest reduction that, in seven-figure SIEM estates, can exceed the cost of the engagement.")},
{"name":"Legal",
 "headline":"Legal research is where a $20 tool already matches a $270 seat — the mid-firm wedge",
 "sub":"Lookup-and-draft is automated; the citator corpus and the judgment stay",
 "workflow":["Legal question","Search Westlaw/Lexis (5–15 hr/wk)","Read + assess cases","Draft memo / redline"],
 "vendors":["Incumbents: Westlaw / CoCounsel, Lexis+ Protégé","AI-native: Harvey ($11B, $1.2–2K/seat), Legora, Spellbook"],
 "disruption":["Lookup-and-draft loop collapses; 25–30% of research is unbillable today","Anthropic's Claude legal plug-ins → ~$285B incumbent selloff"],
 "opportunity":["45–250-attorney firms priced out of Harvey's ~$360K entry","Citator-verified research/draft agent + AI-use governance"],
 "positioning":["INTEGRATE+WORKFLOW: research/draft agent verified to official reporters","Mid-firm price; corpus/citator kept as hybrid; hallucination guardrail"],
 "notes":("Legal is the function where the price dislocation is most vivid. The workflow today: a legal question triggers a "
  "Westlaw or Lexis search — lawyers spend 5–15 hours a week on research, juniors more — followed by reading and assessing "
  "cases and drafting a memo or redline, with 25–30% of that research time written off or unbillable. Incumbents "
  "(Thomson Reuters' Westlaw/CoCounsel, LexisNexis' Lexis+ Protégé) hold the proprietary corpus and citator; AI-natives "
  "Harvey ($11B valuation, $1,200–2,000 per seat, ~$360K entry), Legora and Spellbook attack the research-and-draft loop. "
  "The disruption is twofold: the lookup-and-draft loop collapses, and the category was repriced overnight when "
  "Anthropic's Claude legal plug-ins triggered a roughly $285B selloff across legal-data and software stocks — but the "
  "data fortresses held, which is the strategic lesson: sell on top of the corpus, never as a thin wrapper. The "
  "opportunity is the 45–250-attorney mid-size firm priced out of Harvey's entry but needing more than a $20 consumer "
  "chat tool, and acutely exposed to hallucination risk (firms have been sanctioned for fake citations). DataStaqAI's "
  "position is INTEGRATE+WORKFLOW: a research-and-draft agent whose citations are verified against official reporters with "
  "a citator-verification pass, delivered at mid-firm price with the AI-use governance that keeps the firm out of the "
  "headlines, while the proprietary corpus and citator stay as a hybrid. The pitch line: a $20 tool now matches a $270 "
  "seat, but one bad citation gets you sanctioned — we deliver the verified, governed version.")},
{"name":"Analytics",
 "headline":"Dashboards go unused; the agent answers the question — but only over a governed semantic layer",
 "sub":"Text-to-SQL collapses the BI interface; the warehouse and the semantic layer stay",
 "workflow":["Stakeholder question","Analyst writes SQL / builds dashboard","Dashboard ignored","Slack the analyst anyway"],
 "vendors":["Incumbents: Looker (~$150K), Power BI, Tableau","AI-native: Snowflake Cortex, Databricks Genie, ThoughtSpot, Hex, Julius"],
 "disruption":["NL→SQL answers in context; '1,200 dashboards deleted, nobody noticed'","Accuracy is ~87%→~10% on real schemas without a semantic layer"],
 "opportunity":["The semantic/context layer is the real work; cross-platform has no home","Build the semantic layer + wire an ask-the-warehouse agent"],
 "positioning":["INTEGRATE+WORKFLOW (occasionally BUILD the semantic layer)","Verified NL→SQL over the warehouse; the warehouse stays SoR"],
 "notes":("Analytics is where the agent both threatens and depends on the existing stack, which makes the delivery argument "
  "unusually strong. The workflow today is quietly broken: a stakeholder asks a question, an analyst writes SQL or builds "
  "a dashboard, the dashboard goes largely unused, and the stakeholder Slacks the analyst anyway — one team deleted 1,200 "
  "dashboards and nobody noticed, and dashboards account for as little as 5% of how data actually gets consumed. "
  "Incumbents Looker (~$150K/yr, dev-heavy), Power BI and Tableau own the BI seat; AI-natives Snowflake Cortex Analyst, "
  "Databricks Genie, ThoughtSpot, Hex and Julius offer natural-language querying. The disruption is that NL-to-SQL "
  "collapses the interface and answers in context — but the critical, defensible nuance is that accuracy falls from ~87% "
  "on toy schemas to ~10% on real enterprise schemas without a semantic layer, and the warehouse-native tools are locked "
  "to their own platform so cross-platform questions have no home. That nuance is the opportunity: the semantic and "
  "context layer is the unglamorous, high-value work, and nobody owns it for the mid-market. DataStaqAI's position is "
  "INTEGRATE+WORKFLOW, occasionally BUILD — construct the governed semantic layer and wire an ask-the-warehouse agent "
  "that returns verified answers with the metric definition attached, leaving the warehouse as the system of record. The "
  "pitch is that the model is not the moat and the dashboard is dead; the durable asset is governed context plus an agent "
  "that answers — and building and operating that is delivery, not a product the buyer can self-serve.")},
{"name":"Engineering",
 "headline":"Engineering is where DataStaqAI builds, not integrates — owned-code modernization is the sharpest play",
 "sub":"Code review is a deploy-and-tune attach; legacy and low-code escape are true BUILD plays",
 "workflow":["Legacy / low-code app","Tribal knowledge retires","Manual rewrite (70% fail)","Maintain forever"],
 "vendors":["Incumbents: GitHub Copilot; OutSystems ($9.5B), Mendix, Retool ($3.2B)","AI-native: CodeRabbit, Greptile, Qodo (review); Mechanical Orchard, Replay (modernize)"],
 "disruption":["Behavior-grounded modernization captures tribal knowledge from runtime","Reverse-engineer low-code → owned React/Node in months, not an 18-month rewrite"],
 "opportunity":["The leading modernizers are Global-2000-only; the mid-market is unserved","BUILD the owned-code escape; DEPLOY code-review as an attach"],
 "positioning":["BUILD (sharpest play): owned code the client keeps; no off-the-shelf sub","DEPLOY+TUNE: context-indexed review agent at commit time"],
 "notes":("Engineering is the one cluster where DataStaqAI's posture flips from integrate to build, and it is the sharpest "
  "play in the entire portfolio. The painful workflow is modernization: a legacy or low-code application runs the "
  "business, the engineers who understand it retire, a manual rewrite is attempted and fails ~70% of the time, and the "
  "team maintains an unreadable system forever. Two sub-stories sit here. Code review is a commodity attach: incumbents "
  "(GitHub Copilot) and cheap, viral AI-natives (CodeRabbit, Greptile, Qodo) already do it well, so it is a DEPLOY+TUNE "
  "service, not a build. The real prize is modernization and low-code escape: incumbents are the cages themselves "
  "(OutSystems at $9.5B, Mendix, Retool at $3.2B), and AI-natives Mechanical Orchard and Replay pioneered "
  "behavior-grounded modernization that captures tribal knowledge from the running system and reverse-engineers low-code "
  "into owned React/Node in months rather than an 18-month rewrite. The decisive fact is that the leading modernizers are "
  "explicitly Global-2000-only — Mechanical Orchard even states its platform is built to be operated and delivered by "
  "system integrators — so the mid-market is unserved by design. DataStaqAI's position is BUILD: deliver owned, "
  "git-native code the client keeps, with no off-the-shelf substitute, using the same behavior-first method the leaders "
  "validated; and DEPLOY+TUNE a context-indexed review agent at commit time as an attach. This is where we sell delivery "
  "that cannot be bought as a subscription, which is the highest-defensibility position in the book — lead here.")},
{"name":"Operations",
 "headline":"Operations is where enrichment wins — make the predictive and ITSM investment finally pay off",
 "sub":"IT/employee support and predictive ops are KEEP plays: ride the data, fix the workflow",
 "workflow":["Incident / request","Manual triage / ticket","Chase + resolve","Recurring toil"],
 "vendors":["Incumbents: ServiceNow (Autonomous Workforce), Atlassian; predictive: Honeywell, GE, Siemens","AI-native: Moveworks (→ServiceNow), Aisera (→Automation Anywhere); Augury, Uptake"],
 "disruption":["L1 service-desk AI specialists resolve password/access/provisioning end-to-end","Predictive: fuse signals → work orders, not alarms (false positives = 40% of wrench time)"],
 "opportunity":["Mid-market can't run Moveworks/Augury-scale deployments alone","Deploy + tune the agent on the existing ITSM / sensor stack"],
 "positioning":["DEPLOY+TUNE / KEEP: enrichment that compounds the data moat","Trustworthy triage + work-order agent; the platform stays SoR"],
 "notes":("Operations closes the function tour on the KEEP/enrichment pattern, which matters because it shows DataStaqAI is "
  "not only a disruptor but an amplifier of investments the customer already made. Two operations sub-domains share a "
  "shape. In IT and employee support, the workflow today is incident-or-request, manual triage and ticketing, chase and "
  "resolve, repeat — and the market just consolidated dramatically: ServiceNow acquired Moveworks (Dec 2025) and launched "
  "an Autonomous Workforce with an out-of-the-box Level-1 Service Desk AI Specialist that resolves password resets, "
  "access and provisioning end-to-end, while Aisera (acquired by Automation Anywhere) reports 65–90% deflection. In "
  "industrial operations, predictive maintenance incumbents (Honeywell, GE Vernova, Siemens) and AI-natives (Augury, "
  "Uptake) ride proprietary sensor data, where the failure mode is alarm fatigue — false positives consume ~40% of "
  "wrench time and a real failure once went unnoticed for 11 days at a $340K cost. The disruption in both is the same: "
  "agents that fuse signals and emit a work order rather than another alert. The opportunity is that mid-market operations "
  "teams cannot run a Moveworks- or Augury-scale deployment alone. DataStaqAI's position is DEPLOY+TUNE under a KEEP "
  "framing: stand up and tune the agent on the customer's existing ITSM or sensor stack, build the trustworthy triage and "
  "work-order workflow, and let the platform remain the system of record — the agent makes the investment they already "
  "made finally pay off. For regulated, risk-averse operations buyers, that 'enrichment, not replacement' framing is the "
  "one that gets to yes, and it rounds out the function map ahead of Chapter 4's competitive deep-dive.")},
]
for i,fn in enumerate(FN):
    build(fn, 9+i)

out=H/"DataStaqAI-Book-Ch3-Business-Use-Cases.pptx"
d.save(str(out)); print("OUTPUT:",out,"| slides:",d.n)

# spec
nt=[sl.notes_slide.notes_text_frame.text for sl in d.prs.slides]
spec=["# Chapter 3 — Business Use Cases (Slides 9–18)\n",
      "Each slide: WORKFLOW TODAY flow + 4 cards (Current vendors / AI disruption / Opportunity / DataStaqAI position) + 300w speaker notes. Vendors source-traceable.\n"]
for i,(fn,t) in enumerate(zip(FN,nt)):
    spec+=[f"\n## Slide {9+i} — {fn['name']}: {fn['headline']}\n",
           f"**Workflow today.** {' → '.join(fn['workflow'])}\n",
           f"**Current vendors.** {' · '.join(fn['vendors'])}\n",
           f"**AI disruption.** {' · '.join(fn['disruption'])}\n",
           f"**Opportunity.** {' · '.join(fn['opportunity'])}\n",
           f"**DataStaqAI positioning.** {' · '.join(fn['positioning'])}\n",
           f"**Speaker notes.**\n\n{t}\n"]
(H/"Chapter3-Business-Use-Cases.md").write_text("\n".join(spec),encoding="utf-8")
print("SPEC:",H/"Chapter3-Business-Use-Cases.md")
