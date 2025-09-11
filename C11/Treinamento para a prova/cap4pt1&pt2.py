import numpy as np

# Exercicio 01
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


# Exercicio 02
arr1 = np.arange(0, 51, 2)
arr2 = np.arange(100, 50, -2)

concatene = np.concatenate((arr1, arr2))

print("Array:", np.sort(concatene))

# Exercicio 03
import numpy as np

# a) Criando matriz 2x2 de zeros
matriz = np.zeros((2, 2), dtype=int)

# Matriz de Exibição
matrizEx = np.zeros((2, 2), dtype=object) #

# b) Adicionando 1 em posição aleatória
linha = np.random.randint(0, 2)
coluna = np.random.randint(0, 2)
matriz[linha, coluna] = 1

print("Bem-vindo ao Mini Campo Minado!")
print("Tente encontrar todas as posições sem a mina (1).")

# Inicializando variáveis
jogadas = 0
achou_mina = False

# Pq 3 jogadas? pois o jogo é simples e rápido com 3 tentativas vc ganha o jogo
while jogadas < 3:
    # c) Entrada de dados do usuário
    print("\nMatriz atual:")
    print(matrizEx)
    print("Obs: * Marca a posição como jogada, caso tenha acertado.")

    # Trycatch para evitar erros de entrada, Ex: colocar letras ao invés de números
    try:
        linha = int(input("\nDigite a linha (0 ou 1): "))
        coluna = int(input("Digite a coluna (0 ou 1): "))

        # Verificando se a entrada é válida
        if linha not in [0, 1] or coluna not in [0, 1]:
            print("Posição inválida! Use apenas 0 ou 1.")
            continue

        # Verificando se encontrou a mina
        if matriz[linha, coluna] == 1:
            achou_mina = True
            break
        else:
            print("Posição segura!")
            jogadas += 1 # Incrementando jogadas para cada tentativa correta
            matrizEx[linha, coluna] = '*'  # Marcar posição como jogada

    except ValueError:
        print("Entrada inválida! Use números inteiros.")

# Verificando resultado
if achou_mina: # se achou_mina for true
    print("\nGame Over! :( Try Again!")
else:
    print("\nCongratulations! You beat the game! :)")







# Exercicio 04


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






# Exercicio 05

# Definir seed
np.random.seed(10)

# Criar matriz 4x4 com números aleatórios entre 1 e 50
matriz = np.random.randint(1, 51, (4, 4))

# Média de cada linha e coluna
media_linhas = matriz.mean(axis=1)
media_colunas = matriz.mean(axis=0)

# Maior valor das médias das linhas e das colunas
maior_media_linha = media_linhas.max()
maior_media_coluna = media_colunas.max()

# Quantidade de aparições de cada número na matriz
valores, contagens = np.unique(matriz, return_counts=True)
# Números que aparecem exatamente 2 vezes
numeros_2_vezes = valores[contagens == 2]

# Exibindo resultados
print("Matriz 4x4:")
print(matriz)

print("\nMédia de cada linha:")
print(media_linhas)
print("\nMédia de cada coluna:")
print(media_colunas)

print(f"\nMaior média das linhas: {maior_media_linha}")
print(f"Maior média das colunas: {maior_media_coluna}")

print("\nContagem de aparições de cada número:")
for v, c in zip(valores, contagens):
    print(f"Número {v}: {c} vez(es)")

print("\nNúmeros que aparecem exatamente 2 vezes:")
print(numeros_2_vezes)