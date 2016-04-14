deploy_module
=============

This is a simple script that will install the latest tagged version of 
a project on GitHub as well as ensure that the latest commits in the 
develop branch are iinstalled into a `-latest` directory.

The script also ensures there is an environmental module for both of the above.
You can read more about modules at
https://en.wikipedia.org/wiki/Environment_Modules_%28software%29

The script takes the following arguments:

- Software
- Modules
- GitHub URL

Script Process
--------------

The following example usage would deploy the continuous_delivery project into
the Software directory in your current working directory and then would place
modules for the latest develop version as well as the latest tagged release into
the Modules directory.

.. code-block:: bash

    ./deploy_module.py Software Modules https://github.com/vdbwrair/continous_delivery

Using the software once it is deployed
--------------------------------------

You can simply execute 

.. code-block:: bash

    module use Modules

Which will activate the Modules path such that the module command will 
look for them there(until you close your terminal).

Once that is done you can view all modules via

.. code-block:: bash

    module avail

which should produce something like the following::

    ---------------- Modules ---------------------
    continuous_delivery/continuous_delivery-latest
    continuous_delivery/continuous_delivery-v1.1.0

You can use the module load command to load either of the modules by name

.. code-block:: bash

    module load continuous_delivery/continuous_delivery-latest

Or you can load the latest tagged version via lazy loading

.. code-block:: bash

    module load continuous_delivery

Which would load v1.1.0(or whatever the latest version is)
