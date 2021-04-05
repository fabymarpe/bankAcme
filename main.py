from flask import Flask

from flask_restful import Api
from resources.workflow import WorkFlowApi

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello world too!"

acmeAPI = Api(app)
acmeAPI.add_resource(WorkFlowApi, '/workflow', endpoint='workflow')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
