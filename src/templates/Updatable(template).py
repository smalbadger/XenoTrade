'''
Class:      Updatable
Author(s):  Sam Badger
Date:       Oct 15, 2018
Type:       TEMPLATE
Description:
            This is a template for making a class updatable. Updatable objects
            will be updated strategically based on dependencies described by the
            UpdateDependencyGraph (in xCore).
            
            This template was originally designed to be an abstract class. Since
            multiple inheritance of Qt classes is not supported, this had to be
            made into a template.
            
Requirements:
            Your class must inherit from the QObject class. All Qt classes
            inherit from QObject either directly or indirectly, so if you're
            already inheriting from a widget or something, you don't need to 
            inherit from anything else. If you aren't, inherit from the QObject
            class.
            
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !! THIS TEMPLATE IS NOT COMPLETE !!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
from time import time
import logging

from PySide2.QtCore import Signal

import xCore.Globals as GS


class -----(-----):

    #>>>>>>>>>> INCLUDE THIS!!!
    updateComplete = Signal(bool)   #emit this signal update is finished
                                    # - True: object was updated
                                    # - False: object was not updated
    #<<<<<<<<<<
    
    def __init__(self, kernel):
        super(-----, self).__init__()
        #>>>>>>>>>> INCLUDE THIS!!!
        self._kernel = kernel
        self.initUpdatable(frequency)
        #<<<<<<<<<<
        
    #>>>>>>>>>> INCLUDE THIS!!!
    def initUpdatable(self):
        self.setUpdateFunctionList([])
        
        # TODO: add any update functions you have. These functions will be
        #       called automatically by the runUpdates function.
        #
        #   Ex: self.addUpdateFunction(self.myUpdateFunction1, args, kwargs)
        #       self.addUpdateFunction(self.myUpdateFunction2, args, kwargs)
        #       ...
        #
        # Note: Do not call your update function "update". That's reserved by 
        #       many widgets
        
        self.setUpdateFrequency("""Your frequency goes here""")
        # TODO: change the update frequency in the above function.
        #       This value is the minimum time that you want between your
        #       updates. 
        #
        #   Ex: If you set it to 10, the fastest this class will ever
        #       be updated is once every 10 seconds.
        #
        # Note: This doesn't mean that an update is guaranteed to happen
        #       every 10 seconds.
        #       
        #  Tip: classes that are less speed-critical should update less
        #       frequently. (meaning a higher number. I know, it's counter
        #       intuitive)
        
        self.setLastUpdateTime(None)
        self.resetParents()
        self.resetChildren()
        
        # TODO: add any parents and children. This comes into play in the 
        #       UpdateDependencyGraph. Look at that class (in xCore) to see what
        #       it does if you're interested.
        #
        #   Ex: self.addParent(AnotherUpdatableObject)
        #
        # Note: your parent must be updatable as well. It should also be in the
        #       UpdateDependencyGraph. When
        
    def getLastUpdateTime(self):
        return self._lastUpdateTime
        
    def getUpdateFunctionList(self):
        return self._updateFunctionList

    def getUpdateFrequency(self):
        return self._updateFrequency
        
    def getParents(self):
        return self._parents
        
    def getChildren(self):
        return self._children
        
    def resetParents(self):
        self._parents = []
        
    def resetChildren(self):
        self._children = []
    
    def setLastUpdateTime(self, t):
        self._lastUpdateTime = t
    
    def setUpdateFunctionList(self, fnList):
        self._updateFunctionList = fnList
        
    def setUpdateFrequency(self, freq):
        if freq == None:
            self._updateFrequency = GS.UPDATE_FREQUENCY
        else:
            self._updateFrequency = freq
        
    def addUpdateFunction(self, Fn, *args, **kwargs):
        self.getUpdateFunctionList().append((Fn, args, kwargs))
        
    def addParent(self, parent):
        self.getParents().append(parent)
        
    def printThread(self):
        print("Thread of {:20}:{}({})".format(self.__str__(), threading.currentThread().getName(), threading.get_ident()))
    
    def runUpdates(self):
        """
            Update the object if it either hasn't been updated yet, or if it hasn't been 
            updated recently. Return True if updated and False otherwise.
        """
        shouldUpdate = False
        if (self.getLastUpdateTime() == None):
            shouldUpdate = True
        elif(time() - self.getLastUpdateTime() > self.getUpdateFrequency()):
            shouldUpdate = True
            
        if shouldUpdate:
            self.setLastUpdateTime(time())
            updateFns = self.getUpdateFunctionList()
            print(self)
            if len(updateFns) > 0:
                # iterate through the update functions that the user has set and call them
                for fn, args, kwargs in self.getUpdateFunctionList():
                    try:
                        fn(*args, **kwargs)
                    except Exception as e:
                        print(e)
        self.updateComplete.emit(shouldUpdate)
    #<<<<<<<<<<
        
