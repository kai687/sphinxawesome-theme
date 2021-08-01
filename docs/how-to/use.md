# How to use the theme

```{rst-class} lead
Use one of the following methods to configure Sphinx to use the awesome theme.
```

```{contents} On this page
---
local: true
backlinks: none
---
```

## Load the theme from a Python package

Add the `html_theme` configuration option to the Sphinx configuration file `conf.py`.

```{code-block} python
---
caption: conf.py
---
html_theme = "sphinxawesome_theme"
```

If you install and load the theme as a Python package, the extension
`sphinxawesome.sampdirective` as well as all internal extensions are installed and
loaded automatically.

## Load the theme from a local directory

If you want to make many changes to the theme, you can also skip the packaging.
It may be quicker to load the theme from a local directory.

Follow these steps to load a local version of the theme from a directory:

1. {ref}`Create a local copy of the theme`

1. Add the `src/` directory to the Sphinx configuration.

   ```{code-block} python
   ---
   caption: conf.py
   ---
   import os
   import sys

   sys.path.append(os.path.abspath("sphinsawesome-theme/src"))
   ```

1. Add this directory to the `exclude_patterns` list to prevent Sphinx from searching
   this path for reStructuredText files:

   ```{code-block} python
   ---
   caption: conf.py
   ---
   exclude_patterns = ["sphinxawesome-theme", "..."]
   ```

1. Add the theme both as an extension and as a theme:

   ```{code-block} python
   ---
   caption: conf.py
   ---
   extensions = ["sphinxawesome_theme", "..."]
   html_theme = "sphinxawesome_theme"
   ```

## Theme and extension options

You can configure the theme by modifying the `html_theme_options` dictionary in the
Sphinx configuration file `conf.py`. The options and their default values are shown
below.

```{code-block} python
---
caption: conf.py
---
html_theme_options = {
      "nav_include_hidden": True,
      "show_nav": True,
      "show_breadcrumbs": True,
      "breadcrumbs_separator": "/",
      "show_prev_next": False,
      "show_scrolltop": False
}
```

### Theme options

:::{confval} nav_include_hidden

By default, the
[toctree](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree)
directive includes the content and prints a list of links in the content
area. A `toctree` directive with the `:hidden:` option
includes the content, but doesn't print the list of links in the content area. This can
be useful if navigation links are elsewhere on the page. Printing the same list of
links in the content area would be redundant.

If you don't want to include elements from a _hidden_ toctree directive in the
navigation menu on the left, set:

```{code-block} python
---
caption: conf.py
---
html_theme_options = {"nav_include_hidden": False}
```

When using the `toctree` directive without the `:hidden:` option, insert a headline or
provide a caption with the `:caption:` option. For example:

```{code-block} rst
.. toctree::
   :caption: Contents
```

:::

:::{confval} show_nav

By default, the navigation links are shown in a navigation menu on the left side. If you
want to hide the navigation menu completely, add:

```{code-block} python
---
caption: conf.py
---
html_theme_options = {"show_nav": False}
```

:::

:::{confval} show_breadcrumbs

By default, "[breadcrumbs](https://en.wikipedia.org/wiki/Breadcrumb_navigation)"
navigation links are shown at the top of the content area. They show the position of this
document relative to the top level. If you want to hide the breadcrumbs navigation
links, add:

```{code-block} python
---
caption: conf.py
---
html_theme_options = {"show_breadcrumbs": False}
```

:::

:::{confval} breadcrumbs_separator

If you want to select a different separator for the breadcrumbs navigation links,
set:

```{samp}
html_theme_options = \{"breadcrumbs_separator": "{CHAR}"\}
```

Replace {samp}`{CHAR}` with a character or HTML entity of your choice.
:::

:::{confval} show_prev_next

If you want to show links to the previous and next pages, set:

```{code-block} python
---
caption: conf.py
---
html_theme_options = {"show_prev_next": True}
```

In most cases, documentation isn't read from beginning to end. That's why this option is
turned off by default.
:::

<!-- vale Awesome.SpellCheck = NO -->

:::{confval} show_scrolltop

<!-- vale Awesome.SpellCheck = YES -->

For longer pages, scrolling to the top can be a hassle. If you want to show a button,
that scrolls to the top of the page when clicked, set:

```{code-block} python
---
caption: conf.py
---
html_theme_options = {"show_scrolltop": True}
```

:::

### Extension options

This theme also enables a few internal extensions that enhance the user experience. The
following additional configuration value is set at the top level in the Sphinx
configuration file `conf.py`:

<!-- vale Awesome.SpellCheck = NO -->

:::{confval} html_collapsible_definitions

<!-- vale Awesome.SpellCheck = YES -->

Set this option to `True` to enable collapsible object definitions, such as command
line options, classes, or methods.

```{code-block} python
---
caption: conf.py
---
html_collapsible_definitions = True
```

:::
