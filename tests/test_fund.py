import unittest

import os
import sys
sys.path.insert(0, os.path.abspath(\
    os.path.join(os.path.dirname(__file__), '.')))

import hipack

from context import brest
from brest.config import Config
from brest.ledger import Ledger
from brest.fund import FundPool, SingleFundAnalyzer

class FundTest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.config = None
        self.ledger = None

        self.load_ledger()

    def load_ledger(self):
        config_file = os.path.join(os.path.dirname(__file__), 'test.cfg')
        with open(config_file, 'rb') as file:
            self.config = Config.load(file)

        self.ledger = Ledger(config=self.config)

class FundPoolTest(FundTest):

    def test_get_all_funds(self):
        startdate = '2022-01-01'
        enddate = '2022-01-20'
        pool = FundPool(self.ledger, startdate, enddate)
        funds = pool.get_all_funds()
        print(funds)


class SingleFundAnalyzerTest(FundTest):

    def test_single_fund_analyzer(self):
        testcases = [
            ('F_000940', '2022-01-01', '2022-01-20', 0.0015, 780),
            ('F_005267', '2022-01-01', '2022-01-20', 0.0015, 300),
        ]
        for code, startdate, enddate, fee, total_cost in testcases:
            analyzer = SingleFundAnalyzer(self.ledger, code, startdate, enddate, fee=fee)
            self.assertEqual(total_cost, analyzer.get_total_cost())

if __name__=='__main__':
    unittest.main()