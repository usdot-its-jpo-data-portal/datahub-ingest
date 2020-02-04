import responses
import unittest
from unittest.mock import MagicMock

import ingest

from ElasticsearchDAO import ElasticsearchDAO
from NTLDataFormatter import NTLDataFormatter
from SlackNotifier import SlackNotifier
from SocrataDataFormatter import SocrataDataFormatter


class IngestTest(unittest.TestCase):
    @responses.activate
    def test_ingest_ntl(self):
        responses.add(responses.GET, "http://test_ntl_url",
                  json={'response':'fake_response'}, status=200)

        test_event = {"datasource":"ntl"}
        test_config = {"ntl":{"type":"ntl", "url":"http://test_ntl_url"}}
        mock_ntl_data_formatter = NTLDataFormatter()
        mock_ntl_data_formatter.getNTLDataObjects = MagicMock()

        mock_elasticsearch_dao = ElasticsearchDAO()
        mock_elasticsearch_dao.writeToElasticsearch = MagicMock()

        ingest.ingest(test_event, test_config, mock_ntl_data_formatter, SocrataDataFormatter(), mock_elasticsearch_dao, SlackNotifier(None, None))

        mock_ntl_data_formatter.getNTLDataObjects.assert_called_once()
        mock_elasticsearch_dao.writeToElasticsearch.assert_called_once()
    
    @responses.activate
    def test_ingest_socrata(self):
        responses.add(responses.GET, "http://test_dtg_url",
                  json={'response':'fake_response'}, status=200)

        test_event = {"datasource":"dtg"}
        test_config = {"dtg":{"type":"socrata", "url":"http://test_dtg_url"}}
        mock_socrata_data_formatter = SocrataDataFormatter()
        mock_socrata_data_formatter.getSocrataDataObjects = MagicMock()

        mock_elasticsearch_dao = ElasticsearchDAO()
        mock_elasticsearch_dao.writeToElasticsearch = MagicMock()

        ingest.ingest(test_event, test_config, NTLDataFormatter(), mock_socrata_data_formatter, mock_elasticsearch_dao, SlackNotifier(None, None))

        mock_socrata_data_formatter.getSocrataDataObjects.assert_called_once()
        mock_elasticsearch_dao.writeToElasticsearch.assert_called_once()
    
    @responses.activate
    def test_ingest_unknown(self):
        responses.add(responses.GET, "http://unkown_test_url",
                  json={'response':'fake_response'}, status=200)

        test_event = {"datasource":"dtg"}
        test_config = {"dtg":{"type":"unknown_type", "url":"http://unkown_test_url"}}

        mock_slack_notifier = SlackNotifier(None, None)
        mock_slack_notifier.sendSlackNotification = MagicMock()

        ingest.ingest(test_event, test_config, NTLDataFormatter(), SocrataDataFormatter(), ElasticsearchDAO(), mock_slack_notifier)

        mock_slack_notifier.sendSlackNotification.assert_called_once()