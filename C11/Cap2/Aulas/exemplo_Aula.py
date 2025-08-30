# Para comentar use #
# Para Printar na tela
print('Olá Python') # Somente texto
print(7+7) # Operações matemáticas
print('O resultado de 7 + 7 é', 7+7) # Texto + operaçõe

# Linha em branco
print("\n")

# Criando uma variavel, não é necessário colocar o tipo dela
nome = 'Vicent' # String (str)
idade = 30 # Inteiro (int)
peso = 83.5 # Ponto Flutuante (float)
print('Nome:', nome, 'Idade:', idade, "Peso:", peso)

# Os tipos primitivos do Python são:
int #usado para representar números inteiros positivos e negativos
float #usado para representar números reais positivos e negativos
bool #usado para aceitar valores True e False;
str #usado para armazenar textos dentro de ‘’

# No Python, os operadores aritméticos mais populares são:
# + (soma)
# - (subtração)
# * (multiplicação)
# / (divisão)
# == (igualdade)
# ** (potenciação)
# // (divisão inteira)
# % (resto da divisão)

print("\n")

# Chamando biblioteca math, util para fazer operações rapidas
import math
num1 = 2.5
num2 = 4
print('\nValor 2.5 Truncamento (Remove a parte decimal):', math.trunc(num1))
print('\nValor 2.5 Teto (Arredonda para CIMA):', math.ceil(num1))
print('\nValor 2.5 Piso (Arredonda para BAIXO):', math.floor(num1))
print('\nValor 4 Raiz Quadrada:', math.sqrt(num2))
print('\nValor 4 Fatorial:', math.factorial(num2))

# MANIPULANDO CADEIAS DE CARACTERES
var = "Hello World"
print(var[6]) #captura a letra W da String
print(var[:5]) #captura a palavra Hello
print(var[6:11]) #captura a palavra World (6 inclusive e 11 exclusive)
print(var[6:]) #também captura a palavra World
print(var[0:10:2]) #mostra HloWrd (ou seja, pula de 2 em 2)
print(var)

# STRUTURAS DE DECISÃO
idade = int(input("\nEntre com sua idade: "))
if idade < 18:
    print("Você é menor de idade")
else:
    print("Você é maior de idade")

# LAÇOS DE REPETIÇÃO
for c in range(0,10): #mostrando um conteúdo x vezes
    print("Python é legal")
for c in range(0,10): #a variável c assume um novo valor a cada iteração
    print(c)
for c in range (10,0,-1): #realizando uma contagem regressiva
    print(c)

var = 1
while var < 5:
    print(var)
    var +=1
senha = ""
while senha != "python123":
    senha = input("Entre com a senha correta:")
print("Bem-vindo ao sistema! ☺")