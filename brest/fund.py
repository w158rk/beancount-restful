import re
from brest.ledger import Ledger

format = '''
        SELECT
            units(sum(position)) as units,
            cost(sum(position)) as book_value,
            value(sum(position)) as market_value
        WHERE
            currency = "{}"
            AND date >= {}
        '''

class FundBase:
    def __init__(self, ledger : Ledger, startdate='', enddate='') -> None:
        self.ledger = ledger
        self.startdate = startdate
        self.enddate = enddate

        self.format = ''
        self.header = []
        self.result = None

    def use_format(self, format):
        self.format = re.sub('\s+', ' ', format)

    def run_query(self, *args):
        self.header, self.result = self.ledger.run_query(self.format, *args)

    def clear(self):
        self.format = ''
        self.result = None
        self.header = []

class FundPool(FundBase):

    def use_format_all_funds(self):
        format = '''
        SELECT currency
        WHERE
            currency ~ 'F_.*'
            AND date >= {}
            AND date <= {}
        GROUP BY
            currency
        '''

        self.use_format(format)

    def get_all_funds(self):
        self.use_format_all_funds()
        self.run_query(self.startdate, self.enddate)
        print(self.result)
        return []


class SingleFundAnalyzer(FundBase):
    def __init__(self, ledger : Ledger, code, startdate='', enddate='', fee=0) -> None:
        super().__init__(ledger, startdate, enddate)

        self.code = code
        self.fee = fee               # 买入费率

    def use_format_total_cost(self):
        format = '''
        SELECT
            cost(sum(position)) as book_value
        WHERE
            currency = "{}"
            AND date >= {}
            AND date <= {}
        '''
        self.use_format(format)

    def check_single_result(self):
        assert self.result
        assert len(self.result) == 1

    def extract_result_total_cost(self):
        row = self.result[0]
        inventory = row.book_value
        position = inventory.get_only_position()
        cost_without_fee = float(position.units.number)
        cost = cost_without_fee / (1-self.fee)
        self.result = round(cost)

    def get_total_cost(self):
        self.use_format_total_cost()
        self.run_query(self.code, self.startdate, self.enddate)
        self.check_single_result()
        self.extract_result_total_cost()

        ret = self.result
        self.clear()

        return ret
