.. _sec:hide-right-sidebar:

Example: hide the right sidebar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extend the base templates to make custom layouts
that fit the existing theme.

For example, you can show or hide the *on-page* table of contents in the right sidebar.
To do this, update 2 templates:

- ``layout.html``: Update this template to extend the body to the full width.
- ``page.html``: Update this template to include the table of contents only when necessary.

#. :ref:`Add a templates folder to your docs <sec:add-custom-templates>`.
#. Create a new file :file:`_templates/layout.html` with this content:

   .. code-block:: html+django
      :caption: File: layout.html

      {%- extends "!layout.html" %}

      {{ super() }}

      {%- block main %}
      {%- if meta is defined and meta is not none and 'notoc' in meta %}
        <main class="relative py-6">
      {%- else %}
        <main class="relative py-6 lg:gap-10 lg:py-8 xl:grid xl:grid-cols-[1fr_300px]">
      {%- endif %}
      {%- block body %}{%- endblock %}
      </main>
      {%- endblock main %}

   This change applies different styles to the ``main`` element.
   The styles depend on the ``:notoc:`` field in the document.

#. Create a new file :file:`_templates/page.html` with this content:

   .. code-block:: html+django
      :caption: File: page.html

      {%- extends "!page.html" -%}

      {{ super() }}

      {%- block on_page_toc %}
      {%- if (meta is not defined or meta is none or "notoc" not in meta) and display_toc %}
      {%- include "toc.html" %}
      {%- endif %}
      {% endblock %}

   This change hides the sidebar if the document has a ``:notoc:`` field.

#. Add the ``:notoc:`` field to your documents.

   .. code-block:: reStructuredText

      :notoc: true

      ...

For an example, see :doc:`../../../demo/notoc`.
