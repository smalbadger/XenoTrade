import logging

from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QLabel
from PySide2.QtCore import Signal

from xGUI import StockWidget
import xCore.Globals as GS

class StockListWidget(QGroupBox):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.createElements()
        self.createLayout()
        self.createActions()
        
    def createElements(self):
        self.stockWidgets = []
        self.securities = []
        kernel = GS.KERNEL
        for security in kernel.getCurrentUser().getSecuritiesOwned():
            self.securities.append(security)
            self.stockWidgets.append(Stock(security))
            
    def createLayout(self):
        self.layout = QVBoxLayout()
        for w in self.stockWidgets:
            self.layout.addWidget(w)
        self.setLayout(self.layout)
        
    def addStockWidget(self):
        pass
        
    def removeStockWidget(self):
        pass
               
    def createActions(self):
        pass
         
    def updateStockWidgets(self):
        for security in self.kernel.getCurrentUser().getSecuritiesOwned():
            # remove old widgets
            for w in self.stockWidgets:
                w.setParent(None)
             
            
            # create new widgets
            if security not in self.securities:
                self.securities.add(security)
                newWidget = Stock(security)
                self.stockWidgets.append(newWidget)
                self.layout.addWidget(newWidget)
                
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
