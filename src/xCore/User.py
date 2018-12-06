'''
Class:      User
Author:     Sam Badger
Date:       October 14, 2018
Description:
            This class manages data and functionality related to XenoTrade users.
'''

import logging

from xCore.Stock import Stock
from xCore.abstract import XenoObject

class User(XenoObject):
    
    def __init__(self, kernel, directory):
        super().__init__()
        
        self.setUserDir(directory)
        self.setUserName(directory=directory)
        self.setVerificationStatus(False)

    def __del__(self):
        try:
            #logout of all APIs and database
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
        
        
    ###############################################################################
    #                               SETTERS
    ###############################################################################
    def setUserName(self, directory=None, name=None):
        if directory:
            self._userName  = directory.strip('/')
            self._userName  = self._userName[self._userName.rfind('/')+1:]
        elif name:
            self._userName = name
        else:
            return
        
    def setKernel(self, kernel):
        self._kernel = kernel
        
    def setUserDir(self, directory):
        self._userDir = directory
        
    def setLoggedIn(self, status):
        self._loggedIn = status
    
    def setSecuritiesOwned(self, securities):
        self._securitiesOwned = securities
        
    ###############################################################################
    #                           LOG CURRENT USER OUT
    ###############################################################################
    def logout(self):
        '''
            Attempts to log the current user out.
        '''
        try:
            self.getTrader().logout()
        except:
            return "ERROR: Could not log out."

    ###############################################################################
    #                           LOG CURRENT USER IN
    ###############################################################################
    def login(self, pwd):
        ''' log the current user into the database '''
        if self.loggedIn():
            return True
        try:
            
            self.setVerificationStatus(status)
            return status
        except:
            logging.error("Credentials verification failed for user: {}".format(self.getUserName()))
