.. This file is meant to be included in `add-custom-templates`.
   The heading must be an `h3` to match the structure.

.. _sec:extend-templates:

Extend templates
~~~~~~~~~~~~~~~~

To extend an existing template,
create a new file with the same name. Add this code to the file:

.. code-block:: html+jinja
   :emphasize-text: TEMPLATE

   {% extends "!TEMPLATE" %}

   {{ super() }}

Replace :samp:`{TEMPLATE}` with the name of the template to extend.
The exclamation mark makes Sphinx load the parent template from the HTML theme.
The ``super()`` call renders the original content of the parent template.

.. seealso::

   :doc:`sphinx:development/html_themes/templating`
