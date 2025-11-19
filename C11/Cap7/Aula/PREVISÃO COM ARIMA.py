import pandas as pd
from pmdarima import auto_arima

# importando o dataset
df = pd.read_csv('retail_index_br.csv', delimiter=';', index_col='date', parse_dates=True)

# criando um modelo de previsão
# o parâmetro m indica a sazonalidade, que neste dataset acontece anualmente
model = auto_arima(y = df['retail_index'], m = 12)
# mostrando os melhores parâmetros calculados pelo auto_arima
print(model)

# realizando a previsão
predictions = pd.Series(model.predict(n_periods = 36))
df['retail_index']['2015-01-01':].plot(figsize= (8, 6))
predictions.plot()