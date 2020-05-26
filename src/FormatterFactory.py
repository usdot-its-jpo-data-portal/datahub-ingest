from SocrataDataFormatter import SocrataDataFormatter
from NTLDataFormatter import NTLDataFormatter
from SocrataStoryFormatter import SocrataStoryFormatter

TYPE_NTL = 'ntl'
TYPE_SOCRATA = 'socrata'
TYPE_STORY = 'story'


class FormatterFactory(object):
    def __init__(self):
        super().__init__()

    def get_formatter(self, data_type):
        switcher = {
            TYPE_NTL: NTLDataFormatter(),
            TYPE_SOCRATA: SocrataDataFormatter(),
            TYPE_STORY: SocrataStoryFormatter()
        }

        return switcher.get(data_type, None)
