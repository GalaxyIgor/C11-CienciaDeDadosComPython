# Leitura de dados
nome = input("Nome do aluno: ")
media = float(input("Média do aluno: "))

# Calculo da situação
if media >= 50:
    situacao = "AP"
else:
    situacao = "RP"

# Criação do dicionário
aluno = {
    "Nome": nome,
    "Media": media,
    "situação":situacao
}

# Exibir conteúdo
print("Informações do Aluno: ", aluno)
