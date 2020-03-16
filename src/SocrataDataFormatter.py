import datetime
from DHDataset import DHDataset


class SocrataDataFormatter:

    def __init__(self):
        pass

    def getSocrataDataObjects(self, datasets, ds_name):
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
