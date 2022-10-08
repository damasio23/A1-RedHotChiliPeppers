# A1-RedHotChiliPeppers
## Etapa 1
### DataFrames
Pasta com os dataframes gerados na etapa 1
### Etapa_1
- **length.py**: Pega a duração de cada musica e retorna o dataframe "albums_df_eng.csv"
- **letras.py**: Pega as letras de cada musica e retorna o dataframe "letras_final.csv"
- **popularidade_das_musicas.py**: Pega a popularidade das musicas e retorna o dataframe "tabela_geral_final.csv"
- **merge.py**: Junta a popularidade duração e letras de cada musica dentro do dataframe "new_df.xls"
- **premios.py**: Pega as informações sobre os premios recebidos por cada album e retorna o dataframe "premios.csv"

## Etapa 2
### Etapa_2
**Grupo de Perguntas 1**: Funções que respondem o grupo de perguntas 1 da etapa 2.
- 1. Músicas mais ouvidas e músicas menos ouvidas por Álbum
- 2. Músicas mais longas e músicas mais curtas por Álbum
- 3. Músicas mais ouvidas e músicas menos ouvidas [em toda a história da banda ou artista]
- 4. Músicas mais longas e músicas mais curtas [em toda a história da banda ou artista]
- 5. Álbuns mais premiados
- 6. Intervalo de tempo que contem as musicas mais populares

**Grupo de Perguntas 2**: Funções que respondem o grupo de perguntas 2 da etapa 2.
- 1. Palavras mais comuns nos títulos dos Álbuns
- 2. Palavras mais comuns nos títulos das músicas
- 3. Palavras mais comuns nas letras das músicas, por Álbum
- 4. Palavras mais comuns nas letras das músicas, em toda a discografia
- 5. O título de um álbum é tema recorrente nas letras
- 6. O título de uma música é tema recorrente nas letras?

**Grupo de Perguntas 3**: Funções que respondem o grupo de perguntas 3 da etapa 2.
- 1. Álbum com mais músicas e álbum com menos músicas
- 2. Álbum mais ouvido e álbum menos ouvido
- 3. Média da popularidade das músicas e o desvio padrão
### main.py
Testa as funções da etapa 2.

## Etapa 3
### Plots
Graficos gerados com seaborn para o grupo de perguntas 1 da etapa 2.
### TagClouds
Tag clouds gerados para o grupo de perguntas 2 da etapa 2
### Etapa_3
**Grupo_de_perguntas_1**: Visualizações para as respostas do Grupo de Perguntas 1
- **MaisCurtas/Longas.py**: Gera o barplot "MaisCurtas/Longas.png" com as 50 musicas mais curtas/longas
- **MaisCurtas/LongasAlbum.py**: Gera o barplot "MaisCurtas/LongasPorAlbum.png" com as musicas mais curtas/longas de cada album
- **Mais/MenosOuvidas.py**: Gera o barplot "Mais/MenosOuvidas.png" com as 50 musicas mais/menos ouvidas
- **Mais/MenosOuvidasAlbum.py**: Gera o barplot "Mais/MenosOuvidasPorAlbum.png" com as musicas mais/menos ouvidas de cada album
- **MaisPremiados.py**: Gera o barplot "MaisPremiados.png" com os albums mais premiados
- **Relação.py**: Gera o scatterplot "RelaçãoPopularidadeDuração.png" com a duração em segundos no eixo x e a popularidade no eixo y

**Grupo_de_perguntas_2**: Tag Clouds das respostas das perguntas 2, 3 e 4 do Grupo de Perguntas 2
- **tagcloud.py**: Gera o Tag Cloud "TitulosDasMusicas.png" com as palavras mais comuns nos titulos das musicas
- **tagcloud2.py**: Gera o Tag Cloud "LetrasPorAlbum.png" com as palavras mais comuns nas letras das musicas do album Californication
- **tagcloud3.py**: Gera o Tag Cloud "LetrasDasMusicas.png" com as palavras mais comuns nas letras das musicas em toda a discografia
