import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("new_df.xls", index_col=[0,1])
df.sort_values("Ouvintes", inplace=True)
df = df.head(50)
print(df["Ouvintes"])

sns.set_theme(style="whitegrid")

f, ax = plt.subplots(figsize=(6, 15))

sns.set_color_codes("pastel")
sns.barplot(data=df["Ouvintes"], y=df.index.get_level_values(1), x=df["Ouvintes"], color="b", label="Ouvintes")

ax.legend( loc="upper right", frameon=True)
ax.set(xlim=(0, 90000),ylabel="", xlabel="Os 50 titulos menos ouvidos")