from passlib.apache import HtpasswdFile

class User:
	def __init__(self, kernel, directory):
		self.kernel		= kernel
		temp            = directory.strip('/')
		self.userName   = temp[temp.rfind('/')+1:]
		self.userDir	= directory
		self.verified   = False
		self.credFile   = HtpasswdFile(directory + '.credentials.htpasswd')
		
	def __del__(self):
		pass
		
	def verify(self, password):
		print(self.credFile.users())
		assert(self.userName in self.credFile.users())
		self.verified = self.credFile.check_password(self.userName, password)
		
	def setPassword(self, pwd, verifyFirst=True):
		if verifyFirst:
			pass
		else:
			self.credFile.set_password(self.userName, pwd)
			self.credFile.save()
	
	
	def readSettings(self):
		pass
		
	def setSetting(self, key, value):
		pass
		
	def addStock(self):
		pass
		
	def addCurrency(self):
		pass
		
	def print(self):
		print("Username:", self.userName)
		print("UserDir: ", self.userDir)
		print("Verified:", self.verified)
