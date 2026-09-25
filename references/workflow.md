# InkPost workflow

## Contents

- Source hierarchy
- Content-to-HTML transformation
- Endpoint configuration
- Theme synchronization
- Local user-state boundary
- Release sequence

## Source hierarchy

1. `archebase-vi-guide` for approved brand evidence and release gates.
2. `assets/archebase-wechat-safe.css` in this repository for the canonical WeChat layout CSS payload.
3. InkPost's built-in ArcheBase preset for runtime rendering.
4. A local InkPost theme only for comparison and explicit synchronization.

## Content-to-HTML transformation

The skill should call InkPost directly when a reachable render endpoint is available. The current request shape is:

```http
POST /api/render
Content-Type: application/json

{"markdown":"# Title\n\nBody","css":"...canonical CSS...","filePath":"/absolute/path/article.md"}
```

The response is InkPost's `RenderResult`; use its `html` field as the final WeChat HTML payload and inspect `warnings`, `wordCount`, `imageCount` and `totalSizeKB` before delivery. Do not wrap the result in a new document: InkPost already returns the `#nice` clipboard fragment.

If `/api/render` is unavailable or requires authentication, open the local InkPost UI, load the same Markdown and select the ArcheBase preset. The UI is a fallback invocation surface, not a different renderer. Use its existing preview, scanner and **复制到剪贴板** action.

The skill coordinates this sequence; it does not modify InkPost source or create a second rendering implementation.
## Endpoint configuration

Prefer an explicit endpoint supplied by the runtime or project configuration, for example `INKPOST_RENDER_URL`. If no endpoint is supplied, try the configured InkPost service URL documented by the project; do not guess a production hostname. A successful health check does not prove `/api/render` is authorized: treat HTTP 401/403 as an authentication boundary and use the UI fallback.

The endpoint owns rendering. The skill owns the request payload, canonical CSS, response inspection and release decision.

## Theme synchronization

The canonical CSS source is `assets/archebase-wechat-safe.css`. InkPost embeds the same payload in its built-in preset. Change the canonical asset first, then synchronize and parity-check the runtime preset only when the theme itself changes.

## Local user-state boundary

InkPost persists user themes and drafts under its platform-specific application data directory. This state is not a repository source. Never commit the complete store: it contains drafts, recent files, timestamps and potentially confidential content.

When explicit synchronization is requested, update only the named theme record and preserve every other store field. If the local theme differs from the canonical CSS, report the diff and source identity.

## Release sequence

- Select `guided` or `strict` through `archebase-vi-guide`.
- Fill the article brief and identify claims, assets, rights and naming approvals.
- Validate CSS.
- Render in InkPost and inspect the preview.
- Run InkPost's own scanner.
- Copy the rendered HTML through InkPost's existing action.
- Paste into WeChat and inspect for drift.
- Run the VI Guide release gates.
- Return one verdict with unresolved owner and impact.
