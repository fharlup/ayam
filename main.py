
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
urlsepeda="https://www.olx.co.id/items/q-frame-sepeda"
client=ureq(urlsepeda)
sepeda_html=client.read()
page_soup=soup(sepeda_html,"html.parser")
client.close()
semua=page_soup.findAll("div",{"class":"IKo3_"})
for i in semua:
    awalprice = page_soup.findAll("span", {"class": "_89yzn"})
    price = awalprice[0].text
    awalharga = page_soup.findAll("span", {"class": "_2tW1I"})
    harga = awalharga[0].text
    awaltempat = page_soup.findAll("span", {"class": "tjgMj"})
    tempat = awaltempat[0].text
    print(price)
    print(harga)
    print(tempat)
