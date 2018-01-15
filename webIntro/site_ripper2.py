from BeautifulSoup import BeautifulSoup
import urllib2

# url = "https://www.brainyquote.com/quotes/topics/topic_leadership.html"
url = "https://www.brainyquote.com/quotes/authors/a/albert_einstein.html"
req = urllib2.Request(url, headers={'User-Agent' : 'Magic Browser'})
response = urllib2.urlopen(req)

html = response.read()

soup = BeautifulSoup(html)

#print (soup.prettify())

items = soup.findAll('a', attrs={'title':'view quote'});

#print items

file = open("data.txt", "a")

for item in items:
    x = item.text.replace('&#39', "'")
    file.write(x + "\n")
    print x