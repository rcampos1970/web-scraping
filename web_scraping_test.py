import requests
from bs4 import BeautifulSoup
import numpy

link = "https://seatable.io/en/online-datenbank-kostenlos/"
requisicao = requests.get(link)
site = BeautifulSoup(requisicao.text,"html.parser")
tag = "link"
file_name = "example.txt"
with open(file_name, 'w') as file:
    for variavel in site.find_all(tag):
        print(variavel["href"])
        file.write(variavel["href"])

#list = variavel[5]
#print(list.text)
