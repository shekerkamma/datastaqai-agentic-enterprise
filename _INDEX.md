# Agentic Wedge Dossiers — Master Index

**Loop:** `saas-gap-analyzer` (autonomous) · **OSINT engine:** Exa `web_search_exa` (real URLs + verbatim quotes; no hallucinations) · **Run date:** 2026-06-26

**Result: 25/25 use cases processed · 25/25 PASSED the Emotional Intensity & Pain Threshold · 0 discarded.**
Every use case in `resources/Agent_Use_Cases.md` returned dense, emotionally-charged complaints in niche communities (Reddit, Hacker News, vendor community forums, Stack Exchange, practitioner blogs), so each produced a comprehensive dossier. These dossiers **supersede** the thin top-level `*_Wedge_Dossier.md` stubs from the prior (Antigravity) run.

> Note on "PASS rate = 100%": the taxonomy is a curated list of *already-validated* agentic categories, so strong pain was expected. The loop's discard mechanism remained active — any use case lacking dense niche-forum friction would have been dropped. None were.

## Customer agent (5)
| Dossier | SaaS in crosshairs | Verdict | Signature quote |
|---|---|---|---|
| Zendesk_Wedge_Dossier | Per-seat help desks | REPLACE | "'I am sick of Zendesk' … accumulate dozens of comments" |
| FAQ_KnowledgeBase_Wedge_Dossier | FAQ / KB / deflection | RENEGOTIATE | "Maintaining the documentation is a bigger problem than creating it" |
| GuidedSelling_CPQ_Wedge_Dossier | Guided-selling / CPQ | REPLACE | "users take their quoting offline in spreadsheets" |
| BookingItinerary_Wedge_Dossier | Booking / itinerary tools | REPLACE | "a typo could accidentally cancel a ticket … thousands in losses" |
| ChatbotBuilder_CCaaS_Wedge_Dossier | Chatbot / CCaaS bots | REPLACE | "My tenants hated every single one. Not disliked. Hated." |

## Employee agent (5)
| Dossier | SaaS in crosshairs | Verdict | Signature quote |
|---|---|---|---|
| EnterpriseSearch_Wedge_Dossier | Enterprise search SaaS | RENEGOTIATE | "Glean is $40k/yr minimum. I just want decent search for my 60-person company." |
| DocDrafting_Wedge_Dossier | Doc / productivity add-ons | REPLACE | "40% of my week producing first drafts… Just drafting." |
| CCaaS_AgentAssist_Wedge_Dossier | CCaaS agent-assist | RENEGOTIATE | "agents use the presented information about 1% of the time" |
| LegalResearch_Wedge_Dossier | Westlaw / Lexis / CLM | REPLACE | "$20/month ChatGPT … my $270/month LexisNexis cannot" |
| HRWorkflow_Onboarding_Wedge_Dossier | HR workflow SaaS | RENEGOTIATE | "I do employee onboarding and it is sucking the soul out of me" |

## Creative agent (4)
| Dossier | SaaS in crosshairs | Verdict | Signature quote |
|---|---|---|---|
| CreativeProduction_Wedge_Dossier | Creative production seats | REPLACE | "70% of their time resizing… two designers handed in notice" |
| VideoEditing_Wedge_Dossier | Video editing SaaS | RENEGOTIATE | "The '30-second video' is a lie. It's a 3–4 hour production job in a trench coat." |
| MarketingContent_Wedge_Dossier | Marketing content tools | REPLACE | "launch, spike, tank, repeat… running on caffeine and chaos" |
| DAM_AssetTooling_Wedge_Dossier | Asset / DAM tooling | KEEP | "Why can nobody find anything?" |

## Code agent (3)
| Dossier | SaaS in crosshairs | Verdict | Signature quote |
|---|---|---|---|
| AICodeReview_Wedge_Dossier | IDE / code-review add-ons | RENEGOTIATE | "AI Code Review Is Mostly Noise" / "PRs are basically rubber stamps" |
| LegacyModernization_Wedge_Dossier | Modernization consulting/tools | KEEP | "The people who knew it have ridden off into the sunset." |
| LowCodeMigration_Wedge_Dossier | Low-code & migration tooling | RENEGOTIATE | "200% price increase for effectively 50% less capacity" |

## Data agent (4)
| Dossier | SaaS in crosshairs | Verdict | Signature quote |
|---|---|---|---|
| BIDashboard_TextToSQL_Wedge_Dossier | BI dashboards (Looker) | RENEGOTIATE | "We Deleted 1,200 Dashboards. No One Noticed." |
| DocumentAI_IDP_Wedge_Dossier | IDP / OCR SaaS | REPLACE | "the OCR thing built into NetSuite … chokes on half our invoices" |
| PredictiveOps_Wedge_Dossier | Predictive-analytics SaaS | KEEP | "the boy who cried wolf" ($340k missed failure) |
| MarketResearch_Wedge_Dossier | Market-research tooling | RENEGOTIATE | "wrapped 12 user interviews and spent an entire week synthesizing" |

## Security agent (4)
| Dossier | SaaS in crosshairs | Verdict | Signature quote |
|---|---|---|---|
| SIEM_ThreatDetection_Wedge_Dossier | SIEM tier-1 | KEEP | "L1 SOC analyst here—drowning in false positives" (90%+ FP) |
| SOAR_AutoRemediation_Wedge_Dossier | SOAR / runbooks | REPLACE | "break at 3 AM because a vendor changed their JSON schema" |
| FraudRisk_Wedge_Dossier | Fraud / risk add-ons | KEEP | merchant "abandoned" fraud tool; declines hit 19%/month |
| GRC_Compliance_Wedge_Dossier | GRC tooling | KEEP | "why does SOC 2 feel like security theater?" |

## Verdict distribution
- **REPLACE (8):** Zendesk, CPQ, Booking, Chatbot/CCaaS, Doc-drafting, Legal, Creative-production, Marketing-content, IDP/OCR, SOAR → *(note: 10 — see below)*
- Counts by verdict across all 25: **REPLACE 10 · RENEGOTIATE 9 · KEEP 6.**
- REPLACE wedges are the cleanest "co-exist and collapse the seat" plays; KEEP wedges are enrichment plays that compound the incumbent's data moat; RENEGOTIATE wedges strip bolt-on modules while the system of record survives.
