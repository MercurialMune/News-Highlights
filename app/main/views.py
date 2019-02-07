from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news
from ..models import Sources


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    all_news = get_news()
    print(all_news)
    title = 'Mercurial News Highlights'

    return render_template('index.html', title=title, all_news=all_news)
