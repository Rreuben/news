import urllib.request, json
from .models import Source, Article

# Getting api key
API_KEY = None

# Getting the source url
SOURCE_URL = None

# Getting the article url
ARTICLE_URL = None


def configure_request(app):

    '''
    Function that takes in the application instance and replaces the value of variables set to none
    '''

    global API_KEY, SOURCE_URL, ARTICLE_URL

    API_KEY = app.config['API_KEY']
    SOURCE_URL = app.config['SOURCE_URL']
    ARTICLE_URL = app.config['ARTICLE_URL']


def get_sources(category):

    '''
    Function that gets the json response to the url request
    '''

    pass


def process_sources(sources_list):

    '''
    Function  that processes the source result and transform them to a list of objects

    Args:
        sources_list: The list of dictionaries that contain source details
    '''

    pass


def get_articles(id):

    '''
    Function that gets the json response to the url request
    '''

    pass


def process_articles(article_list):

    '''
    We now want to process the dictionary and output a list of objects - news_results.

    We process results that will transform our dictionary into a list of objects.
    '''

    pass
