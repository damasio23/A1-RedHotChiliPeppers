""" Este é o módulo de funções para a pergunta iii do grupo de perguntas 2 """

import numpy as np
import pandas as pd

# Algumas palavras (como "the", "and", "a") e caracteres especiais podem ser desconsideradas na apuração das palavras mais frequentes
termos_invalidos = ['the', 'a', 'an', 'it', 'some', 'any', 'to', 'in', 'on', 'at', 'for', 'by', 'with', 'out', 'away', 'about', 'of', 'off', 'and', 'or', 'but', 'so', 'because', 'as', 'then', 'if', '"', ':']

###################################################################################################################################
def palavras_mais_comuns_letras_album(dataframe):
    """Função que retorna as palavras mais comuns nas letras das músicas por álbum da banda
    Consideramos como mais comuns as palavras que tiverem frequência maior que o desvio padrão das frequências das palavras nas letras de música por álbum.
        
    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Série cujos índices são os álbuns da banda, e os valores são dicionários nos quais as palavras mais comuns são as chaves, e as frequências são os valores.
    :rtype: pandas.core.series.Series
    """

    try:
        dataframe_copia = dataframe.copy()
        dataframe_copia.reset_index(inplace=True)
    except AttributeError:
        return "Erro na função palavras_mais_comuns_letras_album(): O tipo do argumento deve ser um dataframe de pandas."
    
    # Lista com nomes dos álbums
    try:
        nomes_albuns = list(set(dataframe_copia['Album']))
        nomes_albuns.sort()
    except KeyError:
        return "Erro na função palavras_mais_comuns_letras_album(): No dataframe informado não há nenhuma coluna com o nome 'Album'."

    # Esta função retornará um dicionário cujas chaves são o nome do álbum e os valores são outros dicionários
    # Cada um destes dicionários terá como chaves as palavras mais comuns de suas músicas, e como valor, a frequência desta palavra
    dict_palavras_mais_frequentes = dict()

    # Vamos iterar sobre cada álbum da banda, que corresponderão a cada item do dicionário
    for nome_album in nomes_albuns:
        # Acessando o sub-dataframe das músicas do álbum em questão
        try:
            df_musicas_album = dataframe.loc[nome_album]
            df_musicas_album.reset_index(inplace=True)
        except KeyError:
            return "Erro na função palavras_mais_comuns_letras_album(): O dataframe informado não possui multiindex."

        # Definimos uma lista que vai conter todas as palavras de todas as letras de músicas do álbum em questão
        letras_palavras_separadas = []

        # Lista das letras das músicas
        try:
            letras_musicas = list(df_musicas_album["Letra"])
        except KeyError:
            return "Erro na função palavras_mais_comuns_letras_album(): No dataframe informado não há nenhuma coluna com o nome 'Letra'."

        # Pegando a letra de cada música. Aqui, letra_musica é uma longa string com a letra de cada música
        for letra_musica in letras_musicas:
            try:
                if type(letra_musica) != str:
                    raise AttributeError
            except AttributeError:
                return "Erro na função palavras_mais_comuns_letras_album(): Os elementos da coluna Letra devem ser strings."
            else:
                letra_musica.split()
                for palavra in letra_musica.split():
                    letras_palavras_separadas.append(palavra.lower())
    
        # Organizando a lista por ordem alfabética
        letras_palavras_separadas.sort()

        # Agora, vamos eliminar os termos_invalidos. Para isso, definimos a lista palavras_validas
        palavras_validas = []

        # Vamos selecionar as palavras válidas para fazer append() na lista palavras_validas
        for palavra_analisada in letras_palavras_separadas:
            if palavra_analisada not in termos_invalidos:
                palavras_validas.append(palavra_analisada)

        # Como vamos utilizar agora a lista palavras_validas, podemos deletar letras_palavras_separadas
        del letras_palavras_separadas

        # Convertendo a lista palavras_validas para série a fim de usar value_counts para contar os registros
        serie_palavras_validas = pd.Series(palavras_validas)
        
        # Utilizando value_counts, temos uma série que informa as palavras mais frequentes
        frequencia_palavras_validas = pd.Series(serie_palavras_validas).value_counts()
        
        # A distribuição das frequências das palavras é bastante assimétrica à direita, isto é, grande parte das ocorrências está à esquerda da média
        # Consideraremos, então, as palavras que tiverem frequência maior que o desvio padrão.
        desvio_frequencias = frequencia_palavras_validas.std()

        # Este é o dicionário em que vamos armazenar os registros mais frequentes, a serem tirados da série frequencia_palavras_validas
        palavras_mais_frequentes = dict()

        # Aplicando nesta série a função to_dict, obtemos um dicionário cujas chaves são as palavras, e os valores são as frequências.
        # Vamos, então, iterar sobre os itens deste dicionário
        for item_palavra_frequencia in frequencia_palavras_validas.to_dict().items():
            # Renomeando os componentes da tupla item_palavra_frequencia
            palavra = item_palavra_frequencia[0]
            frequencia = item_palavra_frequencia[1]

            if frequencia > desvio_frequencias:
                # Ou seja, se a frequência da palavra em questão for maior que o desvio padrão das frequências, então ela entra no dicionário palavras_mais_frequentes
                palavras_mais_frequentes[palavra] = frequencia

        # Finalmente, vamos criar o item do dicionário dict_palavras_mais_frequentes, passando como chave o nome do álbum, e como valor, o dicionário palavras_mais_frequentes
        dict_palavras_mais_frequentes[nome_album] = palavras_mais_frequentes

    serie_palavras_mais_frequentes = pd.Series(dict_palavras_mais_frequentes)
    return serie_palavras_mais_frequentes
###################################################################################################################################

# Dataframe com os dados necessários
df = pd.read_excel("DataFrames/new_df.xls", index_col=[0,1])

# Exemplo de funcionamento
print('#'*50)
print("Palavras mais comuns nas letras das músicas por álbum\n")
print(palavras_mais_comuns_letras_album(df))
print('#'*50)
