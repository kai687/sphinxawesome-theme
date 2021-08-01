# Update to version 2.0

```{note}
The Sphinx awesome theme version 2.0 requires Sphinx 4.0 or newer.
```

<!-- vale Google.WordList = NO -->

If you didn't pin the version of the `sphinxawesome-theme` package, the theme's version
should be updated automatically. If you use custom CSS or custom templates, check
carefully, if you need to update your custom additions.

<!-- vale Google.WordList = YES -->

Version 2.0 of the Sphinx awesome theme includes these **major breaking changes**:

<!-- vale Google.Colons = NO -->

Require Sphinx 4 or newer
: Sphinx 4 depends on docutils 0.17, which creates more semantic HTML by default.
This allows to reduce the amount of custom transformations.

Restructure a few templates
: Sphinx awesome theme 2.0 changes the main layout philosophy to [CSS
grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout). This allows
reducing the amount of container elements in the templates.
