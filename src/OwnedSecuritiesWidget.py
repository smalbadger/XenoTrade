from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QLabel


class SecuritiesListWidget(QWidget):
	def __init__(self, kernel, parent=None):
		super(OwnedSecuritiesWidget, self).__init__(parent)
		self.kernel = kernel
		self.parent = parent
		self.initUI()
		self.securities = [] #each element should be a stock
		
	def initUI(self):
		self.createLayout()
		self.createActions()
		
	def createSecuritiesWidgets(self):
		owned = self.kernel.curUser.trader.securities_owned()
		for security in owned['results']:
			print(security['instrument'])
			ins = self.kernel.curUser.trader.instrument(security['instrument'])
			#pprint(ins)
			print("{}:".format(ins['name']))
			fund = self.kernel.curUser.trader.fundamentals(url=ins['fundamentals'])
			pprint(fund)
		#print(self.kernel.curUser.trader.instruments('CMG'))
		
	def createLayout(self):
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.nameLabel)
		self.setLayout(self.layout)
		
	def createActions(self):
		pass
