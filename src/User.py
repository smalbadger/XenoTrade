from PySide2.QtCore import QObject, Signal

import sys
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
import logging

from XenoObject import XenoObject
from Robinhood  import Robinhood
from Stock      import Stock

class User(QObject, XenoObject):
    dataFetchFinished = Signal()

    def __init__(self, kernel, directory):
        logging.info("Creating User Object")
        QObject.__init__(self)
        XenoObject.__init__(self)
        self.kernel		= kernel
        temp            = directory.strip('/')
        self.userName   = temp[temp.rfind('/')+1:]
        self.userDir	= directory
        self.verified   = False
        self.trader     = Robinhood()

    def __del__(self):
        logging.info("Deleting User Object")
        try:
            self.trader.logout()
            self.verified = False
        except:
            return "Logout failed (Unknown reason)"
    
    def __str__(self):
        ret = "{} (".format(self.userName)
        if not self.verified:
            ret += "not "
        ret += "logged in)"
        return ret
            
    def logout(self):
        logging.info("Logging current user out")
        try:
            self.trader.logout()
        finally:
            return "ERROR: Could not log out."

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
        Case 4) Unknown error:
                - return login failed error
        '''
        logging.info("Checking {}'s credentials.".format(self.userName))
        if self.verified:
            logging.info("{} is already logged in".format(self.userName))
            return True

        self.verified = self.trader.login(username=self.userName, password=pwd)
        if self.verified:
            logging.info("{} has been successfully logged in.".format(self.userName))
            return True
        else:
            logging.error("Credentials did not match Robinhood's servers.")
            return False
        

    def stocks(self, owned=False, watched=False):
        if owned:
            logging.info("Getting all owned stocks from the current user.")
            return self.ownedStocks
        elif watched:
            logging.info("Getting all watched stocks from the current user.")
            return self.watchedStocks
        else:
            return []

    def pullStocksFromRobinhood(self):
        logging.info("Pulling {}'s owned stocks from Robinhood servers.".format(self.userName))
        o = self.trader.securities_owned()['results'] # o is for owned
        t = self.trader
        self.ownedStocks = []
        with ThreadPoolExecutor(len(o)) as executor:
            for i in range(len(o)):
                future = executor.submit(Stock, t, pos=o[i]) #Stock(t, pos=o[i])
                future.add_done_callback(self.addStock_callback)
        self.dataFetchFinished.emit()
        
    def addStock_callback(self, future):
        logging.debug("Appending Stock to user's list of stocks")
        self.xeno_LockForWriting()
        self.ownedStocks.append(future.result())
        self.xeno_UnlockAll()
        
    def print(self):
        print("Username:", self.userName)
        print("UserDir: ", self.userDir)
        print("Verified:", self.verified)
        
