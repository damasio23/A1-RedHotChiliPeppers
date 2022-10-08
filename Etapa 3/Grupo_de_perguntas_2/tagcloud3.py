import numpy as np
import pandas as pd
import wordcloud as wc
import matplotlib.pyplot as plt
from PIL import Image
from pregunta3 import palavras_mais_comuns_letras_discografia

df = pd.read_excel("../../DataFrames/new_df.xls", index_col=[0,1])

words = palavras_mais_comuns_letras_discografia(df)

mask = np.array(Image.open("mask3.png"))
cores = np.array(Image.open("cores2.png"))

image_colors = wc.ImageColorGenerator(cores)

cloud = wc.WordCloud(background_color="#ffffff", mask=mask, contour_width=0.2, contour_color="#000000", color_func=image_colors, max_font_size=200).fit_words(words)
fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(cloud, interpolation='bilinear')
ax.set_axis_off()
plt.imshow(cloud)

cloud.to_file("../../TagClouds/LetrasDasMusicas.png")