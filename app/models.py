class News:
    '''
    News class to define News Objects
    '''

    def __init__(self, id, description, author, publishedAt, urlToImage):
        self.source = id
        self.description = description
        self.publishedAt = publishedAt
        self.author = author
        self.urlToImage = urlToImage


class Sources:
    '''
    News class to define News Objects
    '''

    def __init__(self, id, name, url):
        self.source = id
        self.name = name
        self.url = url
