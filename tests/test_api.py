import os
import sys
from threading import Thread, Event
sys.path.insert(0, os.path.abspath(\
    os.path.join(os.path.dirname(__file__), '.')))

from concurrent.futures import ThreadPoolExecutor
from context import brest
from brest.app import app
from time import sleep
import requests
import unittest

class APITest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.response = None

        self.url = ''

    def request_get(self):
        tester = app.test_client(self)
        self.response = tester.get(self.url).json

    def check_response(self):
        expected = {
            'hello' : 'world'
        }

        print(self.response)

        assert expected==self.response

    def test_hello_world(self):
        self.url = '/'
        self.request_get()
        self.check_response()

if __name__ == '__main__':
    unittest.main()