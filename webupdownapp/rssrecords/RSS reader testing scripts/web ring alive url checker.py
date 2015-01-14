# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 14:13:46 2014

@author: Adam
"""
from BeautifulSoup import BeautifulSoup
import urllib2
import csv
import easygui as eg
import requests
import os

x = 0

holder = []

textfile = eg.fileopenbox() #allows user to choose file
f = csv.reader(open(textfile, 'rb'), delimiter='\t') #opens file for reading

for row in f:   #reads in a row at a time and appends it to holder list
    holder.append(row)
    print"this is item #:", x
    ++x

for item in holder:

    headers = {'User-Agent':'Mozilla/5 (Solaris 10) Gecko'}

    page = requests.get(str(item).strip('[\'\']'), headers = headers)
    page_content = page.content
    soup = BeautifulSoup(page_content)
    #print soup
    
    print str(item).strip('[\'\']')
    req = urllib2.Request(str(item).strip('[\'\']'), headers = headers)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    soup.prettify()
    
    #for elem in soup.find_all('a', href=re.compile('http://www\.cobaltautoservices\.com/')):
        #print elem['href']
    titleTag = soup.html.head.title
    print "Parsing: ",titleTag
    print "\n"

    for anchor in soup.findAll('a', href=True):
        
        #print anchor['href']

        str1 = anchor['href']
        find_this = "semanticmastery.com"
        
        if find_this in str1:
            print find_this, " has been found in this link back to the site: ", str1, "via this onpage anchor :", anchor
            print "\n"

            break
        else:
            print "Still looking at: ", str(item).strip('[\'\']')
        #x += 1
        
    print "\n"
print "All Done!"
    #print "there are ", x, " links on this page"
    
    #titleTag = soup.html.head.title
    
    
    #print titleTag.string 

