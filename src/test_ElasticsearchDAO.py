import unittest
import responses
import os

from ElasticsearchDAO import ElasticsearchDAO

class TestElasticsearchDAO(unittest.TestCase):
    @responses.activate
    def test_writeToElasticsearch_nodata(self):
        responses.add(responses.GET, os.environ.get('ELASTICSEARCH_API_BASE_URL') + "/dataassets/_search?size=10000", json={'hits':{'hits': []}})
        test_es_dao = ElasticsearchDAO()
        test_es_dao.writeToElasticsearch([])