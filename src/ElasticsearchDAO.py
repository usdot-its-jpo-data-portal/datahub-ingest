import os
import requests
import json


class ElasticsearchDAO:
    def __init__(self):
        pass

    def writeToElasticsearch(self, datasets):
        ELASTICSEARCH_API_BASE_URL = os.environ.get('ELASTICSEARCH_API_BASE_URL')
        esresult = requests.get(ELASTICSEARCH_API_BASE_URL + '/dataassets/_search?size=10000')
        existingDocs = json.loads(esresult.text)['hits']['hits']
        document = ''
        for dataset in datasets:
            found = False
            lineObj = {}
            lineIndexObj = {}
            for x in existingDocs:
                if x['_source']['id'] == dataset.id: # if document already exists, load and modify
                    found = True
                    lineObj['doc'] = self.mapObjDoc(dataset,x)
                    lineIndexObj['update'] = {'_id': dataset.dh_id, '_index': 'dataassets'}
                    break
                
            if found == False:
                lineObj = self.mapObjDoc(dataset,{})
                lineIndexObj['index'] = {'_id': dataset.dh_id, '_index': 'dataassets'}


            document += json.dumps(lineIndexObj) + '\r\n'
            document += json.dumps(lineObj) + '\r\n'

        if(document != ''):
            print('Writing data to ES')
            header = {'Content-type': 'application/json'}
            es_post_response = requests.post(
                ELASTICSEARCH_API_BASE_URL + '/_bulk', data=document, headers=header)
            print('Data written to ES')

        else:
            print('Elasticsearch already up to date.')

    def mapObjDoc(self, dataset, lineobjDoc):
        lineobjDoc['id'] = dataset.id
        lineobjDoc['name'] = dataset.name
        lineobjDoc['description'] = self.cleanText(dataset.description)
        lineobjDoc['accessLevel'] = dataset.access_level
        lineobjDoc['lastUpdate'] = dataset.last_updated
        lineobjDoc['tags'] = dataset.tags
        lineobjDoc['sourceUrl'] = dataset.source_url
        lineobjDoc['metrics'] = dataset.metrics
        lineobjDoc['dhId'] = dataset.dh_id
        lineobjDoc['dhLastUpdate'] = dataset.dh_last_updated
        lineobjDoc['dhSourceName'] = dataset.dh_source_name

        return lineobjDoc




    def cleanText(self, txt):
        txt = txt.replace('"', '')
        txt = txt.replace('\t', '\\t')
        txt = txt.replace('\n', '\\n')
        txt = txt.replace('\r', '\\r')
        return txt
