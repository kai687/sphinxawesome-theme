.. role:: rst(code)
   :language: rst

=========================
Code, figures, and tables
=========================

----
Code
----

This theme adds a :guilabel:`Copy` button to code blocks. Clicking on the button will
copy the text inside the code block to the clipboard.

Use a :rst:`parsed-literal` directive, when you want to render markup inside a code
block, for example links or emphasized texts. :rst:`parsed-literal` blocks do not have
syntax highlighting.

.. parsed-literal::

   Parsed literal blocks *can* contain reStructuredText!
   But they **don't** have syntax highlighting

Code blocks on the other hand can include syntax highlighting (and captions, and
`other features
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block>`_)
but markup will not be rendered.

.. code-block:: python
   :emphasize-lines: 2
   :caption: Code block caption.

   print("Don't highlight this")
   print("But this!")
   print("And this is unimportant again")


A code block can also have line numbers.

.. code-block:: python
   :emphasize-lines: 2
   :linenos:
   :caption: Code block caption.

   print("Don't highlight this")
   print("But this!")
   print("And this is unimportant again")


This theme implements a `samp` directive, which allows you to define placeholders that a
user should replace. This is similar to the :samp:`enter {SANDMAN}` role.

.. samp::

   $ Enter {SANDMAN}


-------
Figures
-------

.. figure:: image.svg
   :alt: A grey placeholder image

   This is an image caption.

   And you can also provide a legend to the figure that contains more information about
   the image.

------
Tables
------

This is a small table.

.. table:: Table caption
   :width: 66%

   ==========  ==========
   table head  table head
   ==========  ==========
   column      column
   column      column
   column      column
   ==========  ==========
