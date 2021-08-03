---
description: A theme for Sphinx to create beautiful documentation with Python.
keywords: documentation, sphinx, python
"og:title": Sphinx awesome theme
"og:description": A theme for Sphinx to create beautiful documentation with Python.
---

# Sphinx awesome theme

```{rst-class} lead
Bring your Sphinx documentation to the modern times and create beautiful documentation
websites that don't look like from the previous millenium.
```

---

These pages are divided into a _how-to_ and a _demo_ section. In the _how-to_ section,
you can learn:

- {ref}`How to install the theme`
- {ref}`How to use the theme`
- {ref}`How to modify the theme`

The _demo_ section acts as a style reference. If you can't find a markup element in the
_demo_ section, it's likely that styles for it don't exist yet. Create an issue on
GitHub if you need styles for a certain markup element, or add your own custom CSS.

The Sphinx awesome theme is open source software and distributed under the MIT license.
The source code is available on [GitHub](https://github.com/kai687/sphinxawesome-theme).

<!-- vale Google.Headings = NO -->
<!-- vale 18F.Headings = NO -->

```{toctree}
---
hidden: true
caption: how-to
---

how-to/install
how-to/use
how-to/modify
how-to/update
```

```{toctree}
---
hidden: true
caption: demo
glob: true
---

demo/*
```

```{toctree}
---
hidden: true
---

about
```
