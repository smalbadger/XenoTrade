'''
Class:      User
Author:     Sam Badger
Date:       October 14, 2018
Description:
            This class manages data and functionality related to XenoTrade users.
'''

import logging
from time import sleep, time
from concurrent.futures import ThreadPoolExecutor

from PySide2.QtCore import QObject, Signal

import GlobalSettings as GS
from Stock      import Stock
from Robinhood  import Robinhood
from XenoObject import XenoObject

class User(QObject, XenoObject):
    updateComplete = Signal()   #emit this signal when an update is done.

    def __init__(self, kernel, directory):
        logging.info("Creating User Object")
        QObject.__init__(self)
        XenoObject.__init__(self)
        
        self.setKernel(kernel)
        self.setTrader()
        self.setUserDir(directory)
        self.setUserName(directory=directory)
        self.setVerificationStatus(False)
        self.setSecuritiesOwned(set())
        self.setLastUpdateTime(None)

    def __del__(self):
        logging.info("Deleting User Object")
        self.releaseAllLocks()
        try:
            self.getTrader().logout()
            self.setVerificationStatus(False)
        except:
            return "Logout failed (Unknown reason)"
    
    def __str__(self):
        ret = "{} (".format(self.getUserName())
        if not self.getVerificationStatus():
            ret += "not "
        ret += "logged in)"
        return ret
        
    ###############################################################################
    #                               GETTERS
    ###############################################################################
    def getUserName(self):
        return self._userName
        
    def getKernel(self):
        return self._kernel
        
    def getUserDir(self):
        return self._userDir
    
    def getVerificationStatus(self):
        return self._verificationStatus
    
    def getTrader(self):
        return self._trader
        
    def getSecuritiesOwned(self):
        return self._securitiesOwned
        
    def getTaskManager(self):
        return self.getKernel().getTaskManager()
        
    def getLastUpdateTime(self):
        return self._lastUpdateTime
        
    ###############################################################################
    #                               SETTERS
    ###############################################################################
    def setUserName(self, directory=None, name=None):
        logging.debug("Setting user name.")
        if directory:
            self._userName  = directory.strip('/')
            self._userName  = self._userName[self._userName.rfind('/')+1:]
        elif name:
            self._userName = name
        else:
            logging.warning("Username could not be set.")
            return
        logging.debug("Username set to ".format(self._userName))
        
    def setKernel(self, kernel):
        logging.debug("Setting the user's kernel")
        self._kernel = kernel
        
    def setUserDir(self, directory):
        logging.debug("setting the user's directory")
        self._userDir = directory
        
    def setTrader(self):
        logging.debug("setting the user's trader")
        self._trader = Robinhood()
    
    def setVerificationStatus(self, status):
        logging.debug("setting the user's verification status to {}".format(status))
        self._verificationStatus = status
    
    def setSecuritiesOwned(self, securities):
        logging.debug("Setting the user's securities owned")
        self._securitiesOwned = securities
            
    def setLastUpdateTime(self, time):
        logging.debug("Setting the user's last update time")
        self._lastUpdateTime = time
        
    ###############################################################################
    #                           LOG CURRENT USER OUT
    ###############################################################################
    def logout(self):
        '''
            Attempts to log the current user out.
        '''
        logging.info("Logging current user out")
        try:
            self.getTrader().logout()
        except:
            return "ERROR: Could not log out."

    ###############################################################################
    #                           LOG CURRENT USER IN
    ###############################################################################
    def verify(self, pwd):
        '''
        Uses the user's username and the password provided to login to
        the robinhood API.

        Case 1) User is already logged in:
                - return None
        Case 2) User is not logged in, but entered false credentials:
                - return error (see below)
        Case 3) User is not logged in, but entered correct credentials:
                - log user in and return None
        '''
        logging.info("Checking {}'s credentials.".format(self.getUserName()))
        if self.getVerificationStatus():
            logging.info("{} is already logged in".format(self.getUserName()))
            return True

        status = self.getTrader().login(username=self.getUserName(), password=pwd)
        self.setVerificationStatus(status)
        if status:
            logging.info("{} has been successfully logged in.".format(self.getUserName()))
            return True
        else:
            logging.error("Credentials did not match Robinhood's servers.")
            return False
        
    ###############################################################################
    #                              UPDATE METHODS
    ###############################################################################
    def update(self):
        """
            Update the object if it either hasn't been updated yet, or if it hasn't been 
            updated recently. Return True if updated and False otherwise.
        """
        logging.info("Updating {}.".format(self.getUserName()))
        shouldUpdate = False
        if (self.getLastUpdateTime() == None):
            shouldUpdate = True
        elif(time() - self.getLastUpdateTime() > GS.UPDATE_FREQUENCY):
            shouldUpdate = True
            
        if shouldUpdate:
            self.setLastUpdateTime(time())
            self.updateSecuritiesOwned()
        
        self.updateComplete.emit()    
        return shouldUpdate

    def updateSecuritiesOwned(self):
        """
            retrieve a summary of all securities owned. then iterate through the summary and
            retrieve an updated security object.
        """
        logging.info("Updating {}'s securities.".format(self.getUserName()))
        
        t = self.getTrader()
        ownedSummary = t.securities_owned()['results']
        tm = self.getTaskManager()
        for i in range(len(ownedSummary)):
            tm.addNetworkTask(Stock, self.updateSecuritiesOwned_CALLBACK, t, pos=ownedSummary[i])
            
        sleep(20) #remove this later
        
    def updateSecuritiesOwned_CALLBACK(self, future):
        """
            When a security is done being gathered by the task manager, add it to the existing set
        """
        logging.debug("Appending Stock to user's list of stocks")
        print(future.result())
        self.acquireLock("stockData")
        self.getSecuritiesOwned().add(future.result())
        self.releaseLock("stockData")
        
    ###############################################################################
    #                           UTILITY METHODS
    ###############################################################################
    def print(self):
        print("Username:", self.getUserName())
        print("UserDir: ", self.getUserDir())
        print("Verified:", self.getVerificationStatus())
        
