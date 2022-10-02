import numpy as np
import pandas as pd

"""
Músicas mais longas e músicas mais curtas [em toda a história da banda ou artista]
 
"""
##Tabela com as informações. 
df_excel = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])

#Função para retornar a música mais longa em toda a história da banda.
def musica_mais_longa(DataFrame):
    tempo = DataFrame["Length"][DataFrame["Length"] == DataFrame["Length"].max()]
    return tempo  
print("Música mais longa em toda a história da banda\n", musica_mais_longa(df_excel))

#Função para retornar a música mais curta em toda a história da banda.
def musica_mais_curta(DataFrame):
    tempo = DataFrame["Length"][DataFrame["Length"] == DataFrame["Length"].min()]
    return tempo
print("Música mais curta em toda a história da banda\n", musica_mais_curta(df_excel))