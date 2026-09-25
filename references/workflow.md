# InkPost workflow

## Contents

- Source hierarchy
- Content-to-HTML transformation
- Theme synchronization
- Local user-state boundary
- Release sequence

## Source hierarchy

1. `archebase-vi-guide` for approved brand evidence and release gates.
2. `assets/archebase-wechat-safe.css` in this repository for the canonical WeChat layout CSS payload.
3. InkPost's built-in ArcheBase preset for runtime rendering.
4. A local InkPost theme only for comparison and explicit synchronization.

## Content-to-HTML transformation

The normal deliverable is not a modified InkPost installation. It is the HTML produced by InkPost from supplied article content and the canonical CSS:

1. Accept Markdown, or convert supplied prose to Markdown while preserving meaning and claims.
2. Open the content in InkPost and select the ArcheBase WeChat preset.
3. Let InkPost render Markdown, inline CSS, process local images and produce the `#nice` clipboard payload.
4. Inspect the rendered preview and run the CSS scanner.
5. Click InkPost's existing **复制到剪贴板** action.
6. Paste into the WeChat editor and verify the external result.

The skill coordinates this sequence; it does not need a second CLI renderer or a modification to InkPost source for ordinary article work.

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
