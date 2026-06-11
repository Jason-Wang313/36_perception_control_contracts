import csv
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import quote
from urllib.request import urlopen, Request

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
DOCS.mkdir(exist_ok=True)

QUERIES = [
    "robot perception control contract",
    "perception controller interface robot",
    "robotics perception assumption control safety",
    "robot world model controller assumption",
    "control barrier perception uncertainty robot",
    "robot task and motion planning perception",
    "semantic perception control robot",
    "sensor specification robot controller",
    "perception monitoring robot control",
    "robotic state estimation controller assumptions",
]

def fetch_crossref(query, rows=100, offset=0):
    url = f"https://api.crossref.org/works?query={quote(query)}&rows={rows}&offset={offset}"
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["message"]["items"]

def clean(s):
    if not s:
        return ""
    s = re.sub(r"\s+", " ", s)
    return s.strip()

seen = {}
rows = []
for q in QUERIES:
    for off in range(0, 300, 100):
        try:
            items = fetch_crossref(q, rows=100, offset=off)
        except Exception as e:
            print(f"crossref fail {q} {off}: {e}", file=sys.stderr)
            break
        for it in items:
            doi = it.get("DOI", "").lower()
            title = clean(" ".join(it.get("title", [])[:1]))
            year = ""
            issued = it.get("issued", {}).get("date-parts", [[]])
            if issued and issued[0]:
                year = str(issued[0][0])
            key = doi or (title.lower() + year)
            if not key or key in seen:
                continue
            seen[key] = True
            rows.append({
                "query_seed": q,
                "title": title,
                "year": year,
                "venue": clean(" ".join(it.get("container-title", [])[:1])),
                "authors": "; ".join([clean(a.get("family", "") + ", " + a.get("given", "")) for a in it.get("author", [])[:8]]),
                "doi": doi,
                "type": it.get("type", ""),
                "abstract": clean(re.sub(r"<.*?>", " ", it.get("abstract", "")))[:1000],
                "url": it.get("URL", ""),
            })
        time.sleep(0.2)

out = DOCS / "related_work_matrix.csv"
with out.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["query_seed", "title", "year", "venue", "authors", "doi", "type", "abstract", "url"])
    writer.writeheader()
    writer.writerows(rows)
print(f"wrote {len(rows)} rows to {out}")
