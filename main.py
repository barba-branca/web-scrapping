import requests
from bs4 import BeautifulSoup

#adicionar o link para fazer a varredura de dadod

link = "https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

requisicao = requests.get(link, headers=headers)
print(requisicao)
# print(requisicao.text)
site = BeautifulSoup(requisicao.text, "html.parser")
#print (ste.prettify())

titulo = site.find("title")
print(titulo)

#pesquisa = site.find_all("textarea")
#print(pesquisa)

# pesquisa2 = site.find("textarea", class_="gLFyf")
# print(pesquisa2)
# print(pesquisa2["value"])

cotacao_dolar =site.find("span", class_="DFlfde SwHCTb")
print(cotacao_dolar.get_text())
print(cotacao_dolar["data-value"])
