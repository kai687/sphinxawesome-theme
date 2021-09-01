(sec:customize)=

# Customize the theme

```{rst-class} lead
You can customize the theme by adding custom CSS, using custom layouts, or modify
existing templates.
```

```{contents} On this page
---
local: true
backlinks: none
---
```

For the methods listed on this page, it's better to use traditional methods to style
your templates. Extra files, aren't processed by webpack, so you can't use Tailwind's
`@apply` directive. See {ref}`sec:modify`, if you want to modify the
existing templates and use (almost) the full power of Tailwind.

(sec:override-styles)=

## Add or override styles

To add extra CSS files, use the {confval}`sphinx:html_css_files` configuration value.
To add extra JavaScript files, use the {confval}`sphinx:html_js_files` configuration
value.

For example, place additional styles in a file `_static/custom.css` and add the
following options to your Sphinx configuration in `conf.py`:

```{code-block} python
---
caption: conf.py
---
html_static_path = ["_static"]
html_css_files = ["custom.css"]
```

If you want to **override existing styles**, you might have to add `!important`.

```{seealso}
[CSS Specificity (MDN Web Docs)](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity)
```

(sec:additional-layouts)=

## Add additional page layouts

Sometimes, you want to add a custom page to your documentation, for example, a custom
homepage for the documentation project. These pages often have a different layout than the documentation pages themselves.
An example is the
[homepage of the Sphinx documentation](https://www.sphinx-doc.org/en/master/).

To add additional page layouts to your Sphinx documentation:

1. Create a directory in your Sphinx project, for example, `_templates/` and add it to
   your Sphinx configuration:

   ```{code-block} python
   ---
   caption: "File: conf.py"
   ---

   templates_path = ["_templates"]
   ```

   ```{seealso}
   {confval}`sphinx:templates_path`
   ```

1. Create a new layout file, for example, `extra-layout.html`:

   ```{code-block} html+jinja
   ---
   caption: "File: extra-layout.html"
   ---


   {% extends "layout.html" %}

   {% block body %}
   {% endblock %}
   ```

   This creates a rudimentary layout where the main text is inserted directly below
   the page header.

1. To use this custom layout, you have two options:

   - If you write your Sphinx documentation in Markdown, see
     {ref}`sec:override-layouts-locally`.

   - If you {ref}`sec:override-layouts-globally`, you can _extend_ your custom layout.
     For example, you can override the `page` template and use the `extra-layout`
     template defined previously:

     ```{code-block} html+jinja
     ---
     caption: "File: page.html"
     ---

     {% extends "extra-layout.html" %}

     {% block body %}
     {{ body }}
     {% endblock %}
     ```

     Now all pages in your documentation use your custom layout.

(sec:override-layouts-globally)=

## Override page layouts globally

If you want to override a template for _all pages of your documentation_,
place a template file in a custom `_templates` directory, as described in
{ref}`sec:additional-layouts`.

To override an existing template, you need to name it the same. For example, to use a
custom header on all pages:

1. Create a file `header.html` in the `_templates` directory:

   ```{code-block} html+jinja
   ---
   caption: "File: header.html"
   ---

   HEADER
   ```

   This shows the word _HEADER_ on every page of your documentation.

The main templates you may want to override include:

<!-- vale Google.Colons = NO -->

`header.html`
: Template for the header

`footer.html`
: Template for the footer

`page.html`
: Template for the body of the page. This page **must** contain the `{{ body }}`
expression to render the contents of your documentation.
The `page` template extends the layout `with-sidebar` or `without-sidebar`
depending on the context.

`without-sidebar.html`
: Template without navigation sidebar. This template is used, when the theme option
{confval}`show_nav` is set to `False`, or when you set `layout: "without-sidebar"` in
the front matter of your Markdown document. This template extends the main template
`layout`

`with-sidebar.html`
: Template with navigation sidebar on the left. This is the default template for all
documentation pages. It extends from the main template `layout`.

`layout.html`
: Main template defining the overall structure of the page, including the HTML
`<head>` with all imported CSS and JavaScript files.

<!-- vale Google.Colons = YES -->

For more information, see the available templates in the directory
`src/sphinxawesome_theme/` on GitHub.

(sec:override-layouts-locally)=

## Override page layout per page

```{caution}
This section only applies if you use the
[`myst-parser`](https://myst-parser.readthedocs.io/en/latest/index.html) for writing
Sphinx documentation in Markdown.
```

The theme has two page layouts. The default layout shows a sidebar with all navigation
links on the left side.

<!-- vale 18F.UnexpandedAcronyms = NO -->

If you want to override the layout _on one page_, you can use the `layout` option in the
YAML front matter.

<!-- vale 18F.UnexpandedAcronyms = YES -->

For example, the {ref}`sec:about` page uses a layout without a sidebar:

```{code-block} markdown

---
layout: "without-sidebar"
---

# About

...
```
