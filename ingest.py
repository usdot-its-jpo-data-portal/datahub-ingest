import requests
import os
import json
import datetime
from DHDataset import DHDataset


def lambda_handler(event, context):

    try:
        datasource = event['datasource']
        queryURL = getQueryUrl(datasource)
        datasets = makeQueryCall(queryURL)

        if datasource == 'ntl':
            results = getNTLDataObjects(datasets)
        elif datasource == 'dtg' or datasource == 'scgc':
            results = getSocrataDataObjects(datasets, datasource)

        writeToElasticsearch(results)
        # for result in results:
        # print(result.name)
    except Exception as e:
        sendSlackNotification("Error ingesting " +
                              event['datasource'] + " ==> " + str(e))


def getQueryUrl(data_provider):
    queryURL = ''
    if(data_provider == 'dtg'):
        # queryURL = os.environ['DTG_URL']
        queryURL = 'https://api.us.socrata.com/api/catalog/v1?q=data&search_context=data.transportation.gov&domains=data.transportation.gov&tags=intelligent%20transportation%20systems%20(its)&provenance=official'

    elif (data_provider == 'ntl'):
        # queryURL = os.environ['NTL_URL']
        queryURL = 'https://rosap.ntl.bts.gov/fedora/export/view/collection/dot:239?from=2019-05-24T00:00:00Z&rows=9999'

    elif (data_provider == 'scgc'):
        # queryURL = os.environ['SCGC_URL']
        queryURL = 'https://api.us.socrata.com/api/catalog/v1?q=data&search_context=datahub.transportation.gov&domains=datahub.transportation.gov&tags=intelligent%20transportation%20systems%20(its)&provenance=official'

    else:
        print('Incorrect Params')

    return queryURL


def makeQueryCall(queryURL):
    r = requests.get(queryURL)
    response = json.loads(r.text)
    return response


def getNTLDataObjects(datasets):
    result = []
    for doc in datasets['response']['docs']:
        if doc is None:
            continue
        if 'Dataset' not in doc['mods.sm_resource_type']:
            continue

        dt = datetime.datetime.utcnow()
        dt_str = dt.strftime("%Y-%m-%dT%H:%M:%SZ")

        ds = DHDataset()
        ds.dh_source_name = 'ntl'
        ds.dh_id = '{}-{}'.format(ds.dh_source_name, doc['PID'])
        ds.dh_last_updated = dt_str

        ds.id = doc['PID']
        ds.name = doc['dc.title'][0]
        ds.description = doc['mods.abstract'][0]
        access = doc['rdf.isOpenAccess'][0]
        if access is None or access == '' or access == 'true':
            ds.access_level = 'Public'
        else:
            ds.access_level = 'Restricted'
        ds.last_updated = doc['fgs.createdDate']

        tags = []
        for tag in doc['mods.sm_key_words']:
            tags.append(tag)

        ds.tags = tags

        id = ds.id.split(':')[1]
        ds.source_url = '{}{}'.format(
            'https://rosap.ntl.bts.gov/view/dot/', id)

        result.append(ds)

    return result


def getSocrataDataObjects(datasets, ds_name):
    result = []

    for doc in datasets['results']:
        if doc is None:
            continue

        dt = datetime.datetime.utcnow()
        dt_str = dt.strftime("%Y-%m-%dT%H:%M:%SZ")

        ds = DHDataset()
        ds.dh_source_name = ds_name
        ds.dh_id = '{}-{}'.format(ds.dh_source_name, doc['resource']['id'])
        ds.dh_last_updated = dt_str

        ds.id = doc['resource']['id']
        ds.name = doc['resource']['name']
        ds.description = doc['resource']['description']

        access = None
        for access_level in doc['classification']['domain_metadata']:
            if access_level['key'] == 'Common-Core_Public-Access-Level':
                access = access_level['value']
                break

        if access is None or access.lower() == 'public':
            access = 'Public'
        else:
            access = 'Restricted'

        ds.access_level = access

        udt = doc['resource']['updatedAt']
        udt = udt[0: 19] + 'Z'
        ds.last_updated = udt

        tags = []
        for tag in doc['classification']['domain_tags']:
            tags.append(tag)

        ds.tags = tags

        ds.source_url = doc['link']
        result.append(ds)

    return result


def cleanText(txt):
    txt = txt.replace('"', '')
    txt = txt.replace('\t', '\\t')
    txt = txt.replace('\n', '\\n')
    txt = txt.replace('\r', '\\r')
    return txt


def writeToElasticsearch(datasets):
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
        line += '"name":"{}",'.format(cleanText(dataset.name))
        line += '"description":"{}",'.format(cleanText(dataset.description))
        line += '"accessLevel":"{}",'.format(dataset.access_level)
        line += '"lastUpdate":"{}",'.format(dataset.last_updated)
        line += '"tags":[{}],'.format(tags)
        line += '"sourceUrl":"{}",'.format(dataset.source_url)
        line += '"dhId":"{}",'.format(dataset.dh_id)
        line += '"dhLastUpdate":"{}",'.format(dataset.dh_last_updated)
        line += '"dhSourceName":"{}"'.format(dataset.dh_source_name)
        line += '}'
        # fileObj.write('{}\n'.format(line_index))
        # fileObj.write('{}\n'.format(line))
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


def sendSlackNotification(message):
    header = {'Content-type': 'application/json'}
    payload = '{"text":"' + \
        os.environ['ENVIRONMENT_NAME'] + ' | ' + message + '"}'
    slack_response = requests.post(
        os.environ['SLACK_WEBHOOK_URL'], data=payload, headers=header)
