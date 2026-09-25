# InkPost workflow

## Contents

- Source hierarchy
- Manuscript-to-Markdown extraction
- Content-to-HTML transformation
- Runtime pinning
- Theme synchronization
- Local user-state boundary
- Release sequence

## Source hierarchy

1. `archebase-vi-guide` for approved brand evidence and release gates.
2. `assets/archebase-wechat-safe.css` in this repository for the canonical WeChat layout CSS payload.
3. `https://github.com/archebase/inkpost` at a pinned commit or release for rendering.
4. A local InkPost theme only for comparison and explicit synchronization.

## Manuscript-to-Markdown extraction

When input is plain prose rather than Markdown, normalize it before invoking InkPost:

1. Preserve the supplied wording and facts; do not silently rewrite claims.
2. Extract `主标题` as external公众号 title metadata. Do not repeat it in the Markdown body unless the user explicitly requests an in-body title.
3. Convert a value labeled `副标题` to a normal paragraph with a bold lead-in; do not create a heading unless the user explicitly identifies it as a structural section.
4. Convert `摘要` to an `::: info` block; the abstract is content, not a heading.
5. Convert peer top-level body sections such as `智域基石：…`, `千觉：…`, `连接…`, `关于智域基石` and `关于千觉` to `h1`. Convert sections nested under them to `h2`, and deeper subsections to `h3`.
6. Convert explicit `---` separators to Markdown `---`.
7. Convert standalone `[图片]` markers to image placeholders with descriptive alt text. If no actual image file or approved asset exists, do not invent a URL or image; retain a visible `待补充` placeholder and block release.
8. Convert `-` lines to list items, quoted speaker sections to blockquotes, and labeled warnings/confirmation notes to `::: warning` blocks.
9. Preserve every `〔…〕` field as an unresolved placeholder. Add it to the release blocker list; never fill it from inference.
10. Render the normalized Markdown with the canonical CSS through the pinned public InkPost runtime.

The normalized Markdown is an intermediate artifact. The primary delivery remains InkPost's rendered `#nice` HTML.

## Content-to-HTML transformation

InkPost is a separate public runtime and the only renderer implementation. Pin a commit or release, install its dependencies, and invoke its exported `renderMarkdown(markdown, css, filePath?, imageOptions?)` contract from `src/main/renderer.ts`.

The expected result is:

```ts
{
  html: string;
  imageCount: number;
  wordCount: number;
  warnings: string[];
  totalSizeKB: number;
}
```

Use `html` as the WeChat payload. It is already the inline-styled `<section id="nice">…</section>` fragment; do not wrap it or run a second renderer. Inspect warnings and render statistics before delivery.

An authenticated InkPost online deployment may expose the same contract through `POST /api/render`. Use it only when explicitly configured. Otherwise invoke the pinned repository renderer locally. The Electron UI remains an optional human preview/copy surface.

## Runtime pinning

Record the InkPost repository URL and exact commit or release used for each deterministic build. A floating `main` reference is not sufficient evidence that two sessions used the same renderer.

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
