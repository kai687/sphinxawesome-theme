.. _sec:bundled-extensions:

Bundled extensions
------------------

The |product| bundles one Sphinx extension for better code blocks.

``sphinxawesome_theme.highlighting``
   Adds the following highlighting options to Sphinx's ``code-block`` directive:

   - :samp:`:emphasize-added: {LINES}`: highlight lines to be added.
   - :samp:`:emphasize-removed: {LINES}`: highlight lines to be removed.
   - :samp:`:emphasize-text: {TEXT}`: highlight a placeholder word or phrase.

   .. note::

      If you don't add this extension, the spacing in code blocks might appear off.
      You can :ref:`sec:custom-css` with extra padding to ``pre`` elements.

.. seealso::

   :doc:`/demo/code-blocks`,
   :confval:`sphinx:extensions`
