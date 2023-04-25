.. meta::
   :description: See how code blocks look like with the Awesome Theme and discover the awesome enhancements.

.. role:: rst(code)
   :language: rst
   :class: highlight

Code blocks
===========

.. rst-class:: lead

   See how code blocks look like with the |product|.

.. include:: ../includes/header.rst


Sphinx code-block directive
---------------------------

To document code blocks with syntax highlighting,
use Sphinx's :rst:`code-block` directive.

You can provide the language used for syntax highlighting to the :rst:`code-block` directive:

.. code-block:: rst

   .. code-block:: python

      print("Hello World")

This renders as:

.. code-block:: python

   print("Hello World")

All code blocks have a :guilabel:`Copy` button.
Clicking the button copies the code to the clipboard.

If you don't provide an explicit language to the directive, a fallback is used:

#. If you used the :rst:`highlight` directive to set a default language on a per-document basis,
   any code block *after* this directive is highlighted with the language you specified.

#. If you set the global fallback language for highlighting in the Sphinx configuration
   file with the ``highlight_language`` option, this language is used as default.

.. seealso::

   :sphinxdocs:`highlight directive <usage/restructuredtext/directives.html#directive-highlight>`
   :confval:`sphinx:highlight_language`

Add captions to code blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add captions to code blocks with the :samp:`:caption: {CAPTION_TEXT}` option:

.. code-block:: javascript
   :caption: Example code

   console.log("Hello World")


Show line numbers in code blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Show line numbers in code blocks with the ``:linenos:`` option:

.. vale off

.. code-block:: python
   :linenos:

   for i in range(3):
      print(f"{i} line of code")

.. vale on


Highlight lines in code blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To emphasize specific lines in code blocks, use the
:samp:`:emphasize-lines: {LINE_NUMBERS}` option:

.. code-block:: bash
   :emphasize-lines: 2

   echo "Don't emphasize this"
   echo "Emphasize this"
   echo "Don't emphasize this either"

Highlight changes in code blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often, you want to highlight what code need to be changed.
With the |product|, you can use the following options for the :rst:`code-block`
directive:

- To highlight lines, that need to be added,
  use :samp:`:emphasize-added: {LINE_NUMBERS}`.

- To highlight lines that need to be removed,
  use :samp:`:emphasize-removed: {LINE_NUMBERS}`.

.. code-block:: python
   :emphasize-removed: 1
   :emphasize-added: 2

   print("red")
   print("green")
   print("regular highlighting is applied")

The ``:emphasize-added:`` and ``:emphasize-removed:`` options preserve the highlighting
of the code. If you copy the code, the ``+`` and ``-`` characters aren't copied.

If you don't want to use these options, you can use Pygments built-in ``diff`` language:

.. code-block:: diff

   + print("red")
   - print("green")
     print("no highlighting is applied here")

Here, the syntax isn't highlighted.
If you copy the code to the clipboard,
the ``+`` and ``-`` characters are copied as well.

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
<https://github.com/kai687/sphinxawesome-theme/issues/171>`_:

.. code-block::
   :caption: A really long line
   :emphasize-lines: 1

   print("A shorter line of code.")
   print("And a really long line of code that should overflow the container on most screen sizes which illustrates the issue.")

You can't include |rst| markup in code blocks, such as bold text or hyperlinks.

Highlight placeholders in code blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to highlight placeholder text in code blocks,
use the ``:emphasize-text:`` option.

.. code-block:: rst

   .. code-block:: python
      :emphasize-text: WORLD

      print("Hello WORLD")

This renders as:

.. code-block:: python
   :emphasize-text: WORLD

   print("Hello WORLD")


Docutils code directive
-----------------------

The :rst:`code-block` directive only works with Sphinx.
If you want to re-use your |rst| documentation outside Sphinx,
you can also use the ``code`` directive:

.. code:: shell

   echo "This is rendered with the docutils' code directive"

You can't use captions, highlighted lines, or any of the other options for Sphinx code
blocks.

Parsed literal blocks
---------------------

Parsed literal blocks can contain **either** markup **or** syntax.
If you add markup, such as bold text or hyperlinks, syntax highlighting is turned off.

.. parsed-literal::

   This *can* contain markup, but **not** syntax highlighting.


If you don't include any markup, the content is rendered with syntax highlighting.

.. parsed-literal::

   print("Hello world")
