# ArcheBase WeChat Layout

Turns article content into a WeChat-ready `#nice` HTML payload for 智域基石公众号 by normalizing Markdown, applying the canonical WeChat CSS payload and driving the public `archebase/inkpost` renderer.
This repository owns WeChat layout rules, the canonical CSS, compatibility validation and preset parity; it does not own brand evidence and does not render.
`SKILL.md` is the agent-behaviour contract; this README is repository-level orientation only. No agent rule lives here alone.

| Field | Value |
|---|---|
| Skill id | `archebase-wechat-layout` |
| Version | `0.2.0` |
| License | Proprietary. For ArcheBase organization use only; do not redistribute brand assets or internal layout rules. |
| Status | internal release 0.2.0 (no tag or release in this checkout) |
| Dependencies | `archebase-vi-guide, archebase/inkpost` |
| Repository | https://github.com/archebase/archebase-wechat-layout.git |

## Scope

- **Owns:** manuscript-to-Markdown normalization, canonical CSS selection (`assets/archebase-wechat-safe.css`), InkPost invocation, WeChat compatibility rules, preset parity checks and the single release verdict.
- **Delegates:** `archebase-vi-guide` — brand evidence, Logo assets, colors, typography evidence, mode selection and release gates. `archebase/inkpost` — Markdown parsing, preview, CSS inlining, image processing, math rendering and `#nice` HTML generation. `archebase-wechat-editor` — article content and narrative editing before layout.
- **Refuses:** vendoring or independently modifying InkPost renderer code; inventing, redrawing, recoloring or CSS-constructing an ArcheBase Logo; reading the VI Guide p.28 50/25/10/5 labels as component-level CSS quotas; introducing orange as a CTA or status color; suppressing an InkPost scanner warning to make a result pass; releasing on a scanner pass alone; overwriting a user's complete InkPost config store.

## Modes

| Mode | Use when | Required evidence |
|---|---|---|
| `guided` (default) | all normal article layout work | canonical CSS validation, InkPost `warnings` and render statistics, rendered visual inspection |
| `strict` | formal VI compliance, official release preparation or brand-owner approval is requested | the `guided` evidence plus recorded `archebase-vi-guide` release gates |

A `guided` result must never be reported as strict VI approval.

## Quick start

1. Load `archebase-vi-guide` and select `guided` or `strict`. If the dependency is unavailable, report `VI dependency unavailable` and stop short of claiming brand compliance.
2. Normalize the manuscript: keep 主标题 as external title metadata, convert peer sections such as `智域基石：…`, `千觉：…`, `连接…`, `关于智域基石` and `关于千觉` to `h1`, nest deeper levels as `h2`/`h3`, render 摘要 as an `::: info` block, and preserve every `〔…〕` field as an unresolved blocker.
3. Validate the canonical CSS.
4. Pin an `archebase/inkpost` commit or release, then call its renderer with `{ markdown, css, filePath? }`.
5. Inspect the returned HTML, `warnings`, `wordCount`, `imageCount` and `totalSizeKB`; correct the Markdown or CSS and render again.
6. Paste the HTML into the WeChat editor as the external-surface check, then return one verdict: `可发布`, `修复后复审`, or `阻塞，待确认`.

```bash
python3 scripts/validate_inkpost_css.py assets/archebase-wechat-safe.css
```

## Commands

| Command | Purpose |
|---|---|
| `python3 scripts/validate_inkpost_css.py assets/archebase-wechat-safe.css` | Validate the canonical CSS against the approved palette and the WeChat-unsafe property/display/color rules; exits `1` with per-line errors |
| `python3 scripts/check_preset_parity.py /path/to/inkpost` | Compare the canonical CSS with InkPost's preset payload at `src/shared/presets/archebase-wechat-safe.ts`; prints a unified diff and exits `1` on mismatch |
| `python3 -m py_compile scripts/*.py` | Syntax-check both validators |
| `python3 -m json.tool evals/evals.json >/dev/null` | Parse-check the eval suite |

`check_preset_parity.py` takes `--css` to override the canonical payload; the default is `assets/archebase-wechat-safe.css` relative to the script.

### InkPost integration

InkPost is a separate public runtime and the only renderer implementation; its sources are not part of this repository.

- Pinned checkout: call the exported `renderMarkdown(markdown, css, filePath?, imageOptions?)` contract from `src/main/renderer.ts`.
- Configured online deployment: `POST /api/render` with the same inputs, used only when explicitly configured.

```json
{ "html": "string", "imageCount": 0, "wordCount": 0, "warnings": [], "totalSizeKB": 0 }
```

`html` is already the inline-styled `<section id="nice">…</section>` fragment; do not wrap it or run a second renderer.

## Bundle layout

```text
SKILL.md       agent-behaviour contract: boundary, required references, workflow, output contract, hard stops
references/    workflow.md, layout-rules.md, release-checklist.md — loaded before transforming, restyling or releasing
scripts/       validate_inkpost_css.py, check_preset_parity.py — deterministic validators
assets/        archebase-wechat-safe.css — the canonical WeChat CSS payload
evals/         evals.json — five skill evals
.github/       workflows/validate.yml — CI for CSS, script and eval checks
```

`SKILL.md` lists the load trigger for each reference; `references/workflow.md` holds the pinning and synchronization rules.

## Validation

```bash
python3 scripts/validate_inkpost_css.py assets/archebase-wechat-safe.css
python3 -m py_compile scripts/*.py
python3 -m json.tool evals/evals.json >/dev/null
```

These are the steps in `.github/workflows/validate.yml`; they prove palette and property safety plus script and eval parseability.
They cannot prove rendering output, WeChat paste fidelity or preset parity — the parity check needs an InkPost checkout and is not part of this workflow.

## Install

```bash
git clone https://github.com/archebase/archebase-wechat-layout.git
ln -s "$PWD/archebase-wechat-layout" ~/.agents/skills/archebase-wechat-layout
```

Satisfy first: `archebase-vi-guide` in the same skill library, a public `archebase/inkpost` checkout, and Python 3 for the validators.
This repository records no InkPost commit or release: `references/workflow.md` requires the exact commit or release to be recorded per deterministic build and treats a floating `main` reference as insufficient evidence.

## Status

Version `0.2.0`; latest commit `37f9b0b` (`feat: normalize public-account heading hierarchy`, 2026-09-25) on branch `main`.
Verified in-repo: file inventory, both validators' behaviour, the CI steps above, and the 5 eval cases in `evals/evals.json`.
Not run here: preset parity against an InkPost checkout, any InkPost render, and any WeChat paste; the InkPost pin is caller-supplied and not recorded in this repository.

## Related skills

- `archebase-vi-guide` — required dependency for brand evidence, mode selection and release gates.
- `archebase-wechat-editor` — content and narrative editing that precedes this layout layer.
- `archebase/inkpost` — external renderer repository, pinned per build.
