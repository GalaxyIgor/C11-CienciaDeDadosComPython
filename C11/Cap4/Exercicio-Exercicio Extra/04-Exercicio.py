# Conte quantos países são da América do Norte (NORTHERN AMERICA) segundo este dataset;
# Bibliotecas
import numpy as np
# Importando Dataset
ds = np.loadtxt('paises.csv',
                delimiter=";",
                dtype=str,
                encoding='utf-8')

rendas = ds[0:,9]
region = ds[0:,1]
america_index = np.where(region == 'LATIN AMER. & CARIB    ')
rendas_america = rendas[america_index]
local = ds[0:,0]
contry = local[america_index]
maiorRenda = np.argmax(rendas_america)
print(contry[maiorRenda])do Norte: {NAMask}")