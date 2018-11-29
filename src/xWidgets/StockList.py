import logging

from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel

from xWidgets.Stock import Stock
from xCore.abstract.Updatable import Updatable

import time
import threading

class StockList(Updatable, QWidget):
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
        for security in self.kernel.getCurrentUser().getSecuritiesOwned():
            self.stockWidgets.append(Stock(security, self))
            
    def createLayout(self):
        logging.debug("Creating the Stock List Widget layout.")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        for w in self.stockWidgets:
            self.layout.addWidget(w)
        
    def createActions(self):
        logging.debug("Connecting the Stock List Widget's signals and slots.")
        pass
         
    def updateStockWidgets(self):
        logging.debug("CHANGE THIS -- ONLY FOR TESTING -- GETTING NEW STOCKS")
        print("Mama thread: {}".format(threading.get_ident()))
        self.createElements()
        self.createLayout()
        
        self.hide()
        self.show()
        '''
        for stock in self.stockWidgets:
            stock.hide()
            stock.show()
        '''
    def __str__(self):
        return "StockList widget"
            
