import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# importando o dataset
df = pd.read_csv('retail_index_br.csv', delimiter=';', index_col='date', parse_dates=True)

# criando um modelo de previsão
model = ExponentialSmoothing(endog=df.retail_index, trend = 'add',
                             seasonal = 'add', seasonal_periods=12).fit()

# realizando a previsão
# limitando o gráfico para facilitar a visualização
# prevendo 3 anos
predictions = model.forecast(steps = 36)
df['retail_index']['2015-01-01':].plot(figsize= (8, 6))
predictions.plot()
