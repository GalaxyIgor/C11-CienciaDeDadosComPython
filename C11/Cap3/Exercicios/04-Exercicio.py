# Inicializando listas para armazenar nomes e pesos
nomes = []
pesos = []

# Lendo os dados das 3 pessoas
for i in range(3):
    # Lendo dados
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    peso = float(input(f"Digite o peso de {nome} (em kg): "))
    # ADD dados
    nomes.append(nome)
    pesos.append(peso)

# Encontrando o índice da pessoa mais pesada
indice_mais_pesado = pesos.index(max(pesos))
# Encontrando o índice da pessoa mais leve
indice_mais_leve = pesos.index(min(pesos))

# Exibindo os resultados
print(f"\nA pessoa mais pesada é {nomes[indice_mais_pesado]} com {pesos[indice_mais_pesado]} kg")
print(f"A pessoa mais leve é {nomes[indice_mais_leve]} com {pesos[indice_mais_leve]} kg")