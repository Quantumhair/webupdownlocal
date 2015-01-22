


from lxml import html
import requests
import csv
import easygui as eg
from datetime import datetime
from dateutil import parser

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
    tree = html.fromstring(page.text)

    dates = tree.xpath('//a[@class="o-U-s FI Rg"]/text()')

    print dates
    print dates[0]


stripdate = dates[0].replace('-',' ')
print stripdate

date_object = parser.parse(stripdate)
print date_object

