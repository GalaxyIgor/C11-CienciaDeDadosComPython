# Entrada
distancia = float(input("Digite a distância da viagem em Km: "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

# Saida
print(f"O preço da passagem é: R${preco:.2f}")