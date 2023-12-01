.. _sec:bundled-extensions:

Bundled extensions
------------------

The |product| bundles one Sphinx extensions that let you enhance your documentation.

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
