import pandas as pd

# 2. Os valores das Series criadas na Questão 1 representam as fatias de
# mercado (porcentagem) de 3 linguagens de programação populares em
# dois anos consecutivos. Para cada ano, apresente a porcentagem total que
# elas juntas representam no mercado;

dic1 = {"Java": 16.25, "C": 16.04, "Python": 9.85}
dic2 = {"C": 16.21, "Python": 12.12, "Java": 11.68}

seriesAno1 = pd.Series(dic1)
seriesAno2 = pd.Series(dic2)

totalAno1 = seriesAno1.sum()
totalAno2 = seriesAno2.sum()

print("Porcentagem total do primeiro ano:\n", totalAno1)
print("Porcentagem total do segundo ano:\n", totalAno2)
