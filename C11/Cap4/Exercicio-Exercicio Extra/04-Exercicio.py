# Conte quantos países são da América do Norte (NORTHERN AMERICA) segundo este dataset;
# Bibliotecas
import numpy as np
# Importando Dataset
ds = np.loadtxt('paises.csv',
                delimiter=";",
                dtype=str,
                encoding='utf-8')

# Cria máscara para "NORTHERN AMERICA"
NAMask = ds[:, 1] == "NORTHERN AMERICA"

# Seleciona países
NA = ds[NAMask]

# Conta quantos são
qtd = NA.shape[0]

print(f"Quantidade de países na América do Norte: {qtd}")