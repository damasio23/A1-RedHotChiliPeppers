import numpy as np
import pandas as pd

"""
Músicas mais longas e músicas mais curtas por Álbum
"""
#Tabela com as informações. 
df_excel = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])

#Todos os albuns.
albuns = set(df_excel.index.get_level_values("Album"))
#DataFrame dos albuns.
df_albuns = pd.DataFrame(albuns)

#Função para retornar as músicas mais longas de cada album.
def musicas_mais_longas_de_cada_album(DataFrame):  
     musicas_mais_longas = []
     for Album in albuns:
         x = DataFrame["Length"][DataFrame["Length"] == DataFrame.loc[Album]["Length"].max()]
         musicas_mais_longas.append(x)
     musicas_mais_longas = pd.concat(musicas_mais_longas)

     return musicas_mais_longas 
print("Músicas mais longas de cada album\n", musicas_mais_longas_de_cada_album(df_excel))


#Função para retornar as músicas mais curtas de cada album.
def musicas_mais_curtas_de_cada_album(DataFrame):  
     musicas_mais_curtas = []
     for Album in albuns:
         x = DataFrame["Length"][DataFrame["Length"] == DataFrame.loc[Album]["Length"].min()]
         musicas_mais_curtas.append(x)
     musicas_mais_curtas = pd.concat(musicas_mais_curtas)

     return musicas_mais_curtas
print("Músicas mais curtas de cada album\n", musicas_mais_curtas_de_cada_album(df_excel))