nomes = []
idades = []
sexos = []

n = int(input("Quantas pessoas você deseja cadastrar? "))

for i in range(n):
    print(f"\nDados da {i+1}ª pessoa:")
    nomes.append(input("Nome: "))
    idades.append(int(input("Idade: ")))
    sexos.append(input("Sexo (M/F): ").upper())

# Calculando média
media_idade = sum(idades) / n # sum() serve para soma

# Contando mulheres com menos de 20 anos
mulheres_menos_20 = sum(1 for sexo, idade in zip(sexos, idades) # zip(sexos, idades) serve para unir 2 listas em pares ordedados ex:('F', 18)
                        if sexo == 'F' and idade < 20) # Basicamente vamos somar 1 para cada Femino menor de 20 anos

print("\nResultados:")
print(f"A média de idade do grupo é {media_idade:.1f} anos")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")