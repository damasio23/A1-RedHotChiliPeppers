""" Este é o módulo de funções para a pergunta i do grupo de perguntas 2 """

import numpy as np
import pandas as pd

# Algumas palavras (como "the", "and", "a") e caracteres especiais podem ser desconsideradas na apuração das palavras mais frequentes
termos_invalidos = ['the', 'a', 'an', 'it', 'some', 'any', 'to', 'in', 'on', 'at', 'for', 'by', 'with', 'out', 'away', 'about', 'of', 'off', 'and', 'or', 'but', 'so', 'because', 'as', 'then', 'if', '"', ':']

###################################################################################################################################
def palavras_mais_comuns_titulos_albuns(dataframe):
    """Função que retorna as palavras mais comuns nos títulos dos álbuns da banda, isto é, as que tiverem frequência maior ou igual a metade da frequência máxima.
    Por exemplo, se a palavra mais comum aparecer 10 vezes, as mais comuns serão as que tiverem frequência maior ou igual a 5.

    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Série com 
    :rtype: pandas.core.series.Series
    """
    try:
        dataframe_copia = dataframe.copy()
        dataframe_copia.reset_index(inplace=True)
    except AttributeError:
        return "Erro na função palavras_mais_comuns_titulos_albuns(): O tipo do argumento deve ser um dataframe de pandas"
    
    # Lista com nomes dos álbums
    try:
        nomes_albuns = list(set(dataframe_copia['Album']))
    except KeyError:
        return "Erro na função palavras_mais_comuns_titulos_albuns(): No dataframe informado não há nenhuma coluna com o nome 'Album'"
    
    albuns_palavras_separadas = []
    for album in nomes_albuns:
        try:
            if type(album) != str:
                raise AttributeError
        except AttributeError:
            return "Erro na função palavras_mais_comuns_titulos_albuns(): Os elementos da coluna Album devem ser strings"
        else:
            album.split()
            for palavra in album.split():
                albuns_palavras_separadas.append(palavra.lower())

    albuns_palavras_separadas.sort()
    
    # Convertendo a lista albuns_palavras_separadas para série a fim de usar value_counts para contar os registros
    serie_palavras_albuns = pd.Series(albuns_palavras_separadas)
    
    # Utilizando value_counts, temos uma série que informa as palavras mais frequentes
    frequencia_palavras = dict(pd.Series(serie_palavras_albuns).value_counts())
    
    # Filtrando as palavras válidas (aquelas que não estão na lista de termos_invalidos)
    palavras_validas = dict()
    for palavra in frequencia_palavras.items():
        if palavra[0] not in termos_invalidos:
            palavras_validas[palavra[0]] = palavra[1]
    
    # Pegando as mais frequentes. Consideraremos as que tiverem frequência maior que a metade da frequência máxima.
    # Por exemplo, se a palavra mais comum aparecer 10 vezes, as mais comuns serão as que tiverem frequência maior que 5.
    palavras_mais_frequentes = dict()
    for palavra in palavras_validas.items():
        maximo = max([frequencia for frequencia in palavras_validas.values()])
        if palavra[1] > [i for i in range(1, maximo+1)][int(maximo/2)-1]:
            palavras_mais_frequentes[palavra[0]] = palavra[1]
            del maximo
    
    # Consideração final
    if palavras_mais_frequentes == dict():
        return "Não há palavras significativamente frequentes nos títulos dos álbuns analisados"
    else:
        serie_palavras_mais_frequentes = pd.Series(palavras_mais_frequentes, dtype=object)
        return serie_palavras_mais_frequentes

###################################################################################################################################
