import numpy as np
# Importando Dataset
ds = np.loadtxt('space.csv',
                delimiter=";",
                dtype=str,
                encoding='utf-8')
# Exercicio 01
# 1. Apresente a porcentagem de missões que deram certo
ds_status = ds[1:, 7] # Apenas a coluna especifica Success/Failure
ds_total = len(ds_status) # Conta o Total de "Success"
ds_sucess = np.sum(np.char.find(ds_status, "Success") >= 0) # Conta quantos "Success"
ds_porcentagem= (ds_sucess/ds_total)*100 # Porcentagem de missões que deram certo

print("\nPorcentagem das Missoes: ")
print(ds_porcentagem) # Retorna porcentagem de missões que deram certo





# Exercicio 02

# 2. Qual a média de gastos de uma missão especial se baseando em missões que possuam valores disponíveis (> 0)?
ds_gastos = ds[1:, 6].astype(float)
ds_gastosValidos = ds_gastos[ds_gastos > 0]
ds_media = np.mean(ds_gastosValidos)

print("\nMédia de gastos valores disponíveis (> 0): ")
print(ds_media)








# Exercicio 03

# 3. Encontre quantas missões espaciais neste Dataset foram realizadas pelos Estados Unidos (USA)
ds_local = ds[1:, 2]
ds_USA = np.sum(np.char.find(ds_local, "USA") >= 0) # Conta quantos "EUA"

print("\nMissoes realizadas nos USA: ")
print(ds_USA)






# Exercicio 04
ds = np.loadtxt('space.csv',
                delimiter=";",
                dtype=str,
                encoding='utf-8')

spacexMask = ds[:,1] == 'SpaceX'
spacexMissoes = ds[spacexMask]

# Converter custo para float
custos = spacexMissoes[:,6].astype(float)

# Missão mais cara
custoMaxIndex = np.argmax(custos)
missaoMaisCara = spacexMissoes[custoMaxIndex]

print("\nMissão mais cara realizada pela SpaceX: ")
print(f"Mission: {missaoMaisCara[0]}")
print(f"Company: {missaoMaisCara[1]}")
print(f"Location: {missaoMaisCara[2]}")
print(f"Date: {missaoMaisCara[3]}")
print(f"Detail: {missaoMaisCara[4]}")
print(f"Status Rocket: ${missaoMaisCara[5]} million")
print(f"Cost: ${missaoMaisCara[6]} million")
print(f"Status Mission: {missaoMaisCara[7]}")








# Exercicio 05
# Importando Dataset
ds = np.loadtxt('space.csv',
                delimiter=";",
                dtype=str,
                encoding='utf-8')

# 5. Mostre o nome das empresas que já realizaram missões espaciais, juntamente com suas respectivas quantidades de missões (use o for no final para mostrar as informações)
# valores únicos e contagens
empresas, contagem = np.unique(ds[:,1], return_counts=True)

# Converter contagens para string
contagem_str = contagem.astype(str) # se n quiser colocar da erro

# Cria string com separador ": "
empresas_com_separador = np.char.add(empresas, ": ")

# Adiciona as contagens às strings
resultado_final = np.char.add(empresas_com_separador, contagem_str)

print("\nNome das empresas que já realizaram missões espaciais e quantidades de missões: ")

# Junta todas as linhas com quebra de linha
print('\n'.join(resultado_final))
