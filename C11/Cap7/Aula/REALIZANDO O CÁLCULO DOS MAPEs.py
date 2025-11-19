import numpy as np

# Função do MAPE
def MAPE(y_true, y_pred):
  y_true, y_pred = np.array(y_true), np.array(y_pred)
  return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

# Cálculo dos MAPEs
print('MAPE Holt-Winters:', MAPE(conjunto_teste['retail_index'], forecasting_hw))
print('MAPE ARIMA:', MAPE(conjunto_teste['retail_index'], forecasting_arima))