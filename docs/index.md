---
myst:
  html_meta:
    description: Create functional and beautiful websites for your documentation with Sphinx and the Awesome Sphinx Theme.
    keywords: Documentation, Sphinx, Python
---

<!-- vale Google.Headings = NO -->

# Awesome Sphinx Theme

<!-- vale Google.Headings = YES -->

```{rst-class} lead
Create functional and beautiful websites for your documentation with Sphinx.
```

---

## Get started

1. Install the theme:

   ```terminal
   pip install sphinxawesome-theme
   ```

   ```{seealso}
   {ref}`sec:install`
   ```

1. Add the theme to your Sphinx configuration:

   ```{code-block} python
   ---
   caption: "File: conf.py"
   ---
   html_theme = "sphinxawesome_theme"
   extensions = ["sphinxawesome_theme"]
   ```

   ```{seealso}
   {ref}`sec:load`
   {confval}`sphinx:html_theme`
   ```

1. Build your documentation with Sphinx.

   ```{seealso}
   {sphinxdocs}`Getting started with Sphinx <usage/quickstart.html>`
   ```

## Learn more

In the _how-to_ section, you can learn more about using and customizing the theme.

```{seealso}
{ref}`Theme <sec:theme-options>`
{ref}`sec:extension-options`
{ref}`sec:customize`
```

See the _demo_ section for all available styles.

## Give feedback

Is something broken or missing?
Create a [GitHub issue](https://github.com/kai687/sphinxawesome-theme/issues/new).

<!-- vale Google.Headings = NO -->
<!-- vale 18F.Headings = NO -->

```{toctree}
---
hidden: true
caption: How-To
---

how-to/install
how-to/use
how-to/customize
how-to/modify
how-to/update
```

```{toctree}
---
hidden: true
caption: Demo
glob: true
---

demo/*
```
