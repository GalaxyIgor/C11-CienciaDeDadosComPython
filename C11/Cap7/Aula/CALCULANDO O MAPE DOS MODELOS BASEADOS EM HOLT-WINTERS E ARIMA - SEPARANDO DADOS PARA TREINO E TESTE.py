import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# importando o dataset
df = pd.read_csv('retail_index_br.csv', delimiter=';', index_col='date', parse_dates=True)

# no total, o dataset retail_index_br possui 273 meses (De jan 2000 a set 2022)
# 218 serão usados para treinamento e 55 para testes
meses_teste = 55
conjunto_treinamento = df.iloc[:-meses_teste, :]
conjunto_teste = df.iloc[-meses_teste:, :]

print(conjunto_teste)
print(conjunto_treinamento)