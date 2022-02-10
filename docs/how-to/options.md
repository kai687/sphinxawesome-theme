---
html_meta:
  description: |
    Configure the Awesome Theme by changing an option in your Sphinx configuration file.
---

(sec:configure)=

# Configure the theme

```{rst-class} lead
Configure the {{ product }} by changing one of its options.
```

```{contents} On this page
---
local: true
backlinks: none
---
```

```{admonition} What's the difference between theme and extension options?
It's a technical distinction due to the way Sphinx builds a project.

- **Theme options** are defined in the HTML templates. They only control layout/styling aspects.
- **Extension options** are defined in the Python code of the extensions.
  They can control more aspects when building the documentation.
```

(sec:theme-options)=

## Theme options

You can configure the theme by modifying the `html_theme_options` dictionary in the
Sphinx configuration file `conf.py`.

:::{confval} nav_include_hidden

<!-- vale Awesome.SpellCheck = NO -->

By default, the
{sphinxdocs}`toctree <usage/restructuredtext/directives.html#directive-toctree>`
directive includes the content and prints a list of links in the content area. A
`toctree` directive with the `:hidden:` option includes the content, but doesn't print
the list of links in the content area. This can be useful if navigation links are
elsewhere on the page. Printing the same list of links in the content area would be
redundant.

<!-- vale Awesome.SpellCheck = YES -->

If you don't want to include elements from a _hidden_ toctree directive in the
navigation menu on the left, set:

```{code-block} python
---
caption: "File: conf.py"
---
# This option is `True` by default
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
caption: "File: conf.py"
---
# This option is `True` by default
html_theme_options = {"show_nav": False}
```

:::

:::{confval} show_breadcrumbs

By default, "[breadcrumbs](https://en.wikipedia.org/wiki/Breadcrumb_navigation)"
navigation links are shown at the top of the content area. They show the position of
this document relative to the top level. If you want to hide the breadcrumbs navigation
links, add:

```{code-block} python
---
caption: "File: conf.py"
---
# This option is `True` by default
html_theme_options = {"show_breadcrumbs": False}
```

:::

:::{confval} breadcrumbs_separator

To select a different separator for the breadcrumbs navigation links,
set:

```{code-block} python
---
caption: "File: conf.py"
emphasize-text: CHAR
---
# The default separator is `/`
html_theme_options = {"breadcrumbs_separator": "CHAR"}
```

Replace {samp}`{CHAR}` with a character or HTML entity of your choice.
:::

:::{confval} show_prev_next

To show links to the previous and next pages, set:

```{code-block} python
---
caption: "File: conf.py"
---
# This option is `False` by default
html_theme_options = {"show_prev_next": True}
```

In most cases, documentation isn't read from beginning to end. That's why this option is
turned off by default.
:::

<!-- vale Awesome.SpellCheck = NO -->

:::{confval} show_scrolltop

<!-- vale Awesome.SpellCheck = YES -->

On longer pages, scrolling to the top can be a hassle.
To show a button that scrolls to the top when clicked, set the following option:

```{code-block} python
---
caption: "File: conf.py"
---
# This option is `False` by default
html_theme_options = {"show_scrolltop": True}
```

:::

:::{confval} extra_header_links

To add extra links to the header of your documentation, set the following option:

```{code-block} python
---
caption: "File: conf.py"
---
# This option is `False` by default
html_theme_options = {
  extra_header_links = {
    "link1": "/url1",
    "link2": "/url2",
  }
}
```

The keys of the `extra_header_links` dictionary are the link texts. The values are the
absolute URLs to the pages you want to link.

:::

(sec:extension-options)=

## Extension options

This theme also enables a few internal extensions that enhance the user experience. The
following configuration values are set at the top level in the Sphinx
configuration file `conf.py`:

<!-- vale Awesome.SpellCheck = NO -->

:::{confval} html_collapsible_definitions

<!-- vale Awesome.SpellCheck = YES -->

Set this option to `True` to make code references, such as classes, methods, and other
objects, collapsible and expandable. By default, this option is turned off.

```{code-block} python
---
caption: "File: conf.py"
---
# This option is `False` by default
html_collapsible_definitions = True
```

:::

<!-- vale Awesome.SpellCheck = NO -->

:::{confval} html_awesome_headerlinks

Set this option to `False` to restore Sphinx's default behavior for headerlinks.
In the {{ product }}, clicking a headerlink immediately copies the URL to the clipboard.

<!-- vale Awesome.SpellCheck = YES -->

```{code-block} python
---
caption: "File: conf.py"
---
# This option is `True` by default
html_awesome_headerlinks = False
```

:::

<!-- vale Awesome.SpellCheck = NO -->

:::{confval} html_awesome_docsearch

<!-- vale Awesome.SpellCheck = YES -->

Set this option to `True` to use [Algolia DocSearch](https://docsearch.algolia.com/)
instead of the built-in search.

```{code-block} python
---
caption: "File: conf.py"
---
# This option is `False` by default
html_awesome_docsearch = True
```

To configure DocSearch, create a `.env` file in your documentation project directory and
add your Algolia credentials:

- `DOCSEARCH_APP_ID`: the id of your Algolia app
- `DOCSEARCH_API_KEY`: the API key for searching your index on Algolia
- `DOCSEARCH_INDEX_NAME`: the index name

You can also define these environment variables on the command line.

Alternatively, you can also configure DocSearch via a `docsearch_config` dictionary in
your Sphinx configuration file `conf.py`:

```{code-block} python
---
caption: "File: conf.py"
---

docsearch_config = {
  app_id: "",
  api_key: "",
  index_name: ""
}
```

:::
