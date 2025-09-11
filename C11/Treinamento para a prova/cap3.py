# Exercicio 01
times = ['Liverpool', 'Barcelona', 'Arsenal', 'Internazionale', 'Atlético de Madrid']
print("Top 3:", times[:3])
print("Os ultimos 2 colocados: ", times[-2:])
print("Ordem alfabética:",sorted(times))
print("Posicao da Tabela:",times.index("Barcelona")+1)
print("\n")

# Exercicio 02
loja1 = {"iPhone 14", "Galaxy S23", "Xiaomi 13"}
loja2 = {"Xiaomi 13", "Galaxy S23", "Galaxy J7", "iPhone 12"}
print("\nModelos que são vendidos em cada loja")
print("Loja1:",loja1)
print("Loja2:",loja2)
print("Ao todo:",loja1.union(loja2))
print("Ao todo:",loja1|loja2)
print("Ambas vendem:",loja1.intersection(loja2))
print("Ambas vendem:",loja1&loja2)
print("\n")

# Exercicio 03
nome = input("Digite o nome do aluno: ")
media = float(input("Digite a media do aluno: "))

if media >= 50:
    status = "AP"
elif media < 50:
    status = "RP"
aluno = {
    "Nome": nome,
    "Media": media,
    "Status": status
}
print("Info do Aluno:", aluno)
print("\n")

# Exercicio 04
pessoas = []
for i in range(3): # para 3 pessoas
    nome = input("Digite o nome da pessoa: ")
    peso = float(input("Digite o peso da pessoa: "))
    pessoas.append((nome,peso))
    print("Pessoa Mais Pesada:", max(pessoas))
    print("Pessa Mais Leve:", min(pessoas))
print("\n")

# Exercicio 05
grupo = []

n = input("Digite a quantidade de pessoas: ")
for pessoas in range(int(n)):
    nome = input("Digite o nome da pessoa: ")
    idade = float(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa: ")
    grupo.append({"nome": nome, "idade": idade, "sexo": sexo})

media_idade = sum(pessoas["idade"] for pessoas in grupo) / int(n)
print("\nMedia de idades:",media_idade)

quantidade_F_20 = 0
for pessoa in grupo:
    if pessoa["idade"] < 20 and pessoa["sexo"] == "F":
        quantidade_F_20 += 1
print("Mulheres menores de 20 anos:", quantidade_F_20)