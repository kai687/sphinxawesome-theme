---
orphan: true
layout: "without-sidebar"
myst:
  html_meta:
    description: The Awesome Sphinx Theme is built on top of open source assets.
---

# About

```{rst-class} lead
This pages lists assets that the {{ product }} uses to be awesome.
```

---

To see the full list of dependencies, see these files:

- {gh}`pyproject.toml` for Python dependencies
- {gh}`package.json <src/theme-src/package.json>` for JavaScript dependencies

<!-- vale Vale.Spelling = NO -->

| Feature           | Name/Website     | License |
| ----------------- | ---------------- | ------- |
| CSS framework     | [Tailwind]       | [MIT License](https://github.com/tailwindlabs/tailwindcss/blob/master/LICENSE) |
| Copy to clipboard | [Clipboard.js]   | [MIT License](https://github.com/zenorocha/clipboard.js/blob/master/LICENSE) |
| Fonts             | [Roboto]         | [Apache License, Version 2.0] |
|                   | [JetBrains Mono] | [SIL Open Font License, 1.1] |
| Icons             | [Material icons] | [Apache License, Version 2.0] |
| Tooltips          | [Primer/CSS]     | [MIT License](https://github.com/primer/css/blob/main/LICENSE) |
| **Note:** versions ≤ 1.13.1 used these icons instead: | [Entypo] by Daniel Bruce | [Creative Commons Attribution-ShareAlike 4.0] |
|                   | [Zondicons] by Steve Schoger  | ?  |
| Illustrations     | [undraw.co]      | [custom] |

[Tailwind]: https://tailwindcss.com
[Clipboard.js]: https://clipboardjs.com
[Roboto]: https://github.com/googlefonts/roboto
[JetBrains Mono]: https://github.com/JetBrains/JetBrainsMono/
[SIL Open Font License, 1.1]: https://github.com/JetBrains/JetBrainsMono/blob/master/OFL.txt
[Material icons]: https://fonts.google.com
[undraw.co]: https://undraw.co
[custom]: https://undraw.co/license
[Primer/CSS]: https://primer.style/css/
[Entypo]: https://www.entypo.com
[Zondicons]: http://www.zondicons.com
[creative commons attribution-sharealike 4.0]: https://creativecommons.org/licenses/by-sa/4.0/legalcode
[apache license, version 2.0]: https://www.apache.org/licenses/LICENSE-2.0.html

<!-- vale Vale.Spelling = YES -->

## Breaking changes

Updating the {{ product }} is straightforward for most users.
If you use any customization, you might have to update your
customizations manually.

### Version 4.0

Version 4.0 of the {{ product }} includes these **breaking changes**:

Add support for Sphinx 6
: Since Sphinx 6 is only supported with the latest version of the `myst-parser` package
and Sphinx 6 drops support for Python 3.7, this release is a major version update.

Apart from that, this version is identical with version 3 of the {{ product }}.

<!-- vale Google.WordList = NO -->

### Version 3.0

Redesign
: Create a better visual hierarchy which makes the document easier to scan. Heavily
inspired by the [Material Design](https://m2.material.io/) website.

Restructure
: All JavaScript is now using the
[Stimulus](https://stimulus.hotwired.dev/) framework.

### Version 2.0

<!-- vale Google.WordList = YES -->

Version 2.0 of the {{ product }} includes these **breaking changes**:

Require Sphinx 4 or newer
: Sphinx 4 depends on docutils 0.17, which creates more semantic HTML by default.
This allows to reduce the amount of custom transformations.

Restructure several templates
: The layout use
[CSS grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout).
This leads to fewer container elements in the templates.
