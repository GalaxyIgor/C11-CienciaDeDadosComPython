import numpy as np

# Criar matriz de tamanho qualquer, Ex: 3x5
matriz = np.random.randint(1, 100, (3, 5)) # Matriz 3x5 com valores inteiros aleatórios entre 1 e 99

# Número de linhas, colunas
linhas, colunas = matriz.shape # Shape retorna uma tupla (linhas, colunas)

# Calcula o número total de elementos multiplicando linhas por colunas
num_elementos = linhas * colunas

# Verifica se o número total de elementos é par ou ímpar usando operador ternário
par_ou_impar = "par" if num_elementos % 2 == 0 else "ímpar"

# Exibindo resultados
print("Matriz:")
print(matriz)
print(f"Número de linhas: {linhas}")
print(f"Número de colunas: {colunas}")
print(f"Número total de elementos: {num_elementos}")
print(f"Poderia se tornar um vetor unidimensional com número {par_ou_impar} de elementos\n")