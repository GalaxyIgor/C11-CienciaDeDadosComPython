# Entrada
numero = int(input("Digite um número entre 1000 e 9999: "))

if 1000 <= numero <= 9999:

    unidade = numero % 10
    dezena = (numero // 10) % 10
    centena = (numero // 100) % 10
    milhar = numero // 1000

    print(f"Unidade: {unidade}")
    print(f"Dezena: {dezena}")
    print(f"Centena: {centena}")
    print(f"Milhar: {milhar}")
else:
    print("Número fora do intervalo válido.")