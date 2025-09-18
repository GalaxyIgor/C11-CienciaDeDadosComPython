import pandas as pd
ds = pd.read_csv("paises.csv", sep=";")

# 4. Busque o nome de todos os países do Dataset que não possuem costa marítima
# (Coastline (coast/area ratio) == 0) e guarde-os em um novo arquivo chamado noCoast.csv;
no_coast = ds[ds["Coastline (coast/area ratio)"] == 0]
no_coast.to_csv("noCoast.csv", sep=";", index=False)
print("\nArquivo noCoast.csv criado com os países sem costa.")