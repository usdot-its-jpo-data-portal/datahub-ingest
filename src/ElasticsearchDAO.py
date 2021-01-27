import os
import requests
import json


class ElasticsearchDAO(object):
    def __init__(self):
        super().__init__()

    def write_to_elasticsearch(self, datasets):
        ELASTICSEARCH_API_BASE_URL = os.environ.get('ELASTICSEARCH_API_BASE_URL')\
                                     if os.environ.get('ELASTICSEARCH_API_BASE_URL') is not None else 'http://localhost'
        esresult = requests.get(ELASTICSEARCH_API_BASE_URL + '/dataassets/_search?size=10000')
        existing_docs = json.loads(esresult.text)['hits']['hits']
        document = ''
        for dataset in datasets:
            found = False
            line_obj = {}
            line_index_obj = {}
            for x in existing_docs:
                if x['_source']['id'] == dataset.id:  # if document already exists, load and modify
                    found = True
                    line_obj['doc'] = self.map_obj_doc(dataset, x)
                    line_index_obj['update'] = {'_id': dataset.dh_id, '_index': 'dataassets'}
                    break

            if found is False:
                line_obj = self.map_obj_doc(dataset, {})
                line_index_obj['index'] = {'_id': dataset.dh_id, '_index': 'dataassets'}

            document += json.dumps(line_index_obj) + '\r\n'
            document += json.dumps(line_obj) + '\r\n'

        if(document != ''):
            print('Writing data to ES')
            header = {'Content-type': 'application/json'}
            es_post_response = requests.post(
                ELASTICSEARCH_API_BASE_URL + '/_bulk', data=document, headers=header)
            print('Data written to ES: {} {} ({})'.format(es_post_response.status_code,
                                                          es_post_response.reason, len(datasets)))

        else:
            print('Elasticsearch already up to date.')

    def map_obj_doc(self, dataset, line_obj_doc):
        new_lineobj_doc = {}
        new_lineobj_doc['id'] = dataset.id
        new_lineobj_doc['name'] = dataset.name
        new_lineobj_doc['description'] = self.clean_text(dataset.description)
        new_lineobj_doc['accessLevel'] = dataset.access_level
        new_lineobj_doc['lastUpdate'] = dataset.last_updated
        new_lineobj_doc['tags'] = dataset.tags
        new_lineobj_doc['sourceUrl'] = dataset.source_url
        new_lineobj_doc['metrics'] = dataset.metrics
        new_lineobj_doc['doi'] = dataset.doi
        new_lineobj_doc['dhId'] = dataset.dh_id
        new_lineobj_doc['dhLastUpdate'] = dataset.dh_last_updated
        new_lineobj_doc['dhSourceName'] = dataset.dh_source_name
        new_lineobj_doc['dhType'] = dataset.dh_type
        new_lineobj_doc['dhProjects'] = line_obj_doc['_source']['dhProjects']\
            if ('_source' in line_obj_doc and 'dhProjects' in line_obj_doc['_source']) else []
        new_lineobj_doc['dhDataTypes'] = line_obj_doc['_source']['dhDataTypes']\
            if ('_source' in line_obj_doc and 'dhDataTypes' in line_obj_doc['_source']) else []
        return new_lineobj_doc

    def clean_text(self, txt):
        txt = txt.replace('"', '')
        txt = txt.replace('\t', '\\t')
        txt = txt.replace('\n', '\\n')
        txt = txt.replace('\r', '\\r')
        return txt
