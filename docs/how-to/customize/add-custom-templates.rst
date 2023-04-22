.. _sec:add-custom-templates:

Add custom templates
====================

To add, extend or override Jinja2 templates,
create a directory in your Sphinx project—for example,
:file:`_templates/`, and add it to your Sphinx configuration:

.. code-block:: python
  :caption: File: conf.py

  templates_path = ["_templates"]

.. seealso::

   :confval:`sphinx:templates_path`


.. include:: includes/extend-templates.rst
.. include:: includes/extend-template-blocks.rst
.. include:: includes/custom-templates.rst
.. include:: includes/available-templates.rst
