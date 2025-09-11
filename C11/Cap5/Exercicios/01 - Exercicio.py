import pandas as pd

# 1. Crie duas Series com os seguintes valores:
# • seriesAno1: {‘Java’: 16.25, ‘C’: 16.04, ‘Python’: 9.85}
# • seriesAno2: {‘C’: 16.21, ‘Python’: 12.12, ‘Java’: 11.68}

dic1 = {"Java": 16.25, "C": 16.04, "Python": 9.85}
dic2 = {"C": 16.21, "Python": 12.12, "Java": 11.68}

seriesAno1 = pd.Series(dic1)
seriesAno2 = pd.Series(dic2)

print("Serie do Ano 1:\n", seriesAno1)
print("\nSerie do Ano 2:\n", seriesAno2)