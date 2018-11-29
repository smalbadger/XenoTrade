import logging

from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel
from PySide2.QtCore import Signal

from xWidgets.Stock import Stock
from xCore.abstract.Updatable import Updatable

import time

class StockList(Updatable, QWidget):
    MAX_STOCKS = 100
    updateStockWidgetSignals = [Signal() for i in range(MAX_STOCKS)]

    def __init__(self, kernel, parent):
        super(StockList, self).__init__()
        logging.info("Creating the Stock List Widget")
        self.kernel = kernel
        self.addParent(parent)
        self.addUpdateFunction(self.updateStockWidgets)
        self.addUpdateFunction(self.update)
        self.kernel.getUpdateManager().addUpdatable(self)
        self.initUI()
        
    def initUI(self):
        logging.debug("Creating the Stock List Widget UI.")
        self.createElements()
        self.createLayout()
        self.createActions()
        
    def createElements(self):
        logging.debug("Creating the Stock List Widget elements")
        self.stockWidgets = []
        for i in range(StockList.MAX_STOCKS):
            self.stockWidgets.append(Stock(None, self))
        
    def createLayout(self):
        logging.debug("Creating the Stock List Widget layout.")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        for w in self.stockWidgets:
            if w.stock == None:
                break
            self.layout.addWidget(w)
        
    def createActions(self):
        logging.debug("Connecting the Stock List Widget's signals and slots.")
        securities = self.kernel.getCurrentUser().getSecuritiesOwned()
        length = len(securities)
        for i in range(length):
            StockList.updateStockWidgetSignals[i].connect(self.stockWidgets[i].updateText())
         
    def updateStockWidgets(self):
        logging.debug("CHANGE THIS -- ONLY FOR TESTING -- GETTING NEW STOCKS")
        
        securities = self.kernel.getCurrentUser().getSecuritiesOwned()
        length = len(securities)
        for i in range(length):
            if i >= StockList.MAX_STOCKS:
                break
            sec = securities.pop()
            self.stockWidgets[i].setStock(sec)
            StockList.updateStockWidgetSignals[i].emit()
            #self.stockWidgets[i].updateText()
            securities.add(sec)
        
        self.createLayout()
        
        for stock in self.stockWidgets:
            if stock.stock == None:
                break
            stock.show()
        self.show()
        
    def __str__(self):
        return "StockList widget"
            
