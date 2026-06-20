# Reproducibility Checklist

- [x] Original demo command: `python paper/run_demo.py`
- [x] Original stress command: `python paper/run_demo.py --stress-only`
- [x] Full-scale suite command: `python scripts\run_full_scale_perception_contract_suite.py`
- [x] Seed rows: `results/full_scale/seed_metrics.csv`
- [x] Aggregate rows: `results/full_scale/aggregate_metrics.csv`
- [x] Experiment summary: `results/full_scale/experiment_summary.json`
- [x] Experiment validation: `results/full_scale/experiment_validation.json`
- [x] Generated LaTeX tables: `results/full_scale/full_scale_*.tex`
- [x] Generated vector figures: `figures/full_scale/*.pdf`
- [x] Canonical build command: `powershell -ExecutionPolicy Bypass -File scripts/build_pdf.ps1`
- [x] Canonical PDF path: `C:/Users/wangz/Downloads/36.pdf`
- [x] Canonical PDF SHA256: `F9CD804DFC345B0111BEB680CF0B0E9BD78C5C20D5A2D4D61AFD2FAF85FBB8D1`
- [x] Local generated PDF removed after build.
- [x] Final Downloads PDF rendered and visually checked.
- [x] VLA-style link-box QA passed on pages 2, 5, 11, and 25.
- [x] Final PDF metadata recorded in `results/full_scale/validation.json`.
- [ ] Fully pinned Python environment.
- [ ] Continuous integration.
