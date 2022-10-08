import pandas as pd
import numpy as np

DataFrame = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])  

def intervalo_mais_populares(df):
  """Retorna o intervalo de tempo one é possivel achar as musicas mais populares
  """
  ouvintes = df["Ouvintes"]
  desv_pad = np.std(ouvintes)
  media = np.mean(ouvintes)
  
  mais_populares = df[["Ouvintes", "Length"]][ouvintes > media+desv_pad]
  return mais_populares["Length"].min() + "-" + mais_populares["Length"].max()

print(intervalo_mais_populares(DataFrame))