import pandas as pd
import numpy as np

# 8. Faça um Slicing na matriz mostrando apenas as linhas A, C e E
# juntamente com as colunas X e Y. Em seguida, mostre qual seria a soma dos
# elementos de cada uma destas linhas e cada uma destas colunas.
# plantando uma semente aleatória

np.random.seed(10)

df = pd.DataFrame(
    index=["A", "B", "C", "D", "E"],
    columns=["W", "X", "Y", "Z"],
    data=np.random.randint(1, 50, [5, 4]
    ))


subset = df.loc[["A", "C", "E"], ["X", "Y"]]
print("Subconjunto:\n", subset)

soma_linhas = subset.sum(axis=1)
print("\nSoma de cada linha:\n", soma_linhas)

soma_colunas = subset.sum(axis=0)
print("\nSoma de cada coluna:\n", soma_colunas)