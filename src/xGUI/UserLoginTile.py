import sys

from PySide2.QtWidgets import *
from PySide2.QtCore    import *
from PySide2.QtGui     import *

from resources.compiled.UserLoginTile import Ui_Form

class UserLoginTile(QWidget, Ui_Form):
    userSelected = Signal(str)

    def __init__(self, username=None, profilePicPath=None):
        super().__init__()
        
        # load the UI
        self.setupUi(self)
        
        # set the username and profile picture if provided
        if username != None:
            self.usernameBtn.setText(username)
            
        if profilePicPath != None:
            pixmap = QPixmap(profilePicPath)
            self.setProfilePic(pixmap, picFormat="Pixmap")
        
        # connect the UI
        self.usernameBtn.clicked.connect(self.onUserSelected)
        
    def onUserSelected(self):
        self.userSelected.emit(self.usernameBtn.text())
        
    def setProfilePic(self, pic, picFormat="Pixmap"):
        if picFormat == "File":
            pic = QPixmap(pic)
            picFormat = "Pixmap"
    
        if picFormat == "Pixmap":
            self.profilePicLabel.setPixmap(pic)
            self.profilePicLabel.setMask(pic.mask())
            self.profilePicLabel.setText("")
            
    def decorate(self):
        self.setStyleSheet("background-color: green")
        
    def undecorate(self):
        self.setStyleSheet("background-color: white")
  
if __name__ == "__main__":

    username = "smalbadger"
    app = QApplication(sys.argv)
    widget = UserLoginTile("smalbadger", "../../Users/{}/profile/profile_pic.png".format(username))
    widget.show()
    sys.exit(app.exec_())
