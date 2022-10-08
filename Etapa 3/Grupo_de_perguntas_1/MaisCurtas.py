import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])
df.sort_values("Length", inplace=True)
df = df.head(50)

def seconds(time):
    try:
      time = time.split(":")
    except AttributeError:
      return "O tipo do argumento deve ser uma string"
    else:
        seconds = int(time[0])*60 + int(time[1])
        return seconds

df["Length"] = df["Length"].apply(seconds)

sns.set_theme(style="whitegrid")

f, ax = plt.subplots(figsize=(6, 15))

sns.set_color_codes("pastel")
sns.barplot(data=df["Length"], y=df.index.get_level_values(1), x=df["Length"], color="b", label="Duração", errorbar=None)

ax.legend( loc="upper right", frameon=True)
ax.set(xlim=(0, 210),ylabel="", xlabel="As 50 músicas mais curtas")

plt.savefig('../../Plots/MaisCurtas.png', bbox_inches="tight")