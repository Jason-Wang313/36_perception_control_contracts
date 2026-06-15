# Perception-Control Contracts

Paper 36 final v3 full-scale artifact.

## Final Artifact

- Canonical PDF: `C:/Users/wangz/Downloads/36.pdf`
- Final page count: 25
- SHA256: `73AFE97FDFD6D1B598646BA6413F1AD6699F8FBED5FE276C9308D12EE60626DF`
- Local `paper/main.pdf`: removed by the canonical build script
- Repository: `https://github.com/Jason-Wang313/36_perception_control_contracts`

## Evidence

- `scripts/run_full_scale_perception_contract_suite.py`: deterministic RAM-light full-scale suite.
- `results/full_scale/seed_metrics.csv`: 161,280 seed-level rows.
- `results/full_scale/aggregate_metrics.csv`: 1,680 aggregate cells.
- `results/full_scale/experiment_summary.json`: headline metrics.
- `results/full_scale/experiment_validation.json`: experiment row-count and artifact validation.
- `results/full_scale/validation.json`: final PDF/build/render validation.
- `figures/full_scale/*.pdf`: five generated vector figures.
- `paper/run_demo.py`: original v2 mechanism demo and mode-corruption stress.

## Build

Regenerate evidence:

```powershell
python scripts\run_full_scale_perception_contract_suite.py
```

Build the canonical PDF:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\build_pdf.ps1
```

The build script compiles from `paper/`, copies only the final PDF to Downloads, and removes `paper/main.pdf`.
