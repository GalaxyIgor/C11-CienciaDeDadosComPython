import numpy as np

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