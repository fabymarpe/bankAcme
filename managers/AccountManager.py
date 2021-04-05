from database import db


class AccountManager:

    def __init__(self):
        self.collection = db.account

    def insert_one(self, user_id):
        account_id = self.collection.insert({'user_id': user_id, 'balance': 0})
        return account_id

    def get(self, filters):
        """

        :param filters:
        :return:
        """
        return self.collection.find_one(filters)

    def update(self, query, update):
        return self.collection.update_one(query, {"$set": update})
