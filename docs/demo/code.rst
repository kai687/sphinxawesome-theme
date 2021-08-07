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

Syntax highlighting in inline code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, Sphinx doesn't highlight inline code. With the following extra steps,
you can enable it.

#. Create a docutils configuration file :file:`docutils.conf` in the same directory as
   the Sphinx configuration file :file:`conf.py`.

#. Add to the docutils configuration file :file:`docutils.conf`:

   .. code-block:: ini
      :caption: File: docutils.conf

      [restructuredtext parser]
      syntax_highlight = short

   This makes ``docutils`` use short class names for syntax highlighting, the same
   setting as Sphinx uses to highlight code blocks.

   .. note::

      This is necessary so that you can re-use the Pygments stylesheet
      :file:`pygments.css` that Sphinx already uses for code blocks.

#. For each language you want to highlight, create a custom interpreted text role using
   docutils' :rst:`role` directive.

   For example, to highlight inline Python code, add the following code to the beginning
   of the |rst| file, in which you want to use the highlighting:

   .. code-block:: rst

      .. role:: python(code)
        :language: python
        :class: highlight


   This renders a ``code`` element with a class of ``highlight``, which uses the
   highlighting styles from Pygment---the same as for code blocks.

#. Use the new role to highlight inline code. For example:

   .. code-block:: rst

      :python:`print("Hello World")`

   renders :python:`print("Hello World")`.


Interpreted text roles for code-like elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Docutils and Sphinx come with many interpreted text roles to mark up specific elements.
While this can be useful to convey semantic intentions in the |rst| source files,
it's a good idea to use only a few different roles:

- The difference between the many roles are lost in the rendered output. Most of these
  roles are rendered in code font, and most users don't read the |rst| sources.

- Using too many directives puts a burden on documentation writers, who may be more
  familiar with the Markdown format. They have to agree and remember when to use which
  role.

The awesome theme only provides styles for the following interpreted text roles.

.. rubric:: Files and directories

You can designate files with the :rst:`file` role.

.. code-block:: rst

   :file:`Some file name`

This renders as :file:`Some filename`. You can highlight placeholder text in file and
directory names using the following syntax:

.. code-block:: rst

   :file:`/home/{USERNAME}/`

This renders as :file:`/home/{USERNAME}/`. If you want to distinguish directories from
file names, you can append a Slash (``/``) character to directory names.


.. rubric:: Inline code with placeholder text

To highlight inline code with placeholder text, use the :rst:`samp` interpreted text
role:

.. code-block:: rst

   :samp:`Replace {PLACEHOLDER}`

This renders as :samp:`Replace {PLACEHOLDER}`.

.. rubric:: Keyboard input

You can highlight key combinations using the :rst:`kbd` interpreted text role:

.. code-block:: rst

   :kbd:`Ctrl+F`

This renders as :kbd:`Ctrl+F`.

Interpreted text roles for graphical user interface documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Graphical user interface elements are often rendered in a bold font, in contrast to the
monospace font for code elements.

Use the :rst:`guilabel` role to highlight user interface elements, such as buttons:

.. code-block:: rst

   :guilabel:`Help`

This renders as :guilabel:`Help`.

Use the :rst:`menuselection` role to document items in menus.

.. code-block:: rst

   :menuselection:`Start --> Program`

This renders as :menuselection:`Start --> Program`.


Code blocks
-----------

Sphinx and docutils come with several different methods to render code blocks. In most
cases, you should use Sphinx's :rst:`code-block` directive to mark up code blocks.
If you don't provide an explicit language to the directive, a fallback is used:

- You can set the default fallback language for highlighting on a per-document basis
  using the :rst:`highlight` directive. Any code block after this directive will be
  highlighted using that language.

- You can set the global fallback language for highlighting in the Sphinx configuration
  file with the ``highlight_language`` option.

.. seealso::

   `highlight directive <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-highlight>`_,
   `highlight_language <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-highlight_language>`_

It's best to be explicit, unless it's very clear that *all* code blocks in your documentation
are highlighted with the same language.

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
~~~~~~~~~~~~~~~~~~~~~~~

The :rst:`code-block` directive only works with Sphinx. If you want to re-use your
documentation also with other renderers, for example, ``rst2html``, you can also use the
``code`` directive to mark up code blocks.

.. code:: shell

   echo "This is rendered with the docutils' code directive"

Highlight placeholder text in code blocks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To highlight placeholder text in code blocks, you can add the
:samp:`emphasize-text: {PLACEHOLDER}` option.

For example:

.. code-block:: rst
   :caption: Placeholder text

   .. code-block::
      :emphasize-text: PLACEHOLDER

      echo "Enter PLACEHOLDER

is rendered as:

.. code-block:: shell
   :emphasize-text: PLACEHOLDER

   echo "Enter PLACEHOLDER"


Parsed literal blocks
---------------------

If you want to write blocks of literal text containing any markup, such as bold text or
hyperlinks, use a :rst:`parsed-literal` directive.

.. parsed-literal::

   This *can* contain markup, but **not** syntax highlighting.

You can't use syntax highlighting with :rst:`parsed-literal` blocks.
