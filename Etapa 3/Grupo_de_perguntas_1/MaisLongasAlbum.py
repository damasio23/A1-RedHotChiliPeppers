import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])
df = pd.DataFrame(df.groupby(level=0).apply(lambda x: x[x["Length"] == x["Length"].max()])).reset_index(drop=True, level=0)
df = df.reset_index()
df = df.sort_values("Length", ascending = False)

def seconds(time):
    time = time.split(":")
    seconds = int(time[0])*60 + int(time[1])
    return seconds

df["Length"] = df["Length"].apply(seconds)

print(df["Length"])

sns.set_theme(style="whitegrid")

f, ax = plt.subplots(figsize=(6, 15))

sns.set_color_codes("pastel")
sns.barplot(data=df["Length"], y=df["Album"]+":\n"+df["Title"], x=df["Length"], color="b", label="Duração")

ax.legend( loc="lower right", frameon=True)
ax.set(xlim=(0, 500),ylabel="", xlabel="As 50 músicas mais longas")

plt.savefig('../../Plots/MaisLongasPorAlbum.png', bbox_inches="tight")