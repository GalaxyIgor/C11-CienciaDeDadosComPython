import pandas as pd
import numpy as np

# 7. Utilizando do mesmo DataFrame, apresente a média dos elementos da
# linha D usando a função loc() como base e a soma dos elementos da linha E
# usando a função iloc() como base;


np.random.seed(10)


df = pd.DataFrame(
    index=["A", "B", "C", "D", "E"],
    columns=["W", "X", "Y", "Z"],
    data=np.random.randint(1, 50, [5, 4]
    ))


media_linha_D = df.loc["D"].mean()
print("Média da linha D:", media_linha_D)


soma_linha_E = df.iloc[4].sum()
print("Soma da linha E:", soma_linha_E)
