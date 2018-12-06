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
from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QScrollArea
from PySide2.QtCore import Signal

from pprint import pprint
import logging

import xCore.Globals as GS
from xCore.abstract.Updatable import Updatable
from xCore.abstract.XenoObject import XenoObject
from xGUI import StockListWidget


class DashboardWidget(QGroupBox):
    updateComplete = Signal(bool) #emit this signal when an update is done.
    def __init__(self, ):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.createElements()
        self.createLayout()
        self.createActions()
        
    def createElements(self):
        self.scrollArea = QScrollArea()
        self.stockListWidget = StockList()
            
    def createLayout(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.scrollArea)
        self.scrollArea.setWidget(self.stockListWidget)
        
    def createActions(self):
        pass
        
    def __str__(self):
        return "Dashboard Widget"
