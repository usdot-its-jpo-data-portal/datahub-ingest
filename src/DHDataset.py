class DHDataset():

    def __init__(self):
        self._id = None
        self._name = None
        self._description = None
        self._access_level = None
        self._last_updated = None
        self._tags = []
        self._source_url = None
        self._dh_id = None
        self._dh_last_updated = None
        self._dh_source_name = None
        self._dh_type = None
        self._metrics = {}
        self._doi = None

    @property
    def dh_id(self):
        return self._id

    @id.setter
    def dh_id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    def access_level(self, value):
        self._access_level = value

    @property
    def last_updated(self):
        return self._last_updated

    @last_updated.setter
    def last_updated(self, value):
        self._last_updated = value

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value

    @property
    def source_url(self):
        return self._source_url

    @source_url.setter
    def source_url(self, value):
        self._source_url = value

    @property
    def dh_id(self):
        return self._dh_id

    @dh_id.setter
    def dh_id(self, value):
        self._dh_id = value

    @property
    def dh_last_updated(self):
        return self._dh_last_updated

    @dh_last_updated.setter
    def dh_last_updated(self, value):
        self._dh_last_updated = value

    @property
    def dh_source_name(self):
        return self._dh_source_name

    @dh_source_name.setter
    def dh_source_name(self, value):
        self._dh_source_name = value

    @property
    def dh_type(self):
        return self._dh_type

    @dh_type.setter
    def dh_type(self, value):
        self._dh_type = value

    @property
    def metrics(self):
        return self._metrics

    @metrics.setter
    def metrics(self, value):
        self._metrics = value

    @property
    def doi(self):
        return self._doi
    
    @doi.setter
    def doi(self, value):
        self._doi = value