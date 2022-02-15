<h1 align="center">Sphinx awesome theme</h1>

<p align="center">
   <img src="https://img.shields.io/github/license/kai687/sphinxawesome-theme?color=blue&style=for-the-badge" alt="MIT license">
   <img src="https://img.shields.io/pypi/v/sphinxawesome-theme?color=eb5&style=for-the-badge&logo=pypi" alt="PyPI version">
   <img src="https://img.shields.io/netlify/e6d20a5c-b49e-4ebc-80f6-59fde8f24e22?logo=netlify&style=for-the-badge" alt="Netlify Deploy">
   <img src="https://img.shields.io/github/workflow/status/kai687/sphinxawesome-theme/Lint?label=Lint&logo=Github&style=for-the-badge" alt="Lint">
</p>

<p align="center">
   Create beautiful and awesome documentation websites with <a href="https://www.sphinx-doc.org/en/master/">Sphinx</a>.
   See how the theme looks like on <a href="https://sphinxawesome.xyz">sphinxawesome.xyz</a>.
</p>

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

For more information about configuring the theme to your use case, see [How to configure the theme](https://sphinxawesome.xyz/how-to/options/).

## Features

With the Awesome Theme, you can build readable, functional, and beautiful documentation websites.
Compared to other Sphinx themes, these features enhance the user experience:

### Awesome code blocks

The code block shows the language of the code in a header.
Each code block has a **Copy** button for easy copying.
This theme enhances Sphinx's `code-block` directive with:

- `emphasize-added`: highlight lines that should be added to code
- `emphasize-removed`: highlight lines that should be removed from the code
- `emphasize-text: TEXT`: highlight `TEXT` in the code block to emphasize placeholder text the user should replace.

### Collapsible elements

Nested navigation links allow you to reach all pages from all other pages.
You can make code object definitions, like methods, classes, or modules,
collapsible as well, to focus on one item at a time.

<!-- vale Awesome.SpellCheck = NO -->

### Better headerlinks

Clicking the link icon after a header or caption automatically copies the URL to the clipboard.

<!-- vale Awesome.SpellCheck = YES -->

### DocSearch

If you have an Algolia DocSearch account for your documentation (it's free for open-source projects),
you can use DocSearch for a search-as-you-type experience with autocomplete. 

### Better keyboard navigation

<!-- vale 18F.Clarity = NO -->

Use the `Tab` key to quickly skip through all sections on the page.
Use the `Space` key to expand or collapse items in the navigation menu or in code definitions.
