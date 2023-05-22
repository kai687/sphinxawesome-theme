Prepare JavaScript environment
------------------------------

#. Confirm that `Node.js <https://nodejs.org/en/>`_ is installed:

   .. code-block:: bash

      $ node --version
      v20.00.0

   If the preceding command fails, make sure that you installed Node.js.
   If you installed Node.js, make sure that the path to the ``node``
   executable is in your ``PATH`` environment variable.

   .. tip::

      For installing and managing different Node.js versions,
      see these projects: `nvm <https://github.com/nvm-sh/nvm>`_,
      `fnm <https://github.com/Schniz/fnm>`_,
      `Volta <https://volta.sh/>`_,
      `asdf <https://asdf-vm.com/>`_.

#. Optional: install ``pnpm``:

   .. code-block:: bash

      npm install --global pnpm

   If you want to use the same versions of JavaScript packages as in the |product| repository,
   use the pnpm package manager.
