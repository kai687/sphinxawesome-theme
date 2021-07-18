.. role:: rst(code)
   :language: rst
   :class: highlight

.. role:: python(code)
   :language: python
   :class: highlight

Code blocks and inline code
===========================

This page shows styles for inline markup related to code, as well as for the additional
features of code blocks.

.. contents:: On this page
   :local:
   :backlinks: none

Inline Code
-----------

You can mark up generic inline code using two backticks like this: ``inline code``.

Syntax highlighted inline code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to use syntax highlighting for inline code, such as this:
:python:`print("Hello World")`, perform these steps:

#. Create docutils configuration file :file:`docutils.conf`.

   Place this file in the same directory as the Sphinx configuration file
   :file:`conf.py`.

#. Make the syntax highlighter use *short* class names.

   Add this section to the file :file:`docutils.conf`:

   .. code-block:: ini
      :caption: docutils.conf

      [restructuredtext parser]
      syntax_highlight = short

   This creates "short" class names for syntax highlighting, the same as used by
   Sphinx's code blocks.

#. Define custom interpreted text roles using docutils :rst:`role` directive.

   For each language you want to highlight, create a custom interpreted text role. For
   example, to highlight inline Python code, add this to the beginning of the |rst|
   file:

   .. code-block:: rst

      .. role:: python(code)
        :language: python
        :class: highlight

   This adds the class ``highlight`` to the list of classes for the inline code, which
   automatically applies the same styles as for code blocks.

#. Use the new role to markup and highlight inline code.

   For example:

   .. code-block:: rst

      :python:`print("Hello World")`

   renders into :python:`print("Hello World")`.

.. note::

   Inline syntax highlighting is performed by the docutils module on which Sphinx is
   based. Sphinx doesn't provide or extend this feature, which means the user needs to
   perform these additional steps.

More interpreted text roles for code-like elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Docutils and Sphinx come with many interpreted text roles to mark up specific elements.
This theme only provides styles for a few of these roles.

Files can be marked up with the :rst:`file` interpreted text role.

.. code-block:: rst

   :file:`Some filename`

This is rendered as :file:`Some filename`.

You can highlight inline code with placeholders using the :rst:`samp` interpreted text
role.

.. code-block:: rst

   :samp:`Replace {PLACEHOLDER}`

This is rendered as :samp:`Replace {PLACEHOLDER}`. The same placeholder syntax can also
be used with the :rst:`file` role.

Keyboard shortcuts can be entered using the :rst:`kbd` interpreted text role.

.. code-block:: rst

   :kbd:`Ctrl+F`

This is rendered as :kbd:`Ctrl+F`.

Interpreted text roles for graphical user interface documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Graphical user interface elements are often rendered in a bold font, in contrast to the
monospace font for code elements.  Use the :rst:`guilabel` role to document buttons and
other user interface elements.

.. code-block:: rst

   :guilabel:`Help`

This renders as :guilabel:`Help`.

Use the :rst:`menuselection` role to document items in menus.

.. code-block:: rst

   :menuselection:`Start --> Program`

This renders as :menuselection:`Start --> Program`.

Awesome code blocks
-------------------

You can render code blocks using the :rst:`code-block` directive. If you don't specify
a language as an argument to the code block, the default highlighting language is used.

For example:

.. code-block:: python

   print("Hello World")

This uses the Python lexer of Pygments to apply syntax highlighting. Use the
:rst:`highlight` directive to set the default highlighting language on a per-document
basis. See `highlight directive
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-highlight>`_
for more information. Use the :rst:`highlight_language` configuration setting to set
the default highlighting language for the whole project. See `highlight_language
<https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-highlight_language>`_
for more information.

All code blocks have a header section with a :guilabel:`Copy` button.
Clicking the button copies the text inside the code block to the clipboard.
The header also contains a label for the highlighting language as well as
the caption.

.. vale off

.. caution::

   For interactive shell sessions, Pygments provides the ``shell-session`` lexer, with
   an alias of ``console``. The former is too long and the latter to old-fashioned for
   my taste.

   This theme replaces the label ``console`` with the label ``shell`` in the header
   section of code blocks. Unfortunately, ``shell`` is also an alias for shell scripts.
   As shell scripts are likely to be specific to a certain type of shell, I recommend
   being more specific, such as using ``sh``, ``bash``, or ``zsh``.

   If no highlighting language is defined, Sphinx uses ``default``. This is translated
   to *interactive python session*. This theme replaces ``default`` with ``python`` in
   the header section.

.. vale on

The following example shows a code block for JavaScript with a caption.

.. code-block:: javascript
   :caption: Example code

   console.log("Hello World")

Use the ``linenos`` option to show line numbers in the code block.

.. vale off
.. code-block:: python
   :linenos:

   for i in range(3):
      print(f"{i} line of code")

.. vale on

To emphasize specific lines in code blocks, use the ``:emphasize-lines:`` option:

.. code-block:: bash
   :emphasize-lines: 2

   echo "Don't emphasize this"
   echo "Emphasize this"
   echo "Don't emphasize this either"

Likewise, you can emphasize code changes using the ``:emphasize-added:`` and
``:emphasize-removed:`` options.

.. code-block:: python
   :emphasize-removed: 1
   :emphasize-added: 2

   print("red")
   print("green")
   print("regular highlighting is applied")

Note, how the lines are still highlighted using Python syntax. Copy the code and note,
how the ``+`` and ``-`` characters aren't copied.

.. note::

   The ``:emphasize-added:`` and ``:emphasize-removed:`` options only work in this
   theme. If you later change the theme, leaving these options generate a warning and
   skip rendering all code blocks with these options. I recommend using ``sphinx-build
   -W`` to turn warnings into errors.

A portable, built-in alternative is to use Pygments' ``diff`` lexer.

.. code-block:: diff

   + print("red")
   - print("green")
     print("no highlighting is applied here")

This works with all themes, but doesn't highlight the other lines in the code block.
When selecting the code to copy to the clipboard, the ``+`` and ``-`` characters at the
beginning are copied as well.

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
   :caption: Really long line
   :emphasize-lines: 1

   print("A shorter line of code.")
   print("And a really long line of code that should overflow the container on most screen sizes which illustrates the issue.")


Code blocks can't contain any markup, such as bold text or hyperlinks.

Parsed literal blocks
---------------------

If you want to write blocks of literal text containing any markup, such as bold text or
hyperlinks, use a :rst:`parsed-literal` directive.

.. parsed-literal::

   This *can* contain markup, but **not** syntax highlighting.

You can't use syntax highlighting with :rst:`parsed-literal` blocks.

Samp directive
--------------

If you want to highlight placeholder variables, and you can accept only minimal
highlighting, you can use the :rst:`samp` directive.

For example:

.. code-block:: rst
   :caption: samp directive

   .. samp::

      $ echo "Enter {PLACEHOLDER}"

is rendered as:

.. samp::

   $ echo "Enter {PLACEHOLDER}"

.. note::

   The Sphinx awesome theme provides a style for the directive that integrates well with
   the rest of the theme. The parsing is handled by a separate extension
   `sphinxawesome-sampdirective
   <https://github.com/kai687/sphinxawesome-sampdirective>`_. This extension is
   automatically installed and loaded, if the Sphinx awesome theme is installed as a
   Python package. See :ref:`How to install the theme` for more information.

   You can install and activate the extension separately for using with other themes.
