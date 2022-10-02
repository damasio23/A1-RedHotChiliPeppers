import numpy as np
import pandas as pd

"""
 Músicas mais ouvidas e músicas menos ouvidas por Álbum
 
 """

#Tabela com as informações. 
df_excel = pd.read_excel("new_df.xls", index_col=[0,1])

#Todos os albuns.
albuns = set(df_excel.index.get_level_values("Album"))
#DataFrame dos albuns.
df_albuns = pd.DataFrame(albuns)

#Função para retornar as músicas mais ouvidas de cada album.
def musicas_mais_ouvidas_de_cada_album(DataFrame):  
     musicas_mais_ouvidas = []
     for Album in albuns:
         x = DataFrame["Ouvintes"][DataFrame["Ouvintes"] == DataFrame.loc[Album]["Ouvintes"].max()]
         musicas_mais_ouvidas.append(x)
     musicas_mais_ouvidas = pd.concat(musicas_mais_ouvidas)

     return musicas_mais_ouvidas  
print("Músicas mais ouvidas de cada album\n", musicas_mais_ouvidas_de_cada_album(df_excel))
 
#Função para retornar as músicas menos ouvidas de cada album.
def musicas_menos_ouvidas_de_cada_album(DataFrame):  
     musicas_menos_ouvidas = []
     for Album in albuns:
         x = DataFrame["Ouvintes"][DataFrame["Ouvintes"] == DataFrame.loc[Album]["Ouvintes"].min()]
         musicas_menos_ouvidas.append(x)
     musicas_menos_ouvidas = pd.concat(musicas_menos_ouvidas)

     return musicas_menos_ouvidas  
print("Músicas menos ouvidas de cada album\n",musicas_menos_ouvidas_de_cada_album(df_excel))
