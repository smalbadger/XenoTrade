import os
import time
from datetime import datetime
from distutils.dir_util import copy_tree

from User import User

class Kernel:
	def __init__(self, user=None):
		self.currentUser = user
		self.baseDir     = os.getcwd().replace('\\','/')[:-3]
		self.usersDir    = self.baseDir + 'Users/'
		self.curUser     = None
		
	def __del__(self):
		pass
		
	def __str__(self):
		pass
		
	###########################################################################
	#####                           USER METHODS                          #####
	###########################################################################
	def switchUser(self, username, password):
		self.curUser = User(self, self.usersDir + username + '/')
		self.curUser.verify(password)
		if not self.curUser.verified:
			self.curUser = None
			return False
		return True
		
	def getAllUsers(self):
		users = os.listdir(self.baseDir + 'Users/')
		users.remove('.__template__')
		if users == None:
			users = []
		return users
		
	def currentUser(self):
		return self.curUser
	
	def addUser(self, username, password):
		template = self.usersDir + '.__template__/'
		newUserDir = self.usersDir + username + '/'
		os.mkdir(newUserDir)
		copy_tree(template, newUserDir)
		
		self.curUser = User(self, self.usersDir + username + '/')
		self.curUser.setPassword(password, verifyFirst=False)
		self.switchUser(username, password)
		
	def userExists(self, user):
		return user in self.getAllUsers()
		
		
	###########################################################################
	#####                          STOCK METHODS                          #####
	###########################################################################
	def getCurrentUserStocks(self):
		pass
		
	###########################################################################
	#####                       CURRENCY METHODS                          #####
	###########################################################################
	def getCurrentUserCurrencies(self):
		pass
		
	###########################################################################
	#####                        SETTING METHODS                          #####
	###########################################################################
	def getCurrentUserSettings(self):
		pass
		
		
		
if __name__ == '__main__':
	k = Kernel()
	print("-------------------------- KERNEL PROPERTIES --------------------------")
	print("baseDir: {}".format(k.baseDir))
	print("getAllUsers: {}".format(k.getAllUsers()))
