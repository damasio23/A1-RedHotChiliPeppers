import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def seconds(time):
    time = time.split(":")
    seconds = int(time[0])*60 + int(time[1])
    return seconds

df = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])

sns.set_theme(style="whitegrid")

f, ax = plt.subplots(figsize=(7, 7))

df["Length"] = df["Length"].apply(seconds)

sns.set_color_codes("pastel")
sns.scatterplot(data=df,y=df["Ouvintes"], x=df["Length"])

ax.set(xlabel="Duração", ylabel="Popularidade")

plt.savefig('../../Plots/RelaçãoPopularidadeDuração.png', bbox_inches="tight")