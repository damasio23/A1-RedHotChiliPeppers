import pandas as pd

premios = pd.read_csv("../../DataFrames/premios.csv", index_col=[0, 1])

def album_mais_premiado(DataFrame):
    df = pd.DataFrame(DataFrame.groupby(level=0).sum().sum(axis=1))
    df.columns = ["Premios Totais"]
    return df[df["Premios Totais"] == df["Premios Totais"].max()]

print(album_mais_premiado(premios))