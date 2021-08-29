# Update the theme

```{rst-class} lead
If you use any customization on top of this theme and you don't use your own fork,
you might have to update your own modifications, as template structure and names might
have changed. If you don't like any of the changes of a new update, you can always
_pin the version_ of the theme.
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

Version 2.0 of the Sphinx awesome theme includes these **major breaking changes**:

Require Sphinx 4 or newer
: Sphinx 4 depends on docutils 0.17, which creates more semantic HTML by default.
This allows to reduce the amount of custom transformations.

Restructure a few templates
: Sphinx awesome theme 2.0 changes the main layout philosophy to [CSS
grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout). This allows
reducing the amount of container elements in the templates.
