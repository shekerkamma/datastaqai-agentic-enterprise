# Agentic Wedge Dossier — CCaaS Agent-Assist (Contact-Center Agent Assist)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — a contact-center operator's own audit: agents use the assist tool "about 1% of the time"; 45% actively avoid it.

## 1. Target SaaS & Use Case
- **Agent Type:** Employee
- **Use Case:** Contact-center agent assist (real-time next-best-action)
- **SaaS in the crosshairs:** CCaaS agent-assist add-ons (push-prompt modules)
- **Taxonomy Verdict:** RENEGOTIATE (enriches the CCaaS platform; displaces standalone assist add-ons)
- **Deployed proof points:** Humana Agent Assist (next-best-action to live reps), Vodafone

## 2. OSINT Source Map & Methodology
Mined a contact-center practitioner's experiment write-up, RTAA vendor post-mortems, and an on-screen-clutter analysis.

| # | Source | URL |
|---|--------|-----|
| 1 | No Jitter — push vs pull agent assistance (1% usage audit) | https://www.nojitter.com/contact-centers/contact-center-experimenting-with-push-versus-pull-for-agent-assistance |
| 2 | InfiniteCX — Agent Assist Is Broken | https://www.infinitecx.ai/post/agent-assist-is-broken-why-tools-underperform-how-to-fix-them |
| 3 | Cirrus — Real-Time Assist: Backup, Not Big Brother | https://www.cirrusconnects.com/blog/real-time-assist-that-feels-like-backup-not-big-brother/ |
| 4 | Hear.ai — The AI Copilot Myth | https://www.hear.ai/blog/ai-copilot-myth-real-time-intelligence |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **The damning self-audit.** No Jitter, a contact-center team running its own push-assist pilot: *"The results are clear: no one is using it. Manual audits show that agents use the presented information about 1% of the time. Overall feedback from agents is that it's more annoying than helpful."* (Source 1)
- **Distraction dressed as help.** InfiniteCX: *"Many agent assist tools pop up suggestions or scripts at inconvenient moments. Instead of supporting agents, they distract them. Agents get overwhelmed by constant notifications… Agents quickly learn to ignore these prompts, defeating the purpose."* (Source 2)
- **Ignored or actively resented.** Cirrus: *"The vendor promised it would solve everything. But now agents either ignore it or actively resent it… They'll smile and nod in the rollout meeting and then quietly do everything they can to avoid using it."* (Source 3)
- **High-tech clutter on an amnesiac copilot.** Hear.ai: *"45% of agents actively avoid using new tech because it disrupts their flow… When an AI Copilot misinterprets a frustrated customer as 'excited' and prompts an upsell script it destroys the agent's credibility."* The flaw: *"they are 'stateless'… If your AI is only listening to the live call it is functionally amnesiac. It treats every interaction as Day One."* (Source 4)

## 4. User Psychographics
- **Roles:** Contact-center agents, CX ops leaders, WFM/enablement managers.
- **Emotional state:** Agents feel surveilled and distracted ("Big Brother"); ops leaders feel burned — they bought the tool, agents won't touch it, and the vendor blamed "knowledge base quality."
- **The acute bottleneck:** A "push" model that fires generic, context-blind prompts mid-call, adding cognitive load to people already juggling 3 screens and 5 tabs.

## 5. The Agentic Wedge
**Wedge name:** "Pull-First, Full-Context Assist Agent"

**How it works:** An agent the rep *invokes* on demand (pull, not push), grounded in the full customer relationship (history, prior calls, churn risk) rather than the last 10 seconds of audio — so suggestions are relevant when summoned and silent otherwise. Backs up judgment instead of scripting it.

**Why it wins:** It directly fixes the two proven failures — 1% usage (push fatigue) and amnesiac/stateless context. The CCaaS platform stays as system of record (RENEGOTIATE), but the resented standalone push-assist add-on is displaced by an agent agents actually use.

**Buyer trigger:** A usage audit showing the existing assist add-on is touched ~1% of the time.
