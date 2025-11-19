import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Airtravel - Série Temporal
airtravel = pd.read_csv('airtravel.csv')
airtravel['Date'] = pd.to_datetime(airtravel['Date'])
airtravel.set_index('Date', inplace=True)

plt.figure(figsize=(10, 4))
airtravel['Passengers'].plot(title='Passageiros Aéreos', color='blue')
plt.grid(True)
plt.show()

# Airtravel - Decomposição
decomposition_air = seasonal_decompose(airtravel['Passengers'], model='additive', period=12)
decomposition_air.plot()
plt.show()

# CO2 Emissions - Série Temporal
co2_emissions = pd.read_csv('co2_emissions.csv')
co2_emissions['Date'] = pd.to_datetime(co2_emissions['Year'], format='%Y')
co2_emissions.set_index('Date', inplace=True)

plt.figure(figsize=(10, 4))
co2_emissions['CO2_Emissions'].plot(title='Emissões de CO₂', color='red')
plt.grid(True)
plt.show()

# CO2 Emissions - Decomposição 

decomposition_co2 = seasonal_decompose(co2_emissions['CO2_Emissions'], model='additive', period=1)
decomposition_co2.plot()
plt.show()