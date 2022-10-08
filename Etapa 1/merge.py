import pandas as pd
import re

letras_final = pd.read_csv("../DataFrames/letras_final.csv")
albums_df_eng = pd.read_csv("../DataFrames/albums_df_eng.csv")
tabela_geral_final = pd.read_csv("../DataFrames/tabela_geral_final.csv")

letras_final["Title"] = letras_final["Title"].apply(lambda x: x.lower())
albums_df_eng["Title"] = albums_df_eng["Title"].apply(lambda x: x.lower())
tabela_geral_final["Title"] = tabela_geral_final["Title"].apply(lambda x: x.lower())
tabela_geral_final["Ouvintes"] = tabela_geral_final["Ouvintes"].apply(lambda x: int(re.sub("[^0-9]", "", x)))

letras_final.drop_duplicates(subset=["Title"], inplace=True)
letras_final["Title"] = letras_final["Title"].replace(["battle ship", "special secret song inside", "did i let you know?", "mellowship slinky in b-major"], ["battleship", "party on your pussy", "did i let you know", "mellowship slinky in b major"])

tabela_geral_final.drop_duplicates(subset=["Title"], inplace=True)

albums_df_eng = pd.merge(albums_df_eng, tabela_geral_final, how="left", on="Title")
albums_df_eng = pd.merge(albums_df_eng, letras_final, how="left", on="Title")
index = pd.MultiIndex.from_frame(albums_df_eng[["Album", "Title"]])
new_df = pd.DataFrame(index = index, data = {"Length":albums_df_eng["Length"].tolist(), "Ouvintes":albums_df_eng["Ouvintes"].tolist(), "Letra":albums_df_eng["Letra"].tolist()})

new_df.loc[new_df.Ouvintes.isnull(), "Ouvintes"] = [31.0, 1968.0, 2739.0]

new_df.to_excel("../DataFrames/new_df.xls")

print(new_df)