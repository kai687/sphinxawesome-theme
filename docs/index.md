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
   {doc}`how-to/install`
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
   {doc}`how-to/add`
   {confval}`sphinx:html_theme`
   ```

1. Build your documentation.

   ```{seealso}
   {sphinxdocs}`Get started with Sphinx <usage/quickstart.html>`
   ```

## Learn more

In the **How-to** section, you can learn more about using and customizing the theme.

```{toctree}
---
maxdepth: 1
caption: How To
---

how-to/install
how-to/add
how-to/configure
how-to/customize/index
how-to/build-your-own
```

The **Demo** section shows how various elements will look like.

```{toctree}
---
maxdepth: 1
caption: Demo
glob: true
---

demo/*
```
