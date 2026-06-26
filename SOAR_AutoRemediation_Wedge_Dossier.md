# Agentic Wedge Dossier — SOAR / Runbooks (Agentic Auto-Remediation)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — practitioners describe the "SOAR Maintenance Tax": playbooks "break at 3 AM because a vendor changed their JSON schema"; connector repair takes 4–6 weeks.

## 1. Target SaaS & Use Case
- **Agent Type:** Security
- **Use Case:** Agentic auto-remediation
- **SaaS in the crosshairs:** SOAR / runbook-automation seats (Phantom/XSOAR/Swimlane-class)
- **Taxonomy Verdict:** REPLACE (system of record stays for audit; playbook-authoring seats go)
- **Deployed proof points:** Security-agent deployments writing detection rules, isolating workloads, deploying honeytokens within a policy envelope

## 2. OSINT Source Map & Methodology
Mined SOAR-maintenance post-mortems, a "playbooks are dead" analysis, and a practitioner's playbook-to-agent migration account.

| # | Source | URL |
|---|--------|-----|
| 1 | Prophet Security — SOAR playbooks: why they break | https://www.prophetsecurity.ai/blog/soar-playbook-maintenance-problem |
| 2 | D3 Security — The SOAR Maintenance Tax | https://d3security.com/blog/soar-maintenance-tax/ |
| 3 | BlinkOps — From Playbooks to Micro-Agents (practitioner) | https://www.blinkops.com/blog/from-playbooks-to-micro-agents |
| 4 | Simbian — SOAR Playbooks Are Dead | https://simbian.ai/blog/soar-ai-vs-ai-soc-vs-soar-automation |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **The 3 AM schema break.** BlinkOps practitioner: *"I've built SOAR playbooks from scratch, maintained them when they break at 3 AM because a vendor changed their JSON schema, and tried to explain to management why the 'automation platform' still needs a full-time engineer to keep running."* And: *"you'd spend a day debugging which step in which sub-playbook failed because some vendor changed a JSON field name."* (Source 3)
- **The hidden tax.** D3: *"Year three looks different. Hundreds of playbooks. Advanced logic living in Python scripts. Integrations that break the moment a vendor changes an API. Somewhere along the way, one of your engineers became the platform's full-time owner. Not by job description. By necessity."* *"Coverage equals playbooks. Playbooks equal code. Code needs an owner."* Connector repair: *"4 to 6 weeks of engineering time."* (Source 2)
- **Silent failures.** Prophet: *"A vendor updates its detection API, deprecates a field… The playbook continues to execute but operates on missing or malformed data… usually returns a null rather than throwing an exception. Downstream logic runs against the null, and the playbook completes without errors."* (Source 1)
- **The model, not the product, is broken.** Simbian: *"SOAR automation runs human-authored playbooks… Brittle, high-maintenance… When the alert pattern changes, and it always does, the playbook breaks and the engineer rewrites it."* (Source 4)

## 4. User Psychographics
- **Roles:** SOAR architects/engineers, detection engineers, SOC automation leads.
- **Emotional state:** Trapped as the platform's accidental full-time owner, paged at 3 AM over JSON schema changes, unable to justify the maintenance tax that never appeared on the order form.
- **The acute bottleneck:** Static, deterministic playbooks whose coverage scales linearly with maintenance burden — they break silently on every upstream API/schema/detection change.

## 5. The Agentic Wedge
**Wedge name:** "Playbook-Free Response Agent (Reason → Act, Self-Healing)"

**How it works:** An agent that reasons about each alert in context and triggers the *deterministic* response actions (isolate host, ticket, notify) without a static playbook to author or maintain — with self-healing integrations that detect API/schema drift and auto-correct, ending the 3 AM page.

**Why it wins:** It removes the static asset (the playbook) and with it the proven maintenance tax — architect dependency, playbook sprawl, silent integration failures, 4–6-week connector repairs. REPLACE within policy: the agent becomes the responder; the system of record stays for audit; the playbook-authoring seats go.

**Buyer trigger:** A SOAR architect leaving (institutional knowledge walks out) or maintenance hours exceeding hours saved.
