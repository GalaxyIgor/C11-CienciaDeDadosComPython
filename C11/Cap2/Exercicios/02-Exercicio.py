# Entrada
numero = int(input("Digite um número para ver sua tabuada: "))
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

# Saida - Como no enunciado não menciona uma operação especifica fiz com multiplicação
print(f"\nTabuada do {numero} iniciando em {inicio} e terminando no {fim}:")
for i in range(inicio, fim + 1):
    print(f"{numero} x {i} = {numero * i}")