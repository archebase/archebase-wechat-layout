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

The skill carries a standalone InkPost-compatible renderer. It does not require the InkPost app, an online server or a remote endpoint:

```sh
npm install --prefix runtime
npx --prefix runtime tsc
node scripts/render_wechat_html.mjs article.md --output article.html
```

The command reads Markdown, applies `assets/archebase-wechat-safe.css`, runs the vendored Markdown/CSS/image/math pipeline and writes InkPost-compatible `#nice` HTML. It reports warnings and render statistics on stderr.

Use the returned or written HTML as the payload for the WeChat editor. The separate InkPost application remains a visual reference and an optional manual clipboard surface, not a runtime prerequisite.

The skill coordinates this sequence and owns the canonical wrapper; it does not modify the separate InkPost application.

## Endpoint configuration

No endpoint is required for the standard path. If an organization already operates InkPost online, its `/api/render` result may be used only as an explicitly configured comparison oracle; it must not replace the bundled runtime or become an undocumented production dependency.

The renderer owns transformation. The skill owns the Markdown input, canonical CSS, response inspection and release decision.

## Theme synchronization

The canonical CSS source is `assets/archebase-wechat-safe.css`. InkPost embeds the same payload in its built-in preset. Change the canonical asset first, then synchronize and parity-check the runtime preset only when the theme itself changes.

## Local user-state boundary

InkPost persists user themes and drafts under its platform-specific application data directory. This state is not a repository source. Never commit the complete store: it contains drafts, recent files, timestamps and potentially confidential content.

When explicit synchronization is requested, update only the named theme record and preserve every other store field. If the local theme differs from the canonical CSS, report the diff and source identity.

- Select `guided` or `strict` through `archebase-vi-guide`.
- Fill the article brief and identify claims, assets, rights and naming approvals.
- Validate CSS.
- Run the bundled renderer and inspect the generated HTML.
- Check warnings and render statistics.
- Open the generated HTML in a browser or paste it into WeChat for surface verification.
- Use the separate InkPost UI only when a human wants its manual preview/copy surface.
- Run the VI Guide release gates.
- Return one verdict with unresolved owner and impact.
