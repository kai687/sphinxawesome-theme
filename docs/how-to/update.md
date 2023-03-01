---
myst:
  html_meta:
    description: |
      Updating the Awesome Theme is straightforward for most users.
      Find out what you should consider when updating between major versions.
---

# Update the theme

```{rst-class} lead
Updating the {{ product }} is straightforward for most users.
If you use any customization, you might have to update your
customizations manually.
```

---

<!-- vale Google.Colons = NO -->

## Version 4.0

Version 4.0 of the {{ product }} includes these **breaking changes**:

Add support for Sphinx 6
: Since Sphinx 6 is only supported with the latest version of the `myst-parser` package
and Sphinx 6 drops support for Python 3.7, this release is a major version update.

Apart from that, this version is identical with version 3 of the {{ product }}.

<!-- vale Google.WordList = NO -->

## Version 3.0

Redesign
: Create a better visual hierarchy which makes the document easier to scan. Heavily
inspired by the [Material Design](https://m2.material.io/) website.

Restructure
: All JavaScript is now using the
[Stimulus](https://stimulus.hotwired.dev/) framework.

## Version 2.0

<!-- vale Google.WordList = YES -->

Version 2.0 of the {{ product }} includes these **breaking changes**:

Require Sphinx 4 or newer
: Sphinx 4 depends on docutils 0.17, which creates more semantic HTML by default.
This allows to reduce the amount of custom transformations.

Restructure several templates
: The layout use
[CSS grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout).
This leads to fewer container elements in the templates.
