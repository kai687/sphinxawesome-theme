# Update to version 2.0

:::{caution}
The Sphinx awesome theme version 2.0 requires Sphinx 4.0 or newer.
:::

While version 2.0 of the Sphinx awesome theme doesn't include major new features,
two main factors contributed to the decision to make this release a **major breaking change**.

First, version 2.0 requires Sphinx 4 or newer.
This allows to get rid of some custom HTML transformations.
Sphinx 4 depends on docutils 0.17, which builds more semantic HTML by default.
For example, instead of `<div class="section">`, docutils now returns `<section>` by default.

Second, I restructured some templates.
Changing the layout to [CSS grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout) allows reducing the amount of container elements in the templates.
While I expect the effect for regular users to be minor,
be careful if you use custom templates, or custom CSS with this theme.
