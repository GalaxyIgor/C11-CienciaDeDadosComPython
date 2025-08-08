# Exemplo de Lista use []
lista = ['Goku', 'Vegeta', 'Trunks', 'Gohan']
print("Exemplo de Lista: " + str(lista)) # str() esta fazendo a lista virar string, pois não pode concatenar

# Inserindo Elementos
lista.append('Bulma') #adiciona no fim
lista.insert(1,'Kuririn') # adiciona no indice desejado
print("Nova Lista Com Adição: " + str(lista))

# Alterando Elementos
lista[0] = 'piccolo'
print("Lista Com 0 Trocado: " + str(lista))

# Exluindo Elementos
del lista[0] # exclui um elemento pelo índice
lista.remove('Bulma')  # exclui elemento pelo valo
print("Lista Com 0 e Bulma deletado: " + str(lista))
