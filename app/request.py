import urllib.request,json
from .models import News

# Getting api key
api_key = None

# Getting the news base url
base_bbc_url = None
base_cnn_url = None
base_aljazeera_url = None


def configure_request(app):
    global api_key, base_aljazeera_url, base_cnn_url, base_bbc_url
    api_key = app.config['NEWS_API_KEY']
    base_bbc_url = app.config['BBC_API_BASE_URL']
    base_cnn_url = app.config['CNN_API_BASE_URL']
    base_aljazeera_url = app.config['JAZ_API_BASE_URL']


def get_bbc_news():
    '''
    Function that gets the json response to our url request
    '''
    get_bbc_url = base_bbc_url.format(api_key)

    with urllib.request.urlopen(get_bbc_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        bbc_results = None

        if get_news_response['articles']:
            news_bbc_list = get_news_response['articles']
            bbc_results = process_bbc_results(news_bbc_list)

    return bbc_results

def get_cnn_news():
    '''
    Function that gets the json response to our url request
    '''
    get_cnn_url = base_cnn_url.format(api_key)

    with urllib.request.urlopen(get_cnn_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        cnn_results = None

        if get_news_response['articles']:
            news_cnn_list = get_news_response['articles']
            cnn_results = process_cnn_results(news_cnn_list)

    return cnn_results


def get_aljazeera_news():
    '''
    Function that gets the json response to our url request
    '''
    get_jaz_url = base_aljazeera_url.format(api_key)

    with urllib.request.urlopen(get_jaz_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        aljazeera_results = None

        if get_news_response['articles']:
            news_aljazeera_list = get_news_response['articles']
            aljazeera_results = process_jaz_results(news_aljazeera_list)

    return aljazeera_results


def process_jaz_results(news_list):

    aljazeera_results = []

    for news_item in news_list:
        id = news_item.get('id')
        description = news_item.get('description')
        author = news_item.get('author')
        publishedAt = news_item.get('publishedAt')
        urlToImage = news_item.get('urlToImage')

        if urlToImage:
            news_object = News(id,description,author,publishedAt,urlToImage)
            aljazeera_results.append(news_object)


    return aljazeera_results


def process_cnn_results(news_list):

    cnn_results = []

    for news_item in news_list:
        id = news_item.get('id')
        description = news_item.get('description')
        author = news_item.get('author')
        publishedAt = news_item.get('publishedAt')
        urlToImage = news_item.get('urlToImage')

        if urlToImage:
            news_object = News(id,description,author,publishedAt,urlToImage)
            cnn_results.append(news_object)


    return cnn_results


def process_bbc_results(news_list):

    bbc_results = []

    for news_item in news_list:
        id = news_item.get('id')
        description = news_item.get('description')
        author = news_item.get('author')
        publishedAt = news_item.get('publishedAt')
        urlToImage = news_item.get('urlToImage')

        if urlToImage:
            news_object = News(id,description,author,publishedAt,urlToImage)
            bbc_results.append(news_object)


    return bbc_results
