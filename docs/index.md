---
html_meta:
  title: The Awesome Sphinx Theme
  description: Create functional and beautiful websites for your documentation with Sphinx.
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

   ```shell-session
   pip install sphinxawesome-theme
   ```

   ```{seealso}
   {ref}`sec:install`
   ```

2. Add the theme to your Sphinx configuration:

   ```{code-block} python
   ---
   caption: "File: conf.py"
   ---
   html_theme = ["sphinxawesome_theme"]
   ```

   ```{seealso}
   {ref}`sec:load`
   {confval}`sphinx:html_theme`
   ```

3. Build your documentation with Sphinx.

   ```{seealso}
   {sphinxdocs}`Getting started with Sphinx <usage/quickstart.html>`
   ```

In the _how-to_ section, you can learn more about the different
{ref}`Theme <sec:theme-options>` and
{ref}`sec:extension-options` or
{ref}`sec:customize`.
You can get an overview over all available styles in the _demo_ section.

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
