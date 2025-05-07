.. meta::
   :description: See how code blocks look like in your Sphinx project with the Awesome Theme and learn about the supported options.
   :twitter:description: See how code blocks look like in your Sphinx project with the Awesome Theme and learn about the supported options.

Code blocks
===========

.. rst-class:: lead

   See how code blocks look like in your Sphinx project with the |product| and learn about the supported options.

To check the styles for inline markup looks like, see :doc:`inline-code`.

Sphinx code-block directive
---------------------------

To document code blocks with syntax highlighting,
use Sphinx's ``code-block`` directive.

You can provide the language used for syntax highlighting as an argument to the ``code-block`` directive:

.. code-block:: rst

   .. code-block:: python

      print("Hello World")

This renders as:

.. code-block:: python

   print("Hello World")

If you don't provide a language to the directive,
Sphinx uses a fallback:

#. If you used the ``highlight`` directive to set a default language for the **current document**,
   any code block *after* this directive is highlighted with the language you specified.

#. If you set the global fallback language for highlighting in the Sphinx configuration
   file with the ``highlight_language`` option, this language is used as default.

.. seealso::

   :sphinxdocs:`Showing code examples <usage/restructuredtext/directives.html#showing-code-examples>`
   :sphinxdocs:`highlight directive <usage/restructuredtext/directives.html#directive-highlight>`
   :confval:`sphinx:highlight_language`

.. tip::

   It's usually better to be explicit.
   It makes your documentation more portable if you want to copy or re-use your documentation files elsewhere.
   It's also easier to follow for contributors who may not be as familiar with Sphinx and restructuredtext.

**Feature:**
The |product| adds a :guilabel:`Copy` button to every code block,
so that your users can easily copy your code.

Add captions to code blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add captions to code blocks with the :samp:`:caption: {CAPTION_TEXT}` option:

.. code-block:: javascript
   :caption: Example code

   console.log("Hello World")

Adding a caption also adds a link target to the code block.
Hover over a caption to see the headerlink icon.


Show line numbers in code blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Show line numbers in code blocks with the ``:linenos:`` option:

.. code-block:: python
   :linenos:

   for i in range(3):
      print(f"{i} line of code")

Highlight lines in code blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To highlight specific lines in code blocks,
use the :samp:`:emphasize-lines: {LINE_NUMBERS}` option:

.. code-block:: bash
   :emphasize-lines: 2

   echo "Don't emphasize this"
   echo "Emphasize this"
   echo "Don't emphasize this either"

Highlight changes in code blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Feature:**
The |product| adds two new options to the ``code-block`` directive
for highlighting added or removed lines of code:

``:emphasize-added:``
   Highlight added lines with :samp:`:emphasize-added: {LINE_NUMBERS}`.

``:emphasize-removed:``
   Highlight removed lines with :samp:`:emphasize-added: {LINE_NUMBERS}`.

.. code-block:: rst

   .. code-block:: python
      :emphasize-removed: 1
      :emphasize-added: 2

      print("red")
      print("green")
      print("regular highlighting is applied")

This example highlights the first line in red,
and the second line in green:

.. code-block:: python
   :emphasize-removed: 1
   :emphasize-added: 2

   print("red")
   print("green")
   print("regular highlighting is applied")

The ``:emphasize-added:`` and ``:emphasize-removed:`` options preserve the syntax highlighting.
If you copy the code, the ``+`` and ``-`` characters aren't copied.

If you don't want to use these options,
you can use Pygments' built-in ``diff`` language:

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

Highlighting short lines doesn't work well if you also have long, overflowing lines:

.. code-block::
   :caption: A really long line
   :emphasize-lines: 1

   print("A shorter line of code.")
   print("And a really long line of code that should overflow the container on most screen sizes which illustrates the issue.")

You can't include markup in code blocks, such as bold text or hyperlinks.

Highlight placeholders in code blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Feature:**
The |product| adds an ``:emphasize-text:`` option to the ``code-block`` directive
for highlighting placeholder text in code blocks:

.. code-block:: rst

   .. code-block:: python
      :emphasize-text: WORLD

      print("Hello WORLD")

This renders as:

.. code-block:: python
   :emphasize-text: WORLD

   print("Hello WORLD")

Naturally, this should also work in combination with captions:

.. code-block:: python
   :caption: Caption text
   :emphasize-text: WORLD
   :emphasize-added: 2
   :emphasize-removed: 3

   print("Hello WORLD")
   print("Added line")
   print("Removed line")

.. note::
   Separate multiple placeholders by space, not by comma.
   For example, `:emphasize-text: WORD1 WORD2` highlights both WORD1 and WORD2.


Docutils code directive
-----------------------

The ``code-block`` directive only works with Sphinx.
If you want to re-use your |rst| documentation outside Sphinx,
you can also use the ``code`` directive:


.. code-block:: rst

   .. code:: bash

      echo "This is rendered with the docutils' code directive"

This renders:

.. code:: bash

   echo "This is rendered with the docutils' code directive"

You can't use captions, highlighted lines, or any of the other options for Sphinx code
blocks.

.. seealso::

   `Code directive (docutils) <https://docutils.sourceforge.io/docs/ref/rst/directives.html#code>`_

Parsed literal blocks
---------------------

Parsed literal blocks can contain **either** markup **or** syntax.
If you add markup, such as bold text or hyperlinks, syntax highlighting is turned off.

For example:

.. code-block:: rst

   .. parsed-literal::

      This *can* contain markup, but **not** syntax highlighting.
      How about a `link <https://example.org>`_?

This renders as:

.. |feature| replace:: markup

.. parsed-literal::

   This *can* contain |feature|, but **not** syntax highlighting.
   How about a `link <https://example.org>`_?


If you don't include any markup, the content is rendered with syntax highlighting.

.. parsed-literal::

   print("Hello world")

.. seealso::

   `Parsed-literal directive (docutils) <https://docutils.sourceforge.io/docs/ref/rst/directives.html#code>`_

Prompt characters
-----------------

Prompt characters shouldn't be selected when copying code.

For example, if you copy the code from the following ``console`` code block,
the ``$`` character should not be copied:

.. code-block:: console

   $ echo "Prompt characters not selected"

The same is true for Python interactive sessions:

.. code-block:: pycon

   >>> print("Prompt characters not selected.")

Output should also not be selected when copying:

.. code-block:: python

   >>> api.execute(circuit=c)
   [1168]
