<h1 align="center">Sphinx awesome theme</h1>

<p align="center">
   <img src="https://img.shields.io/github/license/kai687/sphinxawesome-theme?color=blue&style=for-the-badge" alt="MIT license">
   <img src="https://img.shields.io/pypi/v/sphinxawesome-theme?color=eb5&style=for-the-badge&logo=pypi" alt="PyPI version">
   <img src="https://img.shields.io/netlify/e6d20a5c-b49e-4ebc-80f6-59fde8f24e22?logo=netlify&style=for-the-badge" alt="Netlify Deploy">
   <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/kai687/sphinxawesome-theme/lint.yml?label=Linted&style=for-the-badge">
</p>

<p align="center">
   Create beautiful and awesome documentation websites with <a href="https://www.sphinx-doc.org/en/master/">Sphinx</a>.
   See how the theme looks like on <a href="https://sphinxawesome.xyz">sphinxawesome.xyz</a>.
</p>

## Get started

1. Install the theme as a Python package:

   ```console
   pip install sphinxawesome-theme
   ```

   For more information, see [Install the theme](https://sphinxawesome.xyz/how-to/install/).

1. Add `sphinxawesome_theme` as an HTML theme in your Sphinx configuration file `conf.py`:

   ```python
   html_theme = "sphinxawesome_theme"
   ```

   For more information, see [Add your theme](https://sphinxawesome.xyz/how-to/add/).

## Features

With the Awesome Theme, you can build readable, functional, and beautiful documentation websites.

### Awesome code blocks

- Code block have a **Copy** button for copying the code.
- You can use these additional options in `code-block` directives:

  - `emphasize-added`. Highlight lines that should be added
  - `emphasize-removed`. Highlight lines that should be removed
  - `emphasize-text: TEXT`. Highlight _`TEXT`_ in the code block

### Better headerlinks

Clicking the link icon after headers or captions automatically copies the URL to the clipboard.

### DocSearch

This theme supports the [`sphinx-docsearch`](https://sphinx-docsearch.readthedocs.io/) extension
to replace the built-in search with Algolia DocSearch.
