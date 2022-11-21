from flask import Blueprint, redirect, render_template, session, url_for
from decouple import config
import requests

category = Blueprint('category', __name__)
api_key = config('NEWS_API')


@category.route('/politics')
def politics():
    if not session:
        return redirect(url_for('views.login'))
    url = "https://newsapi.org/v2/top-headlines?category=politics&language=en&apikey="+api_key+""
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""

    trending_request = requests.get(url).json()
    top_request = requests.get(top).json()

    trending = {
        'articles': trending_request['articles']
    }
    top = {
        'articles': top_request['articles']
    }

    r = requests.get(url).json()
    headline = {
        'articles': r['articles']
    }
    return render_template('/components/categories/politics.html', headlines=headline, search=trending, tops=top)


@category.route('/entertainment')
def entertainment():
    if not session:
        return redirect(url_for('views.login'))
    url = "https://newsapi.org/v2/top-headlines?category=entertainment&language=en&apikey="+api_key+""
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""

    trending_request = requests.get(url).json()
    top_request = requests.get(top).json()

    trending = {
        'articles': trending_request['articles']
    }
    top = {
        'articles': top_request['articles']
    }

    r = requests.get(url).json()
    headline = {
        'articles': r['articles']
    }
    return render_template('/components/categories/entertainment.html', headlines=headline, search=trending, tops=top)


@category.route('/sports')
def sports():
    if not session:
        return redirect(url_for('views.login'))
    url = "https://newsapi.org/v2/top-headlines?category=sports&language=en&apikey="+api_key+""
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""

    trending_request = requests.get(url).json()
    top_request = requests.get(top).json()

    trending = {
        'articles': trending_request['articles']
    }
    top = {
        'articles': top_request['articles']
    }

    r = requests.get(url).json()
    headline = {
        'articles': r['articles']
    }
    return render_template('/components/categories/sports.html', headlines=headline, search=trending, tops=top)


@category.route('/education')
def education():
    if not session:
        return redirect(url_for('views.login'))
    url = "https://newsapi.org/v2/everything?q=education&language=en&apikey="+api_key+""
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""

    trending_request = requests.get(url).json()
    top_request = requests.get(top).json()

    trending = {
        'articles': trending_request['articles']
    }
    top = {
        'articles': top_request['articles']
    }

    r = requests.get(url).json()
    headline = {
        'articles': r['articles']
    }
    return render_template('/components/categories/education.html', headlines=headline, search=trending, tops=top)


@category.route('/health')
def health():
    if not session:
        return redirect(url_for('views.login'))
    url = "https://newsapi.org/v2/top-headlines?category=health&language=en&apikey="+api_key+""
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""

    trending_request = requests.get(url).json()
    top_request = requests.get(top).json()

    trending = {
        'articles': trending_request['articles']
    }
    top = {
        'articles': top_request['articles']
    }

    r = requests.get(url).json()
    headline = {
        'articles': r['articles']
    }
    return render_template('/components/categories/health.html', headlines=headline, search=trending, tops=top)


@category.route('/economy')
def economy():
    if not session:
        return redirect(url_for('views.login'))
    url = "https://newsapi.org/v2/everything?q=economy&language=en&apikey="+api_key+""
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""

    trending_request = requests.get(url).json()
    top_request = requests.get(top).json()

    trending = {
        'articles': trending_request['articles']
    }
    top = {
        'articles': top_request['articles']
    }

    r = requests.get(url).json()
    headline = {
        'articles': r['articles']
    }
    return render_template('/components/categories/economy.html', headlines=headline, search=trending, tops=top)


@category.route('/business')
def business():
    if not session:
        return redirect(url_for('views.login'))
    url = "https://newsapi.org/v2/top-headlines?category=business&language=en&apikey="+api_key+""
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""

    trending_request = requests.get(url).json()
    top_request = requests.get(top).json()

    trending = {
        'articles': trending_request['articles']
    }
    top = {
        'articles': top_request['articles']
    }

    r = requests.get(url).json()
    headline = {
        'articles': r['articles']
    }
    return render_template('/components/categories/business.html', headlines=headline, search=trending, tops=top)


@category.route('/fashion')
def fashion():
    if not session:
        return redirect(url_for('views.login'))
    url = "https://newsapi.org/v2/everything?q=fashion&language=en&apikey="+api_key+""
    top = "https://newsapi.org/v2/top-headlines?sources=techcrunch&language=en&apiKey="+api_key+""

    trending_request = requests.get(url).json()
    top_request = requests.get(top).json()

    trending = {
        'articles': trending_request['articles']
    }
    top = {
        'articles': top_request['articles']
    }

    r = requests.get(url).json()
    headline = {
        'articles': r['articles']
    }
    return render_template('/components/categories/fashion.html', headlines=headline, search=trending, tops=top)
