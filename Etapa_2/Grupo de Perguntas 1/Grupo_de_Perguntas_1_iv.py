""" Música mais longa e música mais curta [em toda a história da banda ou artista] """

import numpy as np
import pandas as pd

# Tabela com as informações. 
df_excel = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])

# Função para retornar a música mais longa em toda a história da banda.
def musica_mais_longa(DataFrame):
    """ Função que retorna a música mais longa em toda a história da banda.
    
    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Dataframe com as informações da música mais longa da banda.
    :rtype: pandas.core.frame.DataFame
    """

    tempo = DataFrame["Length"][DataFrame["Length"] == DataFrame["Length"].max()]
    return tempo  
print("Música mais longa em toda a história da banda\n", musica_mais_longa(df_excel))

# Função para retornar a música mais curta em toda a história da banda.
def musica_mais_curta(DataFrame):
    """ Função que retorna a música mais curta em toda a história da banda.
    
    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Dataframe com as informações da música mais curta da banda.
    :rtype: pandas.core.frame.DataFame
    """

    tempo = DataFrame["Length"][DataFrame["Length"] == DataFrame["Length"].min()]
    return tempo
print("Música mais curta em toda a história da banda\n", musica_mais_curta(df_excel))