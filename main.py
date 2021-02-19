
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
urlsepeda="https://www.olx.co.id/items/q-frame-sepeda"
client=ureq(urlsepeda)
sepeda_html=client.read()
page_soup=soup(sepeda_html,"html.parser")
client.close()
semua=page_soup.findAll("div",{"class":"IKo3_"})
awalprice=page_soup.findAll("span",{"class":"_89yzn"})
price=awalprice[0].text

