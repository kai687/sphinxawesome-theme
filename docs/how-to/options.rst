.. meta::
   :description: Configure the Awesome Theme by changing options in your Sphinx configuration file.

.. _sec:configure:

Configure the theme
===================

.. rst-class:: lead

   Configure the |product| by changing one of the theme or extension options.

.. contents:: On this page
   :local:
   :backlinks: none

.. admonition:: What's the difference between theme and extension options?

   - **Theme options** are defined in the HTML templates.
     They control layout and styling.
   - **Extension options** are defined in the Python code of the extensions.
     They can control more aspects, such as, running extra code.

.. _sec:theme_options:

Theme options
-------------

To configure the theme, modify the ``html_theme_options`` dictionary in your Sphinx configuration.

.. confval:: nav_include_hidden

   If you don't want to include entries from a _hidden_
   :sphinxdocs:`toctree <usage/restructuredtext/directives.html#directive-toctree>`
   directive in the sidebar,
   set ``nav_include_hidden`` to ``False``.

   .. code-block:: python
      :caption: File: conf.py

      # This option is `True` by default
      html_theme_options = {"nav_include_hidden": False}

   By default,
   the ``toctree`` directive includes your content _and_ generates a list of links in the content area of the page.
   With the ``hidden`` option, the content is still included,
   but no links are printed in the main content area.

.. confval:: show_nav

   The |product| shows links to all your documentation pages in the left sidebar.
   To hide the sidebar on all pages, set this option to `False`:

   .. code-block:: python
      :caption: File: conf.py

      # This option is `True` by default
      html_theme_options = {"show_nav": False}


.. confval:: show_breadcrumbs

   The |product| shows `breadcrumbs <https://en.wikipedia.org/wiki/Breadcrumb_navigation>`_ links at the top of each page
   To hide the breadcrumbs, set this option to ``False``:

   .. code-block:: python
      :caption: File: conf.py

      # This option is `True` by default
      html_theme_options = {"show_breadcrumbs": False}

.. confval:: breadcrumbs_separator

   To select a different separator for the breadcrumbs links, set:

   .. code-block:: python
      :caption: File: conf.py
      :emphasize-text: CHAR

      # The default separator is `/`
      html_theme_options = {"breadcrumbs_separator": "CHAR"}

   Replace :samp:`{CHAR}` with a character or HTML entity of your choice.

.. confval:: show_prev_next

   To show links to the previous and next pages, set this option to ``True``:

   .. code-block:: python
      :caption: File: conf.py

      # This option is `False` by default
      html_theme_options = {"show_prev_next": True}

.. confval:: show_scrolltop

   To show a button that scrolls to the top of the page when clicked,
   set this option to ``True``:

   .. code-block:: python
      :caption: File: conf.py

      # This option is `False` by default
      html_theme_options = {"show_scrolltop": True}

.. confval:: extra_header_links

   To add extra links to the header of your documentation, set the following option:

   .. code-block:: python
      :caption: File: conf.py

      # This option is `False` by default
      html_theme_options = {
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

   Set this option to ``True`` to make code references,
   such as classes or methods, collapsible.

   .. code-block:: python
      :caption: File: conf.py

      # This option is `False` by default
      html_collapsible_definitions = True


.. confval:: html_awesome_headerlinks

   By default, clicking a headerlink copies the URL to the clipboard.
   To restore Sphinx's default behavior, set this option to ``False``.

   .. code-block:: python
      :caption: File: conf.py

      # This option is `True` by default
      html_awesome_headerlinks = False

.. confval:: html_awesome_code_headers

   By default, the |product| shows the programming language of a code block in its header.
   To restore Sphinx's default, set this option to ``False``.

   .. code-block:: python
      :caption: File: conf.py

      # This option is `True` by default
      html_awesome_code_headers = False

.. confval:: html_awesome_docsearch

   Set this option to ``True`` to use `Algolia DocSearch <https://docsearch.algolia.com/>`_ instead of the built-in search.

   .. code-block:: python
      :caption: File: conf.py

      # This option is `False` by default
      html_awesome_docsearch = True

Configure Algolia DocSearch
---------------------------

Algolia DocSearch is a third-party service.
You need to `apply <https://docsearch.algolia.com/apply/>`_ and receive your credentials before you can use it.

To make DocSearch work with Sphinx,
you need to add your credentials to the Sphinx configuration,
or via environment variables.

Configure DocSearch via environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the following environment variables, either in your shell or continuous integration environment, or add them to a :file:`.env` file:

`DOCSEARCH_APP_ID`
   The id of your Algolia DocSearch application

`DOCSEARCH_API_KEY`
   The API key for searching your index on Algolia

`DOCSEARCH_INDEX_NAME`
   The name of your Algolia index for your documentation project

.. note::

   If you don't provide the app id, API key, or index name,
   your Sphinx project will still build.
   The DocSearch modal won't show any results and you might see errors in your browser's console.


You can change these **optional** settings:

`DOCSEARCH_INITIAL_QUERY`
   If you want to show initial results when the DocSearch modal opens

`DOCSEARCH_PLACEHOLDER`
   If you want to show a different placeholder (default: "Search docs")

`DOCSEARCH_SEARCH_PARAMETERS`
   If you want to add `search parameter <https://www.algolia.com/doc/api-reference/search-api-parameters/>`_

`DOCSEARCH_MISSING_RESULTS_URL`
   If you want to let users send you a message, or file a GitHub issue,
   when they can't find what they're looking for.
   You can use the current query in the URL. For example:

   .. code-block:: sh

      DOCSEARCH_MISSING_RESULTS_URL=https://github.com/example/docs/issues/new?title=${query}

   .. note::

      In the |product|, you have to provide the URL as a string.
      This deviates from the original DocSearch implementation,
      which accepts a function.

.. seealso::

   `DocSearch API reference <https://docsearch.algolia.com/docs/api/>`_.

Configure DocSearch in the Sphinx configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can configure DocSearch with the ``docsearch_config`` dictionary in your Sphinx configuration:

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
