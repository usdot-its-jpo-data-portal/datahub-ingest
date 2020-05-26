import unittest
from FormatterFactory import FormatterFactory
from NTLDataFormatter import NTLDataFormatter
from SocrataDataFormatter import SocrataDataFormatter
from SocrataStoryFormatter import SocrataStoryFormatter


class TestFormatterFactory(unittest.TestCase):
    def test_get_formatter_ntl(self):
        formatter = FormatterFactory().get_formatter('ntl')
        self.assertTrue(isinstance(formatter, NTLDataFormatter))

    def test_get_formatter_socrata(self):
        formatter = FormatterFactory().get_formatter('socrata')
        self.assertTrue(isinstance(formatter, SocrataDataFormatter))

    def test_get_formatter_story(self):
        formatter = FormatterFactory().get_formatter('story')
        self.assertTrue(isinstance(formatter, SocrataStoryFormatter))

    def test_get_formatter_invalid(self):
        formatter = FormatterFactory().get_formatter('a formater that does not exists')
        self.assertIsNone(formatter)
