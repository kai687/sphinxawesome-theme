.. meta::
   :description: Configure the Awesome Theme by changing options in your Sphinx configuration file.

Configure the theme
===================

.. rst-class:: lead

   Configure the |product| by changing one of the theme or extension options.

.. contents:: On this page
   :local:
   :backlinks: none

.. admonition:: What's the difference between theme and extension options?

   Theme options
      Are available in the HTML templates.
      They control layout and styling.

   Extension options
     Are defined in the Python code of the extensions.
     They can modify most of Sphinx behavior.

.. _sec:theme_options:

Theme options
-------------

To configure the theme, modify the ``html_theme_options`` dictionary in your Sphinx configuration.

.. confval:: nav_include_hidden

   Controls whether to include entries from a *hidden*
   :sphinxdocs:`toctree <usage/restructuredtext/directives.html#directive-toctree>`
   directive in the sidebar.

   .. code-block:: python
      :caption: File: conf.py

      # Default: `True`
      html_theme_options = {"nav_include_hidden": False}

   By default,
   the ``toctree`` directive includes your content *and* generates a list of links in the content area of the page.
   With the ``hidden`` option, the content is still included,
   but no links are printed in the main content area.

.. confval:: show_nav

   Controls whether to render the left sidebar.

   .. code-block:: python
      :caption: File: conf.py

      # Default: `True`
      html_theme_options = {"show_nav": False}


.. confval:: show_breadcrumbs

   Controls whether to include `breadcrumbs <https://en.wikipedia.org/wiki/Breadcrumb_navigation>`_ links at the top of each page.

   .. code-block:: python
      :caption: File: conf.py

      # Default: `True`
      html_theme_options = {"show_breadcrumbs": False}

.. confval:: breadcrumbs_separator

   The separator for the breadcrumbs links.

   .. code-block:: python
      :caption: File: conf.py
      :emphasize-text: CHAR

      # Default: `/`
      html_theme_options = {"breadcrumbs_separator": "CHAR"}

   Replace :samp:`{CHAR}` with a character or HTML entity of your choice.

.. confval:: show_prev_next

   Controls whether to show links to the previous and next pages in the hierarchy.

   .. code-block:: python
      :caption: File: conf.py

      # Default: `False`
      html_theme_options = {"show_prev_next": True}

.. confval:: show_scrolltop

   Controls whether to show a button that scrolls to the top of the page when clicked.

   .. code-block:: python
      :caption: File: conf.py

      # Default: `False`
      html_theme_options = {"show_scrolltop": True}

.. confval:: extra_header_links

   Adds extra links to the header of your documentation.

   .. code-block:: python
      :caption: File: conf.py

      html_theme_options = {
        # Default: `False`
        extra_header_links = {
          "link1": "/url1",
          "link2": "/url2",
        }
      }

   The keys of the ``extra_header_links`` dictionary are the link texts.
   The values are absolute URLs.

.. _sec:extension-options:

Extension options
-----------------

.. note::

   To configure extension options,
   you need to add the theme to the list of extensions in your Sphinx configuration:

   ``extensions = ["sphinxawesome_theme"]``

The |product| enables several internal extensions.
The following options are set at the top level in your Sphinx configuration:

.. confval:: html_collapsible_definitions

   Controls whether to make code objects, such as classes, collapsible.

   .. code-block:: python
      :caption: File: conf.py

      # Default: `False`
      html_collapsible_definitions = True


.. confval:: html_awesome_headerlinks

   Controls whether clicking a headerlink should copy the URL to the clipboard.

   .. code-block:: python
      :caption: File: conf.py

      # Default: `True`
      html_awesome_headerlinks = False

.. confval:: html_awesome_code_headers

   Controls whether to show the highlighted programming language in the headers of code blocks.

   .. code-block:: python
      :caption: File: conf.py

      # Default: `True`
      html_awesome_code_headers = False

.. confval:: html_awesome_docsearch

   Controls whether to use `Algolia DocSearch <https://docsearch.algolia.com/>`_ instead of the built-in search.

   .. code-block:: python
      :caption: File: conf.py

      # Default: `False`
      html_awesome_docsearch = True

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

Algolia DocSearch credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You must provide these credentials, or DocSearch won't work.
The Sphinx project will still build, but the search won't show any results.

.. confval:: app_id

   The id of your Algolia DocSearch application.

   Environment variable: ``DOCSEARCH_APP_ID``

.. confval:: api_key

   The API key for searching your index on Algolia.

   Environment variable: ``DOCSEARCH_API_KEY``

.. confval:: index_name

   The name of your Algolia DocSearch index.

   Environment variable: ``DOCSEARCH_INDEX_NAME``

Optional DocSearch settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. confval:: initial_query

   Provide a search query if you want to show search results as soon as the DocSearch modal opens.

   Environment variable: ``DOCSEARCH_INITIAL_QUERY``

.. confval:: placeholder

   The placeholder for the search box. The default is: *Search docs*.

   Environment variable: ``DOCSEARCH_PLACEHOLDER``

.. confval:: search_parameters

   `Search parameter <https://www.algolia.com/doc/api-reference/search-api-parameters/>`_
   for the Algolia Search.

   Environment variable: ``DOCSEARCH_SEARCH_PARAMETERS``

.. confval:: missing_results_url

   A URL for letting users send you feedback about your search.
   You can use the current query in the URL.

   Environment variable: ``DOCSEARCH_MISSING_RESULTS_URL``

   .. code-block:: terminal
      :caption: Example for using *missing_results_url*

      DOCSEARCH_MISSING_RESULTS_URL=https://github.com/example/docs/issues/new?title=${query}

   .. caution::

      Provide the URL as a string.
      DocSearch itself accepts a function.
      In the templates,
      the |product| creates the function with the string you entered.

.. seealso::

   `DocSearch API reference <https://docsearch.algolia.com/docs/api/>`_
