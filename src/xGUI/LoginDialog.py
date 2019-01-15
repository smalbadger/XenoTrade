'''
Class:      LoginWidget
Author(s):  Sam Badger
Date:       Dec 14, 2018
Type:       FINAL
Description:
            This is the widget that controls the login of existing users AND the
            creation of new users
'''



import sys

if __name__ == "__main__":
    sys.path.insert(0, '..')

import re

from PySide2.QtWidgets import *
from PySide2.QtCore    import *
from PySide2.QtGui     import *

from resources.compiled.LoginDialog import Ui_Dialog

from xDatabase.UserDB import UserDB
from xDatabase.SharedDB import SharedDB
from xGUI.UserLoginTile import UserLoginTile
from xExceptions.UsernameError import UsernameError
from xUtils.UsernameValidator import UsernameValidator


class LoginDialog(QWidget, Ui_Dialog):
    def __init__(self):
        super().__init__()
        
        # group all user buttons together
        self.userTiles = {}
        self.selectedUser = None
        self.userBtnGroup = QButtonGroup()
        self.userBtnGroup.buttonClicked.connect(self.selectUser)
        
        
        # load the UI
        self.setupUi(self)
        
        self.setWindowTitle("XenoTrade - Login")
        self.hideSignUpFrame()
        self.hideSignInFrame()
        self.errorLabel.hide()
        
        self.loadUserTiles()
        self.signUpBtn.clicked.connect(self.showSignUpFrame)
        self.nevermindBtn_1.clicked.connect(self.resetUI)
        self.nevermindBtn_2.clicked.connect(self.resetUI)
        self.createAccountBtn.clicked.connect(self.createAccount)
        self.signInBtn.clicked.connect(self.signIn)
        self.usernameField.returnPressed.connect(self.checkValidUsername)
        self.usernameField.textChanged.connect(self.checkValidUsername)
        self.profilePicChooserBtn.clicked.connect(self.selectProfilePic)
        self.confirmNewPasswordField.textChanged.connect(self.checkPasswordMatch)
        
    def loadUserTiles(self):
        names = UserDB().getUserList()
        for name in names:
            sdb = SharedDB()
            img = sdb.getProfilePicture(name, "Pixmap")
            u = UserLoginTile(username=name)
            u.setProfilePic(img, picFormat="Pixmap")
            self.userTiles[name] = u
            self.userTileFrame.layout().addWidget(u)
            self.userBtnGroup.addButton(u.usernameBtn)
            
    def resetUI(self):
        if self.selectedUser != None:
            #remove selected user decorations
            self.userTiles[self.selectedUser].undecorate()    
            self.selectedUser = None
        
        self.userTileFrame.show()
        self.signUpBtn.show()
        self.hideErrorLabel()
        self.hideSignUpFrame()
        self.hideSignInFrame()
        
    def showSignUpFrame(self):
        self.userTileFrame.hide()
        self.signUpFrame.show()
        self.signUpBtn.hide()
        
    def showSignInFrame(self):
        self.signInFrame.show()
        self.signUpBtn.hide()
        
    def showErrorLabel(self, errorMessage):
        self.errorLabel.setText(errorMessage)
        self.errorLabel.show()
        
    def hideSignUpFrame(self):
        self.signUpFrame.hide()
        
    def hideSignInFrame(self):
        self.signInFrame.hide()
        
    def hideErrorLabel(self):
        self.errorLabel.hide()
        
    def selectProfilePic(self):
        dir = "~/"
        filters = "Images (*.png *.xpm *.jpg)"
        selected_filter = "Images (*.png *.xpm *.jpg)"
        fileObj = QFileDialog.getOpenFileName(None, " Profile Picture Chooser ", dir, filters, selected_filter)
        profilePicPath = fileObj[0]
        self.profilePicPathField.setText(profilePicPath)
        
    def createAccount(self):
        self.hideErrorLabel()
        
        # get user values from UI
        username = self.usernameField.text()
        profilePicPath = self.profilePicPathField.text()
        birthday = self.birthdayEditor.text()
        pwd = self.newPasswordField.text()
        cpwd= self.confirmNewPasswordField.text()
        
        # validate both username and password. If there's an exception, abort.
        try:
            UsernameValidator(username, silent=False)
            PasswordValidator(pwd, confirm=cpwd, silent=False)
        except:
            return
            
            
        userDB = UserDB()
        userDB.createUser(username, pwd, profilePicPath, birthday)
        
    def selectUser(self, btn):
        #if a user is already selected, undecorate it before selecting new user
        if self.selectedUser != None: 
            self.userTiles[self.selectedUser].undecorate()
              
        self.selectedUser = btn.text()
        self.userTiles[self.selectedUser].decorate()
        self.showSignInFrame()
        
    def signIn(self):
        username = self.selectedUser
        pwd = self.passwordField.text()
        
        # TODO: sign the user in. if successful, close this window and open dashboard.
        #       if failed, display error message and clear password field
        
    def checkValidUsername(self, username):
        self.usernameValidator = UsernameValidator(username, silent=True)
        
        
    def checkPasswordMatch(self):
        pwd = self.newPasswordField.text()
        cpwd= self.confirmNewPasswordField.text()
        if pwd != cpwd: 
            return False
        return True
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    widget = LoginDialog()
    widget.show()
    
    sys.exit(app.exec_())
