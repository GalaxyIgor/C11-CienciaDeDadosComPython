# 2. Por meio do dataset space.csv, trace um gráfico em barras mostrando quantas empresas espaciais diferentes os EUA e a CHINA possuem;
# Dica: não se esqueça de retirar os resultados repetidos

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
ds = pd.read_csv("space.csv", sep=";")
ds.columns = ds.columns.str.strip()

# nunique conta valores unicos e na=false ja retira valores nulos
usa_count = ds[ds['Location'].str.contains('USA', na=False)]['Company Name'].nunique()
china_count = ds[ds['Location'].str.contains('China', na=False)]['Company Name'].nunique()

#Cria o gráfico de barras
labels = ['USA', 'China']
counts = [usa_count, china_count]

# Cria o gráfico
plt.figure(figsize=(10, 6))
bars = plt.bar(labels, counts, color=['blue', 'red'], alpha=0.7)

# Adiciona título e labels
plt.title('Número de Empresas Espaciais por País')
plt.xlabel('País')
plt.ylabel('Número de Empresas Únicas')

# Mostra o gráfico
plt.show()
