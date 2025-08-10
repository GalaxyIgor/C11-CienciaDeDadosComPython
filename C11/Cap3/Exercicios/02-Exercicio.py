# Conjunto de modelos de cada loja
loja1 = {"iPhone 14", "Galaxy S23", "Xiaomi 13"}
loja2 = {"Xiaomi 13", "Galaxy S23", "Galaxy J7", "iPhone 12"}

# Modelos que posso comprar visitando ambas as lojas (união, ou)
print("Todos os modelos disponíveis:", loja1 | loja2)

# Modelos disponíveis em ambas (interseção, e)
print("Modelos em ambas as lojas:", loja1 & loja2)
