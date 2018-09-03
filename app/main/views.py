'''Module that contains the view functions of the app'''

from flask import render_template
from . import MAIN
from ..requests import get_articles

@MAIN.route('/')
def index():

    '''
    View root function that returns the index page and its data
    '''

    return render_template('index.html')


@MAIN.route('/news/<id>')
def news(id):

    '''
    View function that returns the source page with its articles
    '''

    title = f'{id}'
    article = get_articles(id)
    highlight = 'Working!!!'

    return render_template('news.html', title=title, article=article, highlight=highlight)
