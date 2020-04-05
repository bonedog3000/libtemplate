Installation instructions
=========================

Insert instructions for installing, updating, and installing your library.

Below we provide such instructions for the ``libtemplate`` library. We also
include instructions for installing the necessary packages for generating
library documentation files.

Installation using conda and pip
--------------------------------

First, install required packages by issuing the following command in the
terminal::

    conda install --file requirements.txt

Once you have installed the required packages, you can install ``libtemplate``
by issuing the following command::

    pip install .

Note that you must include the period as well.

Installation using pip only
---------------------------

First, install required packages by issuing the following command in the
terminal::
  
    pip install -r requirements.txt

Once you have installed the required packages, you can install ``libtemplate``
by issuing the following command::

    pip install .

Note that you must include the period as well.

Update libtemplate
------------------

If you, or someone else has made changes to this library, you can reinstall by
issuing the following command::
  
    pip install .

Uninstall libtemplate
---------------------

To uninstall ``libtemplate``, all you need to type is::

    pip uninstall libtemplate

Generating documention files
----------------------------

To generate documentation in html format from source files you will also need
the sphinx and numpydoc pacakges. These can be installed by typing at the root
directory::

    pip install -r requirements-doc.txt

Then, assuming you are in the root directory of ``libtemplate`` and that
``libtemplate`` is already installed, issue the following commands to generate
html documentation files::

    cd docs
    make html

This will generate a set of html files in ``./_build/html`` containing the
documentation of ``libtemplate``. You can then open any of the files using your
favorite web browser to start navigating the documentation within said browser::

    firefox ./_build/html/index.html &>/dev/null &

If ``libtemplate`` has been updated, the documentation has most likely changed
as well. To update the documentation, first remove the ``reference`` directory
inside ``docs``::

    rm -r reference

and then issue the following command::

    make clean

Now that we have cleaned everything up, we can simply run::

    make html

to generate the new documentation.
