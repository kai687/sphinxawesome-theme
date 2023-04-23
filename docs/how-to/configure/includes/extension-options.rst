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

   .. warning::

      This option is deprecated and will be removed in version 5.0.
      If you want to have collapsible elements,
      use the `sphinx-design <https://sphinx-design.readthedocs.io/en/latest/>`_ extension.

``html_awesome_headerlinks``
   Controls whether clicking a headerlink should copy the URL to the clipboard.

``html_awesome_code_headers``
   Controls whether to show the highlighted programming language in the headers of code blocks.

``html_awesome_docsearch``
   Controls whether to use `Algolia DocSearch <https://docsearch.algolia.com/>`_ instead of the built-in search.
