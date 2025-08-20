import numpy as np

# Criando arrays de números pares
array_pares1 = np.arange(0, 52, 2) # 0 até 51 (inclusive) com passo 2
array_pares2 = np.arange(100, 49, -2)  # 100 até 50 (inclusive) com passo -2

# Exibindo resultados
print("Array de números pares 1:", array_pares1)
print("\nArray de números pares 2:", array_pares2)

# Concatenando e ordenando
array_concatenado = np.concatenate((array_pares1, array_pares2))
array_ordenado = np.sort(array_concatenado)

# Exibindo resultados
print("\nArray concatenado:", array_concatenado)
print("\nArray ordenado:", array_ordenado)