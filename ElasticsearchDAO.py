import os
import requests

ELASTICSEARCH_API_BASE_URL = os.environ.get('ELASTICSEARCH_API_BASE_URL') if os.environ.get('ELASTICSEARCH_API_BASE_URL') else "local"

class ElasticsearchDAO:
    def __init__(self):
        pass

    def writeToElasticsearch(self, datasets):
        document = ''
        for dataset in datasets:
            tags = ''
            for t in dataset.tags:
                tags += '"{}",'.format(t)
            if len(tags) > 0:
                tags = tags[0:len(tags)-1]

            line_index = '{"index":{'
            line_index += '"_index":"dataassets",'
            line_index += '"_id":"{}"'.format(dataset.dh_id)
            line_index += '} }'

            line = '{'
            line += '"id":"{}",'.format(dataset.id)
            line += '"name":"{}",'.format(self.cleanText(dataset.name))
            line += '"description":"{}",'.format(
                self.cleanText(dataset.description))
            line += '"accessLevel":"{}",'.format(dataset.access_level)
            line += '"lastUpdate":"{}",'.format(dataset.last_updated)
            line += '"tags":[{}],'.format(tags)
            line += '"sourceUrl":"{}",'.format(dataset.source_url)
            line += '"dhId":"{}",'.format(dataset.dh_id)
            line += '"dhLastUpdate":"{}",'.format(dataset.dh_last_updated)
            line += '"dhSourceName":"{}"'.format(dataset.dh_source_name)
            line += '}'
            document += line_index + '\r\n'
            document += line + '\r\n'

        if(document != ''):
            print('Writing data to ES')
            header = {'Content-type': 'application/json'}
            es_post_response = requests.post(
                os.environ['ELASTICSEARCH_API_BASE_URL'] + '/_bulk', data=document.encode('utf-8'), headers=header)
            print('Data written to ES')
            print(es_post_response.text)

        else:
            print('Elasticsearch already up to date.')

    def cleanText(self, txt):
        txt = txt.replace('"', '')
        txt = txt.replace('\t', '\\t')
        txt = txt.replace('\n', '\\n')
        txt = txt.replace('\r', '\\r')
        return txt
