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

To add extra CSS files, add your custom styles to a file—for example,
:file:`_static/custom.css` and add the following options to your Sphinx configuration:

.. code-block:: python
   :caption: |conf|

   html_static_path = ["_static"]
   html_css_files = ["custom.css"]

Your custom CSS file is included *after* the theme's default CSS.
Because of different `CSS specificities <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Specificity>`_,
you might need to add ``!important`` to your CSS styles.

.. seealso::

   :confval:`sphinx:html_static_path`
   :confval:`sphinx:html_css_files`

.. important::

   You can't use Tailwind's ``@apply`` directive in custom CSS.
   Use regular CSS instead.

Extend templates with inline CSS
--------------------------------

If you want to add CSS inline,
you can extend the default ``page`` template and override the ``extrahead`` block:

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

You can override these custom properties:

``--color-brand``
   The color for hover, focus, and highlight styles

``--color-links``
   The color for links in the main text.

For example, to change the color of links to green,
add a new CSS file or extend the templates and add the following CSS:

.. code-block:: css

   :root {
      --color-links: green;
   }

.. seealso::

   `CSS custom properties (MDN web docs) <https://developer.mozilla.org/en-US/docs/Web/CSS/--*>`_
