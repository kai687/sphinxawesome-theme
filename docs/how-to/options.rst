.. meta::
   :description: Configure the |product| by changing options in your Sphinx configuration file.

.. _sec:configure:

Configure the theme
===================

.. rst-class:: lead

   Configure the |product| by changing one of its options.

.. contents:: On this page
   :local:
   :backlinks: none

.. admonition:: What's the difference between theme and extension options?

   It's a technical distinction due to the way Sphinx builds a project.

   - **Theme options** are defined in the HTML templates.
     They control layout and styling aspects.
   - **Extension options** are defined in the Python code of the extensions.
     They can control more aspects, for example, running extra code.

.. _sec:theme_options:

Theme options
-------------

You can configure the theme by modifying the ``html_theme_options`` dictionary in the Sphinx configuration file :file:`conf.py`.

.. confval:: nav_include_hidden

   If you don't want to include entries from a _hidden_
   :sphinxdocs:`toctree <usage/restructuredtext/directives.html#directive-toctree>`
   directive in the sidebar,
   set ``nav_include_hidden`` to ``False``.

   .. code-block:: python
      :caption: "File: conf.py"

      # This option is `True` by default
      html_theme_options = {"nav_include_hidden": False}

   By default,
   the ``toctree`` directive includes your content _and_ generates a list of links in the content area of the page.
   With the ``hidden`` option, the content is still included,
   but no links are printed in the main content area.

.. confval:: show_nav

   The |product| shows links to all your documentation pages in sidebar on the left side.
   If you want to hide the sidebar on all pages, set this option to `False`:

   .. code-block:: python
      :caption: "File: conf.py"

      # This option is `True` by default
      html_theme_options = {"show_nav": False}


.. confval:: show_breadcrumbs

   The |product| shows `breadcrumbs <https://en.wikipedia.org/wiki/Breadcrumb_navigation>`_ links at the top of each page
   To hide the breadcrumbs, set this option to ``False``:

   .. code-block:: python
      :caption: "File: conf.py"

      # This option is `True` by default
      html_theme_options = {"show_breadcrumbs": False}

.. confval:: breadcrumbs_separator

   To select a different separator for the breadcrumbs navigation links,
   set:

   .. code-block:: python
      :caption: "File: conf.py"
      :emphasize-text: CHAR

      # The default separator is `/`
      html_theme_options = {"breadcrumbs_separator": "CHAR"}

   Replace :samp:`{CHAR}` with a character or HTML entity of your choice.

.. confval:: show_prev_next

   To show links to the previous and next pages, set this option to ``True``:

   .. code-block:: python
      :caption: "File: conf.py"

      # This option is `False` by default
      html_theme_options = {"show_prev_next": True}

.. confval:: show_scrolltop

   To show a button that scrolls to the top of the page when clicked,
   set this option to ``True``:

   .. code-block:: python
      :caption: "File: conf.py"

      # This option is `False` by default
      html_theme_options = {"show_scrolltop": True}

.. confval:: extra_header_links

   To add extra links to the header of your documentation, set the following option:

   .. code-block:: python
      :caption: "File: conf.py"

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

   Extension options are only available
   if you add the theme to the list of extensions
   in your Sphinx configuration:
   ``extensions = ["sphinxawesome_theme"]``

The |product| enables several internal extensions that enhance the user experience.
The following configuration values are set at the top level in the Sphinx
configuration file ``conf.py``:

.. confval:: html_collapsible_definitions

   Set this option to ``True`` to make code references,
   such as classes, methods, and other objects,
   collapsible and expandable.

   .. code-block:: python
      :caption: "File: conf.py"

      # This option is `False` by default
      html_collapsible_definitions = True


.. confval:: html_awesome_headerlinks

   Set this option to ``False`` to restore Sphinx's default behavior for headerlinks.
   In the |product|, clicking a headerlink copies the URL to the clipboard.

   .. code-block:: python
      :caption: "File: conf.py"

      # This option is `True` by default
      html_awesome_headerlinks = False

.. confval:: html_awesome_code_headers

   By default, the |product| shows the programming language of a code block in its header.
   If you don't want to show the programming language, set this option to ``False``.

   .. code-block:: python
      :caption: "File: conf.py"

      # This option is `True` by default
      html_awesome_code_headers = False

.. confval:: html_awesome_docsearch

   Set this option to ``True`` to use [Algolia DocSearch](https://docsearch.algolia.com/) instead of the built-in search.

   .. code-block:: python
      :caption: "File: conf.py"

      # This option is `False` by default
      html_awesome_docsearch = True

   To configure DocSearch, you can the configuration options as environment variables,
   or you can add them to the ``docsearch_config`` dictionary in your Sphinx configuration file :file:`conf.py`.

   .. rubric:: Configure DocSearch via environment variables

   Add the following environment variables, either on the command line, or as a :file:`.env` file:

   `DOCSEARCH_APP_ID`
      The id of your Algolia app

   `DOCSEARCH_API_KEY`
      The API key for searching your index on Algolia

   `DOCSEARCH_INDEX_NAME`
      The name of your Algolia index for your documentation project.

   .. rubric:: Configure DocSearch in the Sphinx configuration file

   Add the following to the ``docsearch_config`` dictionary in your Sphinx configuration file :file:`conf.py`.

   .. code-block:: python
      :caption: "File: conf.py"

      docsearch_config = {
        app_id: "",
        api_key: "",
        index_name: ""
      }

   .. note::

      Algolia DocSearch is an external web service.
      You need to apply and receive your credentials before you can use it.
