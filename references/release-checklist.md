# InkPost WeChat release checklist

- [ ] `archebase-vi-guide` loaded and mode selected: `guided` or `strict`.
- [ ] Article brief identifies audience, one-sentence takeaway, destination and preview width.
- [ ] One `h1`; no more than three meaningful hierarchy levels.
- [ ] Theme source is named and canonical CSS identity is recorded.
- [ ] `validate_inkpost_css.py` passes against the exact CSS being exported.
- [ ] InkPost's own WeChat scanner has no unreviewed warning.
- [ ] No orange CTA/status color, arbitrary saturated color or layout gradient.
- [ ] Images preserve aspect ratio and are inspected at the actual crop.
- [ ] Any Logo is an unmodified approved V2 asset; no generated or CSS-improvised mark.
- [ ] Claims, metrics, customer material, image rights and naming have sources or owners.
- [ ] Rendered article inspected for wrapping, overflow, contrast, code, tables, callouts and first-screen hierarchy.
- [ ] If the built-in preset changed, `check_preset_parity.py` passes.
- [ ] VI Guide asset/design/claims-rights/export gates are recorded.
- [ ] One release verdict is returned with owner and impact for every unresolved blocker.
