---
name: archebase-wechat-inkpost
description: ArcheBase WeChat article layout and QA workflow for InkPost. Use whenever creating, correcting, reviewing, importing, exporting, or synchronizing InkPost Markdown/CSS for 智域基石, including requests to keep WeChat articles visually consistent, fix typography and hierarchy, check微信兼容性, or prepare content for公众号 publication.
license: Proprietary. For ArcheBase organization use only; do not redistribute brand assets or internal layout rules.
metadata:
  version: "0.1.0"
  source: "ArcheBase VI Guide + InkPost"
  dependency: "archebase-vi-guide"
compatibility: "Requires the archebase-vi-guide skill and either the InkPost repository or a local InkPost installation. Python 3 is required for deterministic validators."
---

# ArcheBase WeChat InkPost

A channel/tool adapter for producing consistent ArcheBase WeChat articles in InkPost. It owns Markdown/CSS layout mechanics, WeChat-safe checks and InkPost preset parity. It does not redefine ArcheBase brand rules: load `archebase-vi-guide` for VI evidence, assets, modes and release gates.

## Boundary

- `archebase-vi-guide` is the source for brand evidence, Logo assets, colors, typography evidence, visual grammar and release governance.
- `archebase-wechat-inkpost` is the source for WeChat article layout, InkPost workflow, CSS compatibility and preset synchronization.
- InkPost is the runtime: Markdown parsing, preview rendering, CSS inlining, image processing and clipboard export.
- `archebase-wechat-editor` may be used for article content and narrative editing; it does not replace this layout workflow.

Do not put InkPost implementation details into `archebase-vi-guide`. Do not treat a local InkPost user theme as the canonical source.

## Required references

1. Load `archebase-vi-guide` before making brand decisions. If it is unavailable, stop short of claiming VI compliance and report the missing dependency.
2. Load `references/workflow.md` before editing or synchronizing an InkPost theme.
3. Load `references/layout-rules.md` before changing Markdown structure or CSS.
4. Load `references/release-checklist.md` before reporting a release verdict.
5. Run `scripts/validate_inkpost_css.py` against the exact CSS being exported.
6. When changing the built-in InkPost preset, run `scripts/check_preset_parity.py` against the InkPost checkout.

## Default mode

Use the VI Guide's `guided` mode by default. Use `strict` only when the user asks for formal VI compliance, official release preparation or brand-owner approval. Never claim strict VI approval from a guided result.

## Workflow

1. Establish article purpose, audience, one-sentence takeaway, Markdown path, target WeChat surface and preview width.
2. Identify whether this is a new layout, a correction, a CSS import/export or a preset synchronization.
3. Resolve the canonical CSS from `assets/archebase-wechat-safe.css`; do not silently take CSS from `~/Library/Application Support/墨帖 InkPost/config.json`.
4. Apply `references/layout-rules.md` to hierarchy, callouts, body copy, images, code and tables.
5. Run the deterministic CSS validator and InkPost's own CSS scanner.
6. Render the real Markdown through InkPost and inspect actual wrapping, overflow, contrast, crop and first-screen hierarchy.
7. For preset changes, run the parity check and update the InkPost wrapper only after the canonical CSS is changed.
8. Apply `archebase-vi-guide` release gates and return one verdict: `可发布`, `修复后复审`, or `阻塞，待确认`.

## Output contract

Return:

- mode, article scope and primary audience judgment;
- theme source and preset identity;
- layout decisions and changed components;
- deterministic validator, InkPost scanner and rendered-preview results;
- claims, asset, rights, naming and type approvals still unresolved;
- final release verdict and owner/impact for every blocker.

## Hard stops

- Never invent, redraw, recolor, distort or CSS-construct an ArcheBase Logo. Resolve supplied V2 assets through `archebase-vi-guide`.
- Never turn the VI Guide p.28 50/25/10/5 labels into component-level CSS quotas; the remaining 10% is unassigned.
- Never introduce orange as an official brand CTA or status color.
- Never suppress an InkPost scanner warning to make a result pass; fix the layout or record an explicit reviewed exception.
- Never overwrite a user's complete InkPost config store. Synchronize only the named theme record when explicitly requested.
- Never release on a scanner pass alone; visual inspection of the rendered article is required.

## Failure handling

- Missing `archebase-vi-guide`: report `VI dependency unavailable`; do not claim brand compliance.
- Missing InkPost app: use repository renderer checks and report runtime preview as skipped.
- CSS parity failure: report the two source paths and stop preset release until they match.
- Ambiguous VI rule: mark `待确认`; do not invent precision.
- Visual overflow, unreadable wrapping or failed export: return `修复后复审` and identify the exact component.
