from pmdarima.arima import auto_arima

# aplicando o modelo com dados de treinamento
model = auto_arima(y = conjunto_treinamento['retail_index'], m = 12)

# mostrando o resultado do melhor modelo ARIMA detectado
print(model)

# realizando as previsoes
forecasting_arima = pd.Series(model.predict(n_periods=len(conjunto_teste)))

# mostrando dados de treinamento
conjunto_treinamento['retail_index']['2015-01-01':].plot(figsize= (8, 6))

# mostrando dados de teste
conjunto_teste['retail_index'][:].plot()

# mostrando previsões
forecasting_arima.plot(legend = True, label='Previsão')