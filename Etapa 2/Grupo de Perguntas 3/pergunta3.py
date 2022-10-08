import numpy as np
import pandas as pd

"""
Média da popularidade das músicas e o desvio padrão
"""
#Tabela com as informações. 
df_excel = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])

#Função para me retornar a média da popularidade das músicas
def med_popularidade(DataFrame):
    mean = DataFrame['Ouvintes'].mean()
    return mean
print("Média da popularidade das músicas da banda:\n", med_popularidade(df_excel),"Ouvintes")

print("#################################################################")

#Função para me retornar o desvio padrão da popularidade das músicas
def std_popularidade(DataFrame):
    desvio_padrao = DataFrame['Ouvintes'].std()
    return desvio_padrao
print("Desvio Padrão da popularidade das músicas da banda:\n", std_popularidade(df_excel), "Ouvintes")

