from pymongo import MongoClient
from decouple import config
# from database import *


class NoSqlClient():
    
    def __init__(self):
        try:
            self.my_client = MongoClient(config('NOSQL_DATABASE_URI'))
            print('MongoDB connection successful!!!')
        except Exception as e:  
            print(f'Could not connect to MongoDB, Error: {e}')
        self.my_db = self.my_client[config('NOSQL_DB_NAME')]
            
    def add_to_collection(self, collection: str, key: dict ,value: dict) -> None:
        my_collection = self.my_db[collection]
        my_collection.update_one(key, value, upsert=True)
        # my_collection.insert_one(value)
    
    def update_collection(self, collection: str, key: dict, value: dict) -> None:
        my_collection = self.my_db[collection]
        my_collection.update_one(key, value)

nosql = NoSqlClient()
''' THIS CODE IS ONLY FOR TRY 

# class NoSqlClient():
#     def __init__(self):
#         try:
#             self.mydb = mysql.connector.connect(
#                 host = " ",
#                 user = " ",
#                 password = " "
#             )
#             print("MySql Connected Succesfully")
#         except Exception as e:
#             print(f"Could not connect to MySqldb , Error{e}")

    
#     def add_to_collection(self, collection: str, key: dict ,value: dict) -> None:
#         my_collection = self.mydb[collection]
#         my_collection.update_one(key, value, upsert=True)
#         my_collection.insert_one(value)



'''