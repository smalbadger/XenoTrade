from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel

import logging

from Stock import Stock
from StockWidget import StockWidget

class StockListWidget(QWidget):
    def __init__(self, kernel, parent=None):
        super(StockListWidget, self).__init__(parent)
        logging.info("Creating the Stock List Widget")
        self.kernel = kernel
        self.parent = parent
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
            self.stockWidgets.append(StockWidget(security))
            
    def createLayout(self):
        logging.debug("Creating the Stock List Widget layout.")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        for w in self.stockWidgets:
            self.layout.addWidget(w)
        
    def createActions(self):
        logging.debug("Connecting the Stock List Widget's signals and slots.")
        pass
