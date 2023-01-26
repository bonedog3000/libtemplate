"""``libtemplate`` (short for 'Library Template') is a Python library that
should be used as a template to build one's own library, as the name suggests.
In this file you should provide a brief description of whatever library you
decide to create out of this template.

"""



#####################################
## Load libraries/packages/modules ##
#####################################

# Import child modules and packages of current package.
import libtemplate.module1
import libtemplate.subpackage
import libtemplate.version



############################
## Authorship information ##
############################

__author__       = "author-placeholder"
__copyright__    = "Copyright copyright-year-placeholder"
__credits__      = ["author-placeholder"]
__version__      = version.version
__full_version__ = version.full_version
__maintainer__   = "author-placeholder"
__email__        = "email-placeholder"
__status__       = "Development"



##################################
## Define classes and functions ##
##################################

# List of public objects in package.
__all__ = ["subpackage",
           "module1",
           "version",
           "show_config"]



def show_config():
    """Print information about the version of ``libtemplate`` and libraries it 
    uses.

    Parameters
    ----------

    Returns
    -------

    """
    print(version.version_summary)

    return None



###########################
## Define error messages ##
###########################
