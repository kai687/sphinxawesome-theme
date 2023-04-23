.. _sec:extension-options:

Extension options
-----------------

If you added the |product| as an extension,
you can configure these options:

.. code-block:: python
   :caption: File: conf.py

   html_collapsible_definitions = False  # Deprecated
   html_awesome_headerlinks = True
   html_awesome_code_headers = True
   html_awesome_docsearch = False

``html_collapsible_definitions``
   Controls whether to make code objects, such as classes, collapsible.

   .. deprecated:: 4.0.3

      Use the sphinx-design_ extension instead. (Removed in 5.0.0)

``html_awesome_headerlinks``
   Controls whether clicking a headerlink should copy the URL to the clipboard.

``html_awesome_code_headers``
   Controls whether to show the highlighted programming language in the headers of code blocks.

``html_awesome_docsearch``
   Controls whether to use `Algolia DocSearch <https://docsearch.algolia.com/>`_ instead of the built-in search.


.. _sphinx-design: https://sphinx-design.readthedocs.io/en/latest/
