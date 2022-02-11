---
html_meta:
  description: |
    Find out how to make your Sphinx documentation awesome by using the features of the
    Awesome Theme.
---

# Make your documentation awesome

```{rst-class} lead
Make the most out of your Sphinx documentation by using the features of the
{{ product }}.
```

```{contents} On this page
:local:
:backlinks: none
```

## Use headerlink icons

By default, Sphinx shows a `¶` character after section titles and captions
("permalinks").
Since Sphinx 3.5, you can change the default with the setting
{confval}`sphinx:html_permalinks_icon`.

For example, you can replace the default character with a `#` character:

```{code-block} python
---
caption: "File: conf.py"
---
html_permalinks_icon = "<span>#</span>"
```

You can use SVG icons (like on this page) or plain characters.
If you're using plain characters with the {{ product }},
wrap them in a `<span>` element.
This shows the headerlinks only when hovering over the heading,
or changing focus with your keyboard.

Headerlinks are often used to share links to specific sections in documentation.
The {{ product }} makes that a little easier by copying the URL to the clipboard
when clicking a headerlink.
To revert to the default behavior, set the option {confval}`html_awesome_headerlinks` to `False`.

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

<!-- vale Google.Headings = NO -->

## Add as-you-type search with Algolia DocSearch

<!-- vale Google.Headings = YES -->

To get a fast and relevant _search-as-you-type_ experience,
you can use Algolia DocSearch as a replacement for Sphinx' built-in search.
It's free for open source documentation projects and blogs with technical content.
