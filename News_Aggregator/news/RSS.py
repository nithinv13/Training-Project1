import feedparser

# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    news = []
    feed = feedparser.parse( rss_url )
    for newsitem in feed['items']:
        if 'published' in newsitem and 'title' in newsitem and 'summary' in newsitem and 'link' in newsitem:
            news.append( { 'published': newsitem['published'], 'title':newsitem['title'] , 'summary':newsitem['summary'] , 'link':newsitem['link'] } )
    #news = sorted(news, key=lambda k: k['published'] , reverse = True)
    print rss_url , '\n', 'Total news items : ' , len(news), '\n'
    return news



# List of RSS feeds that we will fetch and combine
newsurls = {
    'Top-stories' : { 'cnn': 'http://rss.cnn.com/rss/cnn_latest.rss' , 'toi':'feed://timesofindia.indiatimes.com/rssfeedstopstories.cms' },
    'India' : {'zee news':'http://zeenews.india.com/rss/india-national-news.xml'},
    'World' : {'cnn' : 'http://rss.cnn.com/rss/edition_world.rss'},
    'Business' : {'cnn' : 'http://rss.cnn.com/rss/money_news_international.rss'},
    'Technology' : {'cnn' : 'http://rss.cnn.com/rss/edition_technology.rss'},
    'Entertainment' : {'cnn' : 'http://rss.cnn.com/rss/edition_entertainment.rss'},
    'Sports' : {'cnn' : 'http://rss.cnn.com/rss/edition_sport.rss'}
}


# -------------------------- code check -------------------------------

def printCheck():
	for source, url in newsurls.items():
		print ' news : ' , source
		print ' url : ' , url

		headlines = getHeadlines(url)
		for h in headlines[:1]:
			print '\t' , h , '\n\n'
		#print '\n\n\n'

# end of code