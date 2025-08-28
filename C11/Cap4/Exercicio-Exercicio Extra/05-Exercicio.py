import numpy as np

# Carregar dataset
ds = np.loadtxt("paises.csv",
                delimiter=";",
                dtype=str,
                encoding="utf-8")

# Máscara para LATIN AMER. & CARIB
regiao_latam = np.where(ds[:, 1] == "LATIN AMER. & CARIB")

# Extrair renda per capita (coluna 8)
renda = ds[:, 8]
renda = np.where(renda == "unknown", "nan", renda).astype(float)

# Selecionar apenas os valores da região
renda_latam = renda[regiao_latam]

# Encontrar índice do maior
idx = np.nanargmax(renda_latam)

# Extrair países
pais = ds[:, 0][regiao_latam][idx]

print(f"País: {pais} (GDP per capita: {renda_latam[idx]})")
