# InkPost workflow

## Contents

- Source hierarchy
- Theme synchronization
- Local user-state boundary
- Release sequence

## Source hierarchy

1. `archebase-vi-guide` for approved brand evidence and release gates.
2. `assets/archebase-wechat-safe.css` in this repository for the canonical InkPost CSS payload.
3. `src/shared/presets/archebase-wechat-safe.ts` in the InkPost repository for the runtime wrapper.
4. A local InkPost theme only for comparison and explicit synchronization.

## Theme synchronization

The canonical CSS source is `assets/archebase-wechat-safe.css`. The InkPost repository embeds the exact payload inside a TypeScript preset wrapper. Do not make independent edits to the wrapper payload.

Change sequence:

1. Edit the canonical CSS asset.
2. Run `python3 scripts/validate_inkpost_css.py assets/archebase-wechat-safe.css`.
3. Copy the exact payload into InkPost's preset wrapper.
4. Run `python3 scripts/check_preset_parity.py /path/to/inkpost`.
5. Run InkPost tests and TypeScript checks.
6. Review the rendered article before release.

## Local user-state boundary

InkPost persists user themes and drafts under its platform-specific application data directory. This state is not a repository source. Never commit the complete store: it contains drafts, recent files, timestamps and potentially confidential content.

When explicit synchronization is requested, update only the named theme record and preserve every other store field. If the local theme differs from the canonical CSS, report the diff and source identity.

## Release sequence

- Select `guided` or `strict` through `archebase-vi-guide`.
- Fill the article brief and identify claims, assets, rights and naming approvals.
- Validate CSS.
- Run InkPost's own scanner.
- Render at the actual WeChat preview width.
- Inspect the rendered surface, not just source CSS.
- Run the VI Guide release gates.
- Return one verdict with unresolved owner and impact.
