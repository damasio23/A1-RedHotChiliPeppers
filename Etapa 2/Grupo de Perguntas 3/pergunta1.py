import numpy as np
import pandas as pd

"""
Álbum com mais músicas e álbum com menos músicas
"""
#Tabela com as informações. 
df_excel = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])

#A Função vai receber um DataFrame e vai me retornar um int64 com o album com o maior número de músicas.
def album_com_mais_musicas(DataFrame):
    x = pd.DataFrame(DataFrame.groupby(level=0).size())
    x.columns = ["número de músicas"]
    maior_album = x[x["número de músicas"] == x["número de músicas"].max()]
    return maior_album

print("Maior álbum:\n",type(album_com_mais_musicas(df_excel)))

print("#################################################################")

#A Função vai receber um DataFrame e vai me retornar um int64 com o album com o menor número de músicas.
def album_com_menos_musicas(DataFrame):
    x = pd.DataFrame(DataFrame.groupby(level=0).size())
    x.columns = ["número de músicas"]
    menor_album = x[x["número de músicas"] == x["número de músicas"].min()]
    return menor_album

print("Menor álbum:\n", album_com_menos_musicas(df_excel))