import logging
import sys
import os
from time import sleep

from PySide2 import QtGui
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QPalette

from xCore import Kernel
from xGUI import XenoTradeGUI

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
    frame = XenoTradeGUI()
    frame.show()
    logging.info("Starting XenoTrade Application")
    sys.exit(app.exec_())
    
    
