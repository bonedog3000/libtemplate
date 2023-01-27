"""Insert a one-line description of module.

A more detailed description of the module. The more detailed description can
span multiple lines.

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



# Importing a module from within this library. Notice the triple new-line
# spacing between module/package groups.
import libtemplate.subpackage.module2



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

# List of public objects in module.
__all__ = ["Rectangle", "scale_rectangle"]



class Rectangle():
    r"""A one-line description of the class.

    A more detailed description of the class. The more detailed description can
    span multiple lines. In this particular example, we define a class that is
    suppose to represent a rectangle.

    It is a standard naming convention to start class names with captial
    letters. Avoid using underscores.

    Parameters
    ----------
    length : `float`
        A description of the first constructor argument, named ``length`` in
        this example. The user is expected to pass an object of type `float`
        in place of this argument, i.e. ``length`` should be a real-valued
        number. Moreover, it should also be positive.
    width : `float` | `None`, optional
        A description of the second constructor argument, named ``width`` in
        this example. This is an optional argument, i.e. the user need not
        specify this argument. If specified, the user should pass in a `float`,
        otherwise this argument will be set to type `None` and then later
        assigned the same value as ``length``.

    Attributes
    ----------
    length : `float`
        A description of the first class attribute, named ``length`` in this
        this example. It is not always the case that the class attributes will
        be the same as the class construction paramters.
    width : `float`
        A description of the second class attribute, named ``width`` in this
        this example.

    """
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if (width is not None) else length

        try:
            if (self.length <= 0) or (self.width <= 0):
                raise ValueError(_rectangle_err_msg_1)
        except:
            raise TypeError(_rectangle_err_msg_1)

        # It's good practice to always have a return statement at the end of
        # any function/method, even if the function/method isn't suppose to
        # return anything. In the case that the function/method isn't suppose
        # return anything, simply return a `None` object.
        return None

    def area(self):
        r"""A one-line description of the class method.

        A more detailed description of the class method. The more detailed
        description can span multiple lines. In this particular example, we
        define a method that calculates the area of the rectangle.

        It is a standard naming convention to use all lowercase characters to
        name a method. Underscores are fine.

        Returns
        -------
        area : `float`
            A description of the object returned from the class method. In this
            example, the method returns the area of the rectangle, as a `float`.
        """
        area = self.length * self.width

        return area



def scale_rectangle(rectangle, scale):
    r"""A one-line description of the function.

    A more detailed description of the function. The more detailed description
    can span multiple lines. In this particular example, we define a function
    that scales a given rectangle by a given scaling factor. Note that this
    function does not alter the attributes of the original rectangle but creates
    a copy first.

    It is a standard naming convention to use all lowercase characters to name
    a function. Underscores are fine.
    
    Parameters
    ----------
    rectangle : :class:`libtemplate.module1.Rectangle`
        A description of the first function argument, named ``rectangle`` in 
        this example. The user is expected to pass an object of type 
        :class:`libtemplate.module1.Rectangle` in place of this argument. The
        function will subsequently create a copy of the 
        :class:`libtemplate.module1.Rectangle` object and then scale it.
    scale : `float`
        A description of the second function argument, named ``scale`` in this
        example. The user is expected to pass an object of type `float` in 
        place of this argument. The function will scale the given 
        :class:`libtemplate.module1.Rectangle` by ``scale``. Note that ``scale``
        should be a positive number.

    Returns
    -------
    scaled_rectangle : :class:`libtemplate.module1.Rectangle`
        A description of the object returned by the function, named 
        ``scaled_rectangle`` in this example. This object represents the scaled
        rectangle.

    """
    scaled_rectangle = copy.deepcopy(rectangle)  # Performs a deep copy.

    # We imported `libtemplate.subpackage.module2` from another subpackage in
    # this library.
    libtemplate.subpackage.module2.say_something("Scaling the rectangle...")

    try:
        if scale <= 0:
            raise ValueError(_scale_rectangle_err_msg_1)
    except:
        raise TypeError(_scale_rectangle_err_msg_1)

    try:
        scaled_rectangle.length *= scale
        scaled_rectangle.width *= scale
    except:
        raise TypeError(_scale_rectangle_err_msg_2)

    return scaled_rectangle



###########################
## Define error messages ##
###########################

_rectangle_err_msg_1 = \
    ("The objects ``length`` and ``width`` must be positive real numbers.")

_scale_rectangle_err_msg_1 = \
    ("The object ``scale`` must be a positive real number.")
_scale_rectangle_err_msg_2 = \
    ("The object ``rectangle`` must be an instance of the class"
     "`libtemplate.module1.Rectangle`.")
