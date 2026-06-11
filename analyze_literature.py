import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
rows = list(csv.DictReader((DOCS / "related_work_matrix.csv").open(encoding="utf-8")))

keywords = {
    "contracts": ["contract", "assume-guarantee", "assumption", "guarantee", "interface"],
    "perception": ["perception", "vision", "semantic", "segmentation", "detection", "tracking", "state estimation", "sensor"],
    "control": ["control", "controller", "closed-loop", "stability", "safety", "barrier", "mpc", "planning"],
    "robotics": ["robot", "manipulation", "mobile", "navigation", "aerial", "legged", "embodied", "autonomous"],
}

scored = []
for r in rows:
    text = " ".join([r.get("title", ""), r.get("abstract", ""), r.get("venue", "")]).lower()
    score = 0
    hits = []
    for group, pats in keywords.items():
        g = 0
        for p in pats:
            if p in text:
                g += 1
        if g:
            score += g
            hits.append(f"{group}:{g}")
    if score:
        scored.append((score, hits, r))

scored.sort(key=lambda x: (-x[0], x[2].get("year", ""), x[2].get("title", "")))
top = scored[:300]
with (DOCS / "serious_skim_top300.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["score", "hits", "title", "year", "venue", "doi", "url", "abstract"])
    for s, hits, r in top:
        w.writerow([s, "|".join(hits), r["title"], r["year"], r["venue"], r["doi"], r["url"], r["abstract"]])

print("top titles:")
for s, hits, r in top[:50]:
    print(s, r["year"], r["title"][:120])
