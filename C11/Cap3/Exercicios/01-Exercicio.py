# Times Retirados da Champions League 2024
# Lista com os 5 primeiros colocados
times = ['Liverpool', 'Barcelona', 'Arsenal', 'Internazionale', 'Atlético de Madrid']

# a. Apenas os 3 primeiros colocados
print("Top 3: ", times[:3])

# b. Os últimos 2 colocados
print("Os últimos 2 colocados: ", times[-2:])

# c. Uma lista com os times em ordem alfabética
print("Times por ordem alfabética: ", sorted(times))

# d. Em que posição da tabela se encontra o Barcelona
posicao = times.index("Barcelona") + 1
# str() para transformar posição em string para possibilitar concatenação
print("O barcelona esta no " + str(posicao) + "° Lugar")