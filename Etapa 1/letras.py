import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

pg = "https://www.vagalume.com.br"
pagina = requests.get("https://www.vagalume.com.br/red-hot-chili-peppers/")
soup = BeautifulSoup(pagina.text, "html.parser")
a = soup.find_all("a", href=True, class_="nameMusic")

letras = []
print("Tabela 3:")
c = 1
for i in a:
    print(str(c) + "/310")
    c += 1
    x = requests.get(pg + i["href"])
    s = BeautifulSoup(x.text, "html.parser")
    t = s.find_all("div", {"id":"lyrics"})
    letras.append((re.sub(r"\(.*?\)", "", i.text).strip(), re.sub(r"<.*?>", "", re.sub("<br/>", "\n", str(t)))[1:-1]))
letras_final = pd.DataFrame(letras)
letras_final.columns = ["Title", "Letra"]

letras_final.to_csv("../DataFrames/letras_final.csv")