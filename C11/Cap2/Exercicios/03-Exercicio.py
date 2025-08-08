while True:
    # Entrada de Dados
    sexo = input("Digite seu sexo (M/F): ").upper()
    if sexo == 'M':
        print("Você é homem")
        break
    elif sexo == 'F':
        print("Você é mulher")
        break
    else:
        # Caso o usuario digite qualquer outro caracter
        print("Sexo inválido. Digite M ou F.")