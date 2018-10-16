from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel
from PySide2.QtGui     import QPixmap

import logging

class UserTileWidget(QWidget):

    def __init__(self, text='', parent=None):
        logging.info("Creating {}'s user tile".format(text))
        super(UserTileWidget, self).__init__(parent)
        self.parent = parent
        self.nameButton = QPushButton(text)
        
    def setProfilePicture(self, picPath):
        logging.debug("Setting the user tile's profile picture")
        self.profPic = QLabel('')
        pixmap = QPixmap(picPath)
        self.profPic.setPixmap(pixmap)
        self.profPic.setMask(pixmap.mask())
        
    def createLayout(self):
        logging.debug("Creating the user tile's layout")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.profPic)
        self.layout.addWidget(self.nameButton)
        self.setLayout(self.layout)
        
    def createActions(self):
        logging.debug("Connecting the user tile's signals and slots.")
        self.nameButton.clicked.connect(lambda: self.parent.revealLoginForm(self.nameButton.text()))
        
    def resize(self, width, height):
        logging.debug("Resizing the user's tile.")
        super(UserTileWidget, self).resize(width, height)
        
    
        
