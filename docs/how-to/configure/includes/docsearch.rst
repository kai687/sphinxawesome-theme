.. _sec:docsearch:

Algolia DocSearch
-----------------

DocSearch provides search for open source projects and technical blogs for free.
You need to `apply <https://docsearch.algolia.com/apply/>`_ and receive your credentials before you can use it.

The |product| bundles DocSearch as an optional extension.
To replace the built-in search with DocSearch, add the ``sphinxawesome_theme.docsearch`` extension:

.. code-block:: python
   :caption: |conf|

   extensions += ["sphinxawesome_theme.docsearch"]

.. dropdown:: How does DocSearch work?

   If you're part of the program,
   Algolia indexes your content with a `crawler <https://en.wikipedia.org/wiki/Web_crawler>`_.
   You'll add the DocSearch UI component to your layout, which fetches the results from your index on every keystroke.

DocSearch credentials
~~~~~~~~~~~~~~~~~~~~~

Algolia provides you with three credentials for DocSearch.
You must add the application ID and search API key to your site to authenticate and authorize search requests.
Keep the write API key a secret.

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

Instead of storing your credentials in your Sphinx configuration file and committing it to your repository,
it's better to load it from **environment variables**.
A good way of handling environment variables is to store them in a :file:`.env` file.
To do this, add the ``python-dotenv`` package to your project and add the following code to your Sphinx configuration:

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

To avoid committing this file to your repository, add ``.env`` to your :file:`.gitignore` file.

The ``DocSearchConfig`` helper
++++++++++++++++++++++++++++++

To make it easier to configure DocSearch,
the |product| provides a ``DocSearchConfig`` helper class.
If you're okay with (ab)using Python's dynamic character,
you can add the following code:

.. code-block:: python
   :caption: |conf|

   import os
   from python_dotenv import load_dotenv
   from dataclasses import asdict
   from sphinxawesome_theme.docsearch import DocSearchConfig

   load_dotenv()

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

.. py:module:: sphinxawesome_theme.docsearch

.. autoclass:: DocSearchConfig()
   :members:

.. seealso::

   `DocSearch API reference <https://docsearch.algolia.com/docs/api/>`_
