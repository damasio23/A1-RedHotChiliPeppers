import numpy as np
import pandas as pd

"""
Músicas mais ouvidas e músicas menos ouvidas [em toda a história da banda ou artista]
 
"""
##Tabela com as informações. 
df_excel = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])

#Função para retornar a música mais ouvida em toda a história da banda.
def musica_mais_ouvida(DataFrame):
    ouvintes = DataFrame["Ouvintes"][DataFrame["Ouvintes"] == DataFrame["Ouvintes"].max()]
    return ouvintes   
print("Música mais ouvida em toda a história da banda\n", musica_mais_ouvida(df_excel))

#Função para retornar a música menos ouvida em toda a história da banda.
def musica_menos_ouvidas(DataFrame):
    ouvintes = DataFrame["Ouvintes"][DataFrame["Ouvintes"] == DataFrame["Ouvintes"].min()]
    return ouvintes   
print("Música menoss ouvida em toda a história da banda\n", musica_menos_ouvidas(df_excel))








