""" Este é o módulo de funções para a pergunta ii do grupo de perguntas 2 """

import numpy as np
import pandas as pd

# Algumas palavras (como "the", "and", "a") e caracteres especiais podem ser desconsideradas na apuração das palavras mais frequentes
termos_invalidos = ['the', 'a', 'an', 'it', 'some', 'any', 'to', 'in', 'on', 'at', 'for', 'by', 'with', 'out', 'away', 'about', 'of', 'off', 'and', 'or', 'but', 'so', 'because', 'as', 'then', 'if', '"', ':']

###################################################################################################################################
def palavras_mais_comuns_titulos_musicas(dataframe):
    """Função que retorna as palavras mais comuns nos títulos das músicas da banda, isto é, as que tiverem frequência maior que a metade da frequência máxima.
    Por exemplo, se a palavra mais comum aparecer 10 vezes, as mais comuns serão as que tiverem frequência maior que 5.

    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Série com as palavras mais comuns nos títulos das músicas como chave e as frequências como valores
    :rtype: pandas.core.series.Series
    """
    try:
        dataframe_copia = dataframe.copy()
        dataframe_copia.reset_index(inplace=True)
    except AttributeError:
        return "Erro na função palavras_mais_comuns_titulos_musicas(): O tipo do argumento deve ser um dataframe de pandas"
    
    # Lista com nomes dos álbums
    try:
        nomes_musicas = list(set(dataframe_copia['Title']))
    except KeyError:
        return "Erro na função palavras_mais_comuns_titulos_musicas(): No dataframe informado não há nenhuma coluna com o nome 'Title'"

    musicas_palavras_separadas = []
    for musica in nomes_musicas:
        try:
            if type(musica) != str:
                raise AttributeError
        except AttributeError:
            return "Erro na função palavras_mais_comuns_titulos_musicas(): Os elementos da coluna Album devem ser strings"
        else:
            musica.split()
            for palavra in musica.split():
                musicas_palavras_separadas.append(palavra.lower())
    
    musicas_palavras_separadas.sort()
    
    # Convertendo a lista musicas_palavras_separadas para série a fim de usar value_counts para contar os registros
    serie_palavras_musicas = pd.Series(musicas_palavras_separadas)
    
    # Utilizando value_counts, temos uma série que informa as palavras mais frequentes
    frequencia_palavras = dict(pd.Index(serie_palavras_musicas).value_counts())
    
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
        return "Não há palavras significativamente frequentes nos títulos das músicas"
    else:
        serie_palavras_mais_frequentes = pd.Series(palavras_mais_frequentes)
        return serie_palavras_mais_frequentes
###################################################################################################################################

# Dataframe com os dados necessários
df = pd.read_excel("DataFrames/new_df.xls", index_col=[0,1])

# Exemplo de funcionamento
print('#'*50)
print("Palavras mais comuns nos títulos das músicas\n")
print(palavras_mais_comuns_titulos_musicas(df))
print('#'*50)
