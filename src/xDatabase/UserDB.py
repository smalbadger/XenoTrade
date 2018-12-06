'''
Class:      UserDB
Author(s):  Sam Badger
Date:       December 5, 2018
Type:       FINAL
Description:
            <Your description here ...>
'''
import sys
from xDatabase.abstract.MongoClient import MongoClient

class UserDB(MongoClient):
    def __init__(self, username, password):
        super().__init__()
        
        status = self.login()
        if not status:
            #throw some exception
            sys.exit(3)
            
        self.switchDB("XenoTrade.users.{}".format(username))
        
        
    def login(self, username, password):
        ''' login to database '''
        return True
        
    def getAPICredentials(self, criteria):
        self.switchCollection("credentials")
        return self.findDocuments()
        
    def get
