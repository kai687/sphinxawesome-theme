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

  {{ super() }}

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

``--primary``
   The color for sidebar link hover styles and for DocSearch highlights.

``--accent``, ``--accent-foreground``
   The background color and the text color for hover and focus states.

``--muted``, ``--muted-foreground``
   The colors for secondary elements and secondary text.

``--border``, ``--input``
   The color of borders and of form fields.

``--ring``
   The color of the focus outline.

For example, to change the focus outline to green in light mode and in dark mode,
add a new CSS file, or extend the templates. Then add this CSS:

.. code-block:: css

   :root,
   :root.dark {
      --ring: 142 71% 45%;
   }

To set different colors for light mode and dark mode,
set the custom properties on ``:root`` and on ``:root.dark`` separately.

.. seealso::

   `CSS custom properties (MDN web docs) <https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*>`_
