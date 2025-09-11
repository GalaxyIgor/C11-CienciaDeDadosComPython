import pandas as pd
import numpy as np

# 6. Utilizando do DataFrame exemplo do tópico 5.3 deste material, calcule a
# média dos elementos da coluna X que são menores que 30;


np.random.seed(10)
df = pd.DataFrame(
    index=["A", "B", "C", "D", "E"],
    columns=["W", "X", "Y", "Z"],
    data=np.random.randint(1, 50, [5, 4]
    ))

dfX = df["X"]

dfXMenor30 = dfX < 30

media_X_menor_30 = df[dfXMenor30]["X"].mean()
print("Média da coluna X e menores que 30:", media_X_menor_30)
