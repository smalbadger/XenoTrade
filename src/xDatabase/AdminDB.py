'''
Class:      AdminDB
Author(s):  Sam Badger
Date:       January 7, 2019
Type:       FINAL
Description:
            This class is the interface to the XenoTrade.Admin database.
            The admin database will be password protected once a user claims admin privileges. 
'''

import sys
from xDatabase.abstract.MongoClient import MongoClient

class AdminDB(MongoClient):
    def __init__(self):
        super().__init__()
        
    
