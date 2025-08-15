# Importando Bibliotecas
import numpy as np # as é como se dasse um apelido a biblioteca no caso np

# Criando um Array
arr = np.array([10,20,30])
print("Array: ", arr) # mostrando o array
print("Tipo: ", type(arr)) # mostrando o tipo

# Array com vários tipos
arrTeste = np.array([10,20,"teste"]) # Funciona com vários tipos diferentes, mas para performace é ruim
print("Array teste: ", arrTeste) # mostrando o array, para performace ele auto corrige o tipo de todos

# Array com 2 dimensões
mtz = np.array([[10, 20, 30],[40, 50, 60]])
print("Mtz: ", mtz)

# Funções para estruturar NumPy Arrays
# Array 1D de 1s
arr = np.ones(10)
print("Array com 1: ", arr)

# Array 2D e de 0s
mtz = np.zeros(10)
print("Array com 0: ", mtz)

# Para mudar o sentido, por exemplo, colocar em pé usamos o replace
print("Sem Reshape: ", mtz)
mtz.reshape(5,2)
print("Usando Reshape: ", mtz)

# Criando Array Rapido
# Arange, serve para escrever de forma rapida um array
arr = np.arange(10, 101, 10) # comece do 10, até 101
# (101 não está incluso, segundo argumento é excludivo, 100 esta incluso), de 10 em 10
print("Usando Arange: ", arr)

# Funções Essenciais do NumPy
# Menor Valor
print("Minimo: ", arr.min())
# Maior Valor
print("Maximo: ", arr.max())
# Media
print("Media: ", arr.mean())
# Indice de onde está o maior valor
print("Indice do maior Elemento: ", arr.argmax())

# Operações com NumPy Array
arr1 = np.arange(1, 10, 1) # Criando um array crescente
arr2 = np.arange(9, 0, -1) # Criando um array decrescente
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Array 1 + Array 2: ", arr1 + arr2) # pode usar qualquer operandor em operações elemento a elemento

# Para Concatenar NumPy Arrays
print("Concatenando Array1 com Array2", np.concatenate((arr1, arr2))) # juntando array1 e array2

# Criando uma Matriz 2D jan, fev, mar x Água, Luz, Net
# Operações com matrizes
mtz = np.array([[50, 10, 100, 60, 25, 100, 75, 80, 100]]).reshape(3,3)
print("Matriz: ", mtz)
print("Somando Colunas: ", mtz.sum(axis=0))
print("Somando Linhas: ", mtz.sum(axis=1))
print("Somando da primeira Coluna : ", mtz.sum(axis=0)[0])
print("Somando da terceira Linha : ", mtz.sum(axis=1)[2])

# Broadcasting, basicamente transmitindo operações para os elementos
print("Matriz dividida (espalhando operação): ", mtz/10)

# Números Aleatórios
arr = np.random.randint(1, 101, 10) # Do 1 < x < 101, 10 números totais
print("Números Aleatórios: ", arr)

# Números Aleatórios e Únicos, unique consegue retornar apenas elementos unicos sem repetições e de forma crescente
print("Números Aleatórios Únicos: ", np.unique(arr))

# Números Aleatórios e Únicos, unique consegue retornar apenas elementos unicos sem repetições e de forma crescente
# E quantas vezes eles aparecem
print("Números Aleatórios Únicos E Quantas Vezes Aparece: ", np.unique(arr, return_counts=True))

# Números Aleatórios e Únicos, unique consegue retornar apenas elementos unicos sem repetições e de forma crescente
# E quantas vezes eles aparecem
print("Números Aleatórios Únicos E Quantas Vezes Aparece: ", np.unique(arr, return_counts=True))