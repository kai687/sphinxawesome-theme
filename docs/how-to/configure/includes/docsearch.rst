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
   }

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

.. seealso::

   `DocSearch API reference <https://docsearch.algolia.com/docs/api/>`_
