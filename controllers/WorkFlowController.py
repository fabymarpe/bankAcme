import os

from constants import UPLOAD_FOLDER
from util.fileHelper import FileHelper


class WorkFlowController:

    def process_file(self, json_file):
        if json_file:
            file_helper = FileHelper()
            filename = file_helper.save_file()
            my_file = os.path.join(UPLOAD_FOLDER, filename)
            workflow_data = file_helper.read_file(my_file)
