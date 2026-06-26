# Agentic Wedge Dossier — HR Workflow SaaS (HR / Onboarding Agent)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — r/humanresources thread "I do employee onboarding and it is sucking the soul out of me," plus a mapped 75-person company burning 312 hrs/month and $125k/yr.

## 1. Target SaaS & Use Case
- **Agent Type:** Employee
- **Use Case:** HR / onboarding agent
- **SaaS in the crosshairs:** HR workflow SaaS (Workday, Rippling, BambooHR workflow modules)
- **Taxonomy Verdict:** RENEGOTIATE (keep the system of record; drop the workflow seats)
- **Deployed proof points:** Grupo Ruiz (Gemini Enterprise team workflows), employee-agent onboarding deployments

## 2. OSINT Source Map & Methodology
Mined a Reddit r/humanresources-sourced builder brief, HR-system-sprawl analyses, and an integration engineer's first-person account.

| # | Source | URL |
|---|--------|-----|
| 1 | SaaS Fieldwork — Builder Brief (Reddit r/humanresources thread) | https://www.saasfieldwork.com/p/builder-brief-hr-onboarding-workflow |
| 2 | Integrow — HR's 8-System Nightmare ("Stack of Sadness") | https://integrow.com/blog/hr-system-sprawl-onboarding-fix/ |
| 3 | Petie Clark — Why HR System Integrations Are Still a Dumpster Fire in 2026 | https://blog.petieclark.com/why-hr-system-integrations-are-still-a-dumpster-fire-in-2026/ |
| 4 | KnowledgeLib — Employee Onboarding Automation: HRIS to IT | https://knowledgelib.io/business/erp-integration/employee-onboarding-automation/2026 |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **The thread title says it all.** Reddit r/humanresources (via SaaS Fieldwork): *"I do employee onboarding and it is sucking the soul out of me."* In-thread: *"Every new hire requires 10+ manual steps - paperwork, provisioning, intro emails, access requests, device coordination, org chart updates, etc. Then half the time I have to resend links because people lose something."* And: *"No one owns the process end-to-end, so I end up doing all the follow-up. It's burning me out."* HR becomes *"a human router."* (Source 1)
- **The Stack of Sadness.** Integrow: HR is *"buried in 'The Stack of Sadness'—an overwhelming cluster of 8 disconnected systems."* A mapped 75-person company found *"312 hours/month were being spent on manual admin, $125,000/year was wrapped up in hidden operational costs… 5 days to provision a new hire fully."* HR spends *"up to 60% of their time on data entry and workarounds."* (Source 2)
- **Held together with duct tape and prayer.** Integration engineer Petie Clark: *"SSO is solved tech, but identity lifecycle management is still a mess… You end up building middleware… debugging why Sarah from Accounting lost access to Salesforce when she changed departments."* And: *"HR integrations are never 'done.' Workday updates their API quarterly (breaking changes monthly)."* (Source 3)
- **The manual baseline is expensive and error-prone.** KnowledgeLib: manual IT-ticket-per-hire averages *"5-8 hours per employee"* with a *"15-25%"* error rate, versus event-driven provisioning at *"5-15 minutes."* (Source 4)

## 4. User Psychographics
- **Roles:** HR generalists, people-ops managers, onboarding coordinators at 100–500-person SMBs caught in the "tooling chasm."
- **Emotional state:** Burning out, feeling like "professional nags" and "human routers," blamed for a broken cross-functional process they don't control, drowning in side-spreadsheets.
- **The acute bottleneck:** The HRIS is a great database but a terrible *action-taker* — onboarding is a cross-functional orchestration job (HR↔IT↔Finance↔manager) with no system that actually executes the steps.

## 5. The Agentic Wedge
**Wedge name:** "Zero-Touch Onboarding Orchestrator"

**How it works:** An agent that fires on the HRIS new-hire trigger and *executes* the downstream chain — drafts/raises IT provisioning tickets, collects hardware/software needs from the hiring manager conversationally (Slack), monitors background-check portals, and updates the HRIS — turning HR from "human router" into approver.

**Why it wins:** It treats the HRIS as the untouchable system of record (RENEGOTIATE) but strips the per-seat workflow/case-management modules that never actually took the actions. Sells against the proven, quantified pain: 60% of HR time on data entry, 5-day provisioning, "burning me out."

**Buyer trigger:** A Day-5 new hire still without a laptop — and the HR person blamed for it.
