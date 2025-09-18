import pandas as pd
ds = pd.read_csv("paises.csv", sep=";")

# 2. Encontre o nome e a região do país que possui a maior população segundo este Dataset;
pais_maior_pop = ds.loc[ds["Population"].idxmax(), ["Country", "Region", "Population"]]
print("\nPaís com maior população:")
print(pais_maior_pop)