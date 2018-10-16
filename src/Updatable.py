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
'''

from time import time
import logging

from PySide2.QtCore import QObject, Signal

import GlobalSettings as GS


class Updatable(QObject):
    updateComplete = Signal()   #emit this signal when an update is done.
    
    def __init__(self, frequency=None):
        QObject.__init__(self)
        self.setUpdateFunctionList([])
        self.setUpdateFrequency(frequency)
        self.setLastUpdateTime(None)
        
    ###############################################################################
    #                                GETTERS
    ###############################################################################
    def getLastUpdateTime(self):
        return self._lastUpdateTime
        
    def getUpdateFunctionList(self):
        return self._updateFunctionList

    def getUpdateFrequency(self):
        return self._updateFrequency
        
    ###############################################################################
    #                                SETTERS
    ############################################################################### 
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
        
    ###############################################################################
    #                                FUNCTIONAL METHODS
    ###############################################################################
    def update(self):
        """
            Update the object if it either hasn't been updated yet, or if it hasn't been 
            updated recently. Return True if updated and False otherwise.
        """
        logging.info("--- Running the subclass-defined update functions ---.")
        logging.debug("Checking if we should update this time.")
        shouldUpdate = False
        if (self.getLastUpdateTime() == None):
            shouldUpdate = True
        elif(time() - self.getLastUpdateTime() > self.getUpdateFrequency()):
            shouldUpdate = True
            
        if shouldUpdate:
            logging.debug("We should update")
            self.setLastUpdateTime(time())
            # iterate through the update functions that the user has set and call them
            for fn, args, kwargs in self.getUpdateFunctionList():
                logging.debug("Running the update function: {}".format(fn))
                try:
                    fn(*args, **kwargs)
                except Exception as e:
                    print(e)
        
        self.updateComplete.emit()    
        return shouldUpdate
