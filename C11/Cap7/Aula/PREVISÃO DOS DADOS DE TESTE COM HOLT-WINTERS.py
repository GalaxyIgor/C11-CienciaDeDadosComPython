import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# aplicando o modelo com dados de treinamento
model = ExponentialSmoothing(endog=conjunto_treinamento.retail_index, trend = 'mul',
                             seasonal = 'mul', seasonal_periods=12).fit()

# realizando a previsão no mesmo tamanho dos dados de teste
forecasting_hw = model.forecast(steps = len(conjunto_teste))

# mostrando dados de treinamento
df['retail_index']['2015-01-01':].plot(figsize= (8, 6))

# mostrando dados de teste
conjunto_teste['retail_index'][:].plot()

# mostrando previsões
forecasting_hw.plot(legend = True, label='Previsão')