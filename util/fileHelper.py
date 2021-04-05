import json
import requests
from datetime import datetime


class FileHelper:

    @staticmethod
    def save_file():
        return 'workflow_example.json'

    @staticmethod
    def read_file(filename):
        with open(filename) as file:
            return json.load(file)
