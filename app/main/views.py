'''Module that contains the view functions of the app'''

from flask import render_template
from . import MAIN
from ..requests import get_articles, get_sources

@MAIN.route('/')
def index():

    '''
    View root function that returns the index page and its data
    '''

    title = 'Pew News - The #1 News Source Out There'

    # getting source categories
    business_news = get_sources('business')
    entertainment_news = get_sources('entertainment')
    general_news = get_sources('general')
    science_news = get_sources('science')
    sports_news = get_sources('sports')
    technology_news = get_sources('technology')

    return render_template('index.html', title=title, business=business_news,
                           entertainment=entertainment_news, general=general_news,
                           science=science_news, sports=sports_news, technology=technology_news)


@MAIN.route('/news/<id>')
def news(id):

    '''
    View function that returns the source page with its articles
    '''

    title = f'{id}'
    article = get_articles(id)

    return render_template('news.html', title=title, article=article)
