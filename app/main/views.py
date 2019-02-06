from flask import render_template
from app import app
from app.request import get_news


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    all_news = get_news()
    print(all_news)
    title = 'Mercurial News Highlights'

    return render_template('index.html', title=title, all_news=all_news)
