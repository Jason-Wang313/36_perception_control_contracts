import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "demo_results.txt"
random.seed(7)

N = 5000
m = 0.2
desired_advance = 0.35

def sample_case():
    x = random.uniform(0.0, 3.0)
    true_obstacle = x + random.uniform(0.35, 1.25)
    # Bimodal aliased perception: one mode near truth, one distractor mode.
    if random.random() < 0.78:
        mode = 0
        ohat = random.gauss(true_obstacle, 0.15)
    else:
        mode = 1
        ohat = random.gauss(true_obstacle + 0.9, 0.2)
    return x, true_obstacle, mode, ohat

sym_collisions = 0
sym_blocked = 0
rel_collisions = 0
rel_blocked = 0

for _ in range(N):
    x, true_obstacle, mode, ohat = sample_case()
    threshold = x + desired_advance + m

    # Generic symmetric wrapper: one fixed radius for all modes.
    sym_lb = ohat - 0.95
    sym_allow = sym_lb >= threshold
    if not sym_allow:
        sym_blocked += 1
    elif x + desired_advance >= true_obstacle - m:
        sym_collisions += 1

    # Controller-relative contract: admissibility radius depends on the mode.
    rel_radius = 0.18 if mode == 0 else 1.10
    rel_lb = ohat - rel_radius
    rel_allow = rel_lb >= threshold
    if not rel_allow:
        rel_blocked += 1
    elif x + desired_advance >= true_obstacle - m:
        rel_collisions += 1

with OUT.open("w", encoding="utf-8") as f:
    f.write(f"sym_collision_rate={sym_collisions/N:.3f}\n")
    f.write(f"sym_blocked_rate={sym_blocked/N:.3f}\n")
    f.write(f"rel_collision_rate={rel_collisions/N:.3f}\n")
    f.write(f"rel_blocked_rate={rel_blocked/N:.3f}\n")
print(OUT.read_text(encoding='utf-8'))
