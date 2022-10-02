import pandas as pd
from bs4 import BeautifulSoup
import requests

pagina = requests.get("https://pt.wikipedia.org/wiki/Discografia_de_Red_Hot_Chili_Peppers")
soup = BeautifulSoup(pagina.text, "html.parser")
tabela = soup.find("table", {"class":"wikitable"})
tabela = pd.read_html(str(tabela))
df_pt = pd.DataFrame(tabela[0])
premios = df_pt["Certificações"]
premios["Certificações"] = premios["Certificações"].apply(lambda x: str(x).lstrip(":").split(":"))
premios.drop(premios.tail(2).index, inplace=True)
premios.at[10, "Certificações"] =  premios.at[10, "Certificações"][1:]

def f(x):
    l = []
    for i in x:
        i = i.strip()
        try:
            a1 = int(i[0])
            a2 = i[3:-4]
        except:
            a1 = 1
            a2 = i[:-4]
        a3 = i[-3:-1]
        l.append((a1, a2, a3))
    return l

premios["Certificações"] = premios["Certificações"].apply(f)

lista = [item for sublist in premios["Certificações"].to_list() for item in sublist]

lista_premios = ["Prata", "Ouro", "Platina"]

lista_colunas = list(dict.fromkeys(int(i[2]) for i in lista))

df_excel = pd.read_excel("new_df.xls", index_col=[0,1])
albums = list(dict.fromkeys(df_excel.index.get_level_values("Album")))[0:-1]

index = pd.MultiIndex.from_product([albums, lista_premios], names=["Album", "Record"])

df = pd.DataFrame(data = 0, index = index, columns = lista_colunas)
count = 0
for i in albums:
    a = premios["Certificações"][count]
    for j in a:
        df.at[(i, j[1]), int(j[2])] = j[0]
    count += 1

df[28] += df[[31, 36, 39]].sum(axis=1)
df[26] += df[[35, 41]].sum(axis=1)
df[27] += df[45]
df[24] += df[46]

df.drop([31, 35, 36, 39, 41, 45, 46], axis=1, inplace = True)

df.columns = ["GB", "US", "CA", "AU", "DE", "UE", "BR", "NZ", "HU", "EN", "IT"]

print(df)
df.to_csv("../DataFrames/premios.csv")