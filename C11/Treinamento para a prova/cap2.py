# Exercicio 01
print("\nExercio 01")
nome_completo = input("Nome completo: ")
print("Nome com letra maiúsculas",nome_completo.upper())
print("Nome com letra minúsculas",nome_completo.lower())
print("Ao todo tem",len(nome_completo), "letras")
print( "se trocássemos seu último nome para “do Inatel” ficaria",)

quantidade_letras = len(nome_completo.replace(" ", "")) # troca o espaço para sem espaço
print("Quantidade de letras sem espaços:", quantidade_letras)
partes = nome_completo.strip().split()
if len(partes) > 1:
    partes[-1] = "do Inatel"
    nome_trocado = " ".join(partes)
else:
    nome_trocado = nome_completo + " do Inatel"
print("Nome com último nome trocado por 'do Inatel':", nome_trocado)

# Exercicio 02
print("\nExercio 02")
numero_escolhido = int(input("Escolha um numero para fazer a tabuada: "))
comeco_escolhido = int(input("Escolha o inicio: "))
termino_escolhido = int(input("Escolha o fim: "))

print(f"\nTabuada de soma do {numero_escolhido}:")
for i in range(comeco_escolhido, termino_escolhido + 1):
    print(f"{numero_escolhido} + {i} = {numero_escolhido + i}")



# Exercicio 03
print("\nExercio 03")
sexo = input("Digite seu sexo (M/F): ").upper()

while True:
    if sexo == 'M':
        print("Você é homem")
        break
    elif sexo == 'F':
        print("Você é mulher")
        break
    else:
        print("Opção inválida! Digite M ou F.")
        sexo = input("Digite seu sexo (M/F): ").upper()


# Exercicio 04
print("\nExercio 04")
# Entrada
distancia = float(input("Digite a distância da viagem em Km: "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

# Saida
print("valor:",preco)



# Exercicio 05
print("\nExercio 05")
import math

numero = float(input("Digite um número decimal: "))

raiz_quadrada = math.sqrt(numero)
funcao_teto = math.ceil(numero)
funcao_chao = math.floor(numero)
parte_inteira = int(numero)

print(f"Raiz quadrada: {raiz_quadrada:.2f}")
print(f"Função teto: {funcao_teto}")
print(f"Função chão: {funcao_chao}")
print(f"Parte inteira: {parte_inteira}")




