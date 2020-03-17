import configparser
import datetime
import json
import os
import requests
import sys
import yaml

from DHDataset import DHDataset
from NTLDataFormatter import NTLDataFormatter
from SocrataDataFormatter import SocrataDataFormatter
from ElasticsearchDAO import ElasticsearchDAO
from SlackNotifier import SlackNotifier

DATASET_CONFIG_FILEPATH = 'config.yaml'
TYPE_NTL = 'ntl'
TYPE_SOCRATA = 'socrata'

ENVIRONMENT_NAME = os.environ.get('ENVIRONMENT_NAME') if os.environ.get('ENVIRONMENT_NAME') else 'local'
SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL') if os.environ.get(
    'SLACK_WEBHOOK_URL') else 'localhost'


def lambda_handler(event, context):
    ntl_data_formatter = NTLDataFormatter()
    socrata_data_formatter = SocrataDataFormatter()
    elasticsearch_dao = ElasticsearchDAO()
    slack_notifier = SlackNotifier(ENVIRONMENT_NAME, SLACK_WEBHOOK_URL)
    ingest(event, ntl_data_formatter,
           socrata_data_formatter, elasticsearch_dao, slack_notifier)


def ingest(event, ntl_data_formatter, socrata_data_formatter, elasticsearch_dao, slack_notifier):
    with open("config.yaml", 'r') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)

    datasource_name = event['datasource']
    datasource = config['data-sources'][datasource_name]

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

if (__name__ == '__main__'):
    event={'datasource': str(sys.argv[1])}
    lambda_handler(event, None)

