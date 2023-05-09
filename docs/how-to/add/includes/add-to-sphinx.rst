.. _sec:add-to-sphinx:

Add the theme to your Sphinx configuration
------------------------------------------

#. :ref:`sec:install-python-package`.
#. Add the |product| as an HTML theme:

   .. literalinclude:: includes/configure.inc
      :language: python
      :caption: File: conf.py

   .. seealso::

      :confval:`sphinx:html_theme`

Load bundled extensions
-----------------------

The |product| bundles two extensions,
that enhance your ability to provide great documentation.
Both extensions are optional and independent from each other.

To add them to your configuration:

.. code-block:: python
   :caption: File: conf.py

   extensions += [
      "sphinxawesome_theme.docsearch",
      "sphinxawesome_theme.highlighting",
   ]

``sphinxawesome_theme.docsearch``
   Replaces the built-in search with Algolia DocSearch for showing instant search results as you type.

``sphinxawesome_theme.highlighting``
   Add extra highlighting option to Sphinx's ``code-block`` directive.

.. seealso::

   :confval:`sphinx:extensions`
