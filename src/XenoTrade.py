import logging
import sys
import os
from time import sleep

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtGui import QPalette

from xCore import Kernel
from xWidgets import UserSelect, Dashboard, LoadingScreen

class XenoTradeGUI(QMainWindow):
    def __init__(self, kernel, parent=None):
        super(XenoTradeGUI, self).__init__(parent)
        self.kernel = kernel
        self.showMaximized()
        self.setWindowTitle("XenoTrade")

        self.initLoginGUI()

    def initLoginGUI(self):
        widget = UserSelect(kernel, self)
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


#=============================================================================#
def setAppStyle(app):
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.Window, QtGui.QColor(53,53,53))
    palette.setColor(QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QPalette.Base, QtGui.QColor(15,15,15))
    palette.setColor(QPalette.AlternateBase, QtGui.QColor(53,53,53))
    palette.setColor(QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QPalette.Text, QtCore.Qt.white)
    palette.setColor(QPalette.Button, QtGui.QColor(53,53,53))
    palette.setColor(QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QPalette.BrightText, QtCore.Qt.red)

    palette.setColor(QPalette.Highlight, QtGui.QColor(142,45,197).lighter())
    palette.setColor(QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)

def setupLogging(args):
    logFile = "../logbook/XenoTrade.log"
    with open(logFile,"w") as f:
        f.write("{}{}".format("="*80, "\n"))
        f.write("{} {} {}{}".format("="*35,"NEW  LOG","="*35,"\n"))
        f.write("{}{}".format("="*80, "\n"))
        f.close()   # clears log file
    
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
        
    logging.basicConfig(filename = logFile, level = lvl)

if __name__ == '__main__':
    setupLogging(sys.argv)

    app = QApplication(sys.argv)
    setAppStyle(app)
    kernel = Kernel(app)
    frame = XenoTradeGUI(kernel)
    frame.show()
    logging.info("Starting XenoTrade Application")
    sys.exit(app.exec_())
    
    
