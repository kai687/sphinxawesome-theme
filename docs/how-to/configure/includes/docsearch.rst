.. _sec:docsearch:

Algolia DocSearch
-----------------

DocSearch provides search for open source projects and technical blogs for free.
You can `apply <https://docsearch.algolia.com/apply/>`_ and receive your credentials.

To replace the built-in search with DocSearch,
:ref:`sec:add-to-sphinx` and
add the ``sphinxawesome_theme.docsearch`` extension:

.. code-block:: python
   :caption: |conf|

   extensions += ["sphinxawesome_theme.docsearch"]

.. dropdown:: How does DocSearch work?

   Algolia indexes your content with a `crawler <https://en.wikipedia.org/wiki/Web_crawler>`_.
   You'll add the DocSearch UI component to your layout.
   Now, on every keystroke, DocSearch looks for matching results on Algolia's servers
   and updates the view instantly.

DocSearch credentials
~~~~~~~~~~~~~~~~~~~~~

Algolia provides you with three credentials for DocSearch.
You must add the application ID and search API key to your site to authenticate and authorize search requests.
Keep the write API key a secret.
You can find your credentials in the `Algolia dashboard <https://www.algolia.com/dashboard>`_.

Application ID
   The identifier for your project on Algolia.
   It's used to route search requests from your site to your Algolia index.

Search API key
   An API key that allows search requests from your site.

Write API key
   An API key that allows writing to your index.
   Since Algolia indexes your content automatically with a crawler,
   you don't have to use this key.
   **Don't use the write API key in your site.**

Configure DocSearch
~~~~~~~~~~~~~~~~~~~

To configure DocSearch, declare the ``docsearch_*`` options as regular Python variables:

.. code-block:: python
   :caption: |conf|

   docsearch_app_id = "YOUR_APP_ID"
   docsearch_api_key = "YOUR_API_KEY"
   docsearch_index_name = "YOUR_INDEX_NAME"

Use environment variables
+++++++++++++++++++++++++

Instead of exposing your credentials in your Sphinx configuration file,
you can load them from **environment variables**.
For example, you can store them in a in a :file:`.env` file.
To do this, add the ``python-dotenv`` package to your project
and add the following code to your Sphinx configuration:

.. code-block:: python
   :caption: |conf|

   import os
   from python_dotenv import load_dotenv

   # Load environment variables from a .env file
   load_dotenv()

   docsearch_app_id = os.getenv("DOCSEARCH_APP_ID")
   docsearch_api_key = os.getenv("DOCSEARCH_API_KEY")
   docsearch_index_name = os.getenv("DOCSEARCH_INDEX_NAME")

In the same directory as your :file:`conf.py` file, create a :file:`.env` file with these variables:

.. code-block:: text
   :caption: File: .env

   DOCSEARCH_APP_ID=YOUR_APP_ID
   DOCSEARCH_API_KEY=YOUR_API_KEY
   DOCSEARCH_INDEX_NAME=YOUR_INDEX_NAME

To avoid uploading this file to your repository,
add ``.env`` to your :file:`.gitignore` file.

The ``DocSearchConfig`` helper
++++++++++++++++++++++++++++++

To make it easier to configure DocSearch with code completion and hover help,
the |product| provides a ``DocSearchConfig`` helper class.
If you're okay with (ab)using Python's dynamic character,
you can add the following code:

.. code-block:: python
   :caption: |conf|

   import os
   from python_dotenv import load_dotenv
   from dataclasses import asdict
   from sphinxawesome_theme.docsearch import DocSearchConfig

   # This gets you code completion and documentation for your configuration options
   config = DocSearchConfig(
      docsearch_app_id=os.getenv("DOCSEARCH_APP_ID")
      docsearch_api_key=os.getenv("DOCSEARCH_API_KEY")
      docsearch_index_name=os.getenv("DOCSEARCH_INDEX_NAME")
   )

   vars = locals()
   for key, value in asdict(config).items():
      vars.__setitem__(key, value)

DocSearch configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. confval:: docsearch_app_id

   Your Algolia DocSearch application ID. **(Required)**

.. confval:: docsearch_api_key

   Your Algolia DocSearch search API key. **(Required)**

   .. caution::

      Don't use your write API key.

.. confval:: docsearch_index_name

   Your Algolia DocSearch index name. **(Required)**

.. confval:: docsearch_container

   A CSS selector where the DocSearch UI component should be added.
   The default is: ``#docsearch``.

.. confval:: docsearch_placeholder

   The placeholder for the search box.

.. confval:: docsearch_initial_query

   A query for an initial search
   if you want to show search results as soon as the user opens the
   search menu.

.. confval:: docsearch_search_parameter

   Any `Algolia search parameter <https://www.algolia.com/doc/api-reference/search-api-parameters/>`_ you want to add.

.. confval:: docsearch_missing_results_url

   If specified, DocSearch adds a message to the "No results found" screen
   with the link to the URL you specified, for users to report issues with missing search results.
   You can include the current search query as parameter ``${query}``.
   For example:

   .. code-block:: python

      docsearch_missing_results_url = "https://github.com/example/docs/issues/new?title=${query}"

.. seealso::

   `DocSearch API reference <https://docsearch.algolia.com/docs/api/>`_
