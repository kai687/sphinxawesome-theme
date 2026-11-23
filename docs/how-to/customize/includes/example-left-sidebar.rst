.. _sec:left-sidebar-depth:

Example: Adjust the navigation depth in the left sidebar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the left sidebar helps you navigate between pages.
The right sidebar helps you navigate between sections on the same page.

To change this, increase the *depth* of the left sidebar.
To do this, override the template for the left sidebar.

#. :ref:`Add a templates folder to your docs <sec:add-custom-templates>`.
#. Create a new file :file:`_templates/sidebar_toc.html` with this content:

   .. code-block:: html+django
      :caption: File: sidebar_toc.html

      <nav class="table w-full min-w-full my-6 lg:my-8">
        {{ toctree(collapse=false) }}
      </nav>

   The default template uses the ``titles_only`` option.
   This option makes the sidebar show only page titles.
   If you omit this option, the sidebar shows more headings.

   .. seealso::

      `toctree (templating) <https://www.sphinx-doc.org/en/master/development/html_themes/templating.html#toctree>`_
