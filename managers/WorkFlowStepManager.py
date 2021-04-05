from database import db


class WorkFlowStepManager:

    def __init__(self):
        self.collection = db.step

    def insert_many(self, steps):
        """

        :return:
        """
        workflow_id = self.collection.insert_many(steps)

    def get(self, filters):
        workflow_step = self.collection.find_one(filters)
        return workflow_step

