'''
Class:      Updatable
Author(s):  Sam Badger
Date:       Oct 15, 2018
Type:       ABSTRACT
Description:
            This class should be inherited by all objects that need to be in XenoTrade's update loop
            such as widgets and user.
            
How To Use:
            Look at the User class for an example of how this class is used. Notice that the User
            class inherits from the Updatable class. Next, you should notice the call to
            self.addUpdateFunction in the constructor. A function is passed in with all of its
            parameters after. Notice the function that is passed in updates the securities owned.
            Inheriting from this class allows your class to be put in the main update loop of
            XenoTrade which will call the update function in this class. The update function in this
            class will call all of the functions that the subclass has specified.
            
            It is your responsibility to appropriately add your updatable object to the Update
            Manager. To do this, think about where your updatable gets its data from. Is it another
            updatable? If so, you should set ALL updatables that your updatable depends on to be 
            the parents of your updatable. Once this is done, call addUpdatable on the Update
            Manager and pass in your new updatable object.
            
Why parents and children?
            To find out more about this, please see the UpdateManager documentation.

Instructions:
            Because multiple inheritance in PyQt is not allowed, there are a few
            small things you need to add to your subclass.
            
            1. add the following import statement:
            
                from PySide2.QtCore import QObject, Signal
                
            2. if you aren't inheriting from any Qt objects yet, add QObject to
               your inheritance list
            
            3. add the following signal just below the class declaration:
               
                updateComplete = Signal(bool) #emit this signal when an update is done.
            
            4. add the following function:
            
                def runUpdates(self):
                    updateStatus = super().runUpdates()
                    self.updateComplete.emit(updateStatus)
'''

from time import time
import logging

from PySide2.QtCore import Signal

import xCore.GlobalSettings as GS


class Updatable():

    # TODO: copy and paste the line below into the same place in your subclass
    #   updateComplete = Signal(bool)   #emit this signal when an update is done.
    
    def __init__(self, frequency=None):
        super(Updatable, self).__init__()
        self.setUpdateFunctionList([])
        self.setUpdateFrequency(frequency)
        self.setLastUpdateTime(None)
        self.resetParents()
        self.resetChildren()
        
    ###############################################################################
    #                                GETTERS
    ###############################################################################
    def getLastUpdateTime(self):
        logging.debug("Getting last update time.")
        return self._lastUpdateTime
        
    def getUpdateFunctionList(self):
        logging.debug("Getting the update function list.")
        return self._updateFunctionList

    def getUpdateFrequency(self):
        logging.debug("Getting the update frequency.")
        return self._updateFrequency
        
    def getParents(self):
        logging.debug("Getting the parents.")
        return self._parents
        
    def getChildren(self):
        logging.debug("Getting the children.")
        return self._children
        
    ###############################################################################
    #                                SETTERS
    ############################################################################### 
    def resetParents(self):
        self._parents = []
        
    def resetChildren(self):
        self._children = []
    
    def setLastUpdateTime(self, t):
        logging.debug("Setting the last update time: {}".format(t))
        self._lastUpdateTime = t
    
    def setUpdateFunctionList(self, fnList):
        logging.debug("Setting the update function list: {}".format(fnList))
        self._updateFunctionList = fnList
        
    def setUpdateFrequency(self, freq):
        logging.debug("Setting update frequency: {}".format(freq))
        if freq == None:
            self._updateFrequency = GS.UPDATE_FREQUENCY
        else:
            self._updateFrequency = freq
        
    def addUpdateFunction(self, Fn, *args, **kwargs):
        logging.debug("Adding new function to update function list: {}".format(Fn))
        self.getUpdateFunctionList().append((Fn, args, kwargs))
        
    def addParent(self, parent):
        self.getParents().append(parent)
        
    def addChild(self, child):
        self.getChildren().append(child)
        
    ###############################################################################
    #                                FUNCTIONAL METHODS
    ###############################################################################
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
        
        # self.updateComplete.emit(shouldUpdate) Should be called by subclass instead
        return shouldUpdate
