---
myst:
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

- **Theme options** are defined in the HTML templates. They control layout and styling aspects.
- **Extension options** are defined in the Python code of the extensions.
  They can control more aspects, for example, running extra code.
```

(sec:theme-options)=

## Theme options

You can configure the theme by modifying the `html_theme_options` dictionary in the
Sphinx configuration file `conf.py`.

<!-- vale Vale.Spelling = NO -->

:::{confval} nav_include_hidden

<!-- vale Vale.Spelling = YES -->

If you don't want to include entries from a _hidden_
{sphinxdocs}`toctree <usage/restructuredtext/directives.html#directive-toctree>`
directive in the sidebar, set `nav_include_hidden` to `False`.

```{code-block} python
---
caption: "File: conf.py"
---
# This option is `True` by default
html_theme_options = {"nav_include_hidden": False}
```

By default, the `toctree` directive includes your content _and_ generates a list of links in the content
area of the page. With the `hidden` option, the content is still included,
but no links are printed in the main content area.

:::

<!-- vale Vale.Spelling = NO -->

:::{confval} show_nav

<!-- vale Vale.Spelling = YES -->

The {{ product }} shows links to all your documentation pages in sidebar on the left
side.
If you want to hide the sidebar on all pages, set this option to `False`:

```{code-block} python
---
caption: "File: conf.py"
---
# This option is `True` by default
html_theme_options = {"show_nav": False}
```

:::

<!-- vale Vale.Spelling = NO -->

:::{confval} show_breadcrumbs

<!-- vale Vale.Spelling = YES -->

The {{ product }} shows
[breadcrumbs](https://en.wikipedia.org/wiki/Breadcrumb_navigation)
links at the top of each page
To hide the breadcrumbs, set this option to `False`:

```{code-block} python
---
caption: "File: conf.py"
---
# This option is `True` by default
html_theme_options = {"show_breadcrumbs": False}
```

:::

<!-- vale Vale.Spelling = NO -->

:::{confval} breadcrumbs_separator

<!-- vale Vale.Spelling = YES -->

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

<!-- vale Vale.Spelling = NO -->

:::{confval} show_prev_next

<!-- vale Vale.Spelling = YES -->

To show links to the previous and next pages, set this option to `True`:

```{code-block} python
:caption: "File: conf.py"

# This option is `False` by default
html_theme_options = {"show_prev_next": True}
```

:::

<!-- vale Vale.Spelling = NO -->

:::{confval} show_scrolltop

<!-- vale Vale.Spelling = YES -->

To show a button that scrolls to the top of the page when clicked,
set this option to `True`:

```{code-block} python
:caption: "File: conf.py"

# This option is `False` by default
html_theme_options = {"show_scrolltop": True}
```

:::

<!-- vale Vale.Spelling = NO -->

:::{confval} extra_header_links

<!-- vale Vale.Spelling = YES -->

To add extra links to the header of your documentation, set the following option:

```{code-block} python
:caption: "File: conf.py"

# This option is `False` by default
html_theme_options = {
  extra_header_links = {
    "link1": "/url1",
    "link2": "/url2",
  }
}
```

The keys of the `extra_header_links` dictionary are the link texts.
The values are absolute URLs.

:::

(sec:extension-options)=

## Extension options

```{note}
Extension options are only available
if you add the theme to the list of extensions
in your Sphinx configuration:
`extensions = ["sphinxawesome_theme"]`
```

The {{ product }} enables several internal extensions that enhance the user experience.
The following configuration values are set at the top level in the Sphinx
configuration file `conf.py`:

<!-- vale Vale.Spelling = NO -->

:::{confval} html_collapsible_definitions

<!-- vale Vale.Spelling = YES -->

Set this option to `True` to make code references, such as classes, methods, and other
objects, collapsible and expandable.

```{code-block} python
:caption: "File: conf.py"

# This option is `False` by default
html_collapsible_definitions = True
```

:::

<!-- vale Vale.Spelling = NO -->

:::{confval} html_awesome_headerlinks

<!-- vale Vale.Spelling = YES -->

Set this option to `False` to restore Sphinx's default behavior for headerlinks.
In the {{ product }}, clicking a headerlink copies the URL to the clipboard.

```{code-block} python
:caption: "File: conf.py"

# This option is `True` by default
html_awesome_headerlinks = False
```

:::

<!-- vale Vale.Spelling = NO -->

:::{confval} html_awesome_code_headers

<!-- vale Vale.Spelling = YES -->

By default, the {{ product }} shows the programming language
of a code block in its header.
If you don't want to show the programming language, set this option to `False`.

```{code-block} python
:caption: "File: conf.py"

# This option is `True` by default
html_awesome_code_headers = False
```

:::

<!-- vale Vale.Spelling = NO -->

:::{confval} html_awesome_docsearch

<!-- vale Vale.Spelling = YES -->

Set this option to `True` to use [Algolia DocSearch](https://docsearch.algolia.com/)
instead of the built-in search.

```{code-block} python
---
caption: "File: conf.py"
---
# This option is `False` by default
html_awesome_docsearch = True
```

To configure DocSearch, add these environment variables:

<!-- vale Google.Colons = NO -->

`DOCSEARCH_APP_ID`
: The id of your Algolia app

`DOCSEARCH_API_KEY`
: The API key for searching your index on Algolia

`DOCSEARCH_INDEX_NAME`
: The name of your Algolia index for your documentation project.

<!-- vale Google.Colons = YES -->

You can add environment variables with one of these options:

- Add them to a `.env` file in your Sphinx project directory
- Add them on the command line before building your documentation
- Add them to the `docsearch_config` dictionary in your Sphinx configuration file `conf.py`:

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

```{note}
Algolia DocSearch is an external web service.
You need to apply and receive your credentials before you can use it.
```

:::
