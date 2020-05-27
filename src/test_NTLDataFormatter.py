import unittest

from NTLDataFormatter import NTLDataFormatter
from UtilsTest import UtilsTest


class TestNTLDataFormatter(unittest.TestCase):
    def test_getNTLDataObjects(self):
        test_input = UtilsTest().get_ntl_mock_data()
        test_NTLDataFormatter = NTLDataFormatter()
        formatted_output = test_NTLDataFormatter.get_data_objects(test_input)

        self.assertEqual(len(formatted_output), 2)

    def test_validate_fields(self):
        test_input = UtilsTest().get_ntl_mock_data()
        test_NTLDataFormater = NTLDataFormatter()
        formatted_output = test_NTLDataFormater.get_data_objects(test_input)

        doc = test_input['response']['docs'][0]
        data = formatted_output[0]

        self.assertEqual(data.dh_source_name, 'ntl', 'Invalid dh_source_name')
        self.assertEqual(data.dh_type, 'Dataset', 'Invalid dh_type')
        self.assertEqual(data.dh_id, '{}-{}'.format(data.dh_source_name, doc['PID']), 'Invalid dh_id')
        self.assertEqual(data.id, doc['PID'], 'Invalid ID')
        self.assertEqual(data.name, doc['dc.title'][0], 'Invalid name')
        self.assertEqual(data.description, doc['mods.abstract'][0], 'Invalid description')
        self.assertEqual(data.access_level, 'Public', 'Invalid access_level')
        self.assertEqual(data.last_updated, doc['fgs.createdDate'], 'Invalid last_updated')
        self.assertEqual(len(data.tags), len(doc['mods.sm_key_words']), 'Invalid number of tags')
        id = data.id.split(':')[1]
        self.assertEqual(data.source_url, '{}{}'.format('https://rosap.ntl.bts.gov/view/dot/', id),
                         'Invalid source_url')
