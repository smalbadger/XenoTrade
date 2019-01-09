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



class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        
        # load the UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.setWindowTitle("XenoTrade - Login")
        self.hideSignUpFrame()
        self.hideSignInFrame()
        self.ui.errorLabel.hide()
        
        self.loadUserTiles()
        self.ui.signUpBtn.clicked.connect(self.showSignUpFrame)
        self.ui.nevermindBtn_1.clicked.connect(self.resetUI)
        self.ui.nevermindBtn_2.clicked.connect(self.resetUI)
        self.ui.createAccountBtn.clicked.connect(self.createAccount)
        self.ui.signInBtn.clicked.connect(self.signIn)
        self.ui.usernameField.returnPressed.connect(self.checkValidUsername)
        
    def loadUserTiles(self):
        names = UserDB().getUserList()
        for name in names:
            pass
        
    def resetUI(self):
        self.ui.signUpBtn.show()
        self.hideErrorLabel()
        self.hideSignUpFrame()
        self.hideSignInFrame()
        
    def showSignUpFrame(self):
        self.ui.signUpFrame.show()
        self.ui.signUpBtn.hide()
        
    def showSignInFrame(self):
        self.ui.signInFrame.show()
        
    def showErrorLabel(self, errorMessage):
        self.ui.errorLabel.setText(errorMessage)
        self.ui.errorLabel.show()
        
    def hideSignUpFrame(self):
        self.ui.signUpFrame.hide()
        
    def hideSignInFrame(self):
        self.ui.signInFrame.hide()
        
    def hideErrorLabel(self):
        self.ui.errorLabel.hide()
        
    def createAccount(self):
        self.hideErrorLabel()
        
        username = self.ui.usernameField.text()
        if not self.checkValidUsername(username):
            self.showErrorLabel("Please change username")
            return
            
        pwd = self.ui.newPasswordField.text()
        cpwd= self.ui.confirmNewPasswordField.text()
        
        if pwd != cpwd:
            self.showErrorLabel("Passwords don't match")
            return
            
        # TODO: create new account using username and password
        
        
    def signIn(self):
        username = self.selectedUser
        pwd = self.ui.passwordField.text()
        
        # TODO: sign the user in. if successful, close this window and open dashboard.
        #       if failed, display error message and clear password field
        
    def checkValidUsername(self, username):
        # TODO: check if username is available
        
        if len(username) < 2:
            self.showErrorLabel("Your username must be at least 2 characters.")
            return False
            
        if re.search('[A-Z]',username) is None: 
            self.showErrorLabel("Your username must have at least one capital letter.")
            return False
            
        return True
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    widget = LoginDialog()
    widget.show()
    
    sys.exit(app.exec_())
