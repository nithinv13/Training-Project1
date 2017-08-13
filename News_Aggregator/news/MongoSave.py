#Save data to mongo DB
from pymongo import MongoClient
from RSS import *
from NewsClustering import cluster
from bson.binary import Binary
import pickle


def updateCategory(category):
	if category not in newsurls:
		print category ,  ' is not present. - invalid key !!'
		return

	print 'Updating category : ' , category , ' ...'

	news_items = []
	url_list = newsurls[category]
	for url in url_list:
		print 'fetching ' , url
		news = getHeadlines(  url_list[url] )
		news_items.extend(news)
		
	print 'Total news items collected : ' , len(news_items)
	

	if(len(news_items) > 0):
		
		print 'Performing clustering ...'
		clusters = cluster(news_items)
		dbClusters = getDBObject(clusters)
		print 'Clusters formed : ' , len(clusters)

		print 'Saving to DB ...'
		client = MongoClient('localhost:27017')
		db = client['news_app']		
		collection = db[ category ]
		collection.drop()
		collection.insert(dbClusters)
		
		client.close()
		print 'data saved to DB - added' , len(news_items) , ' items in ' , len(clusters) , ' clusters'




def getDBObject(clusters):
	thebytes = pickle.dumps(clusters)
	return {'bin-data': Binary(thebytes)}
	

def check():
	#updateCategory('check-invalid')
	for category in newsurls:
		updateCategory(category)

check()