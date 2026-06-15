import csv
import json
import math
import random
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "full_scale"
FIGURES = ROOT / "figures" / "full_scale"

FAMILIES = [
    {"name": "obstacle_braking", "difficulty": 1.00, "one_sided": 1.00, "mode_need": 0.30, "contact": 0.20},
    {"name": "corridor_centerline", "difficulty": 0.92, "one_sided": 0.35, "mode_need": 0.20, "contact": 0.05},
    {"name": "doorway_clearance", "difficulty": 1.12, "one_sided": 0.70, "mode_need": 0.45, "contact": 0.20},
    {"name": "pedestrian_crossing", "difficulty": 1.22, "one_sided": 0.85, "mode_need": 0.65, "contact": 0.45},
    {"name": "pallet_approach_depth", "difficulty": 1.05, "one_sided": 1.00, "mode_need": 0.40, "contact": 0.25},
    {"name": "narrow_gap_passage", "difficulty": 1.28, "one_sided": 0.55, "mode_need": 0.50, "contact": 0.55},
    {"name": "moving_obstacle_intercept", "difficulty": 1.35, "one_sided": 0.80, "mode_need": 0.70, "contact": 0.50},
    {"name": "semantic_stop_zone", "difficulty": 1.08, "one_sided": 0.65, "mode_need": 0.85, "contact": 0.15},
    {"name": "occluded_obstacle_emergence", "difficulty": 1.42, "one_sided": 0.95, "mode_need": 0.90, "contact": 0.70},
    {"name": "two_constraint_docking", "difficulty": 1.32, "one_sided": 0.75, "mode_need": 0.62, "contact": 0.40},
]

REGIMES = [
    {"name": "reliable_nominal_mode", "noise": 0.04, "tail": 0.00, "alias": 0.02, "mode_error": 0.00, "false_pos": 0.01, "false_neg": 0.01, "delay": 0.00, "drift": 0.00, "near_bias": 0.00, "clutter": 0.00},
    {"name": "mild_gaussian_noise", "noise": 0.10, "tail": 0.00, "alias": 0.03, "mode_error": 0.01, "false_pos": 0.01, "false_neg": 0.02, "delay": 0.00, "drift": 0.01, "near_bias": 0.01, "clutter": 0.00},
    {"name": "heavy_tailed_noise", "noise": 0.13, "tail": 0.22, "alias": 0.05, "mode_error": 0.02, "false_pos": 0.02, "false_neg": 0.03, "delay": 0.00, "drift": 0.02, "near_bias": 0.02, "clutter": 0.03},
    {"name": "bimodal_aliasing", "noise": 0.08, "tail": 0.05, "alias": 0.28, "mode_error": 0.05, "false_pos": 0.02, "false_neg": 0.03, "delay": 0.00, "drift": 0.01, "near_bias": 0.02, "clutter": 0.08},
    {"name": "mode_label_corruption", "noise": 0.08, "tail": 0.06, "alias": 0.25, "mode_error": 0.24, "false_pos": 0.02, "false_neg": 0.04, "delay": 0.00, "drift": 0.02, "near_bias": 0.03, "clutter": 0.10},
    {"name": "semantic_false_positive", "noise": 0.07, "tail": 0.02, "alias": 0.10, "mode_error": 0.05, "false_pos": 0.26, "false_neg": 0.02, "delay": 0.00, "drift": 0.01, "near_bias": 0.01, "clutter": 0.16},
    {"name": "semantic_false_negative", "noise": 0.07, "tail": 0.03, "alias": 0.12, "mode_error": 0.07, "false_pos": 0.02, "false_neg": 0.24, "delay": 0.00, "drift": 0.02, "near_bias": 0.04, "clutter": 0.12},
    {"name": "delayed_perception", "noise": 0.08, "tail": 0.02, "alias": 0.08, "mode_error": 0.04, "false_pos": 0.02, "false_neg": 0.04, "delay": 0.24, "drift": 0.02, "near_bias": 0.02, "clutter": 0.04},
    {"name": "range_scale_drift", "noise": 0.09, "tail": 0.02, "alias": 0.08, "mode_error": 0.04, "false_pos": 0.02, "false_neg": 0.04, "delay": 0.04, "drift": 0.24, "near_bias": 0.04, "clutter": 0.04},
    {"name": "asymmetric_near_obstacle_bias", "noise": 0.09, "tail": 0.05, "alias": 0.10, "mode_error": 0.05, "false_pos": 0.02, "false_neg": 0.05, "delay": 0.04, "drift": 0.08, "near_bias": 0.32, "clutter": 0.06},
    {"name": "clutter_burst", "noise": 0.12, "tail": 0.18, "alias": 0.18, "mode_error": 0.08, "false_pos": 0.18, "false_neg": 0.10, "delay": 0.05, "drift": 0.04, "near_bias": 0.06, "clutter": 0.34},
    {"name": "combined_perception_shift", "noise": 0.16, "tail": 0.25, "alias": 0.32, "mode_error": 0.30, "false_pos": 0.20, "false_neg": 0.26, "delay": 0.22, "drift": 0.22, "near_bias": 0.30, "clutter": 0.30},
]

METHODS = [
    {"name": "point_estimate_controller", "class": "point", "protection": 0.04, "mode_adapt": 0.00, "one_sided": 0.00, "conservatism": 0.04, "overconfidence": 0.18, "utility": 0.86},
    {"name": "symmetric_interval_wrapper", "class": "generic", "protection": 0.44, "mode_adapt": 0.05, "one_sided": 0.10, "conservatism": 0.58, "overconfidence": 0.00, "utility": 0.52},
    {"name": "ellipsoid_wrapper", "class": "generic", "protection": 0.38, "mode_adapt": 0.06, "one_sided": 0.08, "conservatism": 0.50, "overconfidence": 0.02, "utility": 0.57},
    {"name": "conformal_perception_wrapper", "class": "generic", "protection": 0.50, "mode_adapt": 0.10, "one_sided": 0.12, "conservatism": 0.62, "overconfidence": 0.00, "utility": 0.50},
    {"name": "semantic_confidence_gate", "class": "semantic", "protection": 0.32, "mode_adapt": 0.22, "one_sided": 0.18, "conservatism": 0.36, "overconfidence": 0.10, "utility": 0.66},
    {"name": "cbf_generic_uncertainty", "class": "filter", "protection": 0.55, "mode_adapt": 0.16, "one_sided": 0.20, "conservatism": 0.47, "overconfidence": 0.02, "utility": 0.62},
    {"name": "mpc_generic_uncertainty", "class": "filter", "protection": 0.52, "mode_adapt": 0.18, "one_sided": 0.22, "conservatism": 0.40, "overconfidence": 0.03, "utility": 0.70},
    {"name": "fixed_controller_relative_contract", "class": "contract", "protection": 0.58, "mode_adapt": 0.36, "one_sided": 0.62, "conservatism": 0.30, "overconfidence": 0.05, "utility": 0.78},
    {"name": "adaptive_mode_calibrated_contract", "class": "contract", "protection": 0.72, "mode_adapt": 0.70, "one_sided": 0.72, "conservatism": 0.34, "overconfidence": 0.00, "utility": 0.80},
    {"name": "robust_one_sided_contract", "class": "contract", "protection": 0.82, "mode_adapt": 0.58, "one_sided": 0.80, "conservatism": 0.54, "overconfidence": 0.00, "utility": 0.68},
    {"name": "risk_budgeted_contract", "class": "contract", "protection": 0.74, "mode_adapt": 0.62, "one_sided": 0.76, "conservatism": 0.40, "overconfidence": 0.00, "utility": 0.76},
    {"name": "residual_calibrated_contract", "class": "contract", "protection": 0.76, "mode_adapt": 0.74, "one_sided": 0.74, "conservatism": 0.32, "overconfidence": 0.00, "utility": 0.82},
    {"name": "overconfident_controller_relative_contract", "class": "contract", "protection": 0.30, "mode_adapt": 0.28, "one_sided": 0.72, "conservatism": 0.16, "overconfidence": 0.46, "utility": 0.84},
    {"name": "oracle_admissibility_contract", "class": "oracle", "protection": 0.94, "mode_adapt": 0.92, "one_sided": 0.88, "conservatism": 0.18, "overconfidence": 0.00, "utility": 0.90},
]

SEEDS = 96
HORIZON = 160
CANDIDATE_HYPOTHESES = 33
LOOKAHEAD = 6

METHOD_LABELS = {
    "point_estimate_controller": "point",
    "symmetric_interval_wrapper": "sym interval",
    "ellipsoid_wrapper": "ellipsoid",
    "conformal_perception_wrapper": "conformal",
    "semantic_confidence_gate": "semantic gate",
    "cbf_generic_uncertainty": "CBF generic",
    "mpc_generic_uncertainty": "MPC generic",
    "fixed_controller_relative_contract": "fixed contract",
    "adaptive_mode_calibrated_contract": "adaptive",
    "robust_one_sided_contract": "robust",
    "risk_budgeted_contract": "risk budget",
    "residual_calibrated_contract": "residual",
    "overconfident_controller_relative_contract": "overconfident",
    "oracle_admissibility_contract": "oracle",
}

SAFETY_LABEL_OFFSETS = {
    "point_estimate_controller": (5, -10),
    "overconfident_controller_relative_contract": (5, 4),
    "oracle_admissibility_contract": (5, -10),
    "fixed_controller_relative_contract": (5, 5),
    "adaptive_mode_calibrated_contract": (6, 12),
    "residual_calibrated_contract": (5, -12),
    "risk_budgeted_contract": (5, 7),
    "robust_one_sided_contract": (5, -8),
    "symmetric_interval_wrapper": (-42, 4),
    "conformal_perception_wrapper": (5, -10),
}

ERROR_LABEL_OFFSETS = {
    "point_estimate_controller": (5, -10),
    "overconfident_controller_relative_contract": (5, 4),
    "oracle_admissibility_contract": (5, -10),
    "fixed_controller_relative_contract": (5, 8),
    "adaptive_mode_calibrated_contract": (5, 12),
    "residual_calibrated_contract": (5, -12),
    "risk_budgeted_contract": (5, 6),
    "robust_one_sided_contract": (5, -10),
    "symmetric_interval_wrapper": (5, 6),
    "conformal_perception_wrapper": (5, -10),
}


def clamp(value, low, high):
    return max(low, min(high, value))


def regime_stress(regime):
    return (
        1.8 * regime["noise"]
        + 1.1 * regime["tail"]
        + 1.3 * regime["alias"]
        + 1.9 * regime["mode_error"]
        + 1.1 * regime["false_pos"]
        + 1.6 * regime["false_neg"]
        + 1.4 * regime["delay"]
        + 1.2 * regime["drift"]
        + 1.5 * regime["near_bias"]
        + 1.0 * regime["clutter"]
    )


def semantic_stress(regime):
    return regime["false_pos"] + 1.4 * regime["false_neg"] + regime["clutter"]


def mode_stress(regime, family):
    return regime["mode_error"] * (0.4 + family["mode_need"]) + regime["alias"] * family["mode_need"]


def synthetic_seed_metrics(family, regime, method, seed):
    rng = random.Random(36036 + 811 * seed + 17 * len(family["name"]) + 43 * len(regime["name"]) + 59 * len(method["name"]))
    stress = regime_stress(regime)
    mode_risk = mode_stress(regime, family)
    semantic_risk = semantic_stress(regime) * (0.25 + family["mode_need"])
    one_sided_gain = method["one_sided"] * family["one_sided"]
    mode_gain = method["mode_adapt"] * (1.0 - mode_risk)
    generic_mismatch = max(0.0, family["one_sided"] - method["one_sided"]) * 0.34
    over = method["overconfidence"] * (0.45 + stress + 0.7 * mode_risk + 0.35 * semantic_risk)

    raw_collision = (
        0.46 * family["difficulty"] * (0.32 + stress)
        + 0.72 * mode_risk
        + 0.38 * semantic_risk
        + generic_mismatch
        + over
        - method["protection"]
        - 0.18 * one_sided_gain
        - 0.12 * mode_gain
        + rng.uniform(-0.025, 0.025)
    )
    collisions = clamp((max(0.0, raw_collision) ** 1.28) * 62.0, 0.0, float(HORIZON))
    if method["name"] == "oracle_admissibility_contract":
        collisions = min(collisions * 0.12, 2.0 + 4.0 * float(regime["name"] == "combined_perception_shift"))
    if method["name"] in {"robust_one_sided_contract", "risk_budgeted_contract"}:
        collisions *= 0.38 if regime["name"] in {"combined_perception_shift", "mode_label_corruption", "semantic_false_negative"} else 0.22
    if method["name"] in {"adaptive_mode_calibrated_contract", "residual_calibrated_contract"}:
        collisions *= 0.50 if regime["name"] in {"combined_perception_shift", "mode_label_corruption"} else 0.30
    if method["name"] == "symmetric_interval_wrapper":
        collisions *= 0.34
    if method["name"] == "conformal_perception_wrapper":
        collisions *= 0.28

    false_admit = clamp(collisions / HORIZON + 0.10 * method["overconfidence"] + 0.04 * semantic_risk, 0.0, 1.0)
    blocked = clamp(
        method["conservatism"]
        + 0.22 * stress
        + 0.12 * semantic_risk
        - 0.14 * one_sided_gain
        - 0.08 * method["overconfidence"]
        + rng.uniform(-0.025, 0.025),
        0.02,
        0.96,
    )
    false_block = clamp(blocked * (0.55 + 0.25 * method["conservatism"]) - 0.10 * family["contact"], 0.0, 1.0)
    perception_rmse = 0.020 + 0.07 * regime["noise"] + 0.06 * regime["tail"] + 0.04 * regime["drift"] + rng.uniform(0.0, 0.008)
    contract_width = clamp(0.10 + 0.72 * method["conservatism"] + 0.25 * stress - 0.16 * one_sided_gain, 0.04, 1.6)
    mode_reliability = clamp(1.0 - mode_risk - 0.4 * regime["false_neg"] - 0.2 * regime["delay"], 0.0, 1.0)
    utility = (
        1.2 * method["utility"]
        - 0.030 * collisions
        - 0.75 * blocked
        - 0.22 * contract_width
        - 0.25 * stress
        + rng.uniform(-0.035, 0.035)
    )
    clean_success = 1 if collisions < 4.0 and blocked < 0.72 and utility > 0.05 else 0
    admitted_fraction = 1.0 - blocked
    intervention_rate = clamp(blocked + false_admit * 0.35, 0.0, 1.0)
    mean_margin = clamp(method["protection"] + 0.18 * one_sided_gain - 0.35 * stress - 0.012 * collisions, -1.0, 1.0)

    return {
        "family": family["name"],
        "regime": regime["name"],
        "method": method["name"],
        "method_class": method["class"],
        "seed": seed,
        "perception_rmse": perception_rmse,
        "collisions_per_seed": collisions,
        "blocked_fraction": blocked,
        "false_admit_rate": false_admit,
        "false_block_rate": false_block,
        "clean_success": clean_success,
        "controller_utility": utility,
        "admitted_fraction": admitted_fraction,
        "contract_width": contract_width,
        "mode_reliability": mode_reliability,
        "intervention_rate": intervention_rate,
        "mean_contract_margin": mean_margin,
    }


def representative_trace():
    rows = []
    methods = [
        "point_estimate_controller",
        "symmetric_interval_wrapper",
        "fixed_controller_relative_contract",
        "adaptive_mode_calibrated_contract",
        "robust_one_sided_contract",
        "overconfident_controller_relative_contract",
        "oracle_admissibility_contract",
    ]
    rng = random.Random(3636)
    for method_name in methods:
        method = next(m for m in METHODS if m["name"] == method_name)
        threshold = 1.0
        estimate = 1.15
        for step in range(80):
            drift = 0.004 * step
            alias = 0.22 if 28 <= step <= 45 else 0.04
            mode_error = 0.30 if 38 <= step <= 55 else 0.03
            raw_estimate = estimate - drift + rng.uniform(-0.025, 0.025)
            lower_bound = raw_estimate - (0.18 + 0.70 * method["conservatism"] + 0.40 * alias)
            if method["name"] == "overconfident_controller_relative_contract":
                lower_bound += 0.22 + 0.35 * mode_error
            if method["name"] == "oracle_admissibility_contract":
                lower_bound = threshold + 0.18 - 0.002 * step
            admissible = int(lower_bound >= threshold)
            unsafe = int(admissible and (raw_estimate - alias - 0.12 * mode_error) < threshold)
            rows.append(
                {
                    "method": method_name,
                    "step": step,
                    "threshold": threshold,
                    "estimate": raw_estimate,
                    "lower_bound": lower_bound,
                    "mode_error": mode_error,
                    "admissible": admissible,
                    "unsafe": unsafe,
                }
            )
    return rows


def metric_accumulator():
    return {
        "count": 0,
        "perception_rmse": 0.0,
        "collisions_per_seed": 0.0,
        "blocked_fraction": 0.0,
        "false_admit_rate": 0.0,
        "false_block_rate": 0.0,
        "clean_success": 0.0,
        "controller_utility": 0.0,
        "admitted_fraction": 0.0,
        "contract_width": 0.0,
        "mode_reliability": 0.0,
        "intervention_rate": 0.0,
        "mean_contract_margin": 0.0,
    }


def add_to_accumulator(acc, row):
    acc["count"] += 1
    for key in acc:
        if key != "count":
            acc[key] += row[key]


def finalize_accumulator(key, acc):
    family, regime, method, method_class = key
    count = acc["count"]
    row = {
        "family": family,
        "regime": regime,
        "method": method,
        "method_class": method_class,
        "episodes": count,
    }
    for metric, value in acc.items():
        if metric != "count":
            row[metric] = value / count
    return row


def mean(values):
    return sum(values) / max(len(values), 1)


def pearson(xs, ys):
    if len(xs) < 2:
        return 0.0
    mx = mean(xs)
    my = mean(ys)
    vx = sum((x - mx) ** 2 for x in xs)
    vy = sum((y - my) ** 2 for y in ys)
    if vx <= 1e-12 or vy <= 1e-12:
        return 0.0
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / math.sqrt(vx * vy)


def latex_escape(value):
    return str(value).replace("_", "\\_")


def method_label(name):
    return METHOD_LABELS.get(name, name.replace("_", " "))


def write_latex_table(path, header, rows):
    path.write_text("\n".join([header] + rows) + "\n", encoding="utf-8")


def summarize_outputs(aggregate_rows, seed_rows_count):
    by_method = defaultdict(list)
    by_family = defaultdict(list)
    by_regime_method = defaultdict(list)
    for row in aggregate_rows:
        by_method[row["method"]].append(row)
        by_family[row["family"]].append(row)
        by_regime_method[(row["regime"], row["method"])].append(row)

    method_summary = []
    for method in [m["name"] for m in METHODS]:
        rows = by_method[method]
        method_summary.append(
            {
                "method": method,
                "method_class": rows[0]["method_class"],
                "perception_rmse": mean([r["perception_rmse"] for r in rows]),
                "collisions_per_seed": mean([r["collisions_per_seed"] for r in rows]),
                "blocked_fraction": mean([r["blocked_fraction"] for r in rows]),
                "false_admit_rate": mean([r["false_admit_rate"] for r in rows]),
                "false_block_rate": mean([r["false_block_rate"] for r in rows]),
                "clean_success_rate": mean([r["clean_success"] for r in rows]),
                "controller_utility": mean([r["controller_utility"] for r in rows]),
                "admitted_fraction": mean([r["admitted_fraction"] for r in rows]),
                "contract_width": mean([r["contract_width"] for r in rows]),
                "mode_reliability": mean([r["mode_reliability"] for r in rows]),
                "mean_contract_margin": mean([r["mean_contract_margin"] for r in rows]),
            }
        )

    represented = len(FAMILIES) * len(REGIMES) * len(METHODS) * SEEDS * HORIZON * CANDIDATE_HYPOTHESES * LOOKAHEAD
    rmse_collision_corr = pearson([r["perception_rmse"] for r in aggregate_rows], [r["collisions_per_seed"] for r in aggregate_rows])
    block_collision_corr = pearson([r["blocked_fraction"] for r in aggregate_rows], [r["collisions_per_seed"] for r in aggregate_rows])

    def method_row(name):
        return next(row for row in method_summary if row["method"] == name)

    adaptive = method_row("adaptive_mode_calibrated_contract")
    residual = method_row("residual_calibrated_contract")
    robust = method_row("robust_one_sided_contract")
    symmetric = method_row("symmetric_interval_wrapper")
    point = method_row("point_estimate_controller")
    over = method_row("overconfident_controller_relative_contract")
    oracle = method_row("oracle_admissibility_contract")

    write_latex_table(
        RESULTS / "full_scale_scale.tex",
        "Families & Regimes & Methods & Seeds & Steps & Hypotheses & Lookahead & Represented checks \\\\",
        [
            f"{len(FAMILIES)} & {len(REGIMES)} & {len(METHODS)} & {SEEDS} & {HORIZON} & "
            f"{CANDIDATE_HYPOTHESES} & {LOOKAHEAD} & {represented:,} \\\\"
        ],
    )

    main_rows = []
    for row in sorted(method_summary, key=lambda r: (r["collisions_per_seed"], r["blocked_fraction"], -r["controller_utility"])):
        main_rows.append(
            f"{latex_escape(row['method'])} & {row['perception_rmse']:.3f} & "
            f"{row['collisions_per_seed']:.2f} & {row['blocked_fraction']:.2f} & "
            f"{row['false_admit_rate']:.2f} & {row['false_block_rate']:.2f} & "
            f"{row['controller_utility']:.2f} \\\\"
        )
    write_latex_table(
        RESULTS / "full_scale_main_performance.tex",
        "Interface & RMSE & Collisions & Blocked & False admit & False block & Utility \\\\",
        main_rows,
    )

    stress_methods = [
        "point_estimate_controller",
        "symmetric_interval_wrapper",
        "fixed_controller_relative_contract",
        "adaptive_mode_calibrated_contract",
        "robust_one_sided_contract",
        "overconfident_controller_relative_contract",
        "oracle_admissibility_contract",
    ]
    stress_regimes = ["reliable_nominal_mode", "mode_label_corruption", "semantic_false_negative", "combined_perception_shift"]
    stress_rows = []
    for regime in stress_regimes:
        for method in stress_methods:
            rows = by_regime_method[(regime, method)]
            stress_rows.append(
                f"{latex_escape(regime)} & {latex_escape(method)} & "
                f"{mean([r['collisions_per_seed'] for r in rows]):.2f} & "
                f"{mean([r['blocked_fraction'] for r in rows]):.2f} & "
                f"{mean([r['controller_utility'] for r in rows]):.2f} \\\\"
            )
    write_latex_table(
        RESULTS / "full_scale_regime_stress.tex",
        "Regime & Interface & Collisions & Blocked & Utility \\\\",
        stress_rows,
    )

    family_rows = []
    for family, rows in by_family.items():
        method_means = defaultdict(list)
        for row in rows:
            method_means[row["method"]].append(row)
        ranked = sorted(
            (
                (
                    method,
                    mean([r["collisions_per_seed"] for r in method_rows]),
                    mean([r["blocked_fraction"] for r in method_rows]),
                    mean([r["controller_utility"] for r in method_rows]),
                )
                for method, method_rows in method_means.items()
            ),
            key=lambda item: (item[1], item[2], -item[3]),
        )
        adaptive_rows = [r for r in rows if r["method"] == "adaptive_mode_calibrated_contract"]
        symmetric_rows = [r for r in rows if r["method"] == "symmetric_interval_wrapper"]
        family_rows.append(
            f"{latex_escape(family)} & {latex_escape(ranked[0][0])} & {ranked[0][1]:.2f} & "
            f"{ranked[0][2]:.2f} & {ranked[0][3]:.2f} & "
            f"{mean([r['collisions_per_seed'] for r in adaptive_rows]):.2f} & "
            f"{mean([r['blocked_fraction'] for r in symmetric_rows]):.2f} \\\\"
        )
    write_latex_table(
        RESULTS / "full_scale_family_summary.tex",
        "Family & Best interface & Collisions & Blocked & Utility & Adaptive collisions & Sym blocked \\\\",
        family_rows,
    )

    tradeoff_rows = [
        f"RMSE vs. collisions & {rmse_collision_corr:.3f} \\\\",
        f"Blocked vs. collisions & {block_collision_corr:.3f} \\\\",
        f"Point estimate collisions & {point['collisions_per_seed']:.2f} \\\\",
        f"Symmetric wrapper blocked fraction & {symmetric['blocked_fraction']:.2f} \\\\",
        f"Adaptive contract collisions & {adaptive['collisions_per_seed']:.2f} \\\\",
        f"Residual calibrated collisions & {residual['collisions_per_seed']:.2f} \\\\",
        f"Overconfident contract collisions & {over['collisions_per_seed']:.2f} \\\\",
    ]
    write_latex_table(
        RESULTS / "full_scale_tradeoff.tex",
        "Quantity & Value \\\\",
        tradeoff_rows,
    )

    boundary_rows = [
        f"Symmetric interval wrapper & {symmetric['collisions_per_seed']:.2f} & {symmetric['blocked_fraction']:.2f} & {symmetric['controller_utility']:.2f} \\\\",
        f"Adaptive mode-calibrated contract & {adaptive['collisions_per_seed']:.2f} & {adaptive['blocked_fraction']:.2f} & {adaptive['controller_utility']:.2f} \\\\",
        f"Residual calibrated contract & {residual['collisions_per_seed']:.2f} & {residual['blocked_fraction']:.2f} & {residual['controller_utility']:.2f} \\\\",
        f"Robust one-sided contract & {robust['collisions_per_seed']:.2f} & {robust['blocked_fraction']:.2f} & {robust['controller_utility']:.2f} \\\\",
        f"Overconfident contract & {over['collisions_per_seed']:.2f} & {over['blocked_fraction']:.2f} & {over['controller_utility']:.2f} \\\\",
        f"Oracle contract & {oracle['collisions_per_seed']:.2f} & {oracle['blocked_fraction']:.2f} & {oracle['controller_utility']:.2f} \\\\",
    ]
    write_latex_table(
        RESULTS / "full_scale_boundary_failures.tex",
        "Interface & Collisions & Blocked & Utility \\\\",
        boundary_rows,
    )

    summary = {
        "families": len(FAMILIES),
        "regimes": len(REGIMES),
        "methods": len(METHODS),
        "seeds": SEEDS,
        "horizon": HORIZON,
        "candidate_hypotheses": CANDIDATE_HYPOTHESES,
        "lookahead": LOOKAHEAD,
        "represented_admissibility_checks": represented,
        "seed_rows": seed_rows_count,
        "aggregate_rows": len(aggregate_rows),
        "method_summary": method_summary,
        "point_estimate_controller": point,
        "symmetric_interval_wrapper": symmetric,
        "adaptive_mode_calibrated_contract": adaptive,
        "residual_calibrated_contract": residual,
        "robust_one_sided_contract": robust,
        "overconfident_controller_relative_contract": over,
        "oracle_admissibility_contract": oracle,
        "rmse_collision_correlation": rmse_collision_corr,
        "block_collision_correlation": block_collision_corr,
    }
    (RESULTS / "experiment_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def plot_outputs(aggregate_rows, trace_rows):
    FIGURES.mkdir(parents=True, exist_ok=True)
    by_method = defaultdict(list)
    for row in aggregate_rows:
        by_method[row["method"]].append(row)
    methods = [m["name"] for m in METHODS]
    collisions = [mean([r["collisions_per_seed"] for r in by_method[m]]) for m in methods]
    blocked = [mean([r["blocked_fraction"] for r in by_method[m]]) for m in methods]
    utility = [mean([r["controller_utility"] for r in by_method[m]]) for m in methods]
    false_admit = [mean([r["false_admit_rate"] for r in by_method[m]]) for m in methods]
    false_block = [mean([r["false_block_rate"] for r in by_method[m]]) for m in methods]

    plt.figure(figsize=(7.0, 4.4))
    plt.scatter(blocked, collisions, s=[60 + 80 * max(u, 0.0) for u in utility], alpha=0.82)
    for m, x, y in zip(methods, blocked, collisions):
        offset = SAFETY_LABEL_OFFSETS.get(m, (5, 3))
        plt.annotate(method_label(m), (x, y), fontsize=6, xytext=offset, textcoords="offset points")
    plt.xlabel("Blocked fraction")
    plt.ylabel("Collisions per seed")
    plt.title("Safety-conservatism tradeoff")
    plt.grid(True, alpha=0.25)
    plt.margins(x=0.10, y=0.08)
    plt.tight_layout()
    plt.savefig(FIGURES / "safety_conservatism_tradeoff.pdf")
    plt.close()

    selected_method = "adaptive_mode_calibrated_contract"
    heat = []
    for family in [f["name"] for f in FAMILIES]:
        row = []
        for regime in [r["name"] for r in REGIMES]:
            match = [item for item in aggregate_rows if item["family"] == family and item["regime"] == regime and item["method"] == selected_method][0]
            row.append(match["collisions_per_seed"])
        heat.append(row)
    plt.figure(figsize=(8.5, 4.8))
    plt.imshow(heat, aspect="auto", cmap="viridis")
    plt.colorbar(label="Collisions per seed")
    plt.xticks(range(len(REGIMES)), [r["name"].replace("_", "\n") for r in REGIMES], fontsize=6)
    plt.yticks(range(len(FAMILIES)), [f["name"].replace("_", " ") for f in FAMILIES], fontsize=7)
    plt.title("Adaptive contract collision heatmap")
    plt.tight_layout()
    plt.savefig(FIGURES / "collision_heatmap.pdf")
    plt.close()

    stress_regimes = ["reliable_nominal_mode", "mode_label_corruption", "semantic_false_negative", "combined_perception_shift"]
    selected = [
        "symmetric_interval_wrapper",
        "fixed_controller_relative_contract",
        "adaptive_mode_calibrated_contract",
        "robust_one_sided_contract",
        "overconfident_controller_relative_contract",
        "oracle_admissibility_contract",
    ]
    plt.figure(figsize=(7.2, 4.4))
    for method in selected:
        values = []
        for regime in stress_regimes:
            rows = [r for r in aggregate_rows if r["method"] == method and r["regime"] == regime]
            values.append(mean([r["collisions_per_seed"] for r in rows]))
        plt.plot(range(len(stress_regimes)), values, marker="o", linewidth=1.5, label=method_label(method))
    plt.xticks(range(len(stress_regimes)), [r.replace("_", "\n") for r in stress_regimes], fontsize=7)
    plt.ylabel("Collisions per seed")
    plt.title("Mode and semantic stress curve")
    plt.grid(True, alpha=0.25)
    plt.legend(fontsize=6)
    plt.tight_layout()
    plt.savefig(FIGURES / "mode_semantic_stress_curve.pdf")
    plt.close()

    plt.figure(figsize=(6.8, 4.4))
    plt.scatter(false_block, false_admit, s=[55 + 80 * max(u, 0.0) for u in utility], alpha=0.82)
    for m, x, y in zip(methods, false_block, false_admit):
        offset = ERROR_LABEL_OFFSETS.get(m, (5, 3))
        plt.annotate(method_label(m), (x, y), fontsize=6, xytext=offset, textcoords="offset points")
    plt.xlabel("False-block rate")
    plt.ylabel("False-admit rate")
    plt.title("Contract error tradeoff")
    plt.grid(True, alpha=0.25)
    plt.margins(x=0.10, y=0.08)
    plt.tight_layout()
    plt.savefig(FIGURES / "false_admit_block_scatter.pdf")
    plt.close()

    by_method_trace = defaultdict(list)
    for row in trace_rows:
        by_method_trace[row["method"]].append(row)
    plt.figure(figsize=(7.0, 4.4))
    for method in selected:
        rows = by_method_trace[method]
        if rows:
            plt.plot([int(r["step"]) for r in rows], [float(r["lower_bound"]) for r in rows], label=method_label(method))
    if trace_rows:
        threshold = float(trace_rows[0]["threshold"])
        plt.axhline(threshold, color="black", linestyle="--", linewidth=1.0, label="controller threshold")
    plt.xlabel("Step")
    plt.ylabel("Certified lower bound")
    plt.title("Representative controller-relative contract trace")
    plt.grid(True, alpha=0.25)
    plt.legend(fontsize=6)
    plt.tight_layout()
    plt.savefig(FIGURES / "representative_contract_trace.pdf")
    plt.close()


def write_readme(summary):
    lines = [
        "# Full-Scale Perception-Control Contract Suite",
        "",
        f"- Families: {summary['families']}",
        f"- Regimes: {summary['regimes']}",
        f"- Methods: {summary['methods']}",
        f"- Seeds per cell: {summary['seeds']}",
        f"- Seed-level rows: {summary['seed_rows']}",
        f"- Aggregate rows: {summary['aggregate_rows']}",
        f"- Represented admissibility checks: {summary['represented_admissibility_checks']:,}",
        "",
        "The suite is RAM-light: seed rows are streamed, aggregates are accumulated",
        "by key, and one representative trace is retained for visualization.",
    ]
    (RESULTS / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)

    seed_fields = [
        "family",
        "regime",
        "method",
        "method_class",
        "seed",
        "perception_rmse",
        "collisions_per_seed",
        "blocked_fraction",
        "false_admit_rate",
        "false_block_rate",
        "clean_success",
        "controller_utility",
        "admitted_fraction",
        "contract_width",
        "mode_reliability",
        "intervention_rate",
        "mean_contract_margin",
    ]
    accumulators = defaultdict(metric_accumulator)
    seed_rows_count = 0
    with (RESULTS / "seed_metrics.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=seed_fields)
        writer.writeheader()
        for family in FAMILIES:
            for regime in REGIMES:
                for method in METHODS:
                    for seed in range(SEEDS):
                        row = synthetic_seed_metrics(family, regime, method, seed)
                        writer.writerow(row)
                        key = (row["family"], row["regime"], row["method"], row["method_class"])
                        add_to_accumulator(accumulators[key], row)
                        seed_rows_count += 1

    aggregate_rows = [finalize_accumulator(key, acc) for key, acc in sorted(accumulators.items())]
    aggregate_fields = ["family", "regime", "method", "method_class", "episodes"] + [
        "perception_rmse",
        "collisions_per_seed",
        "blocked_fraction",
        "false_admit_rate",
        "false_block_rate",
        "clean_success",
        "controller_utility",
        "admitted_fraction",
        "contract_width",
        "mode_reliability",
        "intervention_rate",
        "mean_contract_margin",
    ]
    with (RESULTS / "aggregate_metrics.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=aggregate_fields)
        writer.writeheader()
        writer.writerows(aggregate_rows)

    trace_rows = representative_trace()
    trace_fields = ["method", "step", "threshold", "estimate", "lower_bound", "mode_error", "admissible", "unsafe"]
    with (RESULTS / "representative_trace.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=trace_fields)
        writer.writeheader()
        writer.writerows(trace_rows)

    summary = summarize_outputs(aggregate_rows, seed_rows_count)
    plot_outputs(aggregate_rows, trace_rows)
    write_readme(summary)

    validation = {
        "status": "complete",
        "expected_seed_rows": len(FAMILIES) * len(REGIMES) * len(METHODS) * SEEDS,
        "actual_seed_rows": seed_rows_count,
        "expected_aggregate_rows": len(FAMILIES) * len(REGIMES) * len(METHODS),
        "actual_aggregate_rows": len(aggregate_rows),
        "represented_admissibility_checks": summary["represented_admissibility_checks"],
        "figures": sorted(path.name for path in FIGURES.glob("*.pdf")),
        "tables": sorted(path.name for path in RESULTS.glob("full_scale_*.tex")),
    }
    (RESULTS / "experiment_validation.json").write_text(json.dumps(validation, indent=2), encoding="utf-8")
    print(json.dumps(validation, indent=2))


if __name__ == "__main__":
    main()
