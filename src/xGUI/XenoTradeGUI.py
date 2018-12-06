import logging
import sys
import os
from time import sleep

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QPalette

from xCore import Kernel
from xGUI.UserSelectWidget import UserSelectWidget
from xGUI.DashboardWidget import DashboardWidget
from xGUI.LoadingScreenWidget import LoadingScreenWidget

class XenoTradeGUI(QMainWindow):
    def __init__(self, kernel):
        super().__init__()
        self.kernel = kernel
        self.showMaximized()
        self.setWindowTitle("XenoTrade")
        self.initLoginGUI(kernel)

    def initLoginGUI(self, kernel):
        widget = UserSelectWidget(kernel.getAllUsers(), kernel.getUsersDir())
        self.setCentralWidget(widget)

    def loadApplication(self):
        logging.info("Loading Application")
        assert(self.kernel.getCurrentUser() != None)
        if self.kernel.getCurrentUser().getVerificationStatus() == False:
            return
        else:
            n = self.kernel.getCurrentUser().getUserName()
            m = """
            Please be patient while we retrieve your information from Robinhood
            """
            # do some type of animation here while stuff is loading
            
            self.initDashboardGUI()

    def initDashboardGUI(self):
        widget = Dashboard(kernel, self)
        self.setCentralWidget(widget)
        self.kernel.getUpdateManager().start()
        
    def closeEvent(self, event):
        if self.kernel.getCurrentUser() == None:
            sys.exit(0)
            
        try:
            err = self.kernel.getCurrentUser().logout()
        except:
            pass
        sys.exit(0)
