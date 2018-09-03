import unittest
from app.models import Article

class TestArticle(unittest.TestCase):

    '''
    Test class to test the behaviours the article class
    '''

    def setUp(self):

        '''
        Method that will run before every test
        '''

        self.new_article = Article('John',
                                   'Article',
                                   'Text conatining article...',
                                   'https://linktoarticle.com/article',
                                   'https://linktoarticle.com/article/image.jpg',
                                   'Published at 16:04')


    def test_instance(self):

        self.assertTrue(isinstance(self.new_article, Article))
