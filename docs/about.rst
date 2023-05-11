:orphan: true

.. vale off

.. meta::
   :description: Miscellaneous information about the Awesome Theme

About
=====

.. rst-class:: lead

   Miscellaneous. This should probably be a blog.

----

I started this project because I wanted to use Sphinx for a documentation project at my job,
but I found all available themes ugly and outdated.
Had I known of the `furo <https://pradyunsg.me/furo/>`_ or
the `sphinx-books-theme <https://sphinx-book-theme.readthedocs.io/en/stable/>`_,
I likely would not have started this project.

Thanks to this project I learned a lot about the inner workings of Sphinx and about building and hosting a website.

About version 5
---------------

Version 5 is a complete rewrite that fundamentally changes the look and feel of the theme.
I wanted to correct a few things that I came to dislike in versions 3 and 4.
I wanted to have a clear separation between on-page navigation links and links to other pages,
the classic three-column layout.
This was difficult to achieve within the existing structure,
so that I gave up on that.

On the Python side, I wanted to get rid of as much code as possible,
while still achieving my goals of improving the user experience.
In version 3, I heavily customized the HTML rendering.
Unfortunately, some methods in Sphinx and Docutils aren't meant to be extended,
so I ended up copying a lot of code---sometimes to change just a single line.

For the design, I wanted to have dark mode and an easy way to customize the look of the page,
without having to redefine everything.
Enter `shadcn/ui <https://ui.shadcn.com/>`_,
which is a set of UI components that uses Tailwind for styling.
While the components are meant to be used in React,
the design can easily be ported, such as plain HTML/CSS as demonstrated by this website.
Dark mode is difficult to make good,
but even more challenging to add to an existing design.

All in all lead to the rather big changes between version 4 and 5.
Rather than creating and maintaining a separate project,
I decided to realize my vision within a single project.

Assets
------

The following table lists the assets used by the |product| to be awesome.

+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
| Feature                                                 | Name/Website                  | License                                                                           |
+=========================================================+===============================+===================================================================================+
| CSS framework                                           | Tailwind_                     | `MIT License <https://github.com/tailwindlabs/tailwindcss/blob/master/LICENSE>`__ |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
| Copy to clipboard                                       | Clipboard.js_                 | `MIT License <https://github.com/zenorocha/clipboard.js/blob/master/LICENSE>`__   |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
| Fonts                                                   | Roboto_ (until version 5.0)   | `Apache License, Version 2.0`_                                                    |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
|                                                         | `JetBrains Mono`_             | `SIL Open Font License, 1.1`_                                                     |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
| Icons                                                   | `Material icons`_             | `Apache License, Version 2.0`_                                                    |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
| Tooltips                                                | `Primer/CSS`_                 | `MIT License <https://github.com/primer/css/blob/main/LICENSE>`__                 |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
| **Note:** versions ≤ 1.13.1 used these icons instead:   | Entypo_ by Daniel Bruce       | `Creative Commons Attribution-ShareAlike 4.0`_                                    |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
|                                                         | Zondicons_ by Steve Schoger   | ?                                                                                 |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+
| Illustrations                                           | undraw.co_                    | custom_                                                                           |
+---------------------------------------------------------+-------------------------------+-----------------------------------------------------------------------------------+

.. _Tailwind: https://tailwindcss.com
.. _Clipboard.js: https://clipboardjs.com
.. _Roboto: https://github.com/googlefonts/roboto
.. _JetBrains Mono: https://github.com/JetBrains/JetBrainsMono/
.. _SIL Open Font License, 1.1: https://github.com/JetBrains/JetBrainsMono/blob/master/OFL.txt
.. _Material icons: https://fonts.google.com
.. _undraw.co: https://undraw.co
.. _custom: https://undraw.co/license
.. _Primer/CSS: https://primer.style/css/
.. _Entypo: http://www.entypo.com
.. _Zondicons: http://www.zondicons.com
.. _Creative Commons Attribution-ShareAlike 4.0: https://creativecommons.org/licenses/by-sa/4.0/legalcode
.. _Apache License, Version 2.0: https://www.apache.org/licenses/LICENSE-2.0.html
