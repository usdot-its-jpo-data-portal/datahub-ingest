import os
import requests
import json

ELASTICSEARCH_API_BASE_URL = os.environ.get('ELASTICSEARCH_API_BASE_URL') if os.environ.get('ELASTICSEARCH_API_BASE_URL') else "local"

class ElasticsearchDAO:
    def __init__(self):
        pass

    def writeToElasticsearch(self, datasets):
        document = ''
        for dataset in datasets:

            line_index_obj = {}
            line_index_obj['index'] = {'_id': dataset.dh_id, '_index': 'dataassets'}

            lineobj = {}
            lineobj['id'] = dataset.id
            lineobj['name'] = dataset.name
            lineobj['description'] = self.cleanText(dataset.description)
            lineobj['accessLevel'] = dataset.access_level
            lineobj['lastUpdate'] = dataset.last_updated
            lineobj['tags'] = dataset.tags
            lineobj['sourceUrl'] = dataset.source_url
            lineobj['metrics'] = dataset.metrics
            lineobj['dhId'] = dataset.dh_id
            lineobj['dhLastUpdate'] = dataset.dh_last_updated
            lineobj['dhSourceName'] = dataset.dh_source_name

            document += json.dumps(line_index_obj) + '\r\n'
            document += json.dumps(lineobj) + '\r\n'

        if(document != ''):
            print('Writing data to ES')
            header = {'Content-type': 'application/json'}
            es_post_response = requests.post(
                os.environ['ELASTICSEARCH_API_BASE_URL'] + '/_bulk', data=document, headers=header)
            print('Data written to ES')

        else:
            print('Elasticsearch already up to date.')


    def cleanText(self, txt):
        txt = txt.replace('"', '')
        txt = txt.replace('\t', '\\t')
        txt = txt.replace('\n', '\\n')
        txt = txt.replace('\r', '\\r')
        return txt
