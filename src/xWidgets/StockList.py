import logging

from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QLabel
from PySide2.QtCore import Signal

from xWidgets.Stock import Stock
from xCore.abstract.Updatable import Updatable

import time
import threading

class StockList(Updatable, QGroupBox):
    updateComplete = Signal(bool) #emit this signal when an update is done.
    
    def __init__(self, kernel, parent):
        super(StockList, self).__init__()
        self.kernel = kernel
        self.addParent(parent)
        self.addUpdateFunction(self.updateStockWidgets)
        self.addUpdateFunction(self.update)
        self.kernel.getUpdateGraph().addUpdatable(self)
        self.initUI()
        
    def initUI(self):
        self.createElements()
        self.createLayout()
        self.createActions()
        
    def createElements(self):
        self.stockWidgets = []
        for security in self.kernel.getCurrentUser().getSecuritiesOwned():
            self.stockWidgets.append(Stock(security, self))
            
    def createLayout(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        for w in self.stockWidgets:
            self.layout.addWidget(w)
        
    def createActions(self):
        pass
         
    def updateStockWidgets(self):
        print("Mama thread: {}".format(threading.get_ident()))
        self.createElements()
        print("elements created")
        self.createLayout()
        print("layout created")
        
        self.hide()
        print("hidden")
        self.show()
        print("shown")
        
        for stock in self.stockWidgets:
            stock.hide()
            stock.show()
        print("flashed")
        
    def __str__(self):
        return "StockList widget"
            
    def runUpdates(self):
        updateStatus = super().runUpdates()
        self.updateComplete.emit(updateStatus)
        
if __name__ == "__main__":
    # imports 
    from PySide2.QtWidgets import QApplication
    import sys
    
    app = QApplication(sys.argv)
    widget = StockList()
    widget.updateText(name="XenoTrade", symbol="XTL", price=100.00, change=.46)
    widget.show()
    sys.exit(app.exec_())
