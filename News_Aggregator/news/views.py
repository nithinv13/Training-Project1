from django.shortcuts import render
from .models import Article, Feed
from .forms import FeedForm
from django.shortcuts import redirect
from MongoRead import *

import feedparser
import datetime
from pymongo import MongoClient
from RSS import *
import copy

# Create your views here.

client = MongoClient('localhost:27017')

def rendering_func(request, cursor, html_file):
    print "in rendering function"
    articles = []
    print cursor
    for entry1 in cursor:
        articles1 = []
        for entry in entry1:
            print "inside entry"
            article = Article()
            article.title = entry['title']
            print ""
            print entry['title']
            print article.title
            article.url = entry['link']
            article.description = entry['summary']
            '''print entry['published']
            print type(entry['published'])
            d = datetime.datetime(*(entry['published']))
            dateString = d.strftime('%Y-%m-%d %H:%M:%S')
            article.publication_date = dateString'''
            articles1 += [copy.deepcopy(article)]
        articles += [copy.deepcopy(articles1)]
        

    #articles = Article.objects.all()
    #print articles
    rows = articles
    print rows
    #rows = [articles[x:x+1] for x in range(0, len(articles), 1)]
    #print "printing rows"
    #print rows
    return render(request, 'news/'+html_file, {'rows': rows})



def articles_list(request):
    #print "In artlicles_list module"
    #db = client.RSSFeed
    #cursor = db.RSSFeed.find()
    cursor = readCategory('Top-stories')
    #for document in cursor:
    #    print(document)
    return rendering_func(request, cursor, 'articles_list.html')
    #client.close()

def world_list(request):
    cursor = readCategory('World')
    return rendering_func(request, cursor, 'world_list.html')

def India_list(request):
    cursor = readCategory('India')
    return rendering_func(request, cursor, 'India_list.html')

def business_list(request):
    cursor = readCategory('Business')
    return rendering_func(request, cursor, 'business_list.html')

def technology_list(request):
    cursor = readCategory('Technology')
    return rendering_func(request, cursor, 'technology_list.html')

def entertainment_list(request):
    cursor = readCategory('Entertainment')
    return rendering_func(request, cursor, 'entertainment_list.html')

def sports_list(request):
    cursor = readCategory('Top-stories')
    return rendering_func(request, cursor, 'sports_list.html')

def science_list(request):
    cursor = readCategory('Science')
    return rendering_func(request, cursor, 'science_list.html')

def health_list(request):
    cursor = readCategory('Health')
    return rendering_func(request, cursor, 'health_list.html')

def feeds_list(request):
    feeds = Feed.objects.all()
    return render(request, 'news/feeds_list.html', {'feeds': feeds})

def feeds_checking(request):
    print "Inside feeds_checking module"
    feeds = Feed.objects.all()
    for feed in feeds:
        print feed
    return render(request, 'news/feeds_checking.html', {'feeds': feeds})

def new_feed(request):
    if request.method == "POST":
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)

            existingFeed = Feed.objects.filter(url = feed.url)
            if len(existingFeed) == 0:
                feedData = feedparser.parse(feed.url)

                # set some fields
                feed.title = feedData.feed.title
                feed.save()

                for entry in feedData.entries:
                    article = Article()
                    article.title = entry.title
                    article.url = entry.link
                    article.description = entry.description

                    d = datetime.datetime(*(entry.published_parsed[0:6]))
                    dateString = d.strftime('%Y-%m-%d %H:%M:%S')

                    article.publication_date = dateString
                    article.feed = feed
                    article.save()

            return redirect('news.views.feeds_list')
    else:
        form = FeedForm()
    return render(request, 'news/new_feed.html', {'form': form})
