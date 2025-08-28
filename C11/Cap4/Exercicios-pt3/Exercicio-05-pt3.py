import numpy as np
# Importando Dataset
ds = np.loadtxt('space.csv',
                delimiter=";",
                dtype=str,
                encoding='utf-8')

# 5. Mostre o nome das empresas que já realizaram missões espaciais, juntamente com suas respectivas quantidades de missões (use o for no final para mostrar as informações)
# valores únicos e contagens
empresas, contagem = np.unique(ds[:,1], return_counts=True)

# Converter contagens para string
contagem_str = contagem.astype(str) # se n quiser colocar da erro

# Cria string com separador ": "
empresas_com_separador = np.char.add(empresas, ": ")

# Adiciona as contagens às strings
resultado_final = np.char.add(empresas_com_separador, contagem_str)

print("\nNome das empresas que já realizaram missões espaciais e quantidades de missões: ")

# Junta todas as linhas com quebra de linha
print('\n'.join(resultado_final))
