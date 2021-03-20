class News_source:
    '''
    Class for defining Source objects
    '''
    def __init__(self,id,name,url,description,category):
        '''
        Method for defining the news variables
        '''
        self.id = id
        self.name = name
        self.url = url
        self.description = description
        self.category =category
        


class News_article:
    '''
    Class for defining article objects
    '''

    def __init__(self,image,title,description,time,articlelink):
        '''
        Method for defining article variables
        '''
        
        self.image = image
        self.title = title
        self.description = description
        self.time = time
        self.articlelink = articlelink

        