import csv
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT.parent / "docs"
OUT = ROOT / "demo_results.txt"

N = 5000
SEED = 7
MARGIN = 0.2
DESIRED_ADVANCE = 0.35


def sample_case(rng):
    x = rng.uniform(0.0, 3.0)
    true_obstacle = x + rng.uniform(0.35, 1.25)
    # Bimodal aliased perception: one mode near truth, one distractor mode.
    if rng.random() < 0.78:
        mode = 0
        ohat = rng.gauss(true_obstacle, 0.15)
    else:
        mode = 1
        ohat = rng.gauss(true_obstacle + 0.9, 0.2)
    return x, true_obstacle, mode, ohat


def evaluate(mode_error_rate=0.0):
    rng = random.Random(SEED)
    corrupt_rng = random.Random(SEED + 36000)
    sym_collisions = 0
    sym_blocked = 0
    rel_collisions = 0
    rel_blocked = 0

    for _ in range(N):
        x, true_obstacle, mode, ohat = sample_case(rng)
        threshold = x + DESIRED_ADVANCE + MARGIN

        # Generic symmetric wrapper: one fixed radius for all modes.
        sym_lb = ohat - 0.95
        sym_allow = sym_lb >= threshold
        if not sym_allow:
            sym_blocked += 1
        elif x + DESIRED_ADVANCE >= true_obstacle - MARGIN:
            sym_collisions += 1

        observed_mode = 1 - mode if corrupt_rng.random() < mode_error_rate else mode
        rel_radius = 0.18 if observed_mode == 0 else 1.10
        rel_lb = ohat - rel_radius
        rel_allow = rel_lb >= threshold
        if not rel_allow:
            rel_blocked += 1
        elif x + DESIRED_ADVANCE >= true_obstacle - MARGIN:
            rel_collisions += 1

    return {
        "mode_error_rate": mode_error_rate,
        "sym_collision_rate": sym_collisions / N,
        "sym_blocked_rate": sym_blocked / N,
        "rel_collision_rate": rel_collisions / N,
        "rel_blocked_rate": rel_blocked / N,
    }


def write_demo_results():
    row = evaluate(0.0)
    with OUT.open("w", encoding="utf-8") as f:
        f.write(f"sym_collision_rate={row['sym_collision_rate']:.3f}\n")
        f.write(f"sym_blocked_rate={row['sym_blocked_rate']:.3f}\n")
        f.write(f"rel_collision_rate={row['rel_collision_rate']:.3f}\n")
        f.write(f"rel_blocked_rate={row['rel_blocked_rate']:.3f}\n")
    print(OUT.read_text(encoding="utf-8"))


def write_mode_corruption_table(rows):
    body = []
    for row in rows:
        body.append(
            f"{row['mode_error_rate']:.2f} & {row['sym_collision_rate']:.3f} & "
            f"{row['sym_blocked_rate']:.3f} & {row['rel_collision_rate']:.3f} & "
            f"{row['rel_blocked_rate']:.3f} \\\\"
        )
    table = (
        "\\begin{table}[t]\n"
        "\\centering\n"
        "\\caption{V2 mode-corruption stress. The controller-relative contract "
        "depends on reliable mode labels for aliased perception. As mode-label "
        "error rises, the contract remains less conservative but becomes less safe "
        "than the symmetric wrapper.}\n"
        "\\label{tab:mode-corruption}\n"
        "\\begin{tabular}{rrrrr}\n"
        "\\toprule\n"
        "Mode error & Sym coll. & Sym blocked & Rel coll. & Rel blocked \\\\\n"
        "\\midrule\n"
        + "\n".join(body)
        + "\n\\bottomrule\n"
        "\\end{tabular}\n"
        "\\end{table}\n"
    )
    (DOCS / "mode_corruption_stress_table.tex").write_text(table, encoding="utf-8")


def write_mode_corruption_stress():
    DOCS.mkdir(exist_ok=True)
    rows = [evaluate(rate) for rate in [0.0, 0.02, 0.05, 0.10, 0.20, 0.40]]
    out = DOCS / "mode_corruption_stress.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    write_mode_corruption_table(rows)
    for row in rows:
        print(row)


if __name__ == "__main__":
    if "--stress-only" in sys.argv:
        write_mode_corruption_stress()
    else:
        write_demo_results()
