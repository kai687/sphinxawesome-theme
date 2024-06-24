.. This file is meant to be included in `add-custom-templates`.
   The heading must be an `h3` to match the structure.

.. _sec:extend-templates:

Extend templates
~~~~~~~~~~~~~~~~

To extend existing templates,
create a new file with the same name and add the following code:

.. code-block:: html+jinja
   :emphasize-text: TEMPLATE

   {% extends "!TEMPLATE" %}

   {{ super() }}

Replace :samp:`{TEMPLATE}` with the name of the template you want to extend.
The exclamation mark lets Sphinx load the parent template from the HTML theme.
Call ``super()`` to render the original content of the parent template.

.. seealso::

   :doc:`sphinx:development/html_themes/templating`
