'''
Class:      Widget
Author(s):  Sam Badger
Date:       Oct 16, 2018
Type:       ABSTRACT
Description:
            This is the base class for a widget in XenoTrade. It simply contains all methods that a
            widget should have. Notice that it inherits from XenoObject and Updatable.
'''

# <Python imports>
# <external library imports>

from XenoObject import XenoObject
from Updatable import Updatable


class Widget(XenoObject, Updatable):
    def __init__(self):
        XenoObject.__init__(self)
        Updatable.__init__(self)

    def __del__(self):
        pass
        
    def __str__(self):
        return ""
