import logging

from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QGroupBox

import threading

class Stock(QGroupBox):
    tickerAndNameWidth = 100
    priceWidth = 80
    percentChangeWidth = 80
    
    baseStyle = """
        QWidget#stock_widget
        {
            border:         2px solid black; 
            border-radius:     20px;
        }
        
        QWidget#stock_symbol
        {
            font-family:     "Monospace", "Courier New";
            font-size:         30px;
        }
        
        QWidget#stock_name
        {
            font-family:    Serif, Times;
            font-size:        11px;
        }
    """
    
    goodStyle = """
        QWidget#stock_percent_change
        {
            color:            green;
        }
    """
    
    badStyle = """
        QWidget#stock_percent_change
        {
            color:            red;
        }
    """
    
    def __init__(self, stock=None, parent=None):
        super(Stock, self).__init__(parent)
        logging.info("Initializing Stock Widget")
        self.stock = stock
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        logging.debug("Initializing the stock widget's UI")
        self.createElements()
        self.updateText()
        self.createLayout()
        self.createStyle()
        self.createActions()
        self.update()
        
    def createElements(self):
        logging.debug("creating the stock widget's elements.")
        self.name = QLabel()
        self.symbol = QLabel()
        self.price = QLabel()
        self.percentChange = QLabel()
       
    def createLayout(self):
        logging.debug("creating the stock widget's layout")
        self.nameLayout = QVBoxLayout()
        self.nameLayout.addWidget(self.symbol)
        self.nameLayout.addWidget(self.name)
        
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.nameLayout)
        self.mainLayout.addWidget(self.price)
        self.mainLayout.addWidget(self.percentChange)
        
        self.setLayout(self.mainLayout)
        
    def createStyle(self):
        logging.debug("setting the stock widget's style")
        self.name.setFixedWidth(Stock.tickerAndNameWidth)
        self.price.setFixedWidth(Stock.priceWidth)
        self.percentChange.setFixedWidth(Stock.percentChangeWidth)
        
        self.setObjectName("stock_widget")
        self.symbol.setObjectName("stock_symbol")
        self.name.setObjectName("stock_name")
        self.price.setObjectName("stock_price")
        self.percentChange.setObjectName("stock_percent_change")
        
    def setStock(self, stock):
        self.stock = stock
    
    def updateText(self):
        logging.debug("Updating stock widget's data")
        if self.stock != None:
            name = self.stock.simpleName()
            if name == None:
                name = ""
            self.name.setText("<i>{}</i>".format(name))
            self.symbol.setText("<strong>{}</strong>".format(self.stock.symbol()))
            self.price.setText("${:.2f}".format(self.stock.lastTradePrice()))
            self.percentChange.setText("{:.3f}%".format(self.stock.percentChange()))

    def updateStyle(self):
        logging.debug("updating the stock widget's style")
        styleStr = Stock.baseStyle
        pc = self.stock.percentChange()
        
        if   pc > 0:
            styleStr += Stock.goodStyle
        elif pc < 0:
            styleStr += Stock.badStyle
            
        self.setStyleSheet(styleStr)
        
    def createActions(self):
        logging.debug("Connecting the stock widget's signals and slots")
        #NOTE: No actions are set 
        pass
