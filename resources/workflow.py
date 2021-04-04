import os

from flask_restful import Resource, request

from controllers.WorkFlowController import WorkFlowController
from util import fileHelper

from constants import UPLOAD_FOLDER


class WorkFlowApi(Resource):

    def post(self):
        """

        :return:
        """
        json_file = request.files.get('file')
        WorkFlowController().process_file(json_file)
