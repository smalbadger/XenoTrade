from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel

from PySide2.QtGui     import QPixmap

class UserTile(QWidget):

	def __init__(self, text='', parent=None):
		super(UserTile, self).__init__(parent)
		self.parent = parent
		self.nameButton = QPushButton(text)
		
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
		self.nameButton.clicked.connect(lambda: self.parent.revealLoginForm(self.nameButton.text()))
		
	def resize(self, width, height):
		super(UserTile, self).resize(width, height)
		
	
		
