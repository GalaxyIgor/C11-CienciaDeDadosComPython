import pandas as pd
ds = pd.read_csv("paises.csv", sep=";")

# 5. Faça uma função que receba a taxa de mortalidade de cada país (Deathrate) e
# retorne o texto ‘Balanced’ caso o valor seja < 9 e ‘Urgent’ caso contrário. Em
# seguida, crie um campo no Dataset chamado ‘Humanitarian Help’ que receba estes
# valores para cada país. No final, mostre o Dataset para verificar se a inserção da nova
# coluna foi feita com sucesso.
def avaliar_ajuda(deathrate):
    return "Balanced" if deathrate < 9 else "Urgent"

ds["Humanitarian Help"] = ds["Deathrate"].apply(avaliar_ajuda)
print("\nDataset com coluna 'Humanitarian Help':")
print(ds.head())