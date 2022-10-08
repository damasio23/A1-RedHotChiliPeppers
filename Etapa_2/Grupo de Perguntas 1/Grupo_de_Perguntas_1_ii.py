""" Músicas mais longas e músicas mais curtas por Álbum """

import numpy as np
import pandas as pd

# Tabela com as informações. 
df_excel = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])

# Todos os álbuns.
albuns = set(df_excel.index.get_level_values("Album"))
# DataFrame dos álbuns.
df_albuns = pd.DataFrame(albuns)

# Função para retornar as músicas mais longas de cada álbum.
def musicas_mais_longas_de_cada_album(DataFrame):
    """ Função que retorna as músicas mais longas de cada álbum da banda.
    
    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Dataframe com os álbuns das bandas, as respectivas músicas mais longas e a duração.
    :rtype: pandas.core.frame.DataFame
    """

    musicas_mais_longas = []
    for Album in albuns:
        musica_longa = DataFrame["Length"][DataFrame["Length"] == DataFrame.loc[Album]["Length"].max()]
        musicas_mais_longas.append(musica_longa)
    musicas_mais_longas = pd.concat(musicas_mais_longas)

    return musicas_mais_longas 
print("Músicas mais longas de cada album\n", musicas_mais_longas_de_cada_album(df_excel))


# Função para retornar as músicas mais curtas de cada álbum.
def musicas_mais_curtas_de_cada_album(DataFrame):
    """ Função que retorna as músicas mais curtas de cada álbum da banda.
    
    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Dataframe com os álbuns das bandas, as respectivas músicas mais curtas e a duração.
    :rtype: pandas.core.frame.DataFame
    """

    musicas_mais_curtas = []
    for Album in albuns:
        musica_curta = DataFrame["Length"][DataFrame["Length"] == DataFrame.loc[Album]["Length"].min()]
        musicas_mais_curtas.append(musica_curta)
    musicas_mais_curtas = pd.concat(musicas_mais_curtas)

    return musicas_mais_curtas
print("Músicas mais curtas de cada album\n", musicas_mais_curtas_de_cada_album(df_excel))