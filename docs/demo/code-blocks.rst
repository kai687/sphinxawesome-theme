.. meta::
   :description: See how code blocks look like with this theme and discover the awesome enhancements.

.. role:: rst(code)
   :language: rst
   :class: highlight

Code blocks
===========

This page shows awesome features of code blocks.

.. contents:: On this page
   :local:
   :backlinks: none


Highlight code blocks with Sphinx' code-block directive
-------------------------------------------------------

In most cases, you should use Sphinx's :rst:`code-block` directive to mark up code
blocks. If you don't provide an explicit language to the directive, a fallback is used:

- You can set the default fallback language for highlighting on a per-document basis
  using the :rst:`highlight` directive. Any code block after this directive are
  highlighted using that language.

- You can set the global fallback language for highlighting in the Sphinx configuration
  file with the ``highlight_language`` option.

.. seealso::

   :sphinxdocs:`highlight directive <usage/restructuredtext/directives.html#directive-highlight>`
   :confval:`sphinx:highlight_language`

Explicit is better than implicit. Unless *all* code blocks in your documentation are
highlighted with the same language, always provide the highlighting language to the code
block directive.

For example:

.. code-block:: rst

   .. code-block:: python

      print("Hello World")

renders as:

.. code-block:: python

   print("Hello World")

All code blocks have a :guilabel:`Copy` button. Clicking the button copies
the code in the code block to the clipboard.

Sphinx's :rst:`code-block` directives have many options:

You can **add a caption** using the :samp:`:caption: {CAPTION_TEXT}` option:

.. code-block:: javascript
   :caption: Example code

   .log("Hello World")


To show **line numbers** in the code block, use the ``:linenos:`` option:

.. vale off

.. code-block:: python
   :linenos:

   for i in range(3):
      print(f"{i} line of code")

.. vale on

To emphasize specific lines in code blocks, use the
:samp:`:emphasize-lines: {LINE_NUMBERS}` option:

.. code-block:: bash
   :emphasize-lines: 2

   echo "Don't emphasize this"
   echo "Emphasize this"
   echo "Don't emphasize this either"

.. rubric:: Highlight code changes

Often, you want to highlight, which code needs to be changed. **The awesome theme
adds two additional options** to the :rst:`code-block` directive.

Use the :samp:`:emphasize-added: {LINE_NUMBERS}` option to highlight lines that
need to be added to the code.
Likewise, use the :samp:`:emphasize-removed: {LINE_NUMBERS}` option to highlight lines
that need to be removed.

.. code-block:: python
   :emphasize-removed: 1
   :emphasize-added: 2

   print("red")
   print("green")
   print("regular highlighting is applied")

The ``:emphasize-added:`` and ``:emphasize-removed:`` option allow the rest of the code
to be highlighted in another language. The ``+`` and ``-`` characters aren't copied with
the code.

If you don't want to use these option, you can use Pygments built-in ``diff`` format:

.. code-block:: diff

   + print("red")
   - print("green")
     print("no highlighting is applied here")

Note, how there's no additional syntax highlighting. If you copy the code to the
clipboard, the ``+`` and ``-`` characters are copied as well.

The following example is for testing the previous options with line numbers:

.. code-block:: python
   :linenos:
   :emphasize-removed: 2
   :emphasize-added: 3
   :emphasize-lines: 4

   print("One line of code")
   print("Removed line of code")
   print("Added line of code")
   print("Emphasized line of code")
   print("Normal line of code")

There is currently one visual bug with emphasizing lines `#171
<https://github.com/kai687/sphinxawesome-theme/issues/171>`_.

For example:

.. code-block::
   :caption: A really long line
   :emphasize-lines: 1

   print("A shorter line of code.")
   print("And a really long line of code that should overflow the container on most screen sizes which illustrates the issue.")

You can't include |rst| markup in code blocks, such as bold text or hyperlinks.

Docutils code directive
-----------------------

The :rst:`code-block` directive only works with Sphinx. If you want to re-use your
documentation outside Sphinx, for example, ``rst2html``, you can also use the
``code`` directive to mark up code blocks.

.. code:: shell

   echo "This is rendered with the docutils' code directive"


Parsed literal blocks
---------------------

If you want to write blocks of literal text containing any markup, such as bold text or
hyperlinks, use a :rst:`parsed-literal` directive.

.. parsed-literal::

   This *can* contain markup, but **not** syntax highlighting.

You can't use syntax highlighting with :rst:`parsed-literal` blocks.
