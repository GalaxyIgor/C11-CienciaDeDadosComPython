import numpy as np
# Importando Dataset
ds = np.loadtxt('space.csv',
                delimiter=";",
                dtype=str,
                encoding='utf-8')

# 2. Qual a média de gastos de uma missão especial se baseando em missões que possuam valores disponíveis (> 0)?
ds_gastos = ds[1:, 6].astype(float)
ds_gastosValidos = ds_gastos[ds_gastos > 0]
ds_media = np.mean(ds_gastosValidos)

print("\nMédia de gastos valores disponíveis (> 0): ")
print(ds_media)

