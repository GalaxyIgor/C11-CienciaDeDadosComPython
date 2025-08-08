# Exemplo de Conjuntos use {}
conjunto = {'Goku', 'Vegeta', 'Trunks', 'Gohan'}
# Se vc printar provavelmente vai sair em ordem aleatoria (Ele não guarda a ordem dos elementos)
print("Exemplo de Conjuntos: " + str(conjunto)) # str() esta fazendo a Conjuntos virar string, pois não pode concatenar

# Adicionando Elementos
conjunto.add("Bulma")
conjunto.add("Bulma") # se vc adicionar um repetido ele simplesmente vai ignorar(não existe conjuntos com elementos iguais)
print("Adicionando a Bulma: " + str(conjunto))

# Removendo Um Elemento (apenas por valor, indice não é possivel)
conjunto.remove("Trunks")
print("Removendo o Trunks: " + str(conjunto))

# Não da para trocar elementos automaticamente
# Para saber o tipo de algo
print(type(conjunto))