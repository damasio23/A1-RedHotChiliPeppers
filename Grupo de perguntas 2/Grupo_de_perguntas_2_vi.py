""" Este é o módulo de funções para a pergunta vi do grupo de perguntas 2 """

import numpy as np
import pandas as pd

# Algumas palavras (como "the", "and", "a") e caracteres especiais podem ser desconsideradas na apuração das palavras mais frequentes
termos_invalidos = ['the', 'a', 'an', 'it', 'some', 'any', 'to', 'in', 'on', 'at', 'for', 'by', 'with', 'out', 'away', 'about', 'of', 'off', 'and', 'or', 'but', 'so', 'because', 'as', 'then', 'if', '"', ':']

###################################################################################################################################

def frequencia_titulo_musica_na_letra(dataframe):
    """Função que avalia se as palavras nos títulos das músicas aparecem nas letras das respectivas músicas
    
    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Série cujos índices são os nomes das músicas, e os valores são o número de recorrências dos títulos das músicas nas letras
    :rtype: pandas.core.series.Series
    """
    try:
        dataframe_copia = dataframe.copy()
        dataframe_copia.reset_index(inplace=True)
    except AttributeError:
        return "Erro na função frequencia_titulo_musica_na_letra(): O tipo do argumento deve ser um dataframe de pandas"
    
    # Lista com nomes das músicas
    try:
        nomes_musicas = list(dataframe_copia['Title'])
    except KeyError:
        return "Erro na função frequencia_titulo_musica_na_letra(): No dataframe informado não há nenhuma coluna com o nome 'Title'"
    
    # Lista com as letras de todas as músicas
    try:
        letras_musicas = list(dataframe_copia["Letra"])
    except KeyError:
        return "Erro na função frequencia_titulo_musica_na_letra(): No dataframe informado não há nenhuma coluna com o nome 'Letra'"
    
    # Vamos definir um dicionário cujas chaves serão os nomes das músicas, e os valores serão os dicionários gerados pelo for loop a seguir
    recorrencia_titulos_musicas_nas_letras = dict()

    # A cada iteração, este for loop gera um dicionário cujas chaves são as palavras nos nomes das músicas, e os valores são a frequência delas nas respectivas letras
    contador = 0
    for nome_musica in nomes_musicas:
        # Lista com as palavras constituintes do nome da música separadas
        try:
            palavras_separadas = nome_musica.split()
        except AttributeError:
            return "Erro na função frequencia_titulo_musica_na_letra(): Os elementos da coluna Title devem ser strings."
        
        # Filtrando as palavras válidas do nome da música
        palavras_validas_musica = []
        for palavra in palavras_separadas:
            if palavra.lower() not in termos_invalidos:
                palavras_validas_musica.append(palavra.lower()) # Aqui, convertemos as palavras para lowercase para evitar duplicatas (como "you" e "You")
        del palavra
        ###############

        # Acessando a letra da música em questão
        letra_musica = letras_musicas[contador]
        contador += 1

        # Lista com as palavras da letra da música separadas
        letra_palavras_separadas = []
        try:
            letra_musica.split()
        except AttributeError:
            return "Erro na função frequencia_titulo_musica_na_letra(): Os elementos da coluna Letra devem ser strings."
        else:
            for palavra in letra_musica.split():
                letra_palavras_separadas.append(palavra.lower()) # Aqui, convertemos as palavras para lowercase para evitar duplicatas (como "you" e "You")
            del palavra
        letra_palavras_separadas.sort()

        # Filtrando as palavras inválidas da letra da música
        palavras_validas_letra = []
        for palavra in letra_palavras_separadas:
            if palavra not in termos_invalidos:
                palavras_validas_letra.append(palavra)
        del palavra
        ###############

        # Convertendo a lista palavras_validas_letra para série, usaremos value_counts para contar os registros
        serie_palavras_validas_letra = pd.Series(palavras_validas_letra)

        # Utilizando value_counts, temos uma série que informa as frequências das palavras
        frequencia_palavras = pd.Series(serie_palavras_validas_letra).value_counts()
        
        # Agora, vamos contabilizar quantas vezes cada palavra no título da música aparece na respectiva letra
        frequencia_palavras_titulo_musica = dict()
        for palavra in palavras_validas_musica: # Para cada palavra no título da música
            if palavra in frequencia_palavras.keys():
                frequencia = frequencia_palavras[palavra]
                frequencia_palavras_titulo_musica[palavra] = frequencia
        ###############

        # Por fim, adicionamos o item ao dicionário recorrencia_titulos_musicas_nas_letras
        recorrencia_titulos_musicas_nas_letras[nome_musica] = frequencia_palavras_titulo_musica
    
    # Convertendo o dicionário final para série
    
    serie_recorrencia_titulos_musicas_nas_letras = pd.Series(recorrencia_titulos_musicas_nas_letras)
    return serie_recorrencia_titulos_musicas_nas_letras
###################################################################################################################################

def recorrencia_titulos_musicas_na_letra(dataframe):
    """Função que mensura a recorrência do tema do título de uma música na sua respectiva letra
    A razão de recorrência foi definida como a razão entre média de registros das palavras nos títulos das músicas na respectiva letra e
    a quantidade total de palavras na letra daquela música.
    Considerou-se "recorrente" o título de uma música em que esta razão é igual ou maior que 0.025, e "não recorrente" caso contrário.

    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Série cujos índices são os nomes das músicas, e os valores são "recorrente" ou "não recorrente", que informam se o título daquela música é tema recorrente na sua letra ou não
    :rtype: pandas.core.series.Series
    """
    try:
        dataframe_copia = dataframe.copy()
        dataframe_copia.reset_index(inplace=True)
    except AttributeError:
        return "Erro na função recorrencia_titulos_musicas_na_letra(): O tipo do argumento deve ser um dataframe de pandas"
    
    # Primeiro, pegamos a série retornada na função anterior
    try:
        serie_recorrencias = frequencia_titulo_musica_na_letra(dataframe)
        if type(serie_recorrencias) == str:
            raise TypeError
    except TypeError:
        return "Erro na função recorrencia_titulos_musicas_na_letra(): A função frequencia_titulo_musica_na_letra() retornou um erro."
    
    nomes_musicas = list(serie_recorrencias.keys())
    
    # Vamos iterar sobre cada um dos valores da lista dos nomes das músicas. Calcularemos para cada um o índice de recorrência do título na respectiva letra
    # Os valores dos índices de recorrência de cada música serão armazenados no dicionário indices_recorrencias
    indices_recorrencias = dict()
    
    contador = 0
    for nome_musica in nomes_musicas:
        dicionario_frequencias = serie_recorrencias[nome_musica]
        valores_frequencias = list(dicionario_frequencias.values())
        
        # O critério definido para avaliar se o título de uma música é tema recorrente na sua letra ou não foi a partir da média de frequências relativa àquela música
        # Quando a lista valores_frequencias é vazia, consideramos que a média é 0.
        try:
            media_frequencias = sum(valores_frequencias)/len(valores_frequencias)
        except ZeroDivisionError:
            media_frequencias = 0
        ####################

        # Em seguida, vamos fazer a razão da média com a quantidade total de palavras na letra daquela música
        # Mas, para isso, precisamos saber o número de palavras na letra da música em questão. Faremos um procedimento semelhante ao da função anterior
        
        # Lista com as letras de todas as músicas
        try:
            letras_musicas = list(dataframe_copia["Letra"])
        except KeyError:
            return "Erro na função recorrencia_titulos_musicas_na_letra(): No dataframe informado não há nenhuma coluna com o nome 'Letra'."

        # Letra da música em questão no for loop
        letra_musica = letras_musicas[contador]
        contador+=1

        # Separando as palavras com split(), filtrando as palavras válidas
        palavras_validas_letra = []

        try:
            if type(letra_musica) != str:
                raise TypeError
        except TypeError:
            return "Erro na função recorrencia_titulos_musicas_na_letra(): Os elementos da coluna 'Letra' devem ser strings."
        else:
            palavras_letra_musica = letra_musica.split()

        for palavra in palavras_letra_musica:
            if palavra.lower() not in termos_invalidos:
                palavras_validas_letra.append(palavra.lower()) # Aqui, convertemos as palavras para lowercase para evitar duplicatas (como "you" e "You")
        del palavra

        # Agora, para saber a quantidade de palavras na letra desta música, aplicamos len() e então calculamos a razão de recorrência
        quant_palavras_letra = len(palavras_validas_letra)
        try:
            razao_recorrencia = media_frequencias/quant_palavras_letra # Note que esta razão é um float entre 0 e 1 muito próximo de 0
        except ZeroDivisionError:
            return "Erro na função recorrencia_titulos_musicas_na_letra(): A coluna Letra é vazia."
        
        # O critério para avaliar se o título de uma música é tema recorrente na sua letra ou não será se a razão for maior ou igual a 0.025
        if razao_recorrencia >= 0.025:
            indices_recorrencias[nome_musica] = "recorrente"
        else:
            indices_recorrencias[nome_musica] = "não recorrente"

    serie_indices_recorrencias = pd.Series(indices_recorrencias)
    return serie_indices_recorrencias
###################################################################################################################################
