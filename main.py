import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests

pagina = "https://m.letras.mus.br"
#pegar o conteudo da pagina
page = requests.get("https://m.letras.mus.br/red-hot-chili-peppers/discografia/")
soup = BeautifulSoup(page.content, "html.parser")
#pegar so a parte que contem a informacao que preciso
results = np.array(soup.find_all("a", href=True, class_="cnt g-1-4 g-p-1-2"))
#tirar tudo que nao seja albums
albums = np.array([i["data-type"] == "album" for i in results])
results = results[albums]

tuple = []

for i in results:
  nome_album = i.find("b").text
  #pegar o conteudo da pagina do album
  page2 = requests.get(pagina + i['href'])
  soup2 = BeautifulSoup(page2.content, "html.parser")
  #pegar so o nome da musica
  results2 = soup2.find_all("b", title=False)
  
  del(results2[-1])
  
  for j in results2:
    nome_cancao = j.text
    tuple.append((nome_album, nome_cancao))

index = pd.MultiIndex.from_tuples(tuple, names=["albums", "tracks"])
s = pd.Series("_", index=index)
print(s)