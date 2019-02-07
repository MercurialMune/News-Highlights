from flask import render_template
from . import main
from ..request import get_cnn_news, get_bbc_news, get_aljazeera_news


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Mercurial News Highlights'

    return render_template('index.html', title=title)


@main.route('/highlights/bbc')
def bbc():

    '''
    View root page function that returns the bbc highlights page and its data
    '''

    bbc_news = get_bbc_news()
    print(bbc_news)
    title = 'Mercurial News Highlights'

    return render_template('bbc-highlights.html', title=title, bbc_news=bbc_news)


@main.route('/highlights/cnn')
def cnn():

    '''
    View root page function that returns the cnn highlights page and its data
    '''

    cnn_news = get_cnn_news()
    print(cnn_news)
    title = 'Mercurial News Highlights'

    return render_template('cnn-highlights.html', title=title, cnn_news=cnn_news)


@main.route('/highlights/aljazeera')
def jaz():

    '''
    View root page function that returns the aljazeera highlights page and its data
    '''

    jaz_news = get_aljazeera_news()
    print(jaz_news)
    title = 'Mercurial News Highlights'

    return render_template('aljazeera-highlights.html', title=title, jaz_news=jaz_news)
