import urllib.request,json
from .models import News_source
 
api_key = None
article_url = None
source_url = None

def configure_request(app):
    global api_key,article_url,source_url
    api_key = app.config['NEWS_API_KEY']
    article_url = app.config['NEWS_ARTICLE_BASE_URL']
    source_url =app.config['NEWS_SOURCE_BASE_URL']

def get_sources(category):
    '''
    This function gets response from the news site
    '''
    get_sources_url = source_url.format(category,api_key)

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
