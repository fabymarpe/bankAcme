import json


class FileHelper:

    def __init__(self):
        pass

    @staticmethod
    def save_file():
        return 'workflow_example.json'

    @staticmethod
    def read_file(filename):
        with open(filename) as file:
            return json.load(file)
