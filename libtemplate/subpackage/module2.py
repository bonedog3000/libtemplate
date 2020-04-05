#!/usr/bin/env python
"""Insert a one-line description of module.
"""



#####################################
## Load libraries/packages/modules ##
#####################################

# Note: It is standard practice to import libraries/modules/packages in a
# particular order. You should import all modules/packages from the Python's
# standard library first. Then you should import third party modules/packages
# e.g. numpy.Then you should import local modules/packages, presumably
# developed by the user. Note the increased spacing between module/package
# groups. Feel free to remove this note from your own library once the
# convention is understood.

# For getting filename and directory paths (from standard library). We don't
# actually use this module. It is included here to illustrate the import
# convention.
import os



# For general array handling (third party). We don't actually use this module.
# It is included here to illustrate the import convention.
import numpy as np



# Here one would normally put the local module/package imports. However we don't
# import any in this module so we simply leave it blank. Notice the triple
# new-line spacing between module/package groups.
from libtemplate.subpackage import module2



############################
## Authorship information ##
############################

__author__     = "author-placeholder"
__copyright__  = "Copyright copyright-year-placeholder"
__credits__    = ["author-placeholder"]
__maintainer__ = "author-placeholder"
__email__      = "email-placeholder"
__status__     = "Development"



##################################
## Define classes and functions ##
##################################

# List of public objects in objects.
__all__ = ["say_something"]



def say_something(statement):
    r"""A one-line description of the function.

    A more detailed description of the function. The more detailed description 
    can span multiple lines. In this particular example, we define a function
    prints a statement given by the user.
    
    Parameters
    ----------
    statement : `str`
        A description of the first (and only) function argument, named
        ``statement`` in this example. The user is expected to pass an object
        of type `str`, i.e. a string. The function will print the string
        `statement`.

    Returns
    -------
    """
    print(statement)

    # It's good practice to always have a return statement at the end of any
    # function/method, even if the function/method isn't suppose to return
    # anything. In the case that the function/method isn't suppose return
    # anything, simply return a `None` object.
    return None
