# Conte quantos países são da América do Norte (NORTHERN AMERICA) segundo este dataset;
# Bibliotecas
import numpy as np
# Importando Dataset
ds = np.loadtxt('paises.csv',
                delimiter=";",
                dtype=str,
                encoding='utf-8')

north_ds = np.sum(np.char.find(ds, 'NORTHERN AMERICA') != -1)
print(north_ds)