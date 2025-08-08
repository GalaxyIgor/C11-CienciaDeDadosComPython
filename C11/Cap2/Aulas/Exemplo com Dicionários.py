# Exemplo de dicionarios use {} tem chave:valor (key:value), lembrar de criar as variaveis, parece json
pessoa = {
            'nome': 'Goku',
            'idade': 43,
            'sexo': 'Masculino'
          }
# pode fazer tbm como: pessoal = {'nome': 'Goku', 'idade': 43, 'sexo': 'Masculino'}

print("Exemplo de dicionarios: " + str(pessoa)) # str() esta dicionarios a Conjuntos virar string, pois não pode concatenar

# Add
pessoa['raca'] = 'Sayajin'
pessoa['familia'] = ['Gohan','Goten','Chichi', 'Pan']

# Update
pessoa['iadade'] = 45

# Delete
del pessoa['sexo']

print("Novo dicionarios: " + str(pessoa))

# Como acessar um valor especifico Chichi neste caso
print("Acessando a " + str(pessoa['familia'][2]))