from PySide2.QtCore import QObject, Signal

import sys
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint

from XenoObject import XenoObject
from Robinhood  import Robinhood
from Stock      import Stock

class User(QObject, XenoObject):
    dataFetchFinished = Signal()

    def __init__(self, kernel, directory):
        QObject.__init__(self)
        XenoObject.__init__(self)
        self.kernel		= kernel
        temp            = directory.strip('/')
        self.userName   = temp[temp.rfind('/')+1:]
        self.userDir	= directory
        self.verified   = False
        self.trader     = Robinhood()

    def __del__(self):
        try:
            self.trader.logout()
            self.verified = False
        except:
            return "Error: Logout failed (Unknown reason)"
            
    def logout(self):
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
        if self.verified:
            return

        try:
            self.verified = self.trader.login(username=self.userName, password=pwd)
            if not self.verified:
                return "Error: Your login credentials did not match with Robinhood's servers"
            self.verified = True
        except:
            return "Error: Login failed (Unknown reason)"

    def stocks(self, owned=False, watched=False):
        if owned:
            return self.ownedStocks
        elif watched:
            return self.watchedStocks
        else:
            return []

    def pullStocksFromRobinhood(self):
        o = self.kernel.curUser.trader.securities_owned()['results'] # o is for owned
        t = self.kernel.curUser.trader
        self.ownedStocks = []
        with ThreadPoolExecutor(len(o)) as executor:
            for i in range(len(o)):
                future = executor.submit(Stock, t, pos=o[i])
                future.add_done_callback(self.addStock_callback)
        self.dataFetchFinished.emit()
        
    def addStock_callback(self, future):
        self.xeno_LockForWriting()
        self.ownedStocks.append(future.result())
        self.xeno_UnlockAll()
        

    def print(self):
        print("Username:", self.userName)
        print("UserDir: ", self.userDir)
        print("Verified:", self.verified)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
