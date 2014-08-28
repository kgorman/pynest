import pymongo
from pymongo import MongoClient
from stathat import StatHat

class Database:
    def __init__(self, db_username, db_password, db_name, db_host, db_port, db_table):
        self.db_username = db_username
        self.db_password = db_password
        self.db_name = db_name
        self.db_host = db_host
        self.db_port = db_port
        self.db_table = db_table

    def persist(self, document):

        self.save_mongo(document)

    def save_mongo(self, document):

        try:
            self.connection = MongoClient(self.db_host, self.db_port)
            self.database = self.connection[self.db_name]
            self.database.authenticate(self.db_username, self.db_password)
            self.database[self.db_name].save(document)
        except:
            print "unable to save data"
