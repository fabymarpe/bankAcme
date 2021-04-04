from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
from resources.workflow import WorkFlowApi

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/bankAcme"
mongodb_client = PyMongo(app)
db = mongodb_client.db


@app.route('/')
def hello():
    return "hello world too!"

acmeAPI = Api(app)
acmeAPI.add_resource(WorkFlowApi, '/workflow', endpoint='workflow')


if __name__ == '__main__':
    app.run()
