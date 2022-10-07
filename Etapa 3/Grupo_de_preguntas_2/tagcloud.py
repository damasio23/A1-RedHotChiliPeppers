import numpy as np
import pandas as pd
import wordcloud as wc
import matplotlib.pyplot as plt
from PIL import Image
from pregunta1 import palavras_mais_comuns_titulos_musicas

df = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])

words = palavras_mais_comuns_titulos_musicas(df)

def color_function(word, font_size, position, orientation, random_state=None, **kwargs):
  origem = tuple(map(sum, zip(position, (-1200, -1200))))
  raio = np.linalg.norm(origem)
  if raio > 750:
    return "#ffffff"
  else:
    return "#ff0000"

mask = np.array(Image.open("mask.png"))

cloud = wc.WordCloud(background_color="#000000", mask=mask, contour_width=0.2, contour_color="#ffffff", color_func=color_function).fit_words(words)
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(cloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(cloud)
cloud.to_file("../../TagClouds/TitulosDasMusicas.png")