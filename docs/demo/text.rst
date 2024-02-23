.. meta::
   :description: Textual elements like paragraphs and headings are essential parts of any documentation. Find out how they look like in this theme.
   :twitter:description: Textual elements like paragraphs and headings are essential parts of any documentation. Find out how they look like in this theme.

Headings and text
=================

.. rst-class:: lead

   See how basic text elements appear in the |product|.

----

The |product| includes styles for heading levels ``h1``, ``h2``, ``h3``, ``h4``,
as well as the special rubric heading.
Only heading levels ``h1``, ``h2``, and ``h3`` show up in the navigation sidebar.

Inline markup
-------------

To emphasize inline text, you can either *emphasize* it or make it a **strong**
statement.

.. centered:: For even more emphasis, you *could* use a ``centered`` directive.

Level 2 heading
---------------

.. vale Vale.Spelling = NO

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vehicula lectus est, ac
volutpat odio fringilla quis. Integer vitae molestie eros, ac eleifend nisi. Proin sit
amet odio non turpis mattis laoreet finibus vitae nisi. Nam vehicula sapien vel pulvinar
facilisis. Duis bibendum tortor sit amet sollicitudin gravida. Donec ut ante mattis,
faucibus nulla cursus, dictum dolor.

Code in a ``header`` is usually wrong
-------------------------------------

Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.

Level 3 heading
~~~~~~~~~~~~~~~

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vehicula lectus est, ac
volutpat odio fringilla quis. Integer vitae molestie eros, ac eleifend nisi. Proin sit
amet odio non turpis mattis laoreet finibus vitae nisi. Nam vehicula sapien vel pulvinar
facilisis. Duis bibendum tortor sit amet sollicitudin gravida. Donec ut ante mattis,
faucibus nulla cursus, dictum dolor.

Level 4 heading
+++++++++++++++

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam vehicula lectus est, ac
volutpat odio fringilla quis. Integer vitae molestie eros, ac eleifend nisi. Proin sit
amet odio non turpis mattis laoreet finibus vitae nisi. Nam vehicula sapien vel pulvinar
facilisis. Duis bibendum tortor sit amet sollicitudin gravida. Donec ut ante mattis,
faucibus nulla cursus, dictum dolor.

.. vale Vale.Spelling = YES

.. rubric:: Rubric heading

A :sphinxdocs:`rubric <usage/restructuredtext/directives.html#directive-rubric>`
is a special type of paragraph heading that doesn't appear in the table of contents.
You can generate it using the :samp:`.. rubric:: {TITLE}` directive.
It's rendered with the same styling as an ``h4`` heading.
