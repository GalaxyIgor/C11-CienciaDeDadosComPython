import pandas as pd
import numpy as np

# Carregando o dataset do Índice de Volume de Vendas no Setor Varejista Brasileiro
dataset = pd.read_csv('retail_index_br.csv', delimiter=';', index_col='date', parse_dates=True)

# Transformando os dados de y em float
dataset['retail_index'].astype(float)

# Plotando a Time Series
dataset['retail_index'].plot(figsize=(8, 6),
title='Índice de volume de vendas no setor varejista brasileiro',
xlabel='Data', ylabel='Índice', x_compat=True)