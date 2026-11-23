.. This file is meant to be included in `add-custom-templates`.
   The heading must be an `h3` to match the structure.

.. _sec:extend-templates:

Extend templates
~~~~~~~~~~~~~~~~

To extend an existing template,
create a new file with the same name. Add this code to the file:

.. code-block:: html+jinja
   :caption: File: _templates/page.html

   {% extends "!page.html" %}

   {% block scripts %}
     {{ super() }}
     {# Add your custom scripts here. #}
   {% endblock %}

The exclamation mark makes Sphinx load the parent template from the HTML theme.
Blocks you do not override keep their original content.
To keep the original content of a block you override, call ``{{ super() }}`` inside that block.

.. seealso::

   :doc:`sphinx:development/html_themes/templating`
