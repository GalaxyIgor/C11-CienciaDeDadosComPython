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