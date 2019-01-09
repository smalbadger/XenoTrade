'''
Class:      LoginDialog
Author(s):  Sam Badger
Date:       Dec 14, 2018
Type:       FINAL
Description:
            This is the widget that controls the login of existing users AND the
            creation of new users
'''

import sys

from PySide2.QtWidgets import *
from PySide2.QtCore    import *
from PySide2.QtGui     import *

from resources.compiled.LoginDialog import Ui_Dialog


class LoginDialog(QWidget):
    def __init__(self):
        super().__init__()
        
        # load the UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # make local modifications and connect the UI
        self._completeUI()
        self._connectUI()
        
    def _completeUI(self):
        self.setWindowTitle("XenoTrade - Login")
        
    def _connectUI(self):
        pass
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    widget = LoginDialog()
    widget.show()
    
    sys.exit(app.exec_())
