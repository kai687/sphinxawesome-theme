.. _sec:add-to-sphinx:

Add the theme to your Sphinx configuration
------------------------------------------

#. :ref:`sec:install-python-package`.
#. Add the |product| as an HTML theme:

   .. literalinclude:: includes/configure.inc
      :language: python
      :caption: |conf|

   .. seealso::

      :confval:`sphinx:html_theme`

#. Optional: load a bundled extension to check if you're using deprecated options:

   .. code-block:: python
      :caption: |conf|

      extensions += [
         "sphinxawesome.deprecated",
      ]

For information about the configuration options, see :doc:`../configure/index`.
