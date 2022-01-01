---
html_meta:
  description: |
    Find out how to make your Sphinx documentation awesome by using the features of the
    Awesome Theme.
---

# Make your documentation awesome

```{rst-class} lead
Make the most out of your Sphinx documentation by using the features of the Awesome
Theme.
```

```{contents} On this page
:local:
:backlinks: none
```

## Use headerlink icons

Sphinx shows a `¶` character after section titles and captions.
Since Sphinx 3.5, you can change the default with the setting
{confval}`sphinx:html_permalinks_icon`.

For example, replace the default character with a `#` character:

```{code-block} python
---
caption: "File: conf.py"
---
html_permalinks_icon = "<span>#</span>"
```

If you want to use plain characters, it's better to wrap them in a HTML `<span>` element.
This way, the icon is only shown when you hover over the heading.
You can also use SVG icons.

Clicking any headerlink directly copies the URL to the clipboard. To revert to the
default behavior, set the option {confval}`html_awesome_headerlinks` to `False`.

## Highlight placeholder text in code blocks

To highlight text in code blocks, add the {samp}`emphasize-text: {PLACEHOLDER}` option to the `code-block`
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

Sometimes, you want to highlight changes in code, for example, lines of code that should
be removed or added.

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

## Provide an awesome search experience with Algolia DocSearch

To get a fast and relevant _search-as-you-type_ experience,
you can use Algolia DocSearch as a replacement for Sphinx' built-in search.
It's free for open-source documentation projects and blogs with technical content.
