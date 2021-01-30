# :filename: tests/test_single_page.py
# to use: "cd tests; python test_single_page.py"


# import std libs
#from datetime import datetime, date, timedelta
import os
import sys
import unittest

# import 3rd parties libs
#from flask              import current_app, g, request, url_for
#from flask              import request
#from werkzeug.routing   import Map, Rule, NotFound, RequestRedirect
#from werkzeug.routing   import NotFound

# import project's libs
# we need to add the project directory to pythonpath to find project's module(s) in development PC without installing it
basedir, _ = os.path.split(os.path.abspath(os.path.dirname(__file__)).replace('\\', '/'))
sys.path.insert(1, basedir)              # ndx==1 because 0 is reserved for local directory
#from single_page       import create_app
from single_page.ajacs import models


class NationsTest(unittest.TestCase):
    '''testing models'''
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_get(self):
        val = models.Nations.get('en')
        self.assertEqual(val, 'England')
    
    def test_keys(self):
        keys = models.Nations.keys()
        #<! self.assertEqual(keys, models.Nations._nations.keys()) fails
        #   because these are two different iterators; we need to compare their values
        self.assertEqual(list(keys), list(models.Nations._nations.keys()))

    def test_set(self):
        models.Nations.set('es', 'Espagna')
        val = models.Nations.get('es')
        self.assertEqual(val, 'Espagna')
        
        val = models.Nations.set('en', 'Englanda')
        val = models.Nations.get('en')
        self.assertEqual(val, 'Englanda')
    
    def test_values(self):
        val = models.Nations.values()
        #<! self.assertEqual(val, models.Nations._nations.values()) fails
        #   because these are two different iterators; we need to compare their values
        self.assertEqual(list(val), list(models.Nations._nations.values()))
        

if __name__ == '__main__':
    unittest.main()
    
    

