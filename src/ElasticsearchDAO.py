import os
import requests
import json


class ElasticsearchDAO(object):
    def __init__(self):
        super().__init__()

    def writeToElasticsearch(self, datasets):
        ELASTICSEARCH_API_BASE_URL = os.environ.get('ELASTICSEARCH_API_BASE_URL')\
                                     if os.environ.get('ELASTICSEARCH_API_BASE_URL') is not None else 'http://localhost'
        esresult = requests.get(ELASTICSEARCH_API_BASE_URL + '/dataassets/_search?size=10000')
        existingDocs = json.loads(esresult.text)['hits']['hits']
        document = ''
        for dataset in datasets:
            found = False
            lineObj = {}
            lineIndexObj = {}
            for x in existingDocs:
                if x['_source']['id'] == dataset.id:  # if document already exists, load and modify
                    found = True
                    lineObj['doc'] = self.mapObjDoc(dataset, x)
                    lineIndexObj['update'] = {'_id': dataset.dh_id, '_index': 'dataassets'}
                    break

            if found is False:
                lineObj = self.mapObjDoc(dataset, {})
                lineIndexObj['index'] = {'_id': dataset.dh_id, '_index': 'dataassets'}

            document += json.dumps(lineIndexObj) + '\r\n'
            document += json.dumps(lineObj) + '\r\n'

        if(document != ''):
            print('Writing data to ES')
            header = {'Content-type': 'application/json'}
            es_post_response = requests.post(
                ELASTICSEARCH_API_BASE_URL + '/_bulk', data=document, headers=header)
            print('Data written to ES: {} {} ({})'.format(es_post_response.status_code,
                                                          es_post_response.reason, len(datasets)))

        else:
            print('Elasticsearch already up to date.')

    def mapObjDoc(self, dataset, lineobjDoc):
        newLineobjDoc = {}
        newLineobjDoc['id'] = dataset.id
        newLineobjDoc['name'] = dataset.name
        newLineobjDoc['description'] = self.cleanText(dataset.description)
        newLineobjDoc['accessLevel'] = dataset.access_level
        newLineobjDoc['lastUpdate'] = dataset.last_updated
        newLineobjDoc['tags'] = dataset.tags
        newLineobjDoc['sourceUrl'] = dataset.source_url
        newLineobjDoc['metrics'] = dataset.metrics
        newLineobjDoc['doi'] = dataset.doi
        newLineobjDoc['dhId'] = dataset.dh_id
        newLineobjDoc['dhLastUpdate'] = dataset.dh_last_updated
        newLineobjDoc['dhSourceName'] = dataset.dh_source_name
        newLineobjDoc['dhType'] = dataset.dh_type
        newLineobjDoc['dhProjects'] = lineobjDoc['_source']['dhProjects']\
            if ('_source' in lineobjDoc and 'dhProjects' in lineobjDoc['_source']) else []
        newLineobjDoc['dhDataTypes'] = lineobjDoc['_source']['dhDataTypes']\
            if ('_source' in lineobjDoc and 'dhDataTypes' in lineobjDoc['_source']) else []
        return newLineobjDoc

    def cleanText(self, txt):
        txt = txt.replace('"', '')
        txt = txt.replace('\t', '\\t')
        txt = txt.replace('\n', '\\n')
        txt = txt.replace('\r', '\\r')
        return txt
