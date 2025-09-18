# Importando bibliotecas para manipulação de dados
import pandas as pd  # Biblioteca principal para análise de dados
import numpy as np   # Biblioteca para operações numéricas

# Importando dataset de um arquivo CSV
# O parâmetro delimiter=";" indica que o separador é ponto e vírgula
ds = pd.read_csv("paises.csv", delimiter=";")

# Exibindo o dataset completo
print("\nDataSet: \n", ds)

# Exibindo os nomes das colunas do dataset
print("\nColunas:\n", ds.columns)

# Mostrando as 2 primeiras linhas do dataset
print("\nLinhas do Topo:\n", ds.head(2))

# Mostrando as 2 últimas linhas do dataset
print("\nLinhas do Fundo:\n", ds.tail(2))

# Calculando a soma total da população usando numpy
somaPopulacao = np.sum(ds["Population"])

# Alternativa comentada: primeiro armazena a coluna, depois soma
# colunaPopulacao = ds["Population"]
# somaPopulacao = np.sum(colunaPopulacao)

# Mostrando a soma total das populações (typo: "doma" deveria ser "soma")
print("\nSoma das Populações:\n", somaPopulacao)

# Calculando a porcentagem que cada população representa do total
populacaoPorcentagem = ds["Population"]/somaPopulacao
print("\nPorcentagem da população:\n", populacaoPorcentagem)

# Adicionando uma nova coluna ao dataset com as porcentagens calculadas
ds["PopulationPercent"] = populacaoPorcentagem

# Mostrando a nova coluna de porcentagens
print("\nColuna de Porcentagem:\n", ds["PopulationPercent"])

# Salvando o dataset modificado em um novo arquivo CSV com separador ponto e vírgula
ds.to_csv("paises2.csv", sep=";")

# Agrupando os dados pela coluna "Region" - cria um objeto GroupBy
group_region = ds.groupby("Region")
print("\nDataframe agrupado:\n", group_region)  # Isso mostra apenas a referência do objeto

# Mostrando a contagem de registros por região (agora sim mostra os dados)
print("\nMostrando agrupamento do jeito certo:\n", group_region.count())

# Mostrando apenas a contagem de países por região (coluna "Country")
print("\nMostrando agrupamento de country do jeito certo:\n", group_region.count()["Country"])

print("\nMostrando agrupamento de country + somatoria:\n", group_region.sum()["Country"])

print("\nMostrando agrupamento de country + somatoria:\n", group_region.sum()["Population"])

#Funcoes Customizadas no Pandas
# Funcao cque da desconto de 10%
def tenpercent(x):
    return x * 0.9

print("Função de desconto:", tenpercent(10))

# pegando taxa de mortalidade
taxaMort = ds["Deathrate"]

# criando uma serie descota 10% de taxa de mortalidade
taxaMor2 = taxaMort.apply(tenpercent)
print(taxaMort)

print(taxaMor2)

df2 = pd.concat([taxaMort, taxaMor2], axis=1)
df2.columns = ["Taxa de Mortalidade","Taxa de Mortalidade com Desconto"]
print(df2)