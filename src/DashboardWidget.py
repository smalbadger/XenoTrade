from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QScrollArea

from pprint import pprint
from Stock import Stock
from StockListWidget import StockListWidget


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
		self.scrollArea = QScrollArea()
		self.stockListWidget = StockListWidget(self.kernel)
			
	def createLayout(self):
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		self.layout.addWidget(self.scrollArea)
		self.scrollArea.setWidget(self.stockListWidget)
		
	def createActions(self):
		pass
