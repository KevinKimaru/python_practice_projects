import requests
#beautifulSoup4
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/john-lewis-murray-ergonomic-office-chair-black/p1919328")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop" : "price", "class" : "now-price"})
str_price = element.text.strip()
str_price_without_symbol = str_price[1:]
price = float(str_price_without_symbol)

if price > 200:
    print("You should by this chair")
    print("The price of the chair is : {}".format(str_price))
else:
    print("This chair is too expensive. Do not buy it")

