Extend template blocks
~~~~~~~~~~~~~~~~~~~~~~

To add code, you can :ref:`extend the page template <sec:extend-templates>` and override the template blocks:

``extrahead``
   Adds your template code before the closing ``</head>`` tag.
   This is useful to add custom styles or JavaScript code.

``body_before``
   Adds content to the top of the page.

``body_after``
   Adds content to the bottom of the page.

.. code-block:: html+jinja
   :caption: File: page.html

   {% extends "!page.html" %}

   {{ super() }}

   {% block extrahead %}
   {# Included before the closing </head> tag #}
   {% endblock %}

   {% block extrabody %}
   {# Included after the main content, before the <footer> #}
   {% endblock %}

.. _sec:hide-right-sidebar:

Example: hide the right sidebar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Extending the base templates is a powerful technique to achieve custom layouts
that integrate well with the existing theme.

For example, you can change the layout to conditionally show or hide the *on-page* table of contents in the right sidebar.
To achieve this, you need to update 2 templates:

- ``layout.html``. You need to update this template to extend the body to the full width.
- ``page.html``. You need to update this template to conditionally include the table of contents.

#. :ref:`Add a templates folder to your docs <sec:add-custom-templates>`.
#. Create a new file :file:`_templates/layout.html` with the following content:

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

   This change leads to different styles being applied to the ``main`` element,
   depending on whether the document has a ``:notoc:`` field or not.

#. Create a new file :file:`_templates/page.html` with the following content:

   .. code-block:: html+django
      :caption: File: page.html

      {%- extends "!page.html" -%}

      {{ super() }}

      {%- block on_page_toc %}
      {%- if (meta is not defined or meta is none or "notoc" not in meta) and display_toc %}
      {%- include "toc.html" %}
      {%- endif %}
      {% endblock %}

   This change hides the sidebar if the document has a ``:notoc:`` option.

#. Include the ``:notoc:`` option in your documents.

   .. code-block:: reStructuredText

      :notoc: true

      ...

For an example, see :doc:`../../../demo/notoc`.
