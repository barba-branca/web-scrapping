# web-scrapping - como rapar cas informaçoes de um site
Web-scrapping integrada com whatspp e db
Primeiro vc deve fazer as instalaçoes 

pip install requests beautifulsoup4 smtplib

Depois voce deve criar importar as bibliotecas

import request
from bs4 import BeautifulSoup

A biblioteca BeaitifulSoap serve para fazer a captura e raspagem de dados da web

Depois voce cria uma variavel chamada link recebendo o site que deseja fazer as rapagem de dados

link = www.gogle.com.br

Para o beautifulsoup acessar o site desejado
Obs: quando você da esse comando o site ja saberar que voce esta fazendo um web-scrapping

Depois é so voce declarar uma variavel

titulo = site.find(title)

Que ele ira fazer uma rapagem dos dados inserida pelo usuario.
