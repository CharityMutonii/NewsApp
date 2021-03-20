import unittest
from app.models import News_article

class NewsSourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.article = News_article("image","The article is about the  ...","12.00am","article website")

    def test_instance(self):
        self.assertTrue(isinstance(self.article,News_article))
