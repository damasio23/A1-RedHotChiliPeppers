import numpy as np
import pandas as pd

"""
Álbum mais ouvido e álbum menos ouvido.
"""
#Tabela com as informações. 
df_excel = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])

#A função vai me retornar o album mais ouvido da história da banda.
def album_mais_ouvido(DataFrame):
    df_ouvintes = pd.DataFrame(DataFrame["Ouvintes"])
    soma_dos_ouvintes = df_ouvintes.groupby(level=0).sum()
    album_mais_popular = soma_dos_ouvintes[soma_dos_ouvintes["Ouvintes"] == soma_dos_ouvintes["Ouvintes"].max()]
    return album_mais_popular 

print("Album mais ouvido da banda\n", album_mais_ouvido(df_excel))

print("#################################################################")

#A função vai me retornar o album menos ouvido da história da banda.
def album_mais_ouvido(DataFrame):
    df_ouvintes = pd.DataFrame(DataFrame["Ouvintes"])
    soma_dos_ouvintes = df_ouvintes.groupby(level=0).sum()
    album_menos_popular = soma_dos_ouvintes[soma_dos_ouvintes["Ouvintes"] == soma_dos_ouvintes["Ouvintes"].min()]
    return album_menos_popular 

print("Album menos ouvido da banda\n", album_mais_ouvido(df_excel))