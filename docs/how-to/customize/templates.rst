.. meta::
   :description: Add, extend, or override Jinja2 templates.
   :twitter:description: Add, extend, or override Jinja2 templates.

.. _sec:add-custom-templates:

Add custom templates
====================

.. rst-class:: lead

   Add, extend, or overrde Jinja2 templates.

Create a directory in your Sphinx project and add it to your Sphinx configuration:

.. code-block:: python
  :caption: |conf|

  templates_path = ["_templates"]

.. seealso::

   :confval:`sphinx:templates_path`


.. include:: includes/extend-templates.rst
.. include:: includes/extend-template-blocks.rst
.. include:: includes/custom-templates.rst
.. include:: includes/available-templates.rst
