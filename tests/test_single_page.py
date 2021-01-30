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
from single_page  import create_app


class InitTest(unittest.TestCase):
    '''testing URLs of views'''
    
    def setUp(self):
        self.app = create_app(test=True)
        
    def tearDown(self):
        pass

    def test_sitemap(self):
        with self.app.test_client() as client:
            response = client.get('/sitemap')
            xml = response.data.decode('utf8')          # type(html) == type(str)
        self.assertEqual(response.content_type, 'text/xml')
        self.assertTrue(xml.startswith('<?xml '))
        self.assertIn('<loc>http://localhost/en/2l/index.html</loc>', xml)
        self.assertTrue(xml.endswith('</urlset>'))

if __name__ == '__main__':
    unittest.main()
    
    

