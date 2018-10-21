'''
Class:      LoadingScreenWidget
Author:     Sam Badger
Date:       12 Sept, 2018
Description:
            This is a widget that simply displays a loading screen. The loading screen updates 
            once per second and has 8 squares in a square formation with the words "LOADING" in
            the center.
'''

from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QGroupBox

from time import sleep
import logging

class LoadingScreen(QGroupBox):
    def __init__(self, kernel, username=None, message=None, parent=None):
        super(LoadingScreen, self).__init__()
        logging.info("Initializing the loading screen")
        self.kernel = kernel
        self.name = username
        self.message = message

        self.createElements()
        self.createStyle()
        self.createLayout()
        self.createActions()
        
    def createElements(self):
        logging.debug("Creating the loading screen elements")
        self.loadMsg = QLabel("LOADING")
        self.loadingSquares = []
        for i in range(8):
            newSquare = QLabel("")
            self.loadingSquares.append(newSquare)
        
    def createLayout(self):
        logging.debug("Creating the loading screen layout")
        vL = QVBoxLayout()

        hL = QHBoxLayout()
        hL.addWidget(self.loadingSquares[0])
        hL.addWidget(self.loadingSquares[1])
        hL.addWidget(self.loadingSquares[2])
        vL.addLayout(hL)
        hL = QHBoxLayout()
        hL.addWidget(self.loadingSquares[7])
        hL.addWidget(self.loadMsg)
        hL.addWidget(self.loadingSquares[3])
        vL.addLayout(hL)
        hL = QHBoxLayout()
        hL.addWidget(self.loadingSquares[6])
        hL.addWidget(self.loadingSquares[5])
        hL.addWidget(self.loadingSquares[4])
        vL.addLayout(hL)

        self.setLayout(vL)
        
    def createActions(self):
        logging.debug("Connecting the loading screen's signals and slots.")
        pass
    
    def createStyle(self):
        logging.debug("Setting the loading screen's style")
        self.loadMsg.setFixedWidth(100)
        self.loadMsg.setFixedHeight(100)
        self.loadMsg.setStyleSheet("font-size: 21px;")
        
        for i in range(8):
            self.loadingSquares[i].setFixedWidth(100)
            self.loadingSquares[i].setFixedHeight(100)
            self.loadingSquares[i].setStyleSheet("background-color: purple")

    def startAnimation(self):
        logging.info("Starting the loading screen's animation")
        self.stop = False
        self.animate()

    def stopAnimation(self):
        logging.info("Stopping the loading screen's animation")
        self.stop = True

    def animate(self):
        logging.info("Playing the loading screen's animation...")
        i = 0
        j = 0
        self.running = True
        while not self.stop:
            sleep(.001)
            if j >= 1000:
                j = 0
                k = i+4
                self.loadingSquares[i % 8].setStyleSheet("background-color: blue")
                self.loadingSquares[i % 8].repaint()
                self.loadingSquares[(i % 8) - 1].setStyleSheet("background-color: purple")
                self.loadingSquares[(i % 8) - 1].repaint()

                self.loadingSquares[k % 8].setStyleSheet("background-color: blue")
                self.loadingSquares[k % 8].repaint()
                self.loadingSquares[(k % 8) - 1].setStyleSheet("background-color: purple")
                self.loadingSquares[(k % 8) - 1].repaint()

                self.kernel.getApp().processEvents()
                i += 1
            j += 1
        self.running = False
