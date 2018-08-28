from PySide2.QtCore import QObject, Signal

from time import sleep

from Robinhood import Robinhood
from Stock     import Stock

from pprint import pprint
from time import sleep

class User(QObject):
    dataFetchFinished = Signal()

    def __init__(self, kernel, directory):
        super(User, self).__init__()
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
        owned = self.kernel.curUser.trader.securities_owned()['results']
        self.ownedStocks = []
        for i in range(len(owned)):
            self.ownedStocks.append(Stock(self.kernel.curUser.trader, pos=owned[i]))
        self.dataFetchFinished.emit()

    def print(self):
        print("Username:", self.userName)
        print("UserDir: ", self.userDir)
        print("Verified:", self.verified)
