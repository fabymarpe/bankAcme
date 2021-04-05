from database import db


class UserManager:

    def __init__(self):
        self.collection = db.user

    def insert_one(self, user_id, pin):
        user_id = self.collection.insert({'user_id': user_id, 'pin': pin})
        return user_id

    def not_exist(self, filters):
        user = self.collection.find_one(filters)
        return user is None
