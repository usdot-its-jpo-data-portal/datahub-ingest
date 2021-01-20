import json
import os
import requests
import yaml
import argparse

from FormatterFactory import FormatterFactory
from ElasticsearchDAO import ElasticsearchDAO
from SlackNotifier import SlackNotifier

DATASET_CONFIG_FILEPATH = 'config.yaml'
ENVIRONMENT_NAME = os.environ.get('ENVIRONMENT_NAME') \
    if os.environ.get('ENVIRONMENT_NAME') else 'local'
SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL') if os.environ.get(
    'SLACK_WEBHOOK_URL') else 'localhost'


def lambda_handler(event, context):
    with open(DATASET_CONFIG_FILEPATH, 'r') as stream:
        config = yaml.load(stream, Loader=yaml.FullLoader)
    ingest(event, config)


def ingest(event, config):
    datasource_name = event['datasource']
    datasource = config['data-sources'][datasource_name]

    try:
        datasets = make_QueryCall(datasource['url'])
        formatter = FormatterFactory().get_formatter(datasource['type'])
        if formatter is None:
            raise ValueError("Unknown datasource type: %s" %
                             datasource['type'])

        results = formatter.get_data_objects(datasets, datasource_name)

        ElasticsearchDAO().writeToElasticsearch(results)
    except Exception as e:
        msg = "Error ingesting " + event['datasource'] + " ==> " + str(e)
        SlackNotifier(ENVIRONMENT_NAME,
                      SLACK_WEBHOOK_URL).send_slack_notification(msg)


def make_query_call(query_url):
    r = requests.get(query_url)
    response = json.loads(r.text)
    return response


if (__name__ == '__main__'):
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--datasource',
                        choices=['dtg', 'ntl', 'scgc', 'story'], required=True)
    args = parser.parse_args()
    event = {'datasource': args.datasource}
    lambda_handler(event, None)
