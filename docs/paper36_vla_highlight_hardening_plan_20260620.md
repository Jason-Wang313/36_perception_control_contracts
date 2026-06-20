# Paper 36 VLA Highlight Hardening Plan

Date: 2026-06-20

## Objective

Harden Paper 36's visible PDF link-box styling so it matches the VLA-v4 role-model PDF's professional red and green boxed link treatment while preserving the final 25-page perception-control-contracts manuscript, deterministic full-scale suite, and all scientific claims.

## Plan-Start Evidence

- Canonical PDF at plan start: `C:/Users/wangz/Downloads/36.pdf`.
- Plan-start size: 357177 bytes.
- Plan-start page count: 25.
- Plan-start affected link pages: 2, 5, 11, and 25.
- Plan-start link annotations: 12 green citation/link annotations, 3 red internal-reference annotations, and 9 cyan URL annotations.
- Plan-start border state: all 24 link annotations already used visible one-point borders, but URL boxes were cyan rather than VLA-style green.
- Plan-start LaTeX source used plain `\usepackage{hyperref}` in `paper/main.tex` without the VLA-v4 `\hypersetup` block.
- Build wrapper is `scripts/build_pdf.ps1`; it builds from `paper/`, exports `C:/Users/wangz/Downloads/36.pdf`, writes ignored `data/build_status.json`, and removes local `paper/main.pdf`.
- Plan-start local `paper/main.pdf` was absent.
- The full-scale suite remains 161,280 seed-level rows, 1,680 aggregate rows, and 5,109,350,400 represented admissibility checks.

## Role-Model Style Target

Match the VLA-v4 role model's link annotation style:

```tex
\usepackage{hyperref}
\hypersetup{
  colorlinks=false,
  pdfborder={0 0 1},
  citebordercolor={0 1 0},
  linkbordercolor={1 0 0},
  urlbordercolor={0 1 0}
}
```

Expected Paper 36 result after rebuild:

- Page count remains 25.
- All 12 existing citation/link annotations remain green.
- All 9 URL annotations become VLA-style green instead of cyan.
- All 3 internal-reference annotations remain red.
- All 24 link annotations keep visible border `(0, 0, 1)`.
- No experiment data, figures, tables, claims, captions, or manuscript body text changes.

## Execution Plan

1. Render the current Downloads PDF pages 2, 5, 11, and 25 to a Paper36 baseline folder under `C:/Users/wangz/highlight_box_hardening/tmp/pdfs/`.
2. Add the VLA-v4 `\hypersetup` block immediately after `\usepackage{hyperref}` in `paper/main.tex`.
3. Rebuild using `scripts/build_pdf.ps1`, which exports only `C:/Users/wangz/Downloads/36.pdf`, records ignored build metadata, and removes local `paper/main.pdf`.
4. Verify with `pypdf` that the rebuilt PDF has 25 pages, 21 green citation/URL link annotations, 3 red internal-reference annotations, and 24 visible `(0, 0, 1)` borders.
5. Render affected post-change pages 2, 5, 11, and 25 and visually inspect the boxes for role-model-like color, line weight, alignment, spacing, and legibility, paying special attention to URL boxes on page 25.
6. Update README, child status, final audit, reproducibility checklist, submission decision, version log, and full-scale execution metadata with the final hash and VLA-style visual QA evidence.
7. Remove Paper36 temporary render folders after QA while preserving the shared `role_model` render.
8. Commit and push the clean repo before moving to Paper35.

## Non-Goals

- Do not rerun the full-scale perception-control-contract suite.
- Do not pad content or alter the 25-page manuscript.
- Do not revise scientific claims, tables, captions, figures, or body text unless visual QA exposes a layout defect that requires a tiny local fix.

## Final QA Result

- Rebuilt canonical PDF: `C:/Users/wangz/Downloads/36.pdf`.
- Final SHA256: `F9CD804DFC345B0111BEB680CF0B0E9BD78C5C20D5A2D4D61AFD2FAF85FBB8D1`.
- Final size: 357177 bytes.
- Page count remains 25.
- Annotation inventory: 21 green citation/URL link boxes, 3 red internal-reference boxes, and 24 visible `(0, 0, 1)` borders.
- Visual QA rendered pages 2, 5, 11, and 25 at 160 dpi. The boxes are thin, aligned, legible, collision-free, and page 25 URL boxes now match the VLA-v4 green treatment.
- Local `paper/main.pdf` was removed by the build wrapper after export.
