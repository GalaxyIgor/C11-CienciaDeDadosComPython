import numpy as np
from sympy.codegen import Print

# Criando um array de 1 a 9
mtz = np.arange(1, 10, 1)
print("\nMatriz (vetor original):\n", mtz)

# Reestruturando a matriz para 3x3
mtz = mtz.reshape(3, 3)  # agora mtz é uma matriz 3x3
print("\nMatriz Reestruturada (3x3):\n", mtz)

# Extraindo apenas uma linha (terceira linha)
print("\nTerceira linha:")

print(mtz[2])
# Extraindo apenas uma coluna (segunda coluna)
print("\nSegunda coluna:")
print(mtz[:, 1])

# Extraindo apenas uma coluna (segunda e terceira colunas)
print("\nSegunda coluna e terceira colunas:")
print(mtz[:, 1:])

# Condicionais
# Evita o uso de ifs
print("\nValores Maiores 5 (true/false):")
print(mtz>5)

print("\nValores Maiores (apenas os numeros):")
print(mtz[mtz>5])

print("\nNúmeros Pares (apenas os numeros):")
print(mtz[mtz%2==0])

# Tratamento textual (subpacote char)
# Criando um array do NumPy com strings (nomes dos personagens)
arr = np.array(['Goku', 'Goten', 'Gohan', 'Trunks', 'Bulma'])

# Mostra todo o array
print("\nArray: ")
print( arr)

# np.char.find percorre cada string do array e procura o índice (posição)
# onde aparece a substring "ha".
# - Se encontrar, retorna a posição (índice baseado em 0).
# - Se não encontrar, retorna -1.
print("\nArray com HA usando retorno de 2 e -1: ")
print(np.char.find(arr,"ha"))

print("\nArray com HA usando true/false: ")
print(np.char.find(arr,"ha")>=0)

print("\nArray com HA: ")
print(arr[np.char.find(arr,"ha")>=0])

# Importando datasets
ds = np.loadtxt(r"C:/Users/igorn/OneDrive/Galaxy Codes Git Hub/C11/C11-CienciaDeDadosComPython/C11/Cap4/assets/space.csv",
                delimiter=";",
                dtype=str,
                encoding='utf-8')

# print(ds)
# Colunas do dataset
print(ds[0, :])

# Calculando a média de uma missao espacial
# Slicing para extrair a coluna custo (cost)
ds_cost = ds[1:, 6]
print("\nMedia das Missoes (String): ")
print(ds_cost)

# Transdormando em float
print("\nMedia das Missoes (Float): ")
ds_cost = ds_cost.astype(float)
print(ds_cost)

# Media
print("\nMedia das Missoes: ")
print(ds_cost.mean()) # mean faz a media
