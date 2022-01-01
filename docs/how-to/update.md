---
html_meta:
  description: |
    Updating the Awesome Theme is straightforward for most users.
    Find out what you should consider when updating between major versions.
---

# Update the theme

```{rst-class} lead
Updating the Awesome Theme is straightforward for most users.
If you use any customization on top of the Awesome Theme,
you might have to update these modifications.
```

---

<!-- vale Google.WordList = NO -->

```{eval-rst}
   "The thing about semver major version numbers are that they don't mean new stuff,
   they're a permanent reminder of how many times you got the API wrong. Semver doesn't
   mean MAJOR.MINOR.PATCH, it means FAILS.FEATURES.BUGS"

   -- @willmcgugan (seen on Twitter)
```

## Version 3.0

<!-- vale Google.Colons = NO -->

Redesign
: Create a better visual hierarchy which makes the document easier to scan. Heavily
inspired by the [Material Design](https://material.io/) website.

Restructure
: This is mostly internal, but all JavaScript is now using the
[Stimulus](https://stimulus.hotwired.dev/) framework.

## Version 2.0

<!-- vale Google.WordList = YES -->

Version 2.0 of the Awesome Theme includes these **major breaking changes**:

Require Sphinx 4 or newer
: Sphinx 4 depends on docutils 0.17, which creates more semantic HTML by default.
This allows to reduce the amount of custom transformations.

Restructure a few templates
: the layout use
[CSS grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout).
This leads to fewer container elements in the templates.
