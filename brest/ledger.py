from brest.config import Config
from beancount.loader import load_file
from beancount.query.query import run_query

class Ledger:
    def __init__(self, config : Config) -> None:
        self.config = config
        self.entries = None
        self.options = None

        self.load()

    def load(self):
        self.entries, _, self.options = load_file(self.config.beanfile)

    def run_query(self, format, *args):
        return run_query(self.entries, self.options, format, *args)
