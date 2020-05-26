import os
import json


class UtilsTest(object):
    def __init__(self):
        super().__init__()
        self.base_path = os.path.dirname(os.path.realpath(__file__))

    def get_ntl_mock_data(self):
        with open(self.base_path+os.sep+'mock_dataset_ntl.json', 'r', encoding='utf-8') as mock_file:
            data = json.load(mock_file)
        return data

    def get_dtg_mock_data(self):
        with open(self.base_path+os.sep+'mock_dataset_dtg.json', 'r', encoding='utf-8') as mock_file:
            data = json.load(mock_file)
        return data

    def get_scgc_mock_data(self):
        with open(self.base_path+os.sep+'mock_dataset_scgc.json', 'r', encoding='utf-8') as mock_file:
            data = json.load(mock_file)
        return data

    def get_story_mock_data(self):
        with open(self.base_path+os.sep+'mock_dataset_story.json', 'r', encoding='utf-8') as mock_file:
            data = json.load(mock_file)
        return data
