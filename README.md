# ArcheBase WeChat InkPost Skill

Organization skill for laying out and quality-checking ArcheBase WeChat articles in InkPost.

## Responsibility boundary

- `archebase-vi-guide`: official brand evidence, Logo assets, visual grammar, modes and release governance.
- `archebase-wechat-inkpost`: WeChat/InkPost layout rules, canonical CSS, compatibility validation and preset parity.
- `InkPost`: Markdown rendering, preview, CSS inlining, image processing and clipboard export.

The skill depends on `archebase-vi-guide`; it does not redefine brand rules.

## Install

Install the repository as `archebase-wechat-inkpost` in the organization's skill library, alongside `archebase-vi-guide`:

```sh
git clone https://github.com/archebase/archebase-wechat-inkpost.git
ln -s "$PWD/archebase-wechat-inkpost" ~/.agents/skills/archebase-wechat-inkpost
```

## Validation

```sh
python3 scripts/validate_inkpost_css.py assets/archebase-wechat-safe.css
python3 scripts/check_preset_parity.py /path/to/inkpost
```

The canonical CSS is `assets/archebase-wechat-safe.css`. The InkPost repository embeds the same payload in its built-in preset and must pass the parity check before a preset release.

Brand assets and the full VI Guide remain governed by `archebase-vi-guide` and are not duplicated here.
