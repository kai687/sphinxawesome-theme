.. meta::
   :description: Learn how you can mark up inline code in Sphinx and see how it would look like on your website.
   :twitter:description: Learn how you can mark up inline code in Sphinx and see how it would look like on your website.

.. role:: python(code)
   :language: python
   :class: highlight

Inline code
===========

.. rst-class:: lead

   See how inline markup looks like in the |product|.

To mark up code in inline text, you can:

- Surround the code with two backtick characters.
- Use the ``code`` interpreted text role.

If you want to see the styles for code blocks, see :doc:`code-blocks`.

Syntax highlighting in inline code
----------------------------------

By default, Sphinx doesn't highlight inline code.
To highlight inline code with Sphinx, follow these steps:

#. Create a docutils configuration file :file:`docutils.conf` in the same directory as the Sphinx configuration file :file:`conf.py`.

#. Add to the docutils configuration file :file:`docutils.conf`:

   .. code-block:: ini
      :caption: File: docutils.conf

      [restructuredtext parser]
      syntax_highlight = short

   .. note::

      This option makes Pygments use short class names for the highlighted code.
      This lets you re-use the same Pygments style sheet
      :file:`pygments.css` that Sphinx already uses for code blocks.

#. For each language you want to highlight,
   create a custom interpreted text role using docutils' ``role`` directive.

   For example, add this code to the beginning of an |rst| file:

   .. code-block:: rst

      .. role:: python(code)
        :language: python
        :class: highlight

   This lets you highlight inline Python code.
   Adding the ``highlight`` class lets you re-use the Pygments CSS styles that Sphinx already uses for code blocks.

#. Use the new role to highlight inline code. For example:

   .. code-block:: rst

      :python:`print("Hello World")`

   This renders :python:`print("Hello World")`.


More interpreted text roles
---------------------------

Docutils and Sphinx have many interpreted text roles.
They can be useful to convey precise semantic intentions in the |rst| source files.
On the other hand, it might be better to only use a few different roles:

- The difference between the many roles are lost in the rendered output.
  Most of these roles are rendered like code (or bold).

- Using too many directives puts a burden on documentation writers,
  who have to agree and remember when to use which role.

The |product| provides styles for the following interpreted text roles.

Files and directories
~~~~~~~~~~~~~~~~~~~~~

You can designate files with the ``file`` role.

.. code-block:: rst

   :file:`Some file name`

This renders as :file:`Some filename`.
You can highlight placeholder text in file and directory names using the following syntax:

.. code-block:: rst

   :file:`/home/{USERNAME}/`

This renders as :file:`/home/{USERNAME}/`.

.. tip::

   To distinguish directories from files, you can append a Slash (``/``) character to directory names.

Inline code with placeholder text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To highlight inline code with placeholder text,
use the ``samp`` interpreted text role:

.. code-block:: rst

   :samp:`Replace {PLACEHOLDER}`

This renders as :samp:`Replace {PLACEHOLDER}`.

Keyboard input
~~~~~~~~~~~~~~

Highlight keyboard shortcuts with the ``kbd`` interpreted text role:

.. code-block:: rst

   :kbd:`Ctrl+F`

This renders as :kbd:`Ctrl+F`.

User interface elements
~~~~~~~~~~~~~~~~~~~~~~~

Use the ``guilabel`` role to highlight user interface elements, such as buttons:

.. code-block:: rst

   :guilabel:`Help`

This renders as :guilabel:`Help`.

Use the ``menuselection`` role to document items in menus.

.. code-block:: rst

   :menuselection:`Start --> Program`

This renders as :menuselection:`Start --> Program`.
