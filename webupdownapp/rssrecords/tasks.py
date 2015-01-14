import psycopg2
import feedparser
import time
from datetime import date
from random import randint

def RssUpdate():
    conn = None
    holder = []
    RSSfeed = None
    id = None
    todaysdate = date.today().timetuple()
    print todaysdate

    try:
        conn = psycopg2.connect("dbname='webupdownusersDB' user='postgres' host='localhost' password='3skateboard'")
    except:
        print "I am unable to connect to the database"

    cur = conn.cursor()
    cur.execute("""SELECT url,uuid FROM rssrecords_rssrecord WHERE url LIKE '%.%/feed%' OR url LIKE '%.%/rss%'""")
    rows = cur.fetchall()

    print "\nShow me the filtered URLs from the database:\n"
    for row in rows:
        print "  ", row[0]
    print "\n"

    for row in rows:
        try:

            RSSfeed = feedparser.parse(row[0])
            print RSSfeed['feed']['title'], " Feed appears to be up! @: ", row[0]
            print "with UUID: ", row[1]
            time.sleep(randint(1,5)) # random wait period to slow down IP blocking
            try:
                #print RSSfeed['feed']['title'],":", str(row).strip('[\'\']')
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
                print "RSS feed was last updated ",round(difference/86400, 1),"days ago""\n"  #takes difference in seconds and divides by
                #24 hours x 60 minutes x 60 seconds = 86,400 seconds to give days difference. Rounds to first decimal place for
                #ease of reading

            except:
                print str(row).strip('[\'\']'),": Cannot find date RSS was last updated. Feed or source may be down!""\n"  #if
                #there is an error above it means that there is no rss feed available at that url. In that case the site is
                #likely down

            try:
                id = row[1]
                cur.execute("""UPDATE rssrecords_rssrecord SET upordown = 'UP', last_checked = CURRENT_TIMESTAMP WHERE uuid = %s""", (id,))
                print "successfully updated database\n"
                conn.commit()
            except:
                print "unable to execute update to database\n"

        except:
            print str(row[0]),": Cannot find date RSS was last updated. Feed or source may be down!"
            try:
                id = row[1]
                cur.execute("""UPDATE rssrecords_rssrecord SET upordown = 'DOWN', last_checked = CURRENT_TIMESTAMP WHERE uuid = %s""", (id,))
                print "successfully updated database\n"
                conn.commit()
            except:
                print "unable to execute update to database\n"

    conn.close()


def dbtest():
    conn = None
    holder = []
    RSSfeed = None
    id = None

    try:
        conn = psycopg2.connect("dbname='webupdownusersDB' user='postgres' host='localhost' password='3skateboard'")
        # change host back to 'localhostl' for use on local machine. also, that host can change, use ENV VAR to call host from heroku
        #dbname='webupdownusersDB' user='postgres' password='3skateboard'
    except:
        print "I am unable to connect to the database"

    cur = conn.cursor()
    cur.execute("""SELECT url,uuid FROM rssrecords_rssrecord""")
    rows = cur.fetchall()

    #for row in rows:
        #holder.append(row)

    #conn.close()

    print "\nShow me the URLs from the database:\n"
    for row in rows:
        print "  ", row[0]
    print "\n"


    #rssfeeds = (SELECT url FROM RSSrecord WHERE user = 'quantumhair')

    #for row in f:   #reads in a row at a time and appends it to holder list
        #holder.append(row)

    for row in rows:
        try:
            #print "first line works: ", row
            RSSfeed = feedparser.parse(row[0])
            #RSSfeed = feedparser.parse(str(row).strip('[\'\']'))   #parses xml file indicated by url and strips [ or ] from the array
            #RSSfeed = feedparser.parse(str(row).replace('(','').replace(')','').replace('u','').replace(''))
            #print RSSfeed['feed']['title'],":", str(row).strip('[\'\']')
            print RSSfeed['feed']['title'], " Feed appears to be up! @: ", row[0]
            print "with UUID: ", row[1]
            #print RSSfeed.entries[0].published_parsed
            #var2 = RSSfeed.entries[0].published_parsed
            #print var2
            #rsspub = time.mktime(var2)
            #print "seconds since epoch rss feed: ", time.mktime(RSSfeed.entries[0].published_parsed)
            #print "seconds since epoch today: ", time.mktime(todaysdate)
            #print todaysdate
            #difference = time.mktime(todaysdate) - time.mktime(RSSfeed.entries[0].published_parsed) #calculates differences
            #in seconds from last RSS feed entry and the current date as of the start of this operation.
            #print "this is seconds difference: ", difference
            #print "RSS feed is ",round(difference/86400, 1),"days old""\n"  #takes difference in seconds and divides by
            #24 hours x 60 minutes x 60 seconds = 86,400 seconds to give days difference. Rounds to first decimal place for
            #ease of reading
            # try:
            #     conn = psycopg2.connect("dbname='webupdownusersDB' user='postgres' host='localhost' password='3skateboard'")
            #     print "conection open"
            # except:
            #     print "I am unable to connect to the database"
            #
            # cur = conn.cursor()

            try:
                #print row[1]
                id = row[1]
                #print id
                cur.execute("""UPDATE rssrecords_rssrecord SET upordown = 'UP', last_checked = CURRENT_TIMESTAMP WHERE uuid = %s""", (id,))
                print "successfully updated database\n"
                conn.commit()
                #conn.close()
            except:
                print "unable to execute update to database\n"

        except:
            print str(row[0]),": Cannot find date RSS was last updated. Feed or source may be down!"
            #print str(row).strip('[\'\']'),": Cannot find date RSS was last updated. Feed or source may be down!""\n"  #if
            #there is an error above it means that there is no rss feed available at that url. In that case the site is
            #likely down
            try:
                #print row[1]
                id = row[1]
                #print id
                cur.execute("""UPDATE rssrecords_rssrecord SET upordown = 'DOWN', last_checked = CURRENT_TIMESTAMP WHERE uuid = %s""", (id,))
                print "successfully updated database\n"
                conn.commit()
                #conn.close()
            except:
                print "unable to execute update to database\n"

    conn.close()