#Save data to mongo DB
from pymongo import MongoClient
from RSS import *
from NewsClustering import printClusters
import json
import pickle


def readCategory(category):
	if category not in newsurls:
		print 'invalid key'
		return

	client = MongoClient('localhost:27017')
	db = client['news_app']
	collection = db[category]

	cursor = collection.find()
	DB_doc = None
	for c in  cursor:
		DB_doc = c

	result = pickle.loads( DB_doc['bin-data'] )
	return result


def check():
	for cat in newsurls:
		print ' --------------- ' , cat , ' --------------- '
		clusters = readCategory(cat)
		for c in clusters:
			print 'Cluster size : ' , len(c)
			for i in c:
				print i['title']
				print i['published']
			print '\n\n'


#check()