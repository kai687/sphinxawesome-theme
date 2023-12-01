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

#. Optional: add the bundled extensions.

   .. code-block:: python
      :caption: |conf|

      extensions += [
         "sphinxawesome.highlighting",
         # To help you with the upgrade to version 5:
         # "sphinxawesome.deprecated",
      ]
