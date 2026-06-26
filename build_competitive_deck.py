#!/usr/bin/env python3
"""
Build the DataStaqAI "Agentic Use Cases — Competitive Landscape & Opportunity Map"
branded .pptx from the six COMPETITIVE_<cluster>.md deep-research files.

Parser-driven: reads the markdown at runtime, emits per-use-case slides
(title card -> incumbents -> AI-native challengers -> pricing -> the gap ->
DataStaqAI's play), auto-paginating dense sections. Hand-written framing slides
top and tail. Validates on save (pptxkit.Deck.save).
"""
import sys, re, os
from pathlib import Path

SKILL = "/home/shekerk/.claude/skills/branded-pptx-deck/scripts"
sys.path.insert(0, SKILL)
from pptxkit import Deck, Inches, Pt, PP_ALIGN  # noqa

HERE = Path("/mnt/d/New folder/Antigravity-test/antigravity-skills/wedge_dossiers")

CLUSTERS = [
    ("Customer", "COMPETITIVE_Customer.md", "Tier-1 customer-facing agents"),
    ("Employee", "COMPETITIVE_Employee.md", "Internal knowledge-worker agents"),
    ("Creative", "COMPETITIVE_Creative.md", "Content & creative-production agents"),
    ("Code",     "COMPETITIVE_Code.md",     "Engineering & modernization agents"),
    ("Data",     "COMPETITIVE_Data.md",     "Analytics, document & ops agents"),
    ("Security", "COMPETITIVE_Security.md", "SecOps, fraud & compliance agents"),
]

# ── markdown helpers ──────────────────────────────────────────────────────────
def clean(line: str) -> str:
    s = line.strip()
    s = re.sub(r'^>+\s*', '', s)
    s = re.sub(r'^[-*+]\s+', '', s)
    s = re.sub(r'^\d+[.)]\s+', '', s)
    s = re.sub(r'^#{1,6}\s+', '', s)
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)   # [text](url) -> text
    s = re.sub(r'https?://\S+', '', s)               # bare urls
    s = s.replace('**', '').replace('__', '').replace('`', '').replace('*', '')
    s = re.sub(r'\|', ' · ', s)                      # table pipes -> dots
    s = re.sub(r'\s{2,}', ' ', s).strip(' -—|')
    return s.strip()

def classify(subhead: str) -> str:
    h = subhead.lower()
    if 'source' in h: return 'skip'
    if 'market' in h: return 'market'
    if 'incumbent' in h: return 'incumbents'
    if 'challenger' in h or 'ai-native' in h or 'ai native' in h: return 'challengers'
    if 'pricing' in h or 'gtm' in h: return 'pricing'
    if 'gap' in h or 'white space' in h: return 'gaps'
    if 'datastaq' in h or 'opportunity' in h or 'positioning' in h or 'play' in h: return 'play'
    return 'other'

def parse_cluster(path: Path):
    """Return (usecases, synthesis_bullets).
    usecases = [ (display_name, {bucket: [bullets...]} ) ]"""
    usecases, synthesis = [], []
    cur_uc = None          # (name, dict)
    cur_bucket = None
    cur_is_synth = False
    text = path.read_text(encoding='utf-8', errors='ignore')
    for raw in text.splitlines():
        if raw.startswith('## '):
            title = raw[3:].strip()
            low = title.lower()
            cur_is_synth = ('synthesis' in low or 'spine' in low)
            if re.match(r'^\d+[.)]', title) and not cur_is_synth:
                name = re.sub(r'^\d+[.)]\s*', '', title)
                cur_uc = (name, {})
                usecases.append(cur_uc)
                cur_bucket = None
            else:
                cur_uc = None
                cur_bucket = 'synthesis' if cur_is_synth else None
            continue
        if raw.startswith('### '):
            sub = raw[4:].strip()
            b = classify(sub)
            if cur_uc is not None:
                cur_bucket = b
                if b not in ('skip',):
                    cur_uc[1].setdefault(b, [])
            elif cur_is_synth:
                cur_bucket = 'synthesis'
            continue
        # body line
        c = clean(raw)
        if not c or len(c) < 3:
            continue
        if cur_is_synth:
            synthesis.append(c)
        elif cur_uc is not None and cur_bucket and cur_bucket not in ('skip',):
            cur_uc[1].setdefault(cur_bucket, []).append(c)
    return usecases, synthesis

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

# ── spec assembly (two-phase so footer totals are correct) ────────────────────
specs = []  # list of dicts

def add(**kw): specs.append(kw)

# cover + framing
add(kind='cover')
add(kind='bullets', fill='navy', title='The thesis: every category split — and both sides left the same hole',
    subtitle='Why a delivery layer wins the agent era',
    bullets=[
        "Incumbents (Zendesk, Salesforce, Westlaw, Splunk, Workday, OutSystems, Looker) bolt AI onto the seat they defend — they will not cannibalise their own seat revenue.",
        "AI-native point solutions (Sierra ~$15.8B, Decagon $4.5B, Harvey $11B, Glean $7.2B, Torq, Vanta, Feedzai) build great agents — but enterprise-first, six-figure, and sold as products you must integrate, tune, own and operate.",
        "Both leave the mid-market underserved: priced out of $50K–$600K floors, no engineering bandwidth to integrate across systems, and unwilling to run yet another silo.",
        "DataStaqAI's wedge: the done-for-you delivery layer — we wire best-of-breed agents into your systems of record, own the client-specific workflow + governance, and run it. Outcome, not a subscription.",
    ])
add(kind='bullets', fill='white', title='The white space is now proven, not asserted',
    subtitle='The market has already conceded it',
    bullets=[
        "AI-natives are shipping 'managed / done-for-you' tiers because mid-market buyers can't operate the agents alone — Crescendo (BPO, bought PartnerHero's 3,000 CX staff), Botpress & Maven 'Managed', Decagon forward-deployed engineers, Sierra six-figure services.",
        "Mechanical Orchard — the best-funded behavior-first modernizer — says its platform is 'built to be operated and delivered by system integrators,' and serves only the Global 2000. The leading method requires a delivery layer.",
        "Frontier models kill thin wrappers, not data fortresses: Anthropic's Claude legal plug-ins triggered a ~$285B incumbent selloff, yet Thomson Reuters' and Glean's context moats held. So sell delivery + governed context + workflow ON TOP of the systems — never a wrapper.",
        "Pricing floors are collapsing ($0.40–1.50 per resolution; $10/mo travel agents). 'Managed' and 'cheap' are becoming table stakes — the defensible anchor is integration + workflow ownership + governance + the client owns the outcome.",
    ])
add(kind='bullets', fill='white', title='How the market competes — the patterns that repeat in every category',
    subtitle='Read these once; they recur on every cluster',
    bullets=[
        "Pricing is bifurcating, not converging: enterprise ACV ($50K–$4.8M/yr) vs usage/outcome ($0.40–1.50/resolution). The model you pick sets unit economics for years.",
        "AI-natives sit ON TOP of the incumbent's system of record (separate helpdesk; warehouse-locked text-to-SQL). Integration + a second tool is the hidden TCO.",
        "The model is no longer the moat — governed context is. Text-to-SQL scores ~87% on toy data but ~10% on real enterprise schemas; accuracy comes from the semantic layer.",
        "'Automated' often means 'organized manual work' — e.g. GRC evidence that's a manually-uploaded screenshot; the integration breaks silently and the dashboard stays green.",
        "Build-vs-buy is unresolved for the buyer: incumbents win on distribution/compliance, AI-natives on agent quality; 58% run both. Nobody sells the delivery of the combination.",
    ])
add(kind='bullets', fill='white', title='The five recurring gaps — this is the opportunity map',
    subtitle='Every cluster is a variation on these',
    bullets=[
        "G1 — Mid-market is underserved: priced out of six-figure floors (Glean $40K+, Harvey ~$360K, Cresta 100-seat min, Revenue Cloud $200/seat).",
        "G2 — No engineering bandwidth to integrate/own: AI-natives require dedicated agent engineers; GRC blockers are integration + skills, not appetite.",
        "G3 — Point solutions don't span the buyer's systems: warehouse-locked analytics; agents needing a separate helpdesk.",
        "G4 — Products, not outcomes: managed/BPO tiers out-positioning pure platforms; 'neither replaces a security program.'",
        "G5 — Governed context / provenance is the real, unglamorous work: the semantic layer drives accuracy; source-grounded evidence beats screenshots.",
    ])

# clusters
for cname, fname, csub in CLUSTERS:
    path = HERE / fname
    if not path.exists():
        continue
    usecases, synth = parse_cluster(path)
    add(kind='section', kicker=f'CLUSTER · {cname.upper()} AGENT', title=f'{cname} agents', subtitle=csub)
    if synth:
        for j, ch in enumerate(chunks(synth, 4)):
            add(kind='bullets', fill='navy',
                title=f'{cname} cluster — the one-slide synthesis' + (' (cont.)' if j else ''),
                subtitle="How the cluster competitive picture nets out", bullets=ch)
    for name, buckets in usecases:
        market = buckets.get('market', [])
        add(kind='titlecard', name=name, cluster=cname, market=market[:6])
        order = [
            ('incumbents', 'Incumbents — how they defend the seat', 7, 'white'),
            ('challengers', 'AI-native challengers — who & how', 6, 'white'),
            ('pricing', 'Pricing & go-to-market patterns', 7, 'white'),
            ('gaps', 'The gap / white space', 7, 'white'),
            ('play', "DataStaqAI's play — position & wedge", 7, 'navy'),
        ]
        for key, label, per, fill in order:
            items = buckets.get(key, [])
            if not items:
                continue
            pages = list(chunks(items, per))
            for j, ch in enumerate(pages):
                add(kind='bullets', fill=fill,
                    title=label + (' (cont.)' if j else ''),
                    subtitle=name, bullets=ch)

# closing
add(kind='section', kicker='WHERE WE WIN', title='DataStaqAI: the delivery layer for the agent era',
    subtitle='Three plays, ranked by fit')
add(kind='bullets', fill='white', title='Three plays, ranked by fit',
    subtitle='The same motion, three postures',
    bullets=[
        "BUILD (sharpest): Low-code escape (#17) + Legacy modernization (#16) — outcome = owned code the client keeps; no off-the-shelf substitute; competitors explicitly need a delivery/SI layer.",
        "INTEGRATE + WORKFLOW (broadest): wire a best-of-breed agent into the client's system of record + own the client-specific workflow + governance (CPQ, IDP, support, legal, fraud, GRC, search…).",
        "DEPLOY + TUNE (fastest): stand up + tune a mature tool the client can't operate alone (SIEM, predictive ops, code-review, agent-assist) — often self-funding via SIEM-ingest / seat reduction.",
        "The one-line pitch: 'The agent tools are real — but they're products you must integrate, tune, own and operate. We deliver the outcome: the agent wired into your systems, the workflow built, the thing running. You keep your systems of record; we run the agent layer on top.'",
    ])
add(kind='bullets', fill='white', title='Go-to-market sequence',
    subtitle='How to enter and expand',
    bullets=[
        "Lead with the BUILD plays for credibility (delivery you can't buy) → land INTEGRATE plays for volume → attach DEPLOY+TUNE for fast wins.",
        "Hottest entry signals: SOC-analyst hiring posts (SIEM), legal 'which-tools' re-evaluations, Salesforce CPQ End-of-Sale, low-code license re-pricing, failed-OCR AP rollouts.",
        "Differentiator to repeat in every deal: mid-market price + done-for-you integration + client owns the outcome + governance — vs enterprise ACV + DIY integration + another silo.",
        "Don't compete on 'managed' or price alone — both are commoditising. Anchor on integration depth, workflow ownership, governed context, and owned outcomes.",
    ])
add(kind='cover_end')

# ── render ────────────────────────────────────────────────────────────────────
d = Deck(footer="DataStaqAI · Agentic Competitive Landscape & Opportunity Map · 2026")
b = d.b
TOTAL = len(specs)

def body_box(s, bullets, *, color=None, top=Inches(1.72), height=Inches(5.05)):
    runs = [{"text": t, "bullet": True, "space_before": 7, "size": 13.5,
             "color": color if color else b.INK} for t in bullets]
    d.text(s, runs, d.M, top, d.CW, height, shrink=True, ls=1.08)

for i, sp in enumerate(specs):
    page = i + 1
    k = sp['kind']
    if k == 'cover':
        s = d.slide(fill=b.NAVY)
        d.rect(s, d.W - Inches(0.22), 0, Inches(0.22), d.H, b.TEAL)
        d.text(s, "COMPETITIVE LANDSCAPE & OPPORTUNITY MAP", d.M, Inches(1.5), Inches(11), Inches(0.4),
               size=15, color=b.TEAL, bold=True)
        d.text(s, "Agentic Use Cases:\nThe Incumbents, The Challengers, The Gaps", d.M, Inches(2.15),
               Inches(11.4), Inches(2.0), size=42, color=b.WHITE, bold=True, shrink=True)
        d.rect(s, d.M, Inches(4.35), Inches(2.0), Inches(0.06), b.TEAL)
        d.text(s, "DataStaqAI — the done-for-you delivery layer for the agent era", d.M, Inches(4.6),
               Inches(11), Inches(0.5), size=18, color=b.LIGHT_TEAL)
        d.text(s, "25 use cases · 6 agent clusters · sourced competitor profiles, pricing, funding & gaps", d.M,
               Inches(5.15), Inches(11), Inches(0.4), size=13, color=b.MUTED)
        continue
    if k == 'cover_end':
        s = d.slide(fill=b.NAVY)
        d.rect(s, 0, Inches(3.15), d.W, Inches(0.06), b.TEAL)
        d.text(s, "You keep your systems of record.\nWe run the agent layer on top.", d.M, Inches(2.4),
               Inches(12), Inches(1.6), size=34, color=b.WHITE, bold=True, align=PP_ALIGN.CENTER, shrink=True)
        d.text(s, "DataStaqAI · done-for-you AI engineering · ~$2–5k/mo", d.M, Inches(4.6), Inches(12),
               Inches(0.5), size=15, color=b.LIGHT_TEAL, align=PP_ALIGN.CENTER)
        continue
    if k == 'section':
        s = d.slide(fill=b.NAVY)
        d.rect(s, 0, 0, Inches(0.18), d.H, b.TEAL)
        d.text(s, sp['kicker'], d.M, Inches(2.5), Inches(11), Inches(0.4), size=15, color=b.TEAL, bold=True)
        d.text(s, sp['title'], d.M, Inches(3.0), Inches(11.6), Inches(1.1), size=40, color=b.WHITE, bold=True, shrink=True)
        d.rect(s, d.M, Inches(4.15), Inches(1.6), Inches(0.05), b.TEAL)
        d.text(s, sp.get('subtitle', ''), d.M, Inches(4.35), Inches(11.4), Inches(0.6), size=15, color=b.LIGHT_TEAL)
        continue
    if k == 'titlecard':
        s = d.slide(fill=b.NAVY)
        d.rect(s, 0, 0, d.W, Inches(0.16), b.TEAL)
        d.text(s, f"USE CASE · {sp['cluster'].upper()} CLUSTER", d.M, Inches(0.7), Inches(11), Inches(0.4),
               size=13, color=b.TEAL, bold=True)
        d.text(s, sp['name'], d.M, Inches(1.2), Inches(12), Inches(1.4), size=34, color=b.WHITE, bold=True, shrink=True)
        d.rect(s, d.M, Inches(2.7), Inches(1.5), Inches(0.05), b.TEAL)
        if sp['market']:
            d.text(s, "WHAT THE MARKET IS PURSUING", d.M, Inches(2.95), Inches(8), Inches(0.35),
                   size=12, color=b.AMBER, bold=True)
            body_box(s, sp['market'], color=b.LIGHT_TEAL, top=Inches(3.35), height=Inches(3.4))
        d.footer(s, page, TOTAL, dark=True)
        continue
    if k == 'bullets':
        navy = sp.get('fill') == 'navy'
        s = d.slide(fill=b.NAVY if navy else b.WHITE)
        if navy:
            d.rect(s, 0, 0, d.W, Inches(0.16), b.TEAL)
            d.text(s, sp['title'], d.M, Inches(0.42), d.CW, Inches(0.7), size=27, color=b.WHITE, bold=True, shrink=True)
            d.rect(s, d.M, Inches(1.16), Inches(1.45), Inches(0.05), b.TEAL)
            if sp.get('subtitle'):
                d.text(s, sp['subtitle'], d.M, Inches(1.28), d.CW, Inches(0.4), size=14, color=b.AMBER, bold=True)
            body_box(s, sp['bullets'], color=b.LIGHT_TEAL)
            d.footer(s, page, TOTAL, dark=True)
        else:
            d.header(s, sp['title'], sp.get('subtitle'))
            body_box(s, sp['bullets'], color=b.INK)
            d.footer(s, page, TOTAL)
        continue

out = HERE / "DataStaqAI-Competitive-Landscape-draft.pptx"
d.save(str(out))
print(f"TOTAL slide specs: {TOTAL}")
print(f"OUTPUT: {out}")
