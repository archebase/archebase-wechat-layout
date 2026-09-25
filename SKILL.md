---
name: archebase-wechat-layout
description: ArcheBase WeChat article layout and QA workflow. Use whenever creating, correcting, reviewing, importing, exporting, or synchronizing Markdown/CSS for 智域基石公众号 articles, including requests to keep WeChat articles visually consistent, fix typography and hierarchy, check微信兼容性, or prepare content for publication in InkPost or another supported layout tool.
license: Proprietary. For ArcheBase organization use only; do not redistribute brand assets or internal layout rules.
metadata:
  version: "0.2.0"
  source: "ArcheBase VI Guide + WeChat layout"
  dependency: "archebase-vi-guide, archebase/inkpost"
  repository: "archebase/archebase-wechat-layout"
compatibility: "Requires archebase-vi-guide, the public archebase/inkpost renderer at a pinned commit or release, and Python 3 for deterministic validators."
---

# ArcheBase WeChat Layout

A content-to-HTML workflow for ArcheBase WeChat articles. Given article content, invoke the public `archebase/inkpost` renderer with Markdown and the canonical CSS, then return its `#nice` HTML payload. The Skill owns content normalization, brand layout decisions and QA; InkPost remains the single rendering implementation.

## Boundary

- `archebase-vi-guide` is the source for brand evidence, Logo assets, colors, typography evidence, visual grammar and release governance.
- `archebase-wechat-layout` is the orchestration layer: content normalization, canonical CSS selection, InkPost invocation and release QA.
- `archebase/inkpost` is the public runtime: Markdown parsing, CSS inlining, image processing, math rendering and `#nice` HTML generation.
- `archebase-wechat-editor` may be used for article content and narrative editing before layout; it does not replace this transformation.

The primary deliverable is rendered HTML. Do not vendor or independently modify InkPost renderer code inside this Skill.

Do not put InkPost implementation details into `archebase-vi-guide`. Do not treat a local InkPost user theme as the canonical source.

## Required references

1. Load `archebase-vi-guide` before making brand decisions. If it is unavailable, stop short of claiming VI compliance and report the missing dependency.
2. Load `references/workflow.md` before transforming article content.
3. Load `references/layout-rules.md` before changing Markdown structure or CSS.
4. Load `references/release-checklist.md` before returning rendered HTML.
5. Validate the canonical CSS with `scripts/validate_inkpost_css.py` before invoking InkPost.
6. Resolve and pin an `archebase/inkpost` commit or release; call its renderer contract rather than carrying a copied implementation.

## Default mode

Use the VI Guide's `guided` mode by default. Use `strict` only when the user asks for formal VI compliance, official release preparation or brand-owner approval. Never claim strict VI approval from a guided result.

## Workflow

1. Receive article content as Markdown or convert supplied prose into Markdown while preserving meaning and claims.
2. Establish audience, one-sentence takeaway, target WeChat surface and preview width.
3. Resolve the canonical CSS from `assets/archebase-wechat-safe.css`.
4. Call InkPost's render endpoint with `{ markdown, css, filePath? }` and capture its `html`, `warnings`, `wordCount`, `imageCount` and `totalSizeKB` result.
5. Inspect the returned HTML or InkPost preview; correct hierarchy, callouts, body copy, code, tables, images and overflow, then render again.
6. Return the rendered `#nice` HTML as the primary result. When operating through the InkPost UI, use its existing **复制到剪贴板** action after preview and scanner checks pass.
7. Paste the HTML into the WeChat editor as the final external-surface check. If wrapping, images, styles or spacing change, return to Markdown/CSS and re-render.
8. Apply `archebase-vi-guide` release gates and return one verdict: `可发布`, `修复后复审`, or `阻塞，待确认`.

## Output contract

The primary output is the rendered HTML copied to the clipboard by InkPost.

Return:

- a confirmation that the HTML was copied through InkPost's existing copy action;
- mode, article scope and primary audience judgment;
- theme source and preset identity;
- layout decisions and changed components;
- deterministic validator, InkPost scanner and rendered-preview results;
- the WeChat paste verification result;
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
