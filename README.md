# Sphinx awesome theme


![GitHub](https://img.shields.io/github/license/kai687/sphinxawesome-theme?color=blue&style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/sphinxawesome-theme?color=eb5&style=for-the-badge&logo=pypi)
![Netlify](https://img.shields.io/netlify/e6d20a5c-b49e-4ebc-80f6-59fde8f24e22?logo=netlify&style=for-the-badge)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/kai687/sphinxawesome-theme/Lint?label=Lint&logo=Github&style=for-the-badge)

<!-- readme-start -->

This is an awesome theme and a set of extensions for the
[Sphinx](https://www.sphinx-doc.org/en/master/) documentation generator. Using this
theme and extension, you can change the look of your documentation website and add a
number of useful improvements. See the theme in action at https://sphinxawesome.xyz.

## Getting started

You can install the awesome theme from the Python package index and modify the Sphinx
configuration file `conf.py`.

To get started using this theme, follow these steps:

1. Install the theme as a Python package:

   ```console
   pip install sphinxawesome-theme
   ```

   See [How to install the theme](https://sphinxawesome.xyz/how-to/install/) for more information.

1. Add the `html_theme` configuration option to the Sphinx configuration file
   `conf.py`:

   ```python
   html_theme = "sphinxawesome_theme"
   ```

   See [How to use the theme](https://sphinxawesome.xyz/how-to/use/) for more information.

## Features

This theme is designed with readability and usability in mind. The theme includes
several extensions that enhance the usability:

- **Awesome code blocks**

    - Code blocks have a header section, displaying the optional caption, as well as the
      programming language used for syntax highlighting
    - The code block headers contain a **Copy** button, allowing you to copy code
      snippets to the clipboard.
    - The theme adds two new options to Sphinx's `code-block` directive:
      `emphasize-added` and `emphasize-removed`, for highlighting changes within other
      highlighted code.

- **Awesome new directive for highlighting placeholder variables**. The theme supports a
  new directive `samp`, which is the equivalent of the built-in
  `:samp:` interpreted text role. This allows you to highlight placeholder variables
  in code blocks.

- **Awesome user experience improvements**. These small features make the theme more
  usable:

    - Better keyboard navigation:

      <!-- vale 18F.Clarity = NO -->
      - Use the `Tab` key to navigate through all sections on the page
      - Use the *Skip to Content* link to bypass the navigation links
      - Use the `/` key (forward Slash) to start a search
      <!-- vale 18F.Clarity = YES -->

    - Better "permalink" mechanism:

      - Hovering over an element with a permalink reveals a *Link* icon
      - Selecting the *Link* icon copies the link to the clipboard
      - Notes, warnings and other admonitions have permalinks by default

    - Collapsible elements:

      - Nested navigation links---all pages are reachable from all other pages
      - Code definitions---code object definitions (functions, classes, modules, etc.), for example, obtained via the `sphinx.ext.autodoc` extension.
