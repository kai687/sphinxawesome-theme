.. _sec:bundled-extensions:

Bundled extensions
------------------

The |product| bundles two Sphinx extensions that let you enhance your documentation.
They're independent from each other, so you can load them separately or together.

``sphinxawesome_theme.docsearch``
   Replaces the built-in search with Algolia DocSearch
   for showing instant search results as you type.
   For more information, see :ref:`sec:docsearch`.

``sphinxawesome_theme.highlighting``
   Adds the following highlighting options to Sphinx's ``code-block`` directive:

   - :samp:`:emphasize-added: {LINES}`: highlight lines to be added.
   - :samp:`:emphasize-removed: {LINES}`: highlight lines to be removed.
   - :samp:`:emphasize-text: {TEXT}`: highlight a placeholder word or phrase.

.. seealso::

   :doc:`/demo/code-blocks`,
   :confval:`sphinx:extensions`

.. note::

   In version 5, many configuration options changed.
   To help you with finding and upgrading deprecated options,
   add the ``sphinxawesome.deprecated`` extension.
   For more information, see :ref:`sec:upgrade-to-5.0`
