import unittest

import os
import sys
sys.path.insert(0, os.path.abspath(\
    os.path.join(os.path.dirname(__file__), '.')))

import hipack

from context import brest
from brest.config import Config
from brest.ledger import Ledger


class ConfigTest(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.config = None
        self.ledger = None

        self.load_config()

    def load_config(self):
        config_file = os.path.join(os.path.dirname(__file__), 'test.cfg')
        with open(config_file, 'rb') as file:
            self.config = Config.load(file)

    def test_ledger_load(self):
        self.ledger = Ledger(config=self.config)
        self.assertIsNotNone(self.ledger)



if __name__=='__main__':
    unittest.main()