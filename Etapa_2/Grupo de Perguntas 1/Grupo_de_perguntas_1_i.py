""" Músicas mais ouvidas e músicas menos ouvidas por Álbum """

import numpy as np
import pandas as pd

# Tabela com as informações. 
df_excel = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])

# Todos os álbuns.
albuns = set(df_excel.index.get_level_values("Album"))

# DataFrame dos álbuns.
df_albuns = pd.DataFrame(albuns)

# Função para retornar as músicas mais ouvidas de cada album.
def musicas_mais_ouvidas_de_cada_album(DataFrame):
    """ Função que retorna as músicas mais ouvidas de cada álbum da banda.
    
    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Dataframe com os álbuns das bandas, as respectivas músicas mais ouvidas e o número de ouvintes.
    :rtype: pandas.core.frame.DataFame
    """
    
    musicas_mais_ouvidas = []
    for Album in albuns:
        musica_popular = DataFrame["Ouvintes"][DataFrame["Ouvintes"] == DataFrame.loc[Album]["Ouvintes"].max()]
        musicas_mais_ouvidas.append(musica_popular)
    musicas_mais_ouvidas = pd.concat(musicas_mais_ouvidas)

    return musicas_mais_ouvidas  
print("Músicas mais ouvidas de cada album\n", musicas_mais_ouvidas_de_cada_album(df_excel))
 
#Função para retornar as músicas menos ouvidas de cada album.
def musicas_menos_ouvidas_de_cada_album(DataFrame):
    """ Função que retorna as músicas menos ouvidas de cada álbum da banda.
    
    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Dataframe com os álbuns das bandas, as respectivas músicas menos ouvidas e o número de ouvintes.
    :rtype: pandas.core.frame.DataFame
    """

    musicas_menos_ouvidas = []
    for Album in albuns:
        musica_pouco_popular = DataFrame["Ouvintes"][DataFrame["Ouvintes"] == DataFrame.loc[Album]["Ouvintes"].min()]
        musicas_menos_ouvidas.append(musica_pouco_popular)
    musicas_menos_ouvidas = pd.concat(musicas_menos_ouvidas)

    return musicas_menos_ouvidas  
print("Músicas menos ouvidas de cada album\n", musicas_menos_ouvidas_de_cada_album(df_excel))
