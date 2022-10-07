import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])
df.sort_values("Length", inplace=True, ascending=False)
df = df.head(50)

def seconds(time):
    time = time.split(":")
    seconds = int(time[0])*60 + int(time[1])
    return seconds

df["Length"] = df["Length"].apply(seconds)

print(df["Length"])

sns.set_theme(style="whitegrid")

f, ax = plt.subplots(figsize=(6, 15))

sns.set_color_codes("pastel")
sns.barplot(data=df["Length"], y=df.index.get_level_values(1), x=df["Length"], color="b", label="Duração")

ax.legend( loc="lower right", frameon=True)
ax.set(xlim=(0, 500),ylabel="", xlabel="As 50 músicas mais longas")

plt.savefig('../../Plots/MaisLongas.png', bbox_inches="tight")