import numpy as np
# Importando Dataset
ds = np.loadtxt('space.csv',
                delimiter=";",
                dtype=str,
                encoding='utf-8')

# 3. Encontre quantas missões espaciais neste Dataset foram realizadas pelos Estados Unidos (USA)
ds_local = ds[1:, 2]
ds_USA = np.sum(np.char.find(ds_local, "USA") >= 0) # Conta quantos "EUA"

print("\nMissoes realizadas nos USA: ")
print(ds_USA)

