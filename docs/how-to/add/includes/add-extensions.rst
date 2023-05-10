Add bundled extensions
----------------------

Two enhance your documentation,
you can add these optional extensions:

.. code-block:: python
   :caption: File: conf.py

   extensions += [
      "sphinxawesome_theme.docsearch",
      "sphinxawesome_theme.highlighting",
   ]

Both extensions are independent from each other.

``sphinxawesome_theme.docsearch``
   Replaces the built-in search with Algolia DocSearch for showing instant search results as you type.

``sphinxawesome_theme.highlighting``
   Adds the following highlighting options to Sphinx's ``code-block`` directive:

   - :samp:`:emphasize-added: {LINES}`: highlight lines to be added.
   - :samp:`:emphasize-removed: {LINES}`: highlight lines to be removed.
   - :samp:`:emphasize-text: {TEXT}`: highlight a placeholder word or phrase.

.. seealso::

   :ref:`sec:docsearch`,
   :doc:`/demo/code-blocks`,
   :confval:`sphinx:extensions`
