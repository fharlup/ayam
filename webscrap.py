
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
urlsepeda="https://www.olx.co.id/items/q-frame-sepeda"
x=0
i=0
client=ureq(urlsepeda)
sepeda_html=client.read()
page_soup=soup(sepeda_html,"html.parser")
client.close()
semua=page_soup.findAll("div",{"class":"IKo3_"})
awalprice = page_soup.findAll("span", {"class": "_89yzn"})
price = awalprice[x].text
awalharga = page_soup.findAll("span", {"class": "_2tW1I"})
harga = awalharga[0].text
awaltempat = page_soup.findAll("span", {"class": "tjgMj"})
tempat = awaltempat[0].text
totalp=len(awalprice)
while i==totalp:

    x=x+1
    print(price)

