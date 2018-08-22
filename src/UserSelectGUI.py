from PySide2 import QtCore

from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow

import sys
import os

from Kernel import Kernel
from UserSelectWidget import UserSelectWidget


class UserSelectGUI(QMainWindow):
	def __init__(self, kernel, parent=None):
		super(UserSelectGUI, self).__init__(parent)
		self.kernel = kernel
		self.widget = UserSelectWidget(kernel, self)
		self.setCentralWidget(self.widget)
		
		
if __name__ == '__main__':
	kernel = Kernel()
	app = QApplication(sys.argv)
	frame = UserSelectGUI(kernel)
	frame.show()
	app.exec_()
