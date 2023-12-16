# coding = utf8

from file_io.xlsx_file import dump_multi_sheet
from unittest import TestCase
import os
import unittest


class TestXlsxFile(TestCase):
    def test_dump_multi_sheet(self):
        name_to_sentences = {
            'foo': [
                'hello',
                'world',
                'aha'
            ],
            'bar': [
                'aha',
                'hello',
                'world'
            ]
        }
        out_file_path = 'tmp/xlsx_file_dump_multi_sheet.xlsx'
        dump_multi_sheet(name_to_sentences, out_file_path)
        self.assertTrue(os.path.isfile(out_file_path))


if __name__ == '__main__':
    unittest.main()
