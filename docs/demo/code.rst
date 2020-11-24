.. role:: rst(code)
   :language: rst

Code blocks and inline code
===========================

This theme adds a :guilabel:`Copy` button to all code blocks. Clicking on the button copies
the text inside the code block to the clipboard.

To mark up code blocks, choose between :rst:`parsed-literal`, :rst:`samp`, or
:rst:`code-block` directives, depending on your needs.

In summary:

- Use :rst:`parsed-literal` directives, if you need to render reStructuredText markup
  inside the code block, but don't need syntax highlighting.
- Use :rst:`samp` directives, if you need to highlight placeholder variables, but
  otherwise don't need markup or syntax highlighting.
- Use :rst:`code-block` directives, if you want advanced features like syntax
  highlighting, captions, line numbers, etc. but don't want to render any markup.

.. note::

   It's currently not possible to have both syntax highlighting *and* markup rendering
   for code blocks in Sphinx.


Parsed literal
--------------

Use a :rst:`parsed-literal` directive, when you want to render markup inside a code
block, for example links or emphasized texts. :rst:`parsed-literal` blocks don't have
syntax highlighting.

.. parsed-literal::

   Parsed literal blocks *can* contain reStructuredText!
   But they **don't** have syntax highlighting

Samp directive
--------------

To highlight placeholder variables in inline code snippets,
Sphinx provides the :rst:`samp` interpreted text role by default.
The `sphinxawesome-sampdirective <https://github.com/kai687/sphinxawesome-sampdirective>`_
extension provides the missing :rst:`samp` directive
for highlighting placeholder variables in code blocks.
The sphinx awesome theme includes this extension by default.

Placeholder variables are variables that users are expected to substitute. For example,
:rst:`:samp:echo "Hello {NAME}"` is rendered as :samp:`echo "Hello {NAME}"`.

The :rst:`samp` directive:

.. code-block:: rst

   .. samp::

      $ echo "Hello {NAME}"

is rendered as:

.. samp::

   $ echo "Hello {NAME}"


Code blocks with syntax highlighting
------------------------------------

Code block directives on the other hand can include syntax highlighting (and captions, and `other
features
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block>`_)
but markup isn't rendered.

.. code-block:: python
   :emphasize-lines: 2
   :caption: Code block caption.

   print("Don't highlight this")
   print("But this!")
   print("And this is unimportant again")


A code block can also have line numbers. You can highlight specific lines with the
``:emphasize-lines:`` option. You can also highlight changes in code using the
``:emphasize-added:`` and ``:emphasize-removed:`` options.

.. code-block:: python
   :emphasize-lines: 2
   :emphasize-removed: 4
   :emphasize-added: 5
   :linenos:
   :caption: Code block caption.

   print("Don't highlight this")
   print("But this!")
   print("And this is unimportant again.")
   print("Change this line")
   print("To this line.")
