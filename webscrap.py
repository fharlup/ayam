from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import os

urlsepeda = "https://www.olx.co.id/items/q-frame-sepeda"
namafile="sepeda1.csv"
f=open(namafile,"w")
header="nama,harga,asal\n"
f.write(header)
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
    print(a.text,b.text,c.text,"\n")
    f.write(a.text.replace(",", "|") + "," + b.text.replace(",", "|") + "," + c.text.replace(",", "|") +"\n" )





f.close()
