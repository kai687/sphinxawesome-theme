---
html_theme:
  description: |
    Learn how to add the Awesome Theme to your Sphinx documentation.
---

(sec:load)=

# Load the theme

```{rst-class} lead
Learn how to add the {{ product }} to your Sphinx documentation.
```

```{contents} On this page
---
local: true
backlinks: none
---
```

## Load the theme from a Python package

If you installed the {{ product }} {ref}`as a Python package <sec:install-python-package>`,
add the `html_theme` configuration option to your Sphinx configuration file `conf.py`:

```{code-block} python
---
caption: "File: conf.py"
---
html_theme = "sphinxawesome_theme"
```

## Load the theme from a local directory

If you want to keep your documentation and theme as a single project,
you can load the {{ product }} from a local directory.
This can be useful, if you want to modify the theme.

:::{note}
When loading the theme from a local directory, you need to manage the dependencies
yourself. This theme needs the `beautifulsoup` package to run. You can install it with
`pip`:

```terminal
pip install bs4
```

:::

:::{rubric} Example

:::

The following example assumes you have a Sphinx project with the following structure,
and you want to load the theme from the `_themes/` folder.

```{code-block} terminal
---
emphasize-lines: 4
---
./
├── conf.py
├── index.rst
├── _themes/
└── ...
```

To load the theme from a local directory, follow these steps:

1. {ref}`sec:fork-and-clone`.

1. Copy the directory `sphinxawesome-theme/src/sphinxawesome_theme/` into your
   Sphinx project:

   ```terminal
   cp -r sphinxawesome-theme/src/sphinxawesome_theme _themes/
   ```

1. Add the `_themes/` directory to the system path in the Sphinx configuration:

   ```{code-block} python
   ---
   caption: "File: conf.py"
   ---
   import os
   import sys

   sys.path.append(os.path.abspath("_themes"))
   ```

   Adding this directory makes it discoverable for Sphinx.

1. Add the `_themes/` directory to the `exclude_patterns`:

   ```{code-block} python
   ---
   caption: "File: conf.py"
   ---
   exclude_patterns = ["_themes"]
   ```

   This prevents Sphinx from searching the `_themes/` directory for documentation files.

1. Add the theme as an extension and as a theme:

   ```{code-block} python
   ---
   caption: "File: conf.py"
   ---
   extensions = ["sphinxawesome_theme"]
   html_theme = "sphinxawesome_theme"
   ```
