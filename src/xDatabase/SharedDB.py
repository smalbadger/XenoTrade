'''
Class:      UserDB
Author(s):  Sam Badger
Date:       December 5, 2018
Type:       FINAL
Description:
            <Your description here ...>
'''

import os
import sys
import base64
from PIL import Image

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from xDatabase.abstract.MongoClient import MongoClient

class SharedDB(MongoClient):
    def __init__(self):
        super().__init__()
        self.switchDB("XenoTrade_shared")
        
    def setProfilePicture(self, username, profilePicPath):
        self.switchCollection("profile_pictures")
        
        doc = {}
        doc['username'] = username
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
        
    def getProfilePicture(self, username, picFormat="Pixmap"):
        """
        picFormat is the way that the image will be returned to the caller. Here are the
        different formats supported:
            Image   - a PIL.Image object
            File    - an image file is created and the path to the file is returned
            Pixmap  - a QPixmap object
        """
        self.switchCollection("profile_pictures")
        
        #find the document
        picDoc = self.findDocument({'username':username})['profile_picture']
        
        #if the user did not select a profile picture, return None
        if not picDoc:
            return None
            
        picStr = picDoc["base64_string"]
        width = picDoc["width"]
        height = picDoc["height"]
        
        name = picDoc["name"].split("/")[-1]
        tempName = "temp_"+name
        with open(tempName, "wb") as tempFile:
            tempFile.write(base64.b64decode(picStr))
            
        if picFormat == "Image":
            img = Image.open(tempName)
            os.remove(tempName)
            return img
            
        if picFormat == "File":
            return tempName
            
        if picFormat == "Pixmap":
            pixmap = QPixmap(tempName)
            os.remove(tempName)
            return pixmap
