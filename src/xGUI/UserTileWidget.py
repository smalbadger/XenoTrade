from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QLabel
from PySide2.QtGui     import QPixmap

from PySide2.QtCore import Signal

import logging

class UserTileWidget(QGroupBox):
    userSelected = Signal()

    def __init__(self, text='', picPath=''):
        super().__init__()
        
        self.nameButton = QPushButton(text)
        self.setProfilePicture(picPath)
        
        self.createLayout()
        self.createActions()
        
    def setProfilePicture(self, picPath):
        self.profPic = QLabel('')
        pixmap = QPixmap(picPath)
        self.profPic.setPixmap(pixmap)
        self.profPic.setMask(pixmap.mask())
        
    def createLayout(self):
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.profPic)
        self.layout.addWidget(self.nameButton)
        self.setLayout(self.layout)
        
    def createActions(self):
        self.nameButton.clicked.connect(self.onUserSelected)
        
    def resize(self, width, height):
        super(UserTile, self).resize(width, height)
        
    def onUserSelected(self):
        print("Selected User: {}".format(self.nameButton.text()))
  
if __name__ == "__main__":
    from PySide2.QtWidgets import QApplication
    import sys
    username = "smalbadger"
    app = QApplication(sys.argv)
    widget = UserTileWidget("smalbadger", "../../Users/{}/profile/profile_pic.png".format(username))
    widget.show()
    sys.exit(app.exec_())
