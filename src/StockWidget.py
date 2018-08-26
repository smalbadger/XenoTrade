from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QGroupBox

from Stock import Stock

class StockWidget(QGroupBox):
	def __init__(self, stock, parent=None):
		super(StockWidget, self).__init__(parent)
		self.stock = stock
		self.parent = parent
		self.initUI()
		
	def initUI(self):
		self.createElements()
		self.createLayout()
		self.createStyle()
		self.createActions()
		
	def createElements(self):
		name = self.stock.simpleName()
		if name == None:
			name = ""
		self.name = QLabel("<i>{}</i>".format(name))
		self.symbol = QLabel("<strong>{}</strong>".format(self.stock.symbol()))
		self.price = QLabel("${:.2f}".format(self.stock.lastTradePrice()))
		self.percentChange = QLabel("{:.3f}%".format(self.stock.percentChange()))

	def createLayout(self):
		self.nameLayout = QVBoxLayout()
		self.nameLayout.addWidget(self.symbol)
		self.nameLayout.addWidget(self.name)
		
		self.mainLayout = QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.mainLayout.addWidget(self.price)
		self.mainLayout.addWidget(self.percentChange)
		
		self.setLayout(self.mainLayout)
		
	def createStyle(self):
		tickerAndNameWidth = 100
		priceWidth = 80
		percentChangeWidth = 80
		styleStr = """
			QWidget#stock_widget
			{
				border: 		2px solid black; 
				border-radius: 	20px;
			}
			
			QWidget#stock_symbol
			{
				font-family: 	"Monospace", "Courier New";
				font-size: 		20px;
			}
			
			QWidget#stock_name
			{
				font-family:	Serif, Times;
				font-size:		11px;
			}
		"""
		self.name.setFixedWidth(tickerAndNameWidth)
		self.price.setFixedWidth(priceWidth)
		self.percentChange.setFixedWidth(percentChangeWidth)
		
		self.setObjectName("stock_widget")
		self.symbol.setObjectName("stock_symbol")
		self.name.setObjectName("stock_name")
		self.price.setObjectName("stock_price")
		self.percentChange.setObjectName
		self.setStyleSheet(styleStr)
		self.symbol.setStyleSheet("")
		
	def createActions(self):
		pass
