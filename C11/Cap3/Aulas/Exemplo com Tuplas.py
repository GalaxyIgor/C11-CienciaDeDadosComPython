# Exemplo de Tupla use ()
tupla = ('Goku', 'Vegeta', 'Trunks', 'Gohan')
print("Exemplo de Tupla: " + str(tupla)) # str() esta fazendo a tupla virar string pois não pode concatenar


# Exemplo com chrud (n lembro como escreve) vai gerar um erro pois é imutavel
# Mostrando Elementos
# tupla = ('Goku', 'Vegeta', 'Trunks', 'Gohan')
# print('Sem alteração: ' + tupla)
# Alterando Elementos
# tupla[0] = 'Bulma'


# Slicing de Elementos (Fatiar)
# Sem fatiamentos
tupla = ('Goku', 'Vegeta', 'Trunks', 'Gohan')
print("Exemplo de Tupla Sem Fatiamento: " + str(tupla))

print('Tuplas Fatiadas: ')
# Fazendo o fatiamento 1 esta incluso e 3 não esta incluso, algo como 1<=x<3
print(tupla[1:3]) # Vegeta e trunks
# Se quiser pegar até o final n prescisa preencher
print(tupla[2:]) # trunks e Gohan
# Indice negativo vai pegar de trás para frente
print(tupla[-2]) # trunks com indice negativo

# Funcoes pre-prontas do python
print ("Funções: ")
print(len(tupla)) # para saber a quantidade
print(max(tupla)) # Pega o Fim, a-z ou 1-9
print(min(tupla)) # Pega o inicio, a-z ou 1-9