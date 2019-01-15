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
import base64
from PIL import Image

from xDatabase.abstract.MongoClient import MongoClient
from xDatabase.SharedDB import SharedDB

class UserDB(MongoClient):
    def __init__(self, username=None, password=None):
        super().__init__()
        
        if username != None:
            existingUsers = self.getUserList()
            if username in existingUsers:
                # if the database already exists, login
                status = self.login()
                if not status:
                    # TODO: throw some exception
                    sys.exit(3)
                
        
    def login(self, username, password):
        ''' login to database '''
        self.authenticate(username, password, source='XenoTrade_user_'+username)
        return True
        
    def createUser(self, username, password, profilePicPath=None, birthday=None):
        user_DB = "XenoTrade_user_"+username
        
        self.switchDB(user_DB)
        self.database().add_user(username, password, roles=[{'role':'readWrite','db':user_DB}])
        self.switchCollection("personal_particulars")
        
        doc = {}
        doc['username'] = username
        doc['password'] = password
        doc['birthday'] = birthday
        
        if profilePicPath:
            # get picture size
            with Image.open(profilePicPath) as pic:
                width, height = pic.size
            # encode image as string
            with open(profilePicPath, "rb") as profilePicture:
                picStr = base64.b64encode(profilePicture.read())
            # insert image data into the collection
            doc['profile_picture'] = {"base64_string":picStr, "name":profilePicPath, "width":width, "height":height}
        else:
            doc['profile_picture'] = None
         
        self.insertDocument(doc)
        
        # Add the picture to the shared database to access it without being logged in
        SharedDB().setProfilePicture(username, profilePicPath)

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
        
        
