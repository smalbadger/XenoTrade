from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QLabel

from pprint import pprint
from Stock import Stock

class DashboardWidget(QWidget):
	def __init__(self, kernel, parent=None):
		super(DashboardWidget, self).__init__(parent)
		self.kernel = kernel
		self.parent = parent
		self.initUI()
		
	def initUI(self):
		self.createElements()
		self.createLayout()
		self.createActions()
		
	def createElements(self):
		self.nameLabel = QLabel('Hi, ' + self.kernel.curUser.userName)
		owned = self.kernel.curUser.trader.securities_owned()
		for security in owned['results']:
			stock = Stock(self.kernel.curUser.trader, pos=security)
			stock.printInfo()
			
	def createLayout(self):
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.nameLabel)
		self.setLayout(self.layout)
		
	def createActions(self):
		pass
