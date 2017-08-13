from SentenceSimilarity import sentence_similarity
import unicodedata

def unicode_to_ascii(line):
    return unicodedata.normalize('NFKD', line).encode('ascii','ignore')


def cluster(headlines, threshold=0.2):

    clusters = [[headlines[0]]]
    for i in xrange(1,len(headlines)):
        assign = -1
        max_score = 0.0
        item = headlines[i]
        for j in xrange(0,len(clusters)):
            sim_score = 0.0
            for c in clusters[j]:
                sim_score = max(sim_score , sentence_similarity( unicode_to_ascii( item['title'] ) + " raw" , unicode_to_ascii( c['title'] ) + " war" ) )
                #print sim_score
            if sim_score > max_score:
                max_score = sim_score
                assign = j
        #print max_score
        if assign != -1 and max_score > threshold:
            clusters[assign].append( item )
        else:
            clusters.append( [item] )

    return clusters


# -------------------------- code check -------------------------------

def printClusters(news_clusters):
    print 'Clusters : ' , len(news_clusters)
    for c in news_clusters:
        print '------------- new cluster ------------'
        for i in c:
            print i['title']
        print '\n\n'

