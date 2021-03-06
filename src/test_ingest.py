import responses
import unittest
import json
from unittest.mock import MagicMock, patch
import ingest
import os
from ElasticsearchDAO import ElasticsearchDAO
from FormatterFactory import FormatterFactory
from SlackNotifier import SlackNotifier
from NTLDataFormatter import NTLDataFormatter
from UtilsTest import UtilsTest

MOCK_DATASET_DTG = 'mock_dataset_dtg.json'


class IngestTest(unittest.TestCase):

    def setUp(self):
        self.mock_dataset_url = "http://test.data.datasets"
        self.mock_es_url = "http://test:9200"
        self.base_path = os.path.dirname(os.path.realpath(__file__))
        with open(self.base_path+os.sep+MOCK_DATASET_DTG, 'r', encoding='utf-8') as mock_file:
            self.mock_data = json.load(mock_file)

    @responses.activate
    def test_makeQueryCall(self):
        mock_data = UtilsTest().get_dtg_mock_data()
        responses.add(responses.GET, self.mock_dataset_url,
                      json=mock_data, status=200)
        resp = ingest.makeQueryCall(self.mock_dataset_url)
        self.assertIsNotNone(resp)

    @patch.object(ElasticsearchDAO, 'writeToElasticsearch')
    def test_ingest_ok(self, mock_writeToElasticsearch):
        test_event = {"datasource": "ntl"}
        test_config = {"data-sources":
                       {"ntl": {"type": "ntl", "url": self.mock_dataset_url}}}

        ingest.makeQueryCall = MagicMock(return_value=UtilsTest().get_ntl_mock_data())

        mock_formatter_factory = FormatterFactory()
        mock_formatter_factory.get_formatter = MagicMock(return_value=NTLDataFormatter())

        mock_formatter = NTLDataFormatter()
        mock_formatter.get_data_objects = MagicMock()

        mock_slack_notifier = SlackNotifier(None, None)
        mock_slack_notifier.sendSlackNotification = MagicMock()

        ingest.ingest(test_event, test_config)

        mock_writeToElasticsearch.assert_called_once()

    @patch.object(FormatterFactory, 'get_formatter')
    @patch.object(SlackNotifier, 'sendSlackNotification')
    def test_ingest_invalid_formatter(self, mock_sendSlackNotification, mock_get_formatter):
        test_event = {"datasource": "ntl"}
        test_config = {"data-sources":
                       {"ntl": {"type": "ntl", "url": self.mock_dataset_url}}}

        ingest.makeQueryCall = MagicMock(return_value=UtilsTest().get_ntl_mock_data())

        mock_get_formatter.return_value = None

        ingest.ingest(test_event, test_config)

        mock_get_formatter.assert_called_once()
        mock_sendSlackNotification.assert_called_once()

    @patch.object(ElasticsearchDAO, 'writeToElasticsearch')
    @patch.object(SlackNotifier, 'sendSlackNotification')
    def test_ingest_error_on_es(self, mock_sendSlackNotification, mock_writeToElasticsearch):
        test_event = {"datasource": "ntl"}
        test_config = {"data-sources":
                       {"ntl": {"type": "ntl", "url": self.mock_dataset_url}}}

        ingest.makeQueryCall = MagicMock(return_value=UtilsTest().get_ntl_mock_data())

        mock_writeToElasticsearch.side_effect = Exception("Test Exception")

        ingest.ingest(test_event, test_config)

        mock_writeToElasticsearch.assert_called_once()
        mock_sendSlackNotification.assert_called_once()
