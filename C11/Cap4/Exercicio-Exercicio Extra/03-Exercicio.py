# Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo este dataset
# Bibliotecas
import numpy as np
ds = np.loadtxt('paises.csv',
                delimiter=";",
                dtype=str,
                encoding='utf-8')

ds_literacy = ds[1:,9].astype(float)
ds_mediaAlfa = np.mean(ds_literacy)

print("Taxa media de alfabetização: ",ds_mediaAlfa)