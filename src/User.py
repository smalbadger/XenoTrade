
from Robinhood      import Robinhood

class User:
	def __init__(self, kernel, directory):
		self.kernel		= kernel
		temp            = directory.strip('/')
		self.userName   = temp[temp.rfind('/')+1:]
		self.userDir	= directory
		self.verified   = False
		self.trader     = Robinhood()
		
	def __del__(self):
		try:
			self.trader.logout()
			self.verified = False
		except:
			return "Error: Logout failed (Unknown reason)"
		
	def verify(self, pwd):
		'''
		Uses the user's username and the password provided to login to 
		the robinhood API.
		
		Case 1) User is already logged in: 
				- return None
		Case 2) User is not logged in, but entered false credentials: 
				- return error (see below)
		Case 3) User is not logged in, but entered correct credentials: 
				- log user in and return None
		Case 4) Unknown error: 
				- return login failed error
		'''
		
		if self.verified:
			return
			
		try:
			self.verified = self.trader.login(username=self.userName, password=pwd)
			if not self.verified:
				return "Error: Your login credentials did not match with Robinhood's servers"
			self.verified = True
		except:
			return "Error: Login failed (Unknown reason)"
	
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
