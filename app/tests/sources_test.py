import unittest
from app.models import Sources
from manage import app

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources(1234,'BBC','https://image.tmdb.org/t/p/w500/khsjha27hbs')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

if __name__ == '__main__':
    app.run()