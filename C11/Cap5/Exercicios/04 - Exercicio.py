import pandas as pd

# Baseado nos resultados da Questão 3, mostre apenas os dados das linguagens que tiveram crescimento;
dic1 = {"Java": 16.25, "C": 16.04, "Python": 9.85}
dic2 = {"C": 16.21, "Python": 12.12, "Java": 11.68}

seriesAno1 = pd.Series(dic1)
seriesAno2 = pd.Series(dic2)

variacao = seriesAno2 - seriesAno1

variacao_positivo = variacao[variacao > 0]

print("Linguagem(s) que teve crescimento:\n", variacao_positivo)
