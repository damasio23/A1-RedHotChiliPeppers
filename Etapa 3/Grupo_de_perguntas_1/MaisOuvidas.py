import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])
df.sort_values("Ouvintes", inplace=True, ascending=False)
df = df.head(50)

sns.set_theme(style="whitegrid")

f, ax = plt.subplots(figsize=(6, 15))

sns.set_color_codes("pastel")
sns.barplot(data=df["Ouvintes"], y=df.index.get_level_values(1), x=df["Ouvintes"], color="b", label="Ouvintes")

ax.legend( loc="lower right", frameon=True)
ax.set(xlim=(0, 2000000),ylabel="", xlabel="Os 50 titulos mais ouvidos")

plt.savefig('../../Plots/MaisOuvidas.png', bbox_inches="tight")
