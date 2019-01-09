import sys

from PySide2.QtWidgets import *
from PySide2.QtCore    import *
from PySide2.QtGui     import *

from resources.compiled.UserLoginTile import Ui_Form

class UserLoginTile(QWidget):
    userSelected = Signal(str)

    def __init__(self, username=None, profilePicPath=None):
        super().__init__()
        
        # load the UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        # set the username and profile picture if provided
        if username != None:
            self.ui.usernameBtn.setText(username)
            
        if profilePicPath != None:
            pixmap = QPixmap(profilePicPath)
            self.ui.profilePicLabel.setPixmap(pixmap)
            self.ui.profilePicLabel.setMask(pixmap.mask())
            self.ui.profilePicLabel.setText("")
        
        # connect the UI
        self.ui.usernameBtn.clicked.connect(self.onUserSelected)
        
    def resize(self, width, height):
        super().resize(width, height)
        
    def onUserSelected(self):
        self.userSelected.emit(self.ui.usernameBtn.text())
  
if __name__ == "__main__":

    username = "smalbadger"
    app = QApplication(sys.argv)
    widget = UserLoginTile("smalbadger", "../../Users/{}/profile/profile_pic.png".format(username))
    widget.show()
    sys.exit(app.exec_())
