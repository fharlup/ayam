from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import itertools
urlsepeda = "https://www.olx.co.id/items/q-frame-sepeda"
result={}
client = ureq(urlsepeda)
sepeda_html = client.read()
page_soup = soup(sepeda_html, "html.parser")
client.close()
semua = page_soup.findAll("ul", {"class": "rl3f9 _3mXOU"})

awalprice = page_soup.findAll("span", {"class": "_89yzn"})
price = awalprice[0].text
nama = page_soup.findAll("span", {"class": "_2tW1I"})
atasnama = nama[0].text
awaltempat = page_soup.findAll("span", {"class": "tjgMj"})
tempat = awaltempat[0].text

for (a,b,c)in zip(nama,awalprice,awaltempat):
    print(a.text,b.text,c.text)






