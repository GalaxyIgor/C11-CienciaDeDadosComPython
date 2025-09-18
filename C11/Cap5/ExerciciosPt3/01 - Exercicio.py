import pandas as pd
ds = pd.read_csv("paises.csv", sep=";")

# 1. Carregue o Dataset paises.csv e em seguida mostre:
# a.Quais são os países da OCEANIA;
# b.Quantos países são da OCEANIA;
# Dica: para busca de padrões textuais no Pandas, use métodos da subclasse str da
# Series. Ex: series.str.contains(‘texto’)

# a)
oceania_paises = ds[ds["Region"].str.contains("OCEANIA")]
print("Países da OCEANIA:")
print(oceania_paises["Country"])


# b)
qtd_oceania = oceania_paises.shape[0]
print("\nQuantidade de países na OCEANIA:", qtd_oceania)