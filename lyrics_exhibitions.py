import requests
import lxml
from bs4 import BeautifulSoup

def extrair_num_exibicoes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")

    parse = str(soup.find_all("div", class_="cnt-info_exib"))
    num_exibicoes = int(parse[42:len(parse)-11].replace(".", ""))
    
    return num_exibicoes

########################

def extrair_letra(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    
    parse = list(soup.find_all("p"))
    for i in range(0,3):
        parse.pop(len(parse)-1)

    lyrics = []
    for item in parse:
        strophe = str(item).replace("/", "").replace("<p>","").replace("<br>","\n")
        #print("=>", strophe)
        lyrics.append(strophe)
    
    return lyrics

######################## Testando as funções ########################

url_test = "https://www.letras.mus.br/red-hot-chili-peppers/32764/"
print(extrair_num_exibicoes(url_test))
print(extrair_letra(url_test))