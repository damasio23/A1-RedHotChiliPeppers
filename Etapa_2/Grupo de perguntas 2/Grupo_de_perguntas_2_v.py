""" Este é o módulo de funções para a pergunta v do grupo de perguntas 2 """

import numpy as np
import pandas as pd

# Algumas palavras (como "the", "and", "a") e caracteres especiais podem ser desconsideradas na apuração das palavras mais frequentes
termos_invalidos = ['the', 'a', 'an', 'it', 'some', 'any', 'to', 'in', 'on', 'at', 'for', 'by', 'with', 'out', 'away', 'about', 'of', 'off', 'and', 'or', 'but', 'so', 'because', 'as', 'then', 'if', '"', ':']

###################################################################################################################################

def frequencia_titulo_album_nas_letras(dataframe):
    """Função que avalia se as palavras nos títulos dos álbuns aparecem nas letras das músicas daquele álbum
    
    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Série cujos índices são os nomes dos álbuns, e os valores são o número de recorrências dos títulos de álbuns nas letras
    :rtype: pandas.core.series.Series
    """
    try:
        dataframe_copia = dataframe.copy()
        dataframe_copia.reset_index(inplace=True)
    except AttributeError:
        return "Erro na função frequencia_titulo_album_nas_letras(): O tipo do argumento deve ser um dataframe de pandas"
    
    # Lista com nomes dos álbums
    try:
        nomes_albuns = list(set(dataframe_copia['Album']))
        nomes_albuns.sort()
    except KeyError:
        return "Erro na função palavras_mais_comuns_titulos_albuns(): No dataframe informado não há nenhuma coluna com o nome 'Album'"
    
    # Vamos definir um dicionário cujas chaves serão os nomes dos álbuns, e os valores serão os dicionários gerados pelo for loop a seguir
    recorrencia_titulos_albuns_nas_letras = dict()

    # A cada iteração, este for loop gera um dicionário cujas chaves são as palavras nos nomes dos álbuns, e os valores são a frequência delas nas letras das músicas
    for nome_album in nomes_albuns:
        # Lista com as palavras constituintes do nome dos álbuns separadas
        try:
            palavras_separadas = nome_album.split()
        except AttributeError:
            return "Erro na função palavras_mais_comuns_titulos_albuns(): Os elementos da coluna Album devem ser strings"

        # Filtrando as palavras válidas do nome do álbum
        palavras_validas_album = []
        for palavra in palavras_separadas:
            if palavra.lower() not in termos_invalidos:
                palavras_validas_album.append(palavra.lower()) # Aqui, convertemos as palavras para lowercase para evitar duplicatas (como "you" e "You")
        del palavra
        ###############

        # Acessando o sub-dataframe das músicas do álbum em questão
        try:
            df_musicas_album = dataframe.loc[nome_album]
            df_musicas_album.reset_index(inplace=True)
        except KeyError:
            return "Erro na função palavras_mais_comuns_titulos_albuns(): O dataframe informado não possui multiindex."

        # Lista com as letras das músicas do referido álbum
        try:
            letras_musicas = list(df_musicas_album["Letra"])
        except KeyError:
            return "Erro na função palavras_mais_comuns_titulos_albuns(): No dataframe informado não há nenhuma coluna com o nome 'Letra'."
        
        # Lista com as palavras das letras das músicas separadas
        letras_palavras_separadas = []
        for letra_musica in letras_musicas:
            try:
                letra_musica.split()
            except AttributeError:
                return "Erro na função palavras_mais_comuns_titulos_albuns(): Os elementos da coluna Letra devem ser strings"
            else:
                for palavra in letra_musica.split():
                    letras_palavras_separadas.append(palavra.lower()) # Aqui, convertemos as palavras para lowercase para evitar duplicatas (como "you" e "You")
                del palavra

        letras_palavras_separadas.sort()

        # Filtrando as palavras inválidas das letras das músicas
        palavras_validas_letras = []
        for palavra in letras_palavras_separadas:
            if palavra not in termos_invalidos:
                palavras_validas_letras.append(palavra)
        del palavra
        ###############

        # Convertendo a lista palavras_validas_letras para série a fim de usar value_counts para contar os registros
        serie_palavras_validas_letras = pd.Series(palavras_validas_letras)

        # Utilizando value_counts, temos uma série que informa as frequências das palavras
        frequencia_palavras = pd.Series(serie_palavras_validas_letras).value_counts()
        
        # Agora, vamos contabilizar quantas vezes cada palavra no título do álbum aparece nas letras das músicas
        frequencia_palavra_album = dict()
        for palavra_album in palavras_validas_album:
            if palavra_album in frequencia_palavras.keys():
                frequencia = frequencia_palavras[palavra_album]
                frequencia_palavra_album[palavra_album] = frequencia
        ###############

        # Por fim, adicionamos o item ao dicionário recorrencia_titulos_albuns_nas_letras
        recorrencia_titulos_albuns_nas_letras[nome_album] = frequencia_palavra_album
    
    # Convertendo o dicionário final para série
    
    serie_recorrencia_titulos_albuns_nas_letras = pd.Series(recorrencia_titulos_albuns_nas_letras)
    return serie_recorrencia_titulos_albuns_nas_letras

###################################################################################################################################

def recorrencia_titulos_albuns_nas_letras(dataframe):
    """Função que mensura a recorrência do tema do título de um álbum nas letras
    A razão de recorrência foi definida como a razão entre média de registros das palavras dos títulos dos álbuns nas letras e
    a quantidade total de palavras nas letras das músicas daquele álbum.
    Considerou-se "recorrente" o título de um álbum em que esta razão é igual ou maior que 0.003, e "não recorrente" caso contrário.

    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Série cujos índices são os nomes dos álbuns, e os valores são "recorrente" ou "não recorrente", que informam se o título daquele álbum é tema recorrente nas letras ou não
    :rtype: pandas.core.series.Series
    """

    try:
        dataframe_copia = dataframe.copy()
        dataframe_copia.reset_index(inplace=True)
    except AttributeError:
        return "Erro na função recorrencia_titulos_albuns_nas_letras(): O tipo do argumento deve ser um dataframe de pandas"
    
    # Lista com nomes dos álbums
    try:
        nomes_albuns = list(set(dataframe_copia['Album']))
        nomes_albuns.sort()
    except KeyError:
        return "Erro na função recorrencia_titulos_albuns_nas_letras(): No dataframe informado não há nenhuma coluna com o nome 'Album'"
    
    # Primeiro, pegamos a série retornada na função anterior
    try:
        serie_recorrencias = frequencia_titulo_album_nas_letras(dataframe)
        if type(serie_recorrencias) == str:
            raise TypeError
    except TypeError:
        return "Erro na função recorrencia_titulos_albuns_nas_letras(): A função frequencia_titulo_album_nas_letras() retornou um erro."
    
    nomes_albuns = list(serie_recorrencias.keys())
    nomes_albuns.sort()

    # Vamos iterar sobre cada um dos valores da lista dos nomes dos álbuns. Calcularemos para cada um o índice de recorrência do título nas suas músicas
    # Os valores dos índices de recorrência de cada álbum serão armazenados no dicionário indices_recorrencias
    indices_recorrencias = dict()
    for nome_album in nomes_albuns:
        dicionario_frequencias = serie_recorrencias[nome_album]
        valores_frequencias = list(dicionario_frequencias.values())
        
        # O critério definido para avaliar se o título de um álbum é tema recorrente nas letras ou não foi a partir da média de frequências relativa àquele álbum
        # Quando a lista valores_frequencias é vazia, consideramos que a média é 0
        try:
            media_frequencias = sum(valores_frequencias)/len(valores_frequencias)
        except ZeroDivisionError:
            media_frequencias = 0
        ####################

        # Em seguida, vamos fazer a razão da média com a quantidade total de palavras naquele álbum
        # Mas, para isso, precisamos da soma dos números de palavras em todas as músicas do álbum em questão. Faremos um procedimento semelhante ao da função anterior
        
        # Acessando o sub-dataframe das músicas do álbum em questão
        try:
            df_musicas_album = dataframe.loc[nome_album]
            df_musicas_album.reset_index(inplace=True)
        except KeyError:
            return f"Erro na função recorrencia_titulos_albuns_nas_letras(): O dataframe informado não possui multiindex."
        
        # Lista com as letras das músicas do referido álbum
        try:
            letras_musicas = list(df_musicas_album["Letra"])
        except KeyError:
            return "Erro na função recorrencia_titulos_albuns_nas_letras(): No dataframe informado não há nenhuma coluna com o nome 'Letra'."

        # Lista com as palavras das letras das músicas separadas
        letras_palavras_separadas = []
        for letra_musica in letras_musicas:
            try:
                if type(letra_musica) != str:
                    raise AttributeError
            except AttributeError:
                return "Erro na função recorrencia_titulos_albuns_nas_letras(): Os elementos da coluna Letra devem ser strings."
            else:
                letra_musica.split()
                for palavra in letra_musica.split():
                    letras_palavras_separadas.append(palavra.lower()) # Aqui, convertemos as palavras para lowercase para evitar duplicatas (como "you" e "You")
                del palavra
        
        letras_palavras_separadas.sort()

        # Filtrando as palavras válidas do nome do álbum
        palavras_validas_album = []
        for palavra in letras_palavras_separadas:
            if palavra.lower() not in termos_invalidos:
                palavras_validas_album.append(palavra.lower()) # Aqui, convertemos as palavras para lowercase para evitar duplicatas (como "you" e "You")
        del palavra
        ###############
        
        # Agora, para saber o número de palavras, basta aplicar a função len(), e então, calcular a razão de recorrência
        quant_total_palavras = len(palavras_validas_album)
        try:
            razao_media_quant_total = media_frequencias/quant_total_palavras # Note que esta razão é um float entre 0 e 1 muito próximo de 0
        except ZeroDivisionError:
            return "Erro na função recorrencia_titulos_albuns_nas_letras(): A coluna Letra é vazia."
        
        # O critério para avaliar se o título de um álbum é tema recorrente nas letras ou não será se a razão for maior ou igual a 0.003
        if razao_media_quant_total >= 0.003:
            indices_recorrencias[nome_album] = "recorrente"
        else:
            indices_recorrencias[nome_album] = "não recorrente"

    
    serie_indices_recorrencias = pd.Series(indices_recorrencias)
    return serie_indices_recorrencias
###################################################################################################################################

# Dataframe com os dados necessários
df = pd.read_excel("DataFrames/new_df.xls", index_col=[0,1])

# Exemplo de funcionamento
print('#'*50)
print("Recorrência do tema dos títulos dos álbuns nas letras\n")
print(recorrencia_titulos_albuns_nas_letras(df))
print('#'*50)
