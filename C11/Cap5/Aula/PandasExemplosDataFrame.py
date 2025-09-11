import pandas as pd
import numpy as np
# Pandas é muito compativel com tabelas como Excel
# Vc tem indices nas linhas e nas colunas
# Um dataframe é um aglomerado de seeries cada uma é uma coluna
print("\n")

# Colocando uma seed para padronizar os resultados aleatorios
np.random.seed(10)

# Criando um DataFrame
df = pd.DataFrame(
    index=["A", "B", "C", "D", "E"],
    columns=["W", "X", "Y", "Z"],
    data=np.random.randint(1, 50, [5,4])
)

print("Tabela com Números Aleatórios: \n", df) # Fica Bonito

print("\n")

# Fazendo um Slicing com iLoc (padrão Numpy - índices numéricos)
print("Fazendo um Slicing 2 primeiras linhas com iLoc: \n", df.iloc[0:2,:])

# Fazendo o mesmo Slicing com Loc, com ele mostro so o que quero
print("Fazendo o mesmo Slicing com Loc: \n", df.loc[['A', 'B'], ["W", "X", "Y", "Z"]])
