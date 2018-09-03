import unittest
from app.models import Source

class TestSource(unittest.TestCase):

    '''
    Test class to test the behaviours the source class
    '''

    def setUp(self):

        '''
        Method that will run before every test
        '''

        self.new_source = Source('ny_times',
                                 'The New York Times',
                                 'Breaking News, World News & Multimedia',
                                 'https://www.nytimes.com/section/politics',
                                 'Politics')


    def test_instance(self):

        self.assertTrue(isinstance(self.new_source, Source))
