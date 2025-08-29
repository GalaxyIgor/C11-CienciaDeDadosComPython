# Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo este dataset
# Bibliotecas
import numpy as np
ds = np.loadtxt('paises.csv',
                delimiter=";",
                dtype=str,
                encoding='utf-8')

# contando
print("Total: ",len(np.unique(ds[:, 1:2])))
print("Regioes: ",ds[:, 1:2])