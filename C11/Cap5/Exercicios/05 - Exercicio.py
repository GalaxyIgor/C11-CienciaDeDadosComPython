import pandas as pd

# Se estas porcentagens de crescimento/declínio se mantivessem iguais
# para os próximos 2 anos, qual seria a linguagem mais popular?
# Dica: use o método nlargest(1) no final para retornar rapidamente a label
# e maior valor de uma Series.
dic1 = {"Java": 16.25, "C": 16.04, "Python": 9.85}
dic2 = {"C": 16.21, "Python": 12.12, "Java": 11.68}

seriesAno1 = pd.Series(dic1)
seriesAno2 = pd.Series(dic2)

variacao = seriesAno2 - seriesAno1

projecao_ano3 = seriesAno2 + variacao
projecao_ano4 = projecao_ano3 + variacao

print("Projeção Ano 3:\n", projecao_ano3)

print("\nProjeção Ano 4:\n", projecao_ano4)


# Descobrindo a mais popular no Ano 4
mais_popular = projecao_ano4.nlargest(1)
print("\nLinguagem mais popular no Ano 4:\n", mais_popular)