# Entrada
# Lendo Nome Completo
nome_completo = input("Digite seu nome completo: ")

# Saida
# Nome em maiúsculas
print("Nome com todas as letras maiúsculas:", nome_completo.upper())

# Nome em minúsculas
print("Nome com todas as letras minúsculas:", nome_completo.lower())

# Quantidade de letras (sem espaços)
quantidade_letras = len(nome_completo.replace(" ", "")) # troca o espaço para sem espaço
print("Quantidade de letras sem espaços:", quantidade_letras)

# Trocar último nome por "do Inatel"
partes = nome_completo.strip().split()
if len(partes) > 1:
    partes[-1] = "do Inatel"
    nome_trocado = " ".join(partes)
else:
    nome_trocado = nome_completo + " do Inatel"
print("Nome com último nome trocado por 'do Inatel':", nome_trocado)