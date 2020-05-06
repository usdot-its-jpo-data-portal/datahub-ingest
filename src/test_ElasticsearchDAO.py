import unittest
import responses

from ElasticsearchDAO import ElasticsearchDAO

class TestElasticsearchDAO(unittest.TestCase):
    @responses.activate
    def test_writeToElasticsearch_nodata(self):
        responses.add(responses.GET, "http://local/dataassets/_search?size=10000", json={'hits':{'hits': []}})
        test_es_dao = ElasticsearchDAO()
        test_es_dao.writeToElasticsearch([])