
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
urlsepeda="https://www.olx.co.id/items/q-frame-sepeda"
client=ureq(urlsepeda)
sepeda_html=client.read()

page_soup=soup(sepeda_html,"html.parser")
client.close()
