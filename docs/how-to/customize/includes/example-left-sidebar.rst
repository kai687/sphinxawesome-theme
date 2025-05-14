.. _sec:left-sidebar-depth:

Example: Adjust the navigation depth in the left sidebar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the left sidebar facilitates navigation between pages.
The right sidebar supports navigation between sections on the same page.

If that's not what you want, you can increase the *depth* of the left sidebar.
To do this, override the template for the left sidebar.

#. :ref:`Add a templates folder to your docs <sec:add-custom-templates>`.
#. Create a new file :file:`_templates/sidebar_toc.html` with the following content:

   .. code-block:: html+django
      :caption: File: sidebar_toc.html

      <nav class="table w-full min-w-full my-6 lg:my-8">
        {{ toctree(collapse=false) }}
      </nav>

   The default template uses the ``titles_only`` option,
   which makes the sidebar only include page titles.
   If you omit this option, more headings are included.

   .. seealso::

      `toctree (templating) <https://www.sphinx-doc.org/en/master/development/html_themes/templating.html#toctree>`_
