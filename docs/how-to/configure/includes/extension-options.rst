.. _sec:extension-options:

Extension options
-----------------

If you added the |product| as an extension,
you can configure these options:

.. code-block:: python
   :caption: File: conf.py

   html_collapsible_definitions = False
   html_awesome_headerlinks = True
   html_awesome_code_headers = True
   html_awesome_docsearch = False
   html_awesome_external_links = False

``html_collapsible_definitions``
   Controls whether to make code objects, such as classes, collapsible.

   .. deprecated:: 4.1.0

      Use the sphinx-design_ extension instead.
      This option will be removed in version 5.0.

``html_awesome_headerlinks``
   Controls whether clicking a headerlink should copy the URL to the clipboard.

.. _opt:html_awesome_code_headers:

``html_awesome_code_headers``
   Controls whether to show the highlighted programming language in the headers of code blocks.

   .. deprecated:: 4.1.0

      This option will be removed in version 5.0.

``html_awesome_docsearch``
   Controls whether to use `Algolia DocSearch`_ instead of the built-in search.

``html_awesome_external_links``
   Controls whether to show an icon after external links.

   .. versionadded:: 4.1.0

      In previous versions, this was always enabled.

.. _sphinx-design: https://sphinx-design.readthedocs.io/en/latest/
.. _Algolia DocSearch: https://docsearch.algolia.com/
