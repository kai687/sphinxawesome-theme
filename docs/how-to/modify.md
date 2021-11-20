---
html_theme:
  description: |
    Make your own theme by building on top of this theme.
    Fully customize the styles, JavaScript, and templates.
---

(sec:modify)=

# Modify the theme

```{rst-class} lead
Learn how to build your own theme by changing the templates or CSS.
```

```{contents} On this page
---
local: true
backlinks: none
---
```

## Modify the templates

You can apply styles in the templates with Tailwind's utility classes.

```{code-block} shell
---
emphasize-lines: 1
---
./src/
├sphinxawesome_theme/
└theme-src/
```

To modify these styles, follow these steps:

1. Install the Python and JavaScript dependencies:

   See {ref}`sec:dev-env` for more information.

1. Make your change.

   For example, to change the background color of the header to orange,
   open the file `sphinxawesome_theme/header.html` and change:

   ```{code-block} html
   ---
   emphasize-removed: 1
   emphasize-added: 2
   ---
   <header class="md:sticky top-0 bg-gray-900 ...">
   <header class="md:sticky top-0 bg-orange-500 ...">
   ```

1. Build the theme:

   ```shell
   yarn build
   ```

## Modify CSS files

Everything that's part of the main content, including everything that's converted from
reStructuredText to HTML is styled using Tailwind's `@apply` directive.

```{code-block} shell
---
emphasize-lines: 3
---
./src/
├sphinxawesome_theme/
└theme-src/
   └css/
```

To modify these styles, follow these steps:

1. Install the Python and JavaScript dependencies.

   See {ref}`sec:dev-env` for more information.

1. Make your change.

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

1. Build the theme:

   ```shell
   yarn build
   ```
