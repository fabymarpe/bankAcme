import json
import os

import requests
from datetime import datetime

from werkzeug.utils import secure_filename

from constants import UPLOAD_FOLDER


class FileHelper:

    @staticmethod
    def save_file(file):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return filename

    @staticmethod
    def read_file(filename):
        my_file = os.path.join(UPLOAD_FOLDER, filename)
        with open(my_file) as file:
            return json.load(file)
