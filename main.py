import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
urlsepeda="https://www.olx.co.id/items/q-frame-sepeda"
client=ureq(urlsepeda)
sepeda_html=client.read()
client.close()
page_soup=soup(sepeda_html,"html.parser")
page_soup.h3
