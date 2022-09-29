from unittest import result
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests

count = 1
tabela_geral = []
#Extraindo as tabelas de todas as páginas
while count < 11:
    count=str(count)
    pagina = requests.get('https://www.last.fm/pt/music/Red+Hot+Chili+Peppers/+tracks?page='+count)
    soup = BeautifulSoup(pagina.text, "html.parser")
    tabela = soup.find("table", {"class":"chartlist"})
#transformando em DataFrame
    tabela = pd.read_html(str(tabela))
    tabela_df = pd.DataFrame(tabela[0])
#limpando os anuncios 
    tabela_df = tabela_df[tabela_df["Ouvintes"].str.contains("Atualize")==False]
#pegando apenas as informações que eu quero (número de ouvintes de cada faixa)
    tabela_df_ouvintes = tabela_df[['Nome da faixa', 'Ouvintes']]
    count=int(count)
    count = count + 1
    tabela_geral.append(tabela_df_ouvintes)
tabela_geral_final = pd.concat(tabela_geral, ignore_index=True)

print(tabela_geral_final)