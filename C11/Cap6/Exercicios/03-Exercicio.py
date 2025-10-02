# 3. Por meio do dataset space.csv, trace um gráfico em torta ilustrando a porcentagem de missões da empresa Roscosmos que
# deram certo e que deram errado;

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
ds = pd.read_csv("space.csv", sep=";")
ds.columns = ds.columns.str.strip()

# Filtrar missões da Roscosmos
roscosmos = ds[ds['Company Name'].str.contains('Roscosmos', case=False)]

# Contar Status Mission (Success vs Failure)
resultado = roscosmos['Status Mission'].value_counts()

# Plotar gráfico em torta
plt.figure(figsize=(6,6))
plt.pie(
    resultado,
    labels=resultado.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=['green', "red", 'yellow'],
    textprops={'rotation': 25}
)
plt.title("Porcentagem de Missões Roscosmos")
plt.show()