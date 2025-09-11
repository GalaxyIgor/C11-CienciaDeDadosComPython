pessoas = []
for i in range(3): # para 3 pessoas
    nome = input("Digite o nome da pessoa: ")
    peso = float(input("Digite o peso da pessoa: "))
    pessoas.append((nome,peso))
print("Pessoa Mais Pesada:", max(pessoas))
print("Pessa Mais Leve:", min(pessoas))