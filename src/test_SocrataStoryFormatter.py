import unittest

from SocrataStoryFormatter import SocrataStoryFormatter
from UtilsTest import UtilsTest


class TestSocrataStoryFormatter(unittest.TestCase):
    def test_getSocrataStoryObjects(self):
        test_inputs = UtilsTest().get_story_mock_data()
        test_socrata_story_formatter = SocrataStoryFormatter()
        formatted_results = test_socrata_story_formatter.get_data_objects(test_inputs, "story")

        assert len(formatted_results) == 2
        assert formatted_results[0].dh_source_name == "story"

    def test_validate_fields_dtg(self):
        test_input = UtilsTest().get_dtg_mock_data()
        test_socrata_story_formatter = SocrataStoryFormatter()
        formatted_results = test_socrata_story_formatter.get_data_objects(test_input, "story")

        doc = test_input['results'][0]
        data = formatted_results[0]

        self.assertEqual(data.dh_type, 'Document')
        self.assertEqual(data.dh_source_name, 'story', 'Invalid dh_source_name')
        self.assertEqual(data.dh_id, '{}-{}'.format(data.dh_source_name, doc['resource']['id']), 'Invalid dh_id')
        self.assertEqual(data.id, doc['resource']['id'], 'Invalid ID')
        self.assertEqual(data.name, doc['resource']['name'], 'Invalid name')
        self.assertEqual(data.description, doc['resource']['description'], 'Invalid description')
        self.assertEqual(data.access_level, 'Public', 'Invalid access_level')
        udt = doc['resource']['updatedAt']
        udt = udt[0: 19] + 'Z'
        self.assertEqual(data.last_updated, udt, 'Invalid last_updated')
        self.assertEqual(len(data.tags), len(doc['classification']['domain_tags']), 'Invalid number of tags')
        self.assertEqual(data.source_url, doc['link'], 'Invalid source_url')
        self.assertEqual(data.metrics['downloadsTotal'], doc['resource']['download_count'])
        self.assertEqual(data.metrics['pageViewsLastMonth'], doc['resource']['page_views']['page_views_last_month'])
        self.assertEqual(data.metrics['pageViewsTotal'], doc['resource']['page_views']['page_views_total'])
