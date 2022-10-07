import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")
sns.set_color_codes("pastel")
f, ax = plt.subplots(figsize=(6, 15))

df = pd.read_csv("../../DataFrames/premios.csv", index_col=[0,1])

print(df.sum(axis=1))

def peso(x):
    x.iat[1] *= 2
    x.iat[2] *= 3
    return x.sum()

ordem = df.sum(axis=1).groupby(level=0).apply(peso).sort_values(0, ascending=False).index.values

df = df.sum(axis=1)

df = df.reindex(ordem, level=0)

print(df)

df = df.reset_index()
sns.barplot(data=df, x=0, y="Album", hue = "Record", palette={"Prata":"silver", "Ouro":"gold", "Platina":"lightsteelblue"})

ax.set(xlabel="Albuns mais premiados")

plt.savefig('../../Plots/MaisPremiados.png', bbox_inches="tight")