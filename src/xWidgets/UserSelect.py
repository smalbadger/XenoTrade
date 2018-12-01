from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QLabel

import logging

from xWidgets.UserTile import UserTile

class UserSelect(QWidget):
    def __init__(self, kernel, parent=None):
        super(UserSelect, self).__init__(parent)
        self.kernel = kernel
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.createElements()
        self.createLayout()
        self.createActions()
        self.hideNewUserForm()
        self.hideLoginForm()
        
    def createElements(self):
        self.userButtons = [UserTile(u, self) for u in self.kernel.getAllUsers()]
        for b, u in zip(self.userButtons, self.kernel.getAllUsers()):
            b.setProfilePicture(self.kernel.getUsersDir()+u+'/profile/profile_pic.png')
            b.createLayout()
            
        self.newUserButton = QPushButton('New User')
        self.nevermindButton = QPushButton("Nevermind")
        self.newUserNameField = QLineEdit("Username")
        self.newUserPasswordField = QLineEdit("Password")
        self.newUserPasswordField.setEchoMode(QLineEdit.Password)
        self.newUserConfirmPasswordField = QLineEdit("Confirm Password")
        self.newUserConfirmPasswordField.setEchoMode(QLineEdit.Password)
        self.submitNewUserButton = QPushButton('submit')
        self.newUserNameErrorLabel = QLabel('')
        self.newPasswordErrorLabel = QLabel('')
        self.existingUserLoginField = QLineEdit('Password')
        self.existingUserLoginField.setEchoMode(QLineEdit.Password)
        self.existingUserLoginButton = QPushButton('Login')
        self.existingUserLoginErrorLabel = QLabel('')
        self.selectedUser = None
        
    def createLayout(self):
        self.existingUsersLayout = QHBoxLayout()
        self.existingUsersLayout.addStretch()
        for ub in self.userButtons:
            ub.resize(100,120)
            self.existingUsersLayout.addWidget(ub)
            self.existingUsersLayout.addStretch()
        
        self.formLayout = QVBoxLayout()
        self.formLayout.addStretch()
        self.formLayout.addWidget(self.newUserButton)
        self.formLayout.addWidget(self.nevermindButton)
        self.formLayout.addWidget(self.newUserNameField)
        self.formLayout.addWidget(self.newUserNameErrorLabel)
        self.formLayout.addWidget(self.newUserPasswordField)
        self.formLayout.addWidget(self.newUserConfirmPasswordField)
        self.formLayout.addWidget(self.newPasswordErrorLabel)
        self.formLayout.addWidget(self.submitNewUserButton)
        self.formLayout.addWidget(self.existingUserLoginField)
        self.formLayout.addWidget(self.existingUserLoginErrorLabel)
        self.formLayout.addWidget(self.existingUserLoginButton)
        self.formLayout.addStretch()
        
        self.lowLayout = QHBoxLayout()
        self.lowLayout.addStretch()
        self.lowLayout.addLayout(self.formLayout)
        self.lowLayout.addStretch()
        
        self.layout = QVBoxLayout(self)
        self.layout.addStretch()
        self.layout.addLayout(self.existingUsersLayout)
        self.layout.addLayout(self.lowLayout)
        self.layout.addStretch()
        
    def createActions(self):
        self.newUserButton.clicked.connect(self.revealNewUserForm)
        self.nevermindButton.clicked.connect(self.hideNewUserForm)
        self.submitNewUserButton.clicked.connect(self.submitNewUserRequest)
        self.existingUserLoginButton.clicked.connect(self.login)
        for btn in self.userButtons:
            btn.nameButton.clicked.connect(
                lambda:self.revealLoginForm(btn.nameButton.text())
            )
        
    def revealNewUserForm(self):
        self.hideLoginForm()
        self.newUserButton.hide()
        self.newUserNameField.show()
        self.newUserPasswordField.show()
        self.newUserConfirmPasswordField.show()
        self.submitNewUserButton.show()
        self.nevermindButton.show()
        
    def hideNewUserForm(self):
        self.newUserButton.show()
        self.newUserNameErrorLabel.hide()
        self.newPasswordErrorLabel.hide()
        self.newUserNameField.hide()
        self.newUserPasswordField.hide()
        self.newUserConfirmPasswordField.hide()
        self.submitNewUserButton.hide()
        self.nevermindButton.hide()
        
    def revealLoginForm(self, user):
        self.hideNewUserForm()
        self.selectedUser = user
        self.existingUserLoginButton.show()
        self.existingUserLoginErrorLabel.show()
        self.existingUserLoginField.show()
        
    def hideLoginForm(self):
        self.selectedUser = None
        self.existingUserLoginButton.hide()
        self.existingUserLoginErrorLabel.hide()
        self.existingUserLoginField.hide()
        
    def submitNewUserRequest(self):
        userName = self.newUserNameField.text()
        pwd = self.newUserPasswordField.text()
        conf_pwd = self.newUserConfirmPasswordField.text()
        
        err_msg = ''
        if pwd != conf_pwd:
            err_msg = 'Error: passwords do not match'
            self.newPasswordErrorLabel.setText(err_msg)
            self.newPasswordErrorLabel.show()
        else:
            self.newPasswordErrorLabel.hide()
            
        if self.kernel.userExists(userName):
            err_msg = 'Error: Username is already taken. Choose something else'
            self.newUserNameErrorLabel.setText(err_msg)
            self.newUserNameErrorLabel.show()
        else:
            self.newUserNameErrorLabel.hide()
            
        if err_msg != '':
            return
        
        err = self.kernel.addUser(userName, pwd)
        
        if err:
            self.newUserNameErrorLabel.setText(err)
            self.newPasswordErrorLabel.setText(err)
            self.newUserNameErrorLabel.show()
            self.newPasswordErrorLabel.show()
        else:
            self.parent.loadApplication()
        
    def login(self):
        assert(self.selectedUser != None)
        pwd = self.existingUserLoginField.text()
        if not self.kernel.switchUser(self.selectedUser, pwd):
            self.existingUserLoginErrorLabel.setText(err)
            self.existingUserLoginErrorLabel.show()
        else:
            self.parent.loadApplication()
