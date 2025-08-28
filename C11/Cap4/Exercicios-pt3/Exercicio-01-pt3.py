import numpy as np
# Importando Dataset
ds = np.loadtxt('space.csv',
                delimiter=";",
                dtype=str,
                encoding='utf-8')

# 1. Apresente a porcentagem de missões que deram certo
ds_status = ds[1:, 7] # Apenas a coluna especifica Success/Failure
ds_total = len(ds_status) # Conta o Total de "Success"
ds_sucess = np.sum(np.char.find(ds_status, "Success") >= 0) # Conta quantos "Success"
ds_porcentagem= (ds_sucess/ds_total)*100 # Porcentagem de missões que deram certo

print("\nPorcentagem das Missoes: ")
print(ds_porcentagem) # Retorna porcentagem de missões que deram certo