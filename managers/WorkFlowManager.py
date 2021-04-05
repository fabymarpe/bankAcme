from datetime import datetime

from bson import ObjectId

from database import db


class WorkFlowManager:

    def __init__(self):
        self.collection = db.workflow

    def insert_one(self, trigger):
        """

        :return:
        """
        workflow_id = self.collection.insert({'trigger': trigger, 'datetime': datetime.utcnow(), 'result': None})
        return workflow_id

    def findById(self, id):
        workflow = self.collection.find_one({"_id": ObjectId(id)})
        return workflow
