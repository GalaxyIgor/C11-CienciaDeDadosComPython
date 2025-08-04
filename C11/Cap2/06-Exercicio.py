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