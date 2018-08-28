from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel

from Stock import Stock
from StockWidget import StockWidget

class StockListWidget(QWidget):
	def __init__(self, kernel, parent=None):
		super(StockListWidget, self).__init__(parent)
		self.kernel = kernel
		self.parent = parent
		self.initUI()
		
	def initUI(self):
		self.createElements()
		self.createLayout()
		self.createActions()
		
	def createElements(self):
		self.stockWidgets = []
		for security in self.kernel.curUser.stocks(owned=True):
			self.stockWidgets.append(StockWidget(security))
			
	def createLayout(self):
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		for w in self.stockWidgets:
			self.layout.addWidget(w)
		
	def createActions(self):
		pass
