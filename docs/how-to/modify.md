# How to modify the theme

Depending on how you want to modify the theme, use one of these options.

```{contents} On this page
---
local: true
backlinks: none
---
```

## Add or override styles

To override or add extra JavaScript and CSS, you don't need to install the theme's
dependencies.

To add extra CSS files,
use the [`html_css_files`](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_js_files) configuration value.
To add extra JavaScript files, use the [`html_js_files`](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_css_files)
configuration value.

For example, place additional styles in a file `_static/custom.css` and add the
following options to your Sphinx configuration in `conf.py`:

```{code-block} python
---
caption: conf.py
---
html_static_path = ["_static"]
html_css_files = ["custom.css"]
```

If you want to override existing styles, you might have to add `!important`. For more
information, see
[Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity) in the
Mozilla Developer Networks Web Docs.

:::{note}
Since these additional CSS and JavaScript files aren't parsed by webpack, use your own
styles and don't use Tailwind's `@apply` directive.
:::

## Modify the templates

Styles in the templates are applied via Tailwind's utility classes.

```{code-block} console
---
emphasize-lines: 1
---
./src/
├sphinxawesome_theme/
└theme-src/
```

To modify these styles, follow these steps:

1. Install the Python and JavaScript dependencies

   See {ref}`Set up a development environment` for more information.

1. Make your change

   For example, to change the background color of the header to orange,
   open :file:`sphinxawesome_theme/header.html` and change:

   ```{code-block} html
   ---
   emphasize-removed: 1
   emphasize-added: 2
   ---
   <header class="md:sticky top-0 bg-gray-900 ...">
   <header class="md:sticky top-0 bg-orange-500 ...">
   ```

1. Build the theme

   ```console
   yarn build
   ```

## Modify CSS files

Everything that's part of the main content,
including everything that's converted from reStructuredText to HTML
is styled using Tailwind's `@apply` directive.

```{code-block} console
---
emphasize-lines: 3
---
./src/
├sphinxawesome_theme/
└theme-src/
   └css/
```

To modify these styles, follow these steps:

1. Install the Python and JavaScript dependencies

   See {ref}`Set up a development environment` for more information.

1. Make your change

   The CSS files are arranged according to the elements they apply to. For example, if you
   want to change the appearance of links from the default blue to an orange, open the file
   `theme-src/css/links.css` and change:

   ```{code-block} css
   ---
   force: true
   emphasize-removed: 7
   emphasize-added: 8
   ---
   p:not(.admonition-title),
   .nav-toc,
   .search,
   .toctree-wrapper,
   .contents.local {
      & a {
         @apply text-blue-700;
         @apply text-orange-500;
      }
   }
   ```

1. Build the theme

   ```console
   yarn build
   ```
