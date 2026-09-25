# WeChat layout rules

## Contents

- Hierarchy
- VI channel mapping
- InkPost containers
- WeChat-safe CSS
- Images and content blocks
- Unconfirmed decisions

## Hierarchy

- Use one `h1` for the article title.
- Use `h2` and `h3` for meaningful sections; keep no more than three meaningful hierarchy levels.
- Put the conclusion before explanatory metadata where the article permits.
- Do not create decorative headings or use color as a substitute for structure.

## VI channel mapping

These are InkPost channel mappings, not new semantic roles in the VI Guide:

| Role | CSS value | Evidence boundary |
|---|---|---|
| Structural headings and links | `#0032FF` | VI Guide p.28 color evidence |
| Secondary hierarchy and quotation edge | `#7172FA` | VI Guide p.28 color evidence |
| Secondary annotation edge | `#619AFD` | VI Guide p.28 color evidence |
| Restrained highlight edge | `#46CFFF` | VI Guide p.28 color evidence |
| Body copy and technical dark field | `#1E2124` | VI Guide pp.30–32 neutral examples |

Use `Source Han Sans SC` / 思源黑体 as the preferred Chinese family with system fallbacks. Poppins is the Latin family displayed by the Guide; production files, CSS weights and licensing remain `待确认`.

Do not treat the p.28 labels 50/25/10/5 as per-component CSS quotas. Their labelled total is 90%; the remaining 10% is not assigned by the Guide.

## InkPost containers

Use `::: block-1`, `::: block-2`, `::: block-3`, `::: info`, `::: tip`, `::: warning` and `::: danger` only for semantic callouts. Reuse a callout treatment consistently for the same meaning within one article.

Keep body copy neutral. Use blue for structural emphasis, not as a large colored body texture. Code and tables should prioritize legibility over decoration.

## WeChat-safe CSS

Avoid properties that InkPost flags or that are unreliable in WeChat:

- `display: flex`, `grid`, `inline-flex`, `inline-grid`;
- `position: fixed` or `sticky`;
- animation, transition, transform and filter;
- masks, clip paths, multi-column layout, object-fit and vertical writing mode;
- gradients as a dependency of ordinary article layout.

Do not introduce orange as an official ArcheBase CTA or status color. Any extra campaign color belongs to a separately approved creative decision and must not be presented as an official token.

## Images and content blocks

Images must carry evidence or narrative. Preserve aspect ratio and inspect the actual WeChat crop. Do not use CSS to reconstruct an official Logo; resolve and place the approved V2 asset through `archebase-vi-guide`.

## Unconfirmed decisions

Mark these `待确认` rather than inventing values:

- exact neutral compositing and opacity implementation;
- production font files, weights and licensing;
- Logo clear space and minimum size in a WeChat article;
- ArcheBase / ArchBase / ARCHBASE naming in article copy;
- warning/error semantic role mapping.
