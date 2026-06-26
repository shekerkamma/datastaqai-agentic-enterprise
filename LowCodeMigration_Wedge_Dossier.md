# Agentic Wedge Dossier — Low-Code & Migration Tooling (App Build / Migration Automation)

> **Loop run:** saas-gap-analyzer · OSINT engine: Exa web_search · No hallucinations.
> **Verdict:** ✅ PASS — dense, verbatim HN/forum rage about lock-in and un-extractable logic; "Why OutSystems Ruined My Dev Job"; a 200% price hike for 50% less capacity.

## 1. Target SaaS & Use Case
- **Agent Type:** Code
- **Use Case:** App build / migration automation
- **SaaS in the crosshairs:** Low-code & migration tooling (OutSystems, Mendix, PowerApps-class)
- **Taxonomy Verdict:** RENEGOTIATE (agent replaces the routine slice; complex/bespoke work still needs humans)
- **Deployed proof points:** Code-agent deployments scaffolding apps + automating migrations

## 2. OSINT Source Map & Methodology
Mined two long-form **Hacker News** practitioner threads, a **Mendix Forum** migration thread, and a developer's "ruined my job" essay.

| # | Source | URL |
|---|--------|-----|
| 1 | Hacker News — no/low-code vendor lock-in critique | https://news.ycombinator.com/item?id=27985266 |
| 2 | Hacker News — PowerApps/Mendix/OutSystems evaluation | https://news.ycombinator.com/item?id=30663246 |
| 3 | Mendix Forum — moving from OutSystems to Mendix (pricing) | https://community.mendix.com/link/spaces/app-development/questions/132239 |
| 4 | Michael Henderson (Medium) — Why OutSystems Ruined My Dev Job | https://medium.com/@michaelhenderson/why-outsystems-ruined-my-dev-job-3119828fd051 |

## 3. Emotional Friction — Verbatim & Near-Verbatim
- **The lock-in litany.** HN: *"they suffer from their business model, which often aims complete vendor lock in… Any apps build with it are not really property of the developer… Datamodel, Algorithm or business logic can not really be extracted from the low code platform… They have non or terrible git integration… it is incredibly painful to migrate your systems… onto a mature, open-source web development ecosystem."* (Source 1)
- **Easier to rebuild than to edit.** HN: *"it is often easier to rebuild a MS Power Automate flow from scratch than to substantially modify an existing one… simple business flows can rapidly become hard to read and update (much harder than code in fact)… 'spaghetti flows'."* (Source 2)
- **The pricing trap that forces migration.** Mendix Forum: *"We were moved from an unlimited AO plan to a limited plan and at a very large price increase. Even after weeks of negotiations we still ended up with a 200% price increase for effectively 50% less capacity."* The escape cost: migrating *"70 applications,"* discovering *"every single application is inherently treated as its own standalone architecture."* (Source 3)
- **The human cost.** Michael Henderson: *"OutSystems ruined the dream and hope I had… Instead, I was stuck dragging and dropping components… calling OutSystems customer support to see how to convert an integer to a string."* No local debugger: *"my boss would ask me why it is not working and I literally did not know because there is so much that happens under the covers."* (Source 4)

## 4. User Psychographics
- **Roles:** Developers and IT leads trapped on OutSystems/Mendix/PowerApps; architects evaluating an exit.
- **Emotional state:** Resentful and trapped — apps they built aren't legally theirs, logic can't be extracted, a license re-pricing forces a Herculean migration, and good engineers "look down on it."
- **The acute bottleneck:** Proprietary, un-exportable business logic + no git/debugger, so escaping (or even maintaining) the platform is a from-scratch rebuild.

## 5. The Agentic Wedge
**Wedge name:** "Lock-In Escape Agent (Low-Code → Owned Code)"

**How it works:** An agent that (1) reverse-engineers existing low-code apps into clean, git-native, owned source (React/.NET/SQL the team can inspect and debug), and (2) scaffolds new well-defined apps directly as real code — replacing the routine build/migration slice while humans own the complex/bespoke parts.

**Why it wins:** It attacks the two loudest pains — un-extractable logic/lock-in and forced-migration pricing — by producing code the customer actually owns, with real git and debugging. RENEGOTIATE: the agent replaces the routine slice that low-code monopolized; complex work stays human.

**Buyer trigger:** A low-code license re-pricing (e.g., "200% more for 50% less") that makes the lock-in unbearable.
