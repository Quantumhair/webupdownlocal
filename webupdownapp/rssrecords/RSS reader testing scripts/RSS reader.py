__author__ = 'adam'


import feedparser
#import csv
#import easygui as eg
from datetime import date
import time


todaysdate = date.today().timetuple()
#print todaysdate
holder = []
rssfeeds = []

#textfile = eg.fileopenbox() #allows user to choose file
#f = csv.reader(open(textfile, 'rb'), delimiter='\t') #opens file for reading

rssfeeds = (SELECT url FROM RSSrecord WHERE user = 'quantumhair')

for row in f:   #reads in a row at a time and appends it to holder list
    holder.append(row)

for item in holder:
    try:
        RSSfeed = feedparser.parse(str(item).strip('[\'\']'))   #parses xml file indicated by url and strips [ or ] from the array
        print RSSfeed['feed']['title'],":", str(item).strip('[\'\']')
        #print RSSfeed.entries[0].published_parsed
        #var2 = RSSfeed.entries[0].published_parsed
        #print var2
        #rsspub = time.mktime(var2)
        #print "seconds since epoch rss feed: ", time.mktime(RSSfeed.entries[0].published_parsed)
        #print "seconds since epoch today: ", time.mktime(todaysdate)
        #print todaysdate
        difference = time.mktime(todaysdate) - time.mktime(RSSfeed.entries[0].published_parsed) #calculates differences
        #in seconds from last RSS feed entry and the current date as of the start of this operation.
        #print "this is seconds difference: ", difference
        print "RSS feed is ",round(difference/86400, 1),"days old""\n"  #takes difference in seconds and divides by
        #24 hours x 60 minutes x 60 seconds = 86,400 seconds to give days difference. Rounds to first decimal place for
        #ease of reading




    except:
        print str(item).strip('[\'\']'),": Cannot find date RSS was last updated. Feed or source may be down!""\n"  #if
        #there is an error above it means that there is no rss feed available at that url. In that case the site is
        #likely down
        pass

#today = date.today()
#print "Current date is: ", today.timetuple()