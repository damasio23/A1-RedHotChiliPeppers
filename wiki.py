import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

pagina = requests.get("https://pt.wikipedia.org/wiki/Discografia_de_Red_Hot_Chili_Peppers")
soup = BeautifulSoup(pagina.text, "html.parser")
tabela = soup.find("table", {"class":"wikitable"})
tabela = pd.read_html(str(tabela))
df_pt = pd.DataFrame(tabela[0])

pg_eng = "https://en.wikipedia.org/"
pagina = requests.get("https://en.wikipedia.org/wiki/Red_Hot_Chili_Peppers_discography")
soup = BeautifulSoup(pagina.text, "html.parser")
tabela = soup.find("table", {"class":"wikitable"})
df_eng = pd.read_html(str(tabela))
df_eng = pd.DataFrame(df_eng[0])

albums = tabela.find_all("a", href=True, title=True)
del(albums[-1])
albums_df_eng = []
for i in albums:
    p = requests.get(pg_eng + i["href"])
    s = BeautifulSoup(p.text, "html.parser")
    t = s.find_all("table", {"class":"tracklist"})
    if t:
      name = s.find("i").text
      df = [pd.read_html(str(i)) for i in t]
      df = [pd.DataFrame(i[0]) for i in df]
      df = pd.concat(df)
      df["No."] = df["No."].astype(str)
      df = df[df["No."].str.contains("Total")==False]
      df = df.drop(["Writer(s)"], axis=1, errors="ignore")
      df = df.drop(["No."], axis=0, errors="ignore")
      df["Title"] = df["Title"].apply(lambda x: re.sub('"', '', x))
      df.insert(0, "coluna", name)
      albums_df_eng.append(df)
    else:
        pass
albums_df_eng = pd.concat(albums_df_eng, ignore_index = True)
index = pd.MultiIndex.from_frame(albums_df_eng[["coluna", "Title"]])
new_df = pd.DataFrame(index = index, data = {"Length":albums_df_eng["Length"].tolist()})
print(new_df.to_string())