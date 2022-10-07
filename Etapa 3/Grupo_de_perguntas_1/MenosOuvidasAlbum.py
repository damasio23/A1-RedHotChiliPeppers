import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("new_df.xls", index_col=[0,1])
df = pd.DataFrame(df.groupby(level=0).apply(lambda x: x[x["Ouvintes"] == x["Ouvintes"].min()])).reset_index(drop=True, level=0)
df = df.reset_index()
df = df.sort_values("Ouvintes")

sns.set_theme(style="whitegrid")

f, ax = plt.subplots(figsize=(6, 15))

sns.set_color_codes("pastel")
sns.barplot(data=df["Ouvintes"],y=df["Album"] + ":\n" + df["Title"], x=df["Ouvintes"], color="b", label = "Ouvintes")

ax.legend( loc="upper right", frameon=True)
ax.set(xlim=(0, 450000),ylabel="", xlabel="Musicas menos ouvidas de cada album")