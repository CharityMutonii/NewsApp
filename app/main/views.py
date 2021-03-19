from flask import render_template,request,redirect,url_for
from .import main
from ..request import get_sources,get_articles
from ..models import News_article,News_source

@main.route('/')
def index():
    '''
    Home page function returns news sources
    '''

    news_sources = get_sources()


    title = "Welcome to news-app"
    return render_template('index.html',title = title, sources = news_sources)

@main.route('/articles/<articles>')
def articles(articles):
    '''
    Displays articles from a specific news source
    '''

    news_article = get_articles(articles)

    title=f"news-app articles"
    return render_template('articles.html', title = title,articles = news_article)