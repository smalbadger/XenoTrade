from PySide2 import QtCore
from PySide2 import QtGui

from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow
from PySide2.QtGui	   import QPalette

import sys
import os

from Kernel           import Kernel
from UserSelectWidget import UserSelectWidget
from DashboardWidget  import DashboardWidget
from StockListWidget  import StockListWidget


class XenoTradeGUI(QMainWindow):
	def __init__(self, kernel, parent=None):
		super(XenoTradeGUI, self).__init__(parent)
		self.kernel = kernel
		self.showMaximized()
		self.setWindowTitle("XenoTrade")
		
		self.initLoginGUI()
		
	def initLoginGUI(self):
		widget = UserSelectWidget(kernel, self)
		self.setCentralWidget(widget)
		
	def initTradingGUI(self):
		pass
		
	def initDashboardGUI(self):
		widget = DashboardWidget(kernel, self)
		self.setCentralWidget(widget)
		
		
		
		
		
def setAppStyle(app):
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
		
		
		
if __name__ == '__main__':
	kernel = Kernel()
	app = QApplication(sys.argv)
	setAppStyle(app)
	frame = XenoTradeGUI(kernel)
	frame.show()
	sys.exit(app.exec_())
