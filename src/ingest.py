import configparser
import datetime
import json
import os
import requests

from DHDataset import DHDataset
from NTLDataFormatter import NTLDataFormatter
from SocrataDataFormatter import SocrataDataFormatter
from ElasticsearchDAO import ElasticsearchDAO
from SlackNotifier import SlackNotifier

DATASET_CONFIG_FILEPATH = 'datasets.ini'
TYPE_NTL = 'ntl'
TYPE_SOCRATA = 'socrata'

ENVIRONMENT_NAME = os.environ.get('ENVIRONMENT_NAME') if os.environ.get('ENVIRONMENT_NAME') else 'local'
SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL') if os.environ.get(
    'SLACK_WEBHOOK_URL') else 'localhost'


def lambda_handler(event, context):
    config = configparser.ConfigParser()
    config.read(DATASET_CONFIG_FILEPATH)
    ndf = NTLDataFormatter()
    sdf = SocrataDataFormatter()
    esdao = ElasticsearchDAO()
    snf = SlackNotifier(ENVIRONMENT_NAME, SLACK_WEBHOOK_URL)
    ingest(event, config, ndf,
           sdf, esdao, snf)


def ingest(event, config, ntl_data_formatter, socrata_data_formatter, elasticsearch_dao, slack_notifier):
    datasource = config[event['datasource']]
    try:
        datasets = makeQueryCall(datasource['url'])

        if datasource['type'] == TYPE_NTL:
            results = ntl_data_formatter.getNTLDataObjects(datasets)
        elif datasource['type'] == TYPE_SOCRATA:
            results = socrata_data_formatter.getSocrataDataObjects(
                datasets, datasource)
        else:
            raise ValueError("Unknown datasource type: %s" %
                             datasource['type'])
        elasticsearch_dao.writeToElasticsearch(results)
    except Exception as e:
        slack_notifier.sendSlackNotification("Error ingesting " +
                                             event['datasource'] + " ==> " + str(e))


def makeQueryCall(queryURL):
    r = requests.get(queryURL)
    response = json.loads(r.text)
    return response
