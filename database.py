import pymongo

mongo_client = pymongo.MongoClient('mongodb://localhost:27017/bankAcme')
db = mongo_client.get_default_database()



