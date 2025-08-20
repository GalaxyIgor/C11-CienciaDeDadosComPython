# Bibliotecas
import numpy as np

# Criando os arrays
arr_1 = np.ones(8) # Array de 1's
arr_Aleatorio = np.random.randint(0, 10, 8) # Aleatorio

# Somando arrays
arr_soma = arr_1 + arr_Aleatorio

# Verificando a soma total
soma = np.sum(arr_soma) 

# Remodelando conforme a condição
if soma >= 40:
    # Mais linhas que colunas (4x2)
    arr_Remodelando = arr_soma.reshape(4, 2)
else:
    # Mais colunas que linhas (2x4)
    arr_Remodelando = arr_soma.reshape(2, 4)

print("Array de 1's:", arr_1)
print("Array aleatório:", arr_Aleatorio)
print("Array resultante da soma:", arr_soma)
print("Soma total dos elementos:", soma)
print("Array remodelado:\n", arr_Remodelando)