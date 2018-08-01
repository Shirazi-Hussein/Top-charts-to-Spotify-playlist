import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as BS

#experimental, use whatever yo
my_url = "https://www.at40.com/charts/top-40-238/latest/"

#dont change, read and dump info
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

BS_soup = BS(page_html, "html.parser")

#grabs song name
containers = BS_soup.findAll("article", {"class":"shz-partial-track audio-play-indicator audio-play"})
container = containers[0]

for container in containers:
	title = container.div.div.a.img["alt"]

	price_container = container.findAll('span', {'class':'s-item__price'})
	listing_price = price_container[0].text

	print("title: " + title)
	print("listing_price: " + listing_price)