import pandas as pd

# Apresente o crescimento/declínio no mercado de cada linguagem do primeiro ano para o segundo ano;
dic1 = {"Java": 16.25, "C": 16.04, "Python": 9.85}
dic2 = {"C": 16.21, "Python": 12.12, "Java": 11.68}

seriesAno1 = pd.Series(dic1)
seriesAno2 = pd.Series(dic2)

variacao = seriesAno2 - seriesAno1

print("Crescimento/Declínio:\n", variacao)

