'''
Class:      StockGrabber
Author(s):  Sam Badger
Date:       October 4, 2018
Type:       FINAL
Description:
            interface to easily grab stock data from mongoDB
'''

from xDatabase.abstract.MongoClient import MongoClient

class StockGrabber(MongoClient):
    def __init__(self):
        super().__init__()
        
        
        
