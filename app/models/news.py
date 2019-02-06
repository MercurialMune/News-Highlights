lass Movie:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,description,author,name,url):
        self.source =id
        self.description = description
        self.name = name
        self.author = author
        self.url = url
