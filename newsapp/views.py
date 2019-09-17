# importing api
from django.shortcuts import render
from newsapi import NewsApiClient
import requests

# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key='1422a42ec5e54af29e1a020bcfdd1bc4')
    top = newsapi.get_everything(sources='techcrunch')

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'index.html', context={"mylist": mylist})
