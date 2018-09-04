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

    get_sources_url = SOURCE_URL.format(category, API_KEY)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results


def process_sources(sources_list):

    '''
    Function  that processes the source result and transform them to a list of objects

    Args:
        sources_list: The list of dictionaries that contain source details
    '''

    sources_results = []

    for item in sources_list:
        id = item.get('id')
        name = item.get('name')
        description = item.get('description')
        url = item.get('url')
        category = item.get('category')

        sources_object = Source(id, name, description, url, category)
        sources_results.append(sources_object)

    return sources_results


def get_articles(id):

    '''
    Function that gets the json response to the url request
    '''

    get_articles_url = ARTICLE_URL.format(id, API_KEY)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_data = url.read()
        article_response = json.loads(articles_data)

        articles_results = None

        if article_response['articles']:
            article_results_list = article_response['articles']
            articles_results = process_articles(article_results_list)

    return articles_results


def process_articles(article_list):

    '''
    We now want to process the dictionary and output a list of objects - news_results.

    We process results that will transform our dictionary into a list of objects.
    '''

    article_results = []

    for item in article_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        image_url = item.get('urlToImage')
        publish_time = item.get('publishedAt')

        articles_object = Article(author, title, description, url, image_url, publish_time)
        article_results.append(articles_object)

    return article_results



