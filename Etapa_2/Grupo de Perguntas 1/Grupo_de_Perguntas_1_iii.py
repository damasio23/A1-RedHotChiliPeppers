""" Música mais ouvida e música menos ouvida [em toda a história da banda ou artista] """

import numpy as np
import pandas as pd

# Tabela com as informações. 
df_excel = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])

# Função para retornar a música mais ouvida em toda a história da banda.
def musica_mais_ouvida(DataFrame):
    """ Função que retorna a música mais ouvida em toda a história da banda.
    
    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Dataframe com as informações da música mais ouvida da banda.
    :rtype: pandas.core.frame.DataFame
    """

    ouvintes = DataFrame["Ouvintes"][DataFrame["Ouvintes"] == DataFrame["Ouvintes"].max()]
    return ouvintes   
print("Música mais ouvida em toda a história da banda\n", musica_mais_ouvida(df_excel))

# Função para retornar a música menos ouvida em toda a história da banda.
def musica_menos_ouvidas(DataFrame):
    """ Função que retorna a música menos ouvida em toda a história da banda.
    
    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Dataframe com as informações da música menos ouvida da banda.
    :rtype: pandas.core.frame.DataFame
    """

    ouvintes = DataFrame["Ouvintes"][DataFrame["Ouvintes"] == DataFrame["Ouvintes"].min()]
    return ouvintes   
print("Música menoss ouvida em toda a história da banda\n", musica_menos_ouvidas(df_excel))
