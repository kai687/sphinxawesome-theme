.. meta::
   :description: Learn how you can mark up inline code in Sphinx and see how it would look like on your website.

.. role:: rst(code)
   :language: rst
   :class: highlight

.. role:: python(code)
   :language: python
   :class: highlight

Inline code
===========

.. rst-class:: lead

   See how inline markup looks like in the |product|.


.. contents:: On this page
   :local:
   :backlinks: none

To mark up code in inline text, you can:

- Surround the code with two backtick characters.
- Use the :rst:`code` interpreted text role.

Syntax highlighting in inline code
----------------------------------

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

      This is necessary so that you can re-use the Pygments style sheet
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
   highlighting styles from Pygments---the same as for code blocks.

#. Use the new role to highlight inline code. For example:

   .. code-block:: rst

      :python:`print("Hello World")`

   This renders :python:`print("Hello World")`.


More interpreted text roles
---------------------------

Docutils and Sphinx come with many interpreted text roles to mark up specific elements.
While this can be useful to convey semantic intentions in the |rst| source files,
it's a good idea to use only a few different roles:

- The difference between the many roles are lost in the rendered output. Most of these
  roles are rendered like code (or bold).

- Using too many directives puts a burden on documentation writers, who may be more
  familiar with the Markdown format. They have to agree and remember when to use which
  role.

The awesome theme only provides styles for the following interpreted text roles.


Files and directories
~~~~~~~~~~~~~~~~~~~~~

You can designate files with the :rst:`file` role.

.. code-block:: rst

   :file:`Some file name`

This renders as :file:`Some filename`. You can highlight placeholder text in file and
directory names using the following syntax:

.. code-block:: rst

   :file:`/home/{USERNAME}/`

This renders as :file:`/home/{USERNAME}/`. If you want to distinguish directories from
file names, you can append a Slash (``/``) character to directory names.


Inline code with placeholder text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To highlight inline code with placeholder text, use the :rst:`samp` interpreted text
role:

.. code-block:: rst

   :samp:`Replace {PLACEHOLDER}`

This renders as :samp:`Replace {PLACEHOLDER}`.


Keyboard input
~~~~~~~~~~~~~~

You can highlight keyboard combinations using the :rst:`kbd` interpreted text role:

.. code-block:: rst

   :kbd:`Ctrl+F`

This renders as :kbd:`Ctrl+F`.

User interface elements
~~~~~~~~~~~~~~~~~~~~~~~

Graphical user interface elements are often rendered in a bold font.

Use the :rst:`guilabel` role to highlight user interface elements, such as buttons:

.. code-block:: rst

   :guilabel:`Help`

This renders as :guilabel:`Help`.

Use the :rst:`menuselection` role to document items in menus.

.. code-block:: rst

   :menuselection:`Start --> Program`

This renders as :menuselection:`Start --> Program`.
