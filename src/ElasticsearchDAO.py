import os
import requests
import json


class ElasticsearchDAO(object):
    def __init__(self):
        super().__init__()

    def write_To_Elasticsearch(self, datasets):
        ELASTICSEARCH_API_BASE_URL = os.environ.get('ELASTICSEARCH_API_BASE_URL')\
                                     if os.environ.get('ELASTICSEARCH_API_BASE_URL') is not None else 'http://localhost'
        esresult = requests.get(ELASTICSEARCH_API_BASE_URL + '/dataassets/_search?size=10000')
        existing_Docs = json.loads(esresult.text)['hits']['hits']
        document = ''
        for dataset in datasets:
            found = False
            line_Obj = {}
            line_IndexObj = {}
            for x in existing_Docs:
                if x['_source']['id'] == dataset.id:  # if document already exists, load and modify
                    found = True
                    lineObj['doc'] = self.mapObjDoc(dataset, x)
                    lineIndexObj['update'] = {'_id': dataset.dh_id, '_index': 'dataassets'}
                    break

            if found is False:
                lineObj = self.mapObjDoc(dataset, {})
                lineIndexObj['index'] = {'_id': dataset.dh_id, '_index': 'dataassets'}

            document += json.dumps(line_IndexObj) + '\r\n'
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

    def mapObj_Doc(self, dataset, line_obj_Doc):
        newLineobj_Doc = {}
        newLineobj_Doc['id'] = dataset.id
        newLineobj_Doc['name'] = dataset.name
        newLineobj_Doc['description'] = self.cleanText(dataset.description)
        newLineobj_Doc['accessLevel'] = dataset.access_level
        newLineobj_Doc['lastUpdate'] = dataset.last_updated
        newLineobj_Doc['tags'] = dataset.tags
        newLineobj_Doc['sourceUrl'] = dataset.source_url
        newLineobj_Doc['metrics'] = dataset.metrics
        newLineobj_Doc['doi'] = dataset.doi
        newLineobj_Doc['dhId'] = dataset.dh_id
        newLineobj_Doc['dhLastUpdate'] = dataset.dh_last_updated
        newLineobj_Doc['dhSourceName'] = dataset.dh_source_name
        newLineobj_Doc['dhType'] = dataset.dh_type
        newLineobj_Doc['dhProjects'] = line_obj_Doc['_source']['dhProjects']\
            if ('_source' in line_obj_Doc and 'dhProjects' in line_obj_Doc['_source']) else []
        newLineobj_Doc['dhDataTypes'] = line_obj_Doc['_source']['dhDataTypes']\
            if ('_source' in line_obj_Doc and 'dhDataTypes' in line_obj_Doc['_source']) else []
        return newLineobj_Doc

    def clean_Text(self, txt):
        txt = txt.replace('"', '')
        txt = txt.replace('\t', '\\t')
        txt = txt.replace('\n', '\\n')
        txt = txt.replace('\r', '\\r')
        return txt
