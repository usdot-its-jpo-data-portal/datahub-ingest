import datetime
from DHDataset import DHDataset


class NTLDataFormatter:
    def __init__(self):
        pass

    def getNTLDataObjects(self, datasets):
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