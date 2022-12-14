from pymongo import MongoClient
from bson.json_util import dumps



class Database:
    def __init__(self):
        self.client = MongoClient('momgodb://root:root@monguito:27017')
    
    
        database = 'marvel_comics'
        collection = 'users'
        cursor =self.client[database]
        self.collection =cursor[collection]


    def read(self,credentials):
        return self.collection.find_one(credentials)
    
    def read(self,credentials):
        return self.collection.find_one(credentials)

    def write(self, new_document):
        response = self.collection.insert_one(new_document)
        new_document['_id'] = str(response.inserted_id)
        new_document.pop('password', None)
        new_document.pop('_id', None)
        return dumps(new_document)
