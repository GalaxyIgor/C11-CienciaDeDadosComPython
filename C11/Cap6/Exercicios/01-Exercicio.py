# 1. Por meio do dataset paises.csv, trace dois gráficos de linhas em um mesmo plano cartesiano, um mostrando a taxa de mortalidade
# (Deathrate) e outro a taxa de natalidade (Birthrate) dos países da América do Norte;

import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
ds = pd.read_csv("paises.csv", sep=";")

# Remover espaços extras nas strings
ds["Region"] = ds["Region"].str.strip()

# Filtrar América do Norte
norte_america = ds[ds["Region"] == "NORTHERN AMERICA"]

# Criando o grafico
plt.figure(figsize=(12,6))

plt.plot(norte_america["Country"], norte_america["Birthrate"], color="blue", marker="o", label="Taxa de Natalidade")
plt.plot(norte_america["Country"], norte_america["Deathrate"], color="red", marker="s", label="Taxa de Mortalidade")

plt.xlabel("Países da América do Norte")
plt.ylabel("Taxa (%)")
plt.title("Taxa de Natalidade vs Taxa de Mortalidade - América do Norte")

plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

plt.show()