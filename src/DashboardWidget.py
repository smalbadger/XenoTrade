'''
Class:      DashboardWidget
Author:     Sam Badger
Date:       12 Sept, 2018
Description:
            This is a large widget that contains any widgets you may want in a trading application.
            It should be fairly self explanatory, so not many comments are needed.
'''
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QScrollArea

from pprint import pprint
import logging

from Stock import Stock
from StockListWidget import StockListWidget


class DashboardWidget(QWidget):
    def __init__(self, kernel, parent=None):
        super(DashboardWidget, self).__init__()
        logging.info("Initializing Dashboard Widget.")
        self.kernel = kernel
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        logging.debug("Initializing the Dashboard's user interface.")
        self.createElements()
        self.createLayout()
        self.createActions()
        
    def createElements(self):
        logging.debug("Creating the Dashboard's elements.")
        self.scrollArea = QScrollArea()
        self.stockListWidget = StockListWidget(self.kernel)
            
    def createLayout(self):
        logging.debug("Creating the Dashboard's layout.")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.scrollArea)
        self.scrollArea.setWidget(self.stockListWidget)
        
    def createActions(self):
        logging.debug("Connecting the Dashboard's signals and slots.")
        pass
