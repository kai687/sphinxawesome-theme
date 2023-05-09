Configure Algolia DocSearch
---------------------------

Algolia DocSearch is a third-party service.
You need to `apply <https://docsearch.algolia.com/apply/>`_ and receive your credentials before you can use it.

You can configure DocSearch with the ``docsearch_config`` dictionary in your Sphinx configuration,
by adding environment variables to your environment, or both.
The environment variables have precedence.

.. note::

   The |product| supports :file:`.env` files for your environment variables.


.. code-block:: python
   :caption: File: conf.py

   docsearch_config = {
       app_id: "",
       api_key: "",
       index_name: ""
       initial_query: "",
       placeholder: "",
       search_parameters: "",
       missing_results_url: ""
   }

Algolia DocSearch reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: sphinxawesome_theme.docsearch.DocSearchConfig
   :members:

Algolia DocSearch credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You must provide these credentials, or DocSearch won't work.
The Sphinx project will still build, but the search won't show any results.

``app_id``, ``DOCSEARCH_APP_ID``
   The id of your Algolia DocSearch application.

``api_key``, ``DOCSEARCH_API_KEY``
   The API key for searching your index on Algolia.

``index_name``, ``DOCSEARCH_INDEX_NAME``
   The name of your Algolia DocSearch index.

Optional DocSearch settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``initial_query``, ``DOCSEARCH_INITIAL_QUERY``
   Provide a search query if you want to show search results as soon as the DocSearch modal opens.

   .. versionadded:: 5.0.0

``placeholder``, ``DOCSEARCH_PLACEHOLDER``
   The placeholder for the search box. The default is: *Search docs*.

   .. versionadded:: 5.0.0

``search_parameters``, ``DOCSEARCH_SEARCH_PARAMETERS``
   `Search parameter <https://www.algolia.com/doc/api-reference/search-api-parameters/>`_
   for the Algolia Search.

   .. versionadded:: 5.0.0

``missing_results_url``, ``DOCSEARCH_MISSING_RESULTS_URL``
   A URL for letting users send you feedback about your search.
   You can use the current query in the URL.

   .. code-block:: bash
      :caption: Example for using *missing_results_url*

      DOCSEARCH_MISSING_RESULTS_URL=https://github.com/example/docs/issues/new?title=${query}

   .. caution::

      Provide the URL as a string.
      DocSearch itself accepts a function.
      In the templates,
      the |product| creates the function with the string you entered.

   .. versionadded:: 5.0.0

.. seealso::

   `DocSearch API reference <https://docsearch.algolia.com/docs/api/>`_
