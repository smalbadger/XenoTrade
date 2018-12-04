'''
Class:      MongoClient
Author(s):  Sam Badger
Date:       December 4, 2018
Type:       FINAL
Description:
            Communicate with MongoDB
            
Notes:      If it hangs forever when you make a query, try starting the service:
                > sudo service mongodb start
'''

import os
import sys

import logging
import pymongo
from bson.objectid import ObjectId

class MongoClient():
    def __init__(self):
        super().__init__()
        
        self.initClient()
        
        
    
    def initClient(self):
        try:
            self._client = pymongo.MongoClient('localhost', 27017)
        except:
            # logging.critical("Failed to create mongo client. Make sure MongoDB is installed and started.")
            print("Error: Couldn't connect to mongo instance")
            sys.exit(2)
            
    def switchDB(self, dbName):
        ''' switch databases '''
        self._db = self._client[dbName]
        
    def switchCollection(self, collectionName):
        ''' switch to a collection inside self._db '''
        self._collection = self._db[collectionName]
        
    def insertDocument(self, document):
        ''' insert one document '''
        result = self._collection.insert_one(document)
        return result
        
    def insertDocuments(self, documents):
        ''' insert many documents '''
        result = self._collection.insert_many(documents)
        return result.inserted_ids
        
    def findDocument(self, criteria={}):
        ''' find a single documents '''
        if '_id' in criteria and type(criteria['_id']) == str:
            criteria['_id'] = ObjectId(criteria['_id'])
        return self._collection.find_one(criteria)
        
    def findDocuments(self, criteria={}):
        ''' find multiple documents (returns cursor) '''
        return self._collection.find(criteria)
        
    def countDocuments(self, criteria={}):
        ''' get the number of all documents fitting the criteria '''
        return self._collection.count_documents(criteria)
        
        
        
                

if __name__ == "__main__":
    client = MongoClient()
    client.switchDB("XenoTrade")
    client.switchCollection("users.smalbadger")
    client.insertDocument({"Date Created": "October 4, 2018"})
    for i in client.findDocuments():
        print(i)
    print(client.countDocuments())
    
    
    
    
