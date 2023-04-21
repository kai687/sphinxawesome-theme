---
myst:
  html_meta:
    description: |
      Make your own theme by building on top of this theme.
      Fully customize the styles, JavaScript, and templates.
---

# Build your own theme

```{rst-class} lead
Build your own theme by changing the templates or CSS.
```

```{contents} On this page
---
local: true
backlinks: none
---
```

## Modify the templates

You can style the templates with Tailwind's utility classes.

```{code-block} terminal
---
emphasize-lines: 1
---
./src/
├sphinxawesome_theme/
└theme-src/
```

To modify these styles, follow these steps:

1. Install the Python and JavaScript dependencies.

   ```{seealso}
   {ref}`sec:dev-env`
   ```

1. Make your change.

   For example, to change the background color of the header to orange,
   open the file `sphinxawesome_theme/header.html` and change:

   ```{code-block} html
   ---
   emphasize-removed: 1
   emphasize-added: 2
   ---
   <div class="bg-gray-900 ...">
   <div class="bg-orange-500 ...">
   ```

1. Build the theme:

   ```terminal
   yarn build
   ```

## Modify CSS files

Everything that's part of the main content,
including everything that's converted from
reStructuredText or Markdown to HTML is styled using Tailwind's `@apply` directive.

```{code-block} terminal
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

   ```{seealso}
   {ref}`sec:dev-env`
   ```

1. Make your change.

   The CSS files are arranged according to the elements they apply to.

1. Build the theme:

   ```terminal
   yarn build
   ```
