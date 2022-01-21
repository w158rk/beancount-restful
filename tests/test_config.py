import unittest

import os
import sys
sys.path.insert(0, os.path.abspath(\
    os.path.join(os.path.dirname(__file__), '.')))

import hipack

from context import brest
from brest.config import Config


class ConfigTest(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.config_file = os.path.join(os.path.dirname(__file__), 'test.cfg')
        self.expected = None

        self.load_expected()

    def load_expected(self):
        with open(self.config_file, 'rb') as f:
            self.expected = hipack.load(f)


    def test_config(self):
        with open(self.config_file, 'rb') as f:
            config = Config.load(f)

        for k,v in self.expected.items():
            self.assertEqual(v, getattr(config, k))



if __name__=='__main__':
    unittest.main()