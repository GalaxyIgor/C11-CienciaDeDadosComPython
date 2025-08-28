import numpy as np
# Importando Dataset
ds = np.loadtxt('space.csv',
                delimiter=";",
                dtype=str,
                encoding='utf-8')

spacexMask = ds[:,1] == 'SpaceX'
spacexMissoes = ds[spacexMask]

# Converter custo para float
custos = spacexMissoes[:,6].astype(float)

# Missão mais cara
custoMaxIndex = np.argmax(custos)
missaoMaisCara = spacexMissoes[custoMaxIndex]

print("\nMissão mais cara realizada pela SpaceX: ")
print(f"Mission: {missaoMaisCara[0]}")
print(f"Company: {missaoMaisCara[1]}")
print(f"Location: {missaoMaisCara[2]}")
print(f"Date: {missaoMaisCara[3]}")
print(f"Detail: {missaoMaisCara[4]}")
print(f"Status Rocket: ${missaoMaisCara[5]} million")
print(f"Cost: ${missaoMaisCara[6]} million")
print(f"Status Mission: {missaoMaisCara[7]}")