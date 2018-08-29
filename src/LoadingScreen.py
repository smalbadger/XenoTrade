from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QGroupBox

from time import sleep

class LoadingScreen(QGroupBox):
    def __init__(self, kernel, username=None, message=None, parent=None):
        super(LoadingScreen, self).__init__(parent)
        self.kernel = kernel
        self.name = username
        self.message = message

        self.loadMsg = QLabel("LOADING")
        self.loadMsg.setFixedWidth(100)
        self.loadMsg.setFixedHeight(100)
        self.loadMsg.setStyleSheet("font-size: 21px;")

        self.loadingSquares = []
        for i in range(8):
            newSquare = QLabel("")
            newSquare.setFixedWidth(100)
            newSquare.setFixedHeight(100)
            newSquare.setStyleSheet("background-color: purple")
            self.loadingSquares.append(newSquare)

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

    def startAnimation(self):
        self.stop = False
        self.animate()

    def stopAnimation(self):
        self.stop = True

    def animate(self):
        i = 0
        j = 0
        self.running = True
        print("Running!")
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

                self.kernel.app.processEvents()
                i += 1
            j += 1
        self.running = False
        print("Not Running!")