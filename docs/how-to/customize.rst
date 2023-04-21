.. meta::
   :description: Adapt the Awesome Theme to your needs by adding custom styles, using custom layouts, or changing the default templates.

Customize the theme
===================

.. rst-class:: lead

   Customize the |product| by adding custom CSS or custom JavaScript.
   Use custom page layout or modify existing templates.

.. contents:: On this page
   :local:
   :backlinks: none

Override CSS custom properties
------------------------------

You can override these custom properties (variables):

``--color-brand``
   The color for hover, focus, and highlight styles

``--color-links``
   The color for links in the main text.


To override custom properties, :ref:`add a new CSS file <sec:override-styles>` with new values.
For example, change the link color to green:

.. code-block:: css

   :root {
     --color-links: green;
   }

.. _sec:override-styles:

Add custom CSS
--------------

To add extra CSS files,
use the :confval:`sphinx:html_css_files` configuration option.

For example, place custom styles in a file :file:`_static/custom.css` and
add the following options to your Sphinx configuration:

.. code-block:: python
   :caption: File: conf.py

   html_static_path = ["_static"]
   html_css_files = ["custom.css"]

If you want to **override existing styles**, you might have to add `!important`.

.. seealso::

   `CSS Specificity (MDN Web Docs) <https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity>`_

.. important::

   You can't use Tailwind's ``@apply`` directive in custom CSS.
   Use regular CSS instead.

Add custom JavaScript
---------------------

To add extra JavaScript files,
use the :confval:`sphinx:html_js_files` configuration option.

For example, place your custom JavaScript in a file :file:`_static/custom.js`
and add the following options to your Sphinx configuration:

.. code-block:: python
   :caption: File: conf.py

   html_static_path = ["_static"]
   html_js_files = ["custom.js"]


.. _sec:additional-layouts:

Add page layouts
----------------

To add page layouts to your Sphinx documentation,
create a directory in your Sphinx project—for example,
:file:`_templates/`, and add it to your Sphinx configuration:

.. code-block:: python
  :caption: File: conf.py

  templates_path = ["_templates"]

.. seealso::

  :confval:`sphinx:templates_path`

Extend existing templates
~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new file with the same name as the template you want to extend.
For example, to add custom HTML tags to your ``<head>`` element:

.. code-block:: html+jinja
  :caption: File: page.html

  {% extends "!page.html" %}

  {{ super() }}

  {% block extrahead %}
  <!-- Add extra HTML tags here. For example: analytics scripts -->
  {% endblock %}

You can use this method to add inline CSS or JavaScript that runs on every page.

The main templates you can override are:

``header.html``
   Template for the header.

``footer.html``
   Template for the footer.

``page.html``
   Template for the body of the page.

   This page **must** contain the ``{{ body }}`` expression to render the contents of your documentation.
   The ``page`` template extends the layout ``with-sidebar`` or ``without-sidebar`` depending on the context.

`without-sidebar.html`
   Template for a page without navigation sidebar.
   This template is used when the option :confval:`show_nav` is set to ``False``,
   or when you set ``layout: "without-sidebar"`` in the frontmatter of your Markdown document.
   This template extends the main template ``layout``.

``with-sidebar.html``
   Template with navigation sidebar on the left.
   This is the default template for all documentation pages.
   It extends from the main template ``layout``.

``layout.html``
   Main template defining the structure of the page, including the HTML ``<head>`` with all imported CSS and JavaScript files.

For more information, see the available templates in the directory
`\`src/sphinxawesome_theme/\` <https://github.com/kai687/sphinxawesome-theme/tree/master/src/sphinxawesome_theme>`_.

.. _sec:override-layouts-locally:

Override per-page layout
------------------------

.. important::

   You can only select per-page layouts if you write your documentation in Markdown
   using the `\`myst-parser\` <https://myst-parser.readthedocs.io/en/latest/index.html>`_ extension.

The |product| has two page layouts.
The default layout shows a sidebar with all navigation links on the left side.

If you want to override the layout *on one page*,
you can use the ``layout`` option in the YAML frontmatter.

For example, the :doc:`../about` page uses a layout without a sidebar:

.. code-block:: markdown

   ---
   layout: "without-sidebar"
   ---

   # About
