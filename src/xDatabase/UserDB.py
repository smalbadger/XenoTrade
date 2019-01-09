'''
Class:      UserDB
Author(s):  Sam Badger
Date:       December 5, 2018
Type:       FINAL
Description:
            <Your description here ...>
'''

# TODO: verify that user authentication is working


import sys

from xDatabase.abstract.MongoClient import MongoClient

class UserDB(MongoClient):
    def __init__(self, username=None, password=None):
        super().__init__()
        
        if username != None:
            existingUsers = self.getUserList
            if username in existingUsers:
                # if the database already exists, login
                status = self.login()
                if not status:
                    # TODO: throw some exception
                    sys.exit(3)
   
            else:
                assert password != None
                # create the user's database, 
                self.switchDB("XenoTrade_user_"+username)
                # create user with password and authorize the user to read/write their database,
                self.database().add_user(username, password, read_only=False, roles=[{'role':'readWrite','db':'XenoTrade_user_'+username}])
            
            self.switchDB("XenoTrade_user_{}".format(username))
        
    def login(self, username, password):
        ''' login to database '''
        self.authenticate(username, password, source='XenoTrade_user_'+username)
        return True
        
    def getAPICredentials(self, criteria):
        self.switchCollection("credentials")
        return self.findDocuments()
        
    def getUserList(self):
        users = []
        prefix = "XenoTrade_user_"
        for db in self._client.list_database_names():
            if prefix in db:
                users.append(db[len(prefix):])
        return users
        
        
