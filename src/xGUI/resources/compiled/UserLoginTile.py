# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './designer/UserLoginTile.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.profilePicLabel = QtWidgets.QLabel(Form)
        self.profilePicLabel.setObjectName("profilePicLabel")
        self.verticalLayout.addWidget(self.profilePicLabel)
        self.usernameBtn = QtWidgets.QPushButton(Form)
        self.usernameBtn.setObjectName("usernameBtn")
        self.verticalLayout.addWidget(self.usernameBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.profilePicLabel.setText(_translate("Form", "profile picture goes here"))
        self.usernameBtn.setText(_translate("Form", "username goes here"))

