#!/usr/bin/env python
"""A one-line description of the script example.

A more detailed description of the script example. This can span multiple lines.
One suggestion would be to provide a brief outline of what the script does.
In this script, we create a rectangle, and then create another rectangle that
is twice the size of the first.
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

# For deep copies of objects (from standard library). 
import copy



# For general array handling (third party). We don't actually use this module.
# It is included here to illustrate the import convention.
import numpy as np



# Import classes and functions from within the current library. Notice the
# triple new-line spacing between module/package groups.
from libtemplate.module1 import Rectangle, scale_rectangle



############################
## Authorship information ##
############################

__author__     = "author-placeholder"
__copyright__  = "Copyright copyright-year-placeholder"
__credits__    = ["author-placeholder"]
__maintainer__ = "author-placeholder"
__email__      = "email-placeholder"
__status__     = "Development"



#########################
## Main body of script ##
#########################

length = 2.0
width = 3.0
rectangle = Rectangle(length=length, width=width)

print("Dimensions of original rectangle:")
print("    length =", rectangle.length)
print("    width =", rectangle.width)
print()

scale = 2.0
scaled_rectangle = scale_rectangle(rectangle, scale)

print("Dimensions of rectangle after scaling:")
print("    length =", scaled_rectangle.length)
print("    width =", scaled_rectangle.width)
print()
