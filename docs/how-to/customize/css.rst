.. meta::
   :description: Customize your styles by adding CSS files or adding styles inline.
   :twitter:description: Customize your styles by adding CSS files or adding styles inline.

.. _sec:custom-css:

Add custom CSS
==============

.. rst-class:: lead

   Customize your styles by adding CSS files or adding styles inline.

Add CSS files
-------------

To add extra CSS files, put your custom styles in a file, for example :file:`_static/custom.css`.
Then add these options to your Sphinx configuration:

.. code-block:: python
   :caption: |conf|

   html_static_path = ["_static"]
   html_css_files = ["custom.css"]

Sphinx loads your custom CSS file *after* the default CSS of the theme.
Because of different `CSS specificities`_,
sometimes you must add ``!important`` to your CSS styles.

.. _CSS specificities: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity

.. seealso::

   :confval:`sphinx:html_static_path`
   :confval:`sphinx:html_css_files`

.. important::

   Do not use the ``@apply`` directive of Tailwind in custom CSS.
   Use regular CSS instead.

Extend templates with inline CSS
--------------------------------

To add CSS inline,
extend the default ``page`` template and override the ``extrahead`` block:

.. code-block:: html+jinja
  :caption: File: page.html

  {% extends "!page.html" %}

  {% block extrahead %}
  <style>
   /* Add your CSS styles here */
  </style>
  {% endblock %}

Override CSS custom properties
------------------------------

The theme defines its colors as CSS custom properties on the ``:root`` element.
The dark mode values are on ``:root.dark``.
Each value is a list of hue, saturation, and lightness (HSL) values, without the ``hsl()`` function.
For example, ``222.2 47.4% 11.2%``.

You can override these custom properties:

``--background``, ``--foreground``
   The color of the page and the color of the main text.

``--brand``
   The accent color for the active sidebar link, the active table of contents entry, and DocSearch highlights.

``--accent``, ``--accent-foreground``
   The background color and the text color for hover and focus states.

``--muted``, ``--muted-foreground``
   The colors for secondary elements, such as code block backgrounds, tooltips, and secondary text.

``--popover``, ``--popover-foreground``
   The colors for the DocSearch modal.

``--card``, ``--card-foreground``
   The colors for cards, for example from ``sphinx-design``.

``--border``, ``--input``
   The color of borders and of form fields.

``--ring``
   The color of the keyboard focus ring on the built-in search field and the DocSearch button.
   It does not change other focus outlines.

``--note``, ``--tip``, ``--warning``, ``--danger``
   The hues for admonitions and version notes.
   ``--danger`` also colors the error output of ``myst-nb`` cells and the JavaScript fallback message on the search page.

``--diff-add``, ``--diff-remove``
   The background hue for added and removed lines in diffs and in highlighted code blocks.

``--diff-add-foreground``, ``--diff-remove-foreground``
   The text color for added and removed lines.

``--radius``
   The base corner radius, for example ``0.5rem``.
   This value is a length, not an HSL list.

``--font-mono``
   The font stack for code and other monospace text.
   This value is a list of font families, not an HSL list.
   For example, ``--font-mono: "Fira Code", ui-monospace, monospace;``.

.. note::

   Syntax highlighting colors are not CSS custom properties.
   To change them, set :confval:`sphinx:pygments_style` and ``pygments_style_dark``.

To make the search focus ring green in both light and dark mode,
add this CSS to a custom stylesheet or template:

.. code-block:: css

   :root,
   :root.dark {
      --ring: 142 71% 45%;
   }

Press Tab until the search field or DocSearch button has focus to see the green ring.

To set different colors for light mode and dark mode,
set the custom properties on ``:root`` and on ``:root.dark`` separately.

Extension variables
~~~~~~~~~~~~~~~~~~~

The theme maps its colors to the variables of ``sphinx-design``, ``myst-nb``, and DocSearch.
To change one element only, override the variable of the extension directly.
These variables hold complete colors, such as ``hsl(0 80% 95%)``, not HSL lists:

- ``--sd-color-*`` for ``sphinx-design`` tabs and cards
- ``--mystnb-*`` for ``myst-nb`` code cells and output
- ``--docsearch-*`` for DocSearch

.. seealso::

   `CSS custom properties (MDN web docs) <https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*>`_
