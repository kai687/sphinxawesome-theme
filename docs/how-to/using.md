# Make your documentation awesome

```{rst-class} lead
Make the most out of your Sphinx documentation by using the features of the awesome
theme.
```

```{contents} On this page
:local:
:backlinks: none
```

## Use headerlink icons

```{note}
By default, the awesome theme uses Sphinx's default headerlink icons.
```

Sphinx shows a `¶` character after section titles and captions. Since Sphinx 3.5, you
can use the setting {confval}`sphinx:html_permalinks_icon` to change this default.

For example, to replace the default character with a `#` character:

```{code-block} python
---
caption: "File: conf.py"
---
html_permalinks_icon = "<span>#</span>"
```

If you want to use plain characters, it's better to wrap them in a HTML `<span>` element.
This way, the icon is only shown when you hover over the heading.
You can also insert SVG icons (as you can see on these pages).

Clicking any headerlink directly copies the URL to the clipboard. To revert to the
default behavior, set the option {confval}`html_awesome_headerlinks` to `False`.

## Highlight placeholder text in code blocks

To highlight text in code blocks, that users should replace with their own instances,
you can add the {samp}`emphasize-text: {PLACEHOLDER}` option to the `code-block`
directive.

For example:

```rst

.. code-block::
   :emphasize-text: PLACEHOLDER

   echo "Replace PLACEHOLDER text"
```

renders as:

```{code-block} shell
---
emphasize-text: PLACEHOLDER
---
echo "Replace PLACEHOLDER"
```

## Highlight code changes

Sometimes, you want to highlight changes in code. The awesome theme adds two options to
the `code-block` directive.

To highlight removed lines in a code snippet, use the `emphasize-removed` option.
To highlight added lines, use the `emphasize-added` option.

For example:

```rst

.. code-block:: shell
   :emphasize-removed: 1
   :emphasize-added: 2

   echo "Hello World"
   echo "Hello You"
```

renders as:

```{code-block} shell
---
emphasize-removed: 1
emphasize-added: 2
---
echo "Hello World"
echo "Hello You"
```

:::{note}
You can also use the built-in `diff` language to get a similar effect:

```rst

.. code-block:: diff

   + echo "Hello You"
   - echo "Hello World"
```

renders as:

```{code-block} diff
+ echo "Hello You"
- echo "Hello World"
```

Using this approach, you _only_ highlight the changes. The rest of the lines render as
plain text without syntax highlighting. If you copy the code, the `+` and `-` characters
are copied as well.
:::
