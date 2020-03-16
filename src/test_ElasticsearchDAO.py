import unittest

from ElasticsearchDAO import ElasticsearchDAO

class TestElasticsearchDAO(unittest.TestCase):
    def test_writeToElasticsearch_nodata(self):
        test_es_dao = ElasticsearchDAO()
        test_es_dao.writeToElasticsearch([])