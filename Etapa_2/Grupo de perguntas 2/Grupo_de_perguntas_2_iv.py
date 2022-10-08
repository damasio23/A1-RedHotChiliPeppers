""" Este é o módulo de funções para a pergunta iv do grupo de perguntas 2 """

import numpy as np
import pandas as pd

# Algumas palavras (como "the", "and", "a") e caracteres especiais podem ser desconsideradas na apuração das palavras mais frequentes
termos_invalidos = ['the', 'a', 'an', 'it', 'some', 'any', 'to', 'in', 'on', 'at', 'for', 'by', 'with', 'out', 'away', 'about', 'of', 'off', 'and', 'or', 'but', 'so', 'because', 'as', 'then', 'if', '"', ':']

###################################################################################################################################
def palavras_mais_comuns_letras_discografia(dataframe):
    """Função que retorna as palavras mais comuns nas letras de música de toda a discografia da banda
    Consideramos como mais comuns as palavras que tiverem frequência maior que o desvio padrão das frequências das palavras nas letras das músicas.
     
    :param dataframe: Dataframe fonte
    :type dataframe: pandas.core.frame.DataFrame
    :return: Série com as palavras mais comuns como índices e suas respectivas frequências como valores  
    :rtype: pandas.core.series.Series
    """
    try:
        dataframe_copia = dataframe.copy()
        dataframe_copia.reset_index(inplace=True)
    except AttributeError:
        return "Erro na função palavras_mais_comuns_letras_discografia(): O tipo do argumento deve ser um dataframe de pandas."
    
    # Vamos criar uma lista com as letras de todas as músicas da discografia.
    try:
        letras_musicas = list(dataframe_copia['Letra'])
    except KeyError:
        return "Erro na função palavras_mais_comuns_letras_discografia(): No dataframe informado, não há nenhuma coluna com o nome 'Letra'."

    # Todas as palavras de todas as letras serão colocadas em uma única lista.
    letras_palavras_separadas = []

    # Vamos iterar sobre cada letra de música da banda, separando as palavras.
    for letra_musica in letras_musicas:
        try:
            if type(letra_musica) != str:
                raise AttributeError
        except AttributeError:
            return "Erro na função palavras_mais_comuns_letras_discografia(): Os elementos da coluna Letra devem ser strings."
        else:
            letra_musica.split() # Lista das palavras que compõem a letra da música em questão
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

    # Aplicando em frequencia_palavras_validas a função to_dict, obtemos um dicionário cujas chaves são as palavras, e os valores são as frequências.
    # Vamos, então, iterar sobre os itens deste dicionário
    for item_palavra_frequencia in frequencia_palavras_validas.to_dict().items():
        # Renomeando os componentes da tupla item_palavra_frequencia
        palavra = item_palavra_frequencia[0]
        frequencia = item_palavra_frequencia[1]

        if frequencia > desvio_frequencias:
            # Ou seja, se a frequência da palavra em questão for maior que o desvio padrão das frequências, então ela entra no dicionário palavras_mais_frequentes
            palavras_mais_frequentes[palavra] = frequencia
    
    serie_palavras_mais_frequentes = pd.Series(palavras_mais_frequentes)
    return serie_palavras_mais_frequentes
###################################################################################################################################

# Dataframe com os dados necessários
df = pd.read_excel("DataFrames/new_df.xls", index_col=[0,1])

# Exemplo de funcionamento
print('#'*50)
print("Palavras mais comuns nas letras das músicas em toda a discografia\n")
print(palavras_mais_comuns_letras_discografia(df))
print('#'*50)
