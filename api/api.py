from flask_restful import Api
from main import app
from resources.workflow import WorkFlowApi


acmeAPI = Api(app)

acmeAPI.add_resource(WorkFlowApi, '/workflow', endpoint='workflow')
