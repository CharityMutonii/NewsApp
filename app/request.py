import urllib.request,json
from .models import News_source,News_article

api_key = None

base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_sources():
    '''
    This function gets response from the news site
    '''
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
           
        source_results = None

        if get_sources_response['sources']:

           source_results_list = get_sources_response['sources']
           source_results = process_results(source_results_list)

    return source_results        

 
def process_results(sources_list):
    '''
    Functions that takes in list of sources results and transforms them into objects
    '''
    source_list = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        url = source_item.get('url')
        description = source_item.get('description')
        category = source_item.get('category')

        source_object = News_source(id,name,url,description,category)
        source_list.append(source_object)

    return source_list


def get_articles(newssource):
    '''
    A function to get articles from the apis
    '''
    get_articles_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(newssource,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response ['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results

def process_articles(article_list):
    '''
    A function to process articles list and transform them into objects
    '''
    articles_list = []
    for article in article_list:
        
        image = article.get('urlToImage')
        title = article.get('title')
        description = article.get('description')
        time = article.get('publishedAt')
        articlelink = article.get('url')

        article_object = News_article(image,title,description,time,articlelink)
        articles_list.append(article_object)

    return articles_list
