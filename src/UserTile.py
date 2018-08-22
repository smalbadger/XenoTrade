from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel
from PySide2.QtGui     import QIcon

class UserTile(QPushButton):
	def __init__(self, text=''):
		super(UserTile, self).__init__(text)
		self.setBaseSize(100, 120)
		
	def setProfilePicture(self, picPath):
		self.setIcon(QIcon(picPath))
		
	
		
