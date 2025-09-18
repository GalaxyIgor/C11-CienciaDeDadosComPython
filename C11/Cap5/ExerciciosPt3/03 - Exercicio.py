import pandas as pd
ds = pd.read_csv("paises.csv", sep=";")

# 3. Agrupe os países por Regiões. Em seguida, mostre a média de alfabetização (Literacy (%)) de cada região do planeta
media_alfabetizacao = ds.groupby("Region")["Literacy (%)"].mean()
print("\nMédia de alfabetização por região:")
print(media_alfabetizacao)