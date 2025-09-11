# Importando o Pandas
import pandas as pd

# o pandas tem s coleções Series (1D) e DataFrame(2D)

# Criando uma "series"
indices = ["a", "b", "c"]
valores = [1, 2, 3]

# Dicionario é parecido com Series
dic1 = {"a": 10, "b": 20, "c": 30}
dic2 = {"a": 10, "b": 20, "d": 40}

#series = pd.Series(index=indices, data=valores) # Jeito normal de alimentar uma Series
series1 = pd.Series(dic1) # Vc pode alimentar uma Series com Dicionario
series2 = pd.Series(dic2)

print("Printando uma Series: \n", series1)
print("Tipo da Series: ", type(series1)) # Mostrando o Tipo

print("\n")

# Buscando Valor
print("Valor a: ", series1['a'])
print("Valor b: ", series1['b'])
print("Valor c: ", series1['c'])

print("\n")

# Operações entre Series, quando ele acha o index ele executa a operação caso não mostra NaN a=a b=b c!=d
print("Somando: \n", series1 + series2)
print("Subtraindo: \n", series1 - series2)

print("\n")

# Caso queira forçar essa soma usar funções pre-prontas do pandas
print("Somando: \n",series1.add(series2, fill_value=0))
print("Subtraindo: \n",series1.sub(series2, fill_value=0))

print("\n")
print("Mascara:\n", series1 <= 20) # mask
print("Aplicando a mascara:\n", series1[series1 <= 20])