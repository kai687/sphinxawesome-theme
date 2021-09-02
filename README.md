# Sphinx awesome theme

![GitHub](https://img.shields.io/github/license/kai687/sphinxawesome-theme?color=blue&style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/sphinxawesome-theme?color=eb5&style=for-the-badge&logo=pypi)
![Netlify](https://img.shields.io/netlify/e6d20a5c-b49e-4ebc-80f6-59fde8f24e22?logo=netlify&style=for-the-badge)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/kai687/sphinxawesome-theme/Lint?label=Lint&logo=Github&style=for-the-badge)

Create beautiful and awesome documentation websites with
[Sphinx](https://www.sphinx-doc.org/en/master/).

Go to [sphinxawesome.xyz](https://sphinxawesome.xyz) to get an impression of how the
theme looks like.

## Get started

To use this theme for your documentation, install it via `pip` and add it to your
Sphinx configuration.

1. Install the theme as a Python package:

   ```console
   pip install sphinxawesome-theme
   ```

   See [How to install the theme](https://sphinxawesome.xyz/how-to/install/) for more information.

1. Set `html_theme` in the Sphinx configuration file `conf.py`:

   ```python
   html_theme = "sphinxawesome_theme"
   ```

   See [How to load the theme](https://sphinxawesome.xyz/how-to/load/) for more information.

You can change some parts of this theme.
See [How to configure the theme](https://sphinxawesome.xyz/how-to/configure/) for more
information.

## Features

With this awesome theme, you can build documentation websites that are readable,
functional, and easily scannable for content. Compared to regular Sphinx themes,
these features enhance the user experience:

- **Code blocks.** The code block shows the language of the code in a header. Each code
  block has a **Copy** button for easy copying. This theme adds three new options to
  Sphinx's `code-block` directive:

  - `emphasize-added`: highlight lines that should be added to code
  - `emphasize-removed`: highlight lines that should be removed from the code
  - `emphasize-placeholder: PLACEHOLDER`: highlight `PLACEHOLDER` in the code block to
    emphasize placeholder text the user should replace.

- **Collapsible elements.**
  Nested navigation links allow you to reach all pages from all other pages.
  You can make code object definitions, like methods, classes, or modules,
  collapsible as well, to focus on one block at a time.

<!-- vale Awesome.SpellCheck = NO -->

- **Better headerlinks.**
  Clicking the link icon after a header or caption automatically copies the URL to the clipboard.

<!-- vale Awesome.SpellCheck = YES -->

- **Better keyboard navigation.**
  <!-- vale 18F.Clarity = NO -->
  Use the `/` key to start searching.
  Use the `Tab` key to quickly skip through all sections on the page.
  Use the `Space` key to expand or collapse items in the navigation menu or in code definitions.
