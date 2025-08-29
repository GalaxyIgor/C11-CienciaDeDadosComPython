# Faça um slicing no dataset para mostrar apenas o País (Country), Região (Region), População (Population) e Area (Area (sq. mi.)) dos países contidos nele
# Bibliotecas
import numpy as np
ds = np.loadtxt('paises.csv',
                delimiter=";",
                dtype=str,
                encoding='utf-8')
# Fazendo slicing direto
print(ds[:, 0:6])