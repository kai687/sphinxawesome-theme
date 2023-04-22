.. _sec:add-to-sphinx:

Add the theme to your Sphinx configuration
------------------------------------------

To use the |product| in your documentation:

#. :ref:`sec:install-python-package`.
#. Add the |product| as an HTML theme and extension:

   .. literalinclude:: includes/configure.inc
      :language: python
      :caption: File: conf.py

   .. seealso::

      :ref:`sec:extension-options`
      :confval:`sphinx:html_theme`
      :confval:`sphinx:extensions`
