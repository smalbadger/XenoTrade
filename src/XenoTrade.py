from PySide2 import QtCore
from PySide2 import QtGui

from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui	   import QPalette

import sys
import os
from time import sleep

import logging

from Kernel           import Kernel
from UserSelectWidget import UserSelectWidget
from DashboardWidget  import DashboardWidget
from StockListWidget  import StockListWidget
from LoadingScreen    import LoadingScreen

class XenoTradeGUI(QMainWindow):
    def __init__(self, kernel, parent=None):
        logging.info("Initializing XenoTrade GUI")
        super(XenoTradeGUI, self).__init__(parent)
        self.kernel = kernel
        self.showMaximized()
        self.setWindowTitle("XenoTrade")

        self.initLoginGUI()

    def initLoginGUI(self):
        widget = UserSelectWidget(kernel, self)
        self.setCentralWidget(widget)

    def loadApplication(self):
        if not self.kernel.getCurrentUser().getVerificationStatus():
            return
        else:
            n = self.kernel.getCurrentUser().getUserName()
            m = """
            Please be patient while we retrieve your information from Robinhood
            """
            p = self
            self.loadWidget = LoadingScreen(self.kernel, username=n, message=m)
            self.setCentralWidget(self.loadWidget)
            self.animateThread = QtCore.QThread()
            self.animateThread.started.connect(self.loadWidget.startAnimation)
            self.animateThread.start()

            #######################################################################
            # This section of code moves the user object to another thread, pulls #
            # all stock information from the robinhood servers (which can take    #
            # a while), and then loads the dashboard GUI. While the stock         #
            # information is being pulled, a loading screen is shown.             #
            #######################################################################
            self.tempThread = QtCore.QThread()
            self.kernel.getCurrentUser().moveToThread(self.tempThread)
            self.kernel.getCurrentUser().updateComplete.connect(self.initDashboardGUI)
            self.tempThread.started.connect(self.kernel.getCurrentUser().update)
            self.tempThread.start()


    def initDashboardGUI(self):
        self.tempThread.quit()
        self.loadWidget.stopAnimation()
        self.animateThread.quit()

        widget = DashboardWidget(kernel, self)
        self.setCentralWidget(widget)
        
    def closeEvent(self, event):
        if self.kernel.getCurrentUser() == None:
            sys.exit(0)
            
        try:
            err = self.kernel.getCurrentUser().logout()
            logging.error(err)
        except:
            logging.error("No current user")
        sys.exit(0)


#=============================================================================#
def setAppStyle(app):
    logging.info("Setting application style")
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(15,15,15))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53,53,53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)

    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142,45,197).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)

def setupLogging(args):
    if "--logging-level" in args:
        lvlStr = ""
        try:
            idx = args.index("--logging-level")
            lvlStr = args[idx + 1]
        except:
            print("USAGE: <python_interpreter> XenoTrade.py --logging-level <importance_level>")
            sys.exit(1)
        
        lvl = None
        if lvlStr == "DEBUG":
            lvl = logging.DEBUG
        elif lvlStr == "INFO":
            lvl = logging.INFO
        elif lvlStr == "WARNING":
            lvl = logging.WARNING
        elif lvlStr == "ERROR":
            lvl = logging.ERROR
        elif lvlStr == "CRITICAL":
            lvl = logging.CRITICAL
        else:
            print("Logging level {} is not recognized".format(lvlStr))
            print("Using INFO as the logging level by default.")
            lvl = logging.INFO
    else:
        print("Logging level not specified.")
        print("Using INFO as the logging level by default.")
        lvl = logging.INFO
        
    logging.basicConfig(filename = '../logbook/XenoTrade.log', level = lvl)
    logging.info("================================== NEW LOG ==================================")




if __name__ == '__main__':
    setupLogging(sys.argv)

    logging.info("Creating Qt application")
    app = QApplication(sys.argv)
    setAppStyle(app)
    kernel = Kernel(app)
    frame = XenoTradeGUI(kernel)
    frame.show()
    sys.exit(app.exec_())
    
    
