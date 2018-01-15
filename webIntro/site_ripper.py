from BeautifulSoup import BeautifulSoup
# import requests
import urllib2

url = "http://www.values.com/inspirational-quotes"

response = urllib2.urlopen(url)

html = response.read()

# print (html)

soup = BeautifulSoup(html)

# print (soup.prettify())

items = soup.findAll('h6')

print (type(items))

# print (items)

for item in items:
    print item.text