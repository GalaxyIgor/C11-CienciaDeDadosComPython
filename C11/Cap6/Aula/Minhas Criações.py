# Importação das bibliotecas necessárias
import numpy as np  # Para operações numéricas e arrays
import pandas as pd  # Para manipulação de dados (embora não seja usado neste exemplo)
import matplotlib.pyplot as plt  # Para criação de gráficos e visualizações

# Configuração do estilo visual dos gráficos
plt.style.use('default')  # Usa o estilo padrão do matplotlib
plt.rcParams['figure.figsize'] = (10, 6)  # Define o tamanho padrão das figuras
plt.rcParams['font.size'] = 12  # Define o tamanho padrão da fonte

# Criação de dados de exemplo usando numpy
x = np.array([1, 2, 3, 4, 5])  # Cria um array com valores de 1 a 5
y = x * 2  # Cria um segundo array onde cada elemento é o dobro do correspondente em x

# Exemplo 1: Gráfico de linha básico com marcadores especiais
plt.figure(figsize=(12, 8))  # Cria uma nova figura com tamanho específico

# Cria um subplot em uma grade 2x3, posição 1
plt.subplot(2, 3, 1)
# Plota os dados com formato "s:r":
# - "s" significa marcadores quadrados
# - ":" significa linha pontilhada
# - "r" significa cor vermelha
plt.plot(x, y, "s:r", linewidth=3, markersize=8)
plt.xlabel("Valores de X")  # Rótulo do eixo X
plt.ylabel("Valores de Y")  # Rótulo do eixo Y
plt.title("Gráfico de Linha com Marcadores")  # Título do gráfico
plt.grid(True, alpha=0.3)  # Adiciona grade com transparência

# Exemplo 2: Gráfico de barras
plt.subplot(2, 3, 2)  # Segundo subplot na grade
categorias = ['A', 'B', 'C', 'D', 'E']  # Rótulos das categorias
valores = [23, 45, 56, 12, 67]  # Valores para cada categoria
cores = ['red', 'blue', 'green', 'orange', 'purple']  # Cores para cada barra
# Cria gráfico de barras com cores e transparência
plt.bar(categorias, valores, color=cores, alpha=0.7)
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.title("Gráfico de Barras")

# Exemplo 3: Gráfico de dispersão (scatter plot)
plt.subplot(2, 3, 3)  # Terceiro subplot
# Gera dados aleatórios para o scatter plot
x_scatter = np.random.rand(50) * 10  # 50 valores entre 0 e 10
y_scatter = x_scatter * 2 + np.random.randn(50) * 2  # Valores y com relação a x + ruído
# Cria scatter plot com cor verde, transparência e tamanho dos pontos
plt.scatter(x_scatter, y_scatter, c='green', alpha=0.6, s=80)
plt.xlabel("Variável X")
plt.ylabel("Variável Y")
plt.title("Gráfico de Dispersão")

# Exemplo 4: Gráfico de pizza (pie chart)
plt.subplot(2, 3, 4)  # Quarto subplot
labels = ['Python', 'Java', 'C++', 'JavaScript', 'Outros']  # Rótulos
sizes = [45, 20, 15, 10, 10]  # Tamanhos das fatias (percentuais)
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']  # Cores personalizadas
# Cria gráfico de pizza com porcentagem, ângulo inicial e cores
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Garante que o gráfico seja circular (não elíptico)
plt.title("Distribuição de Linguagens de Programação")

# Exemplo 5: Histograma
plt.subplot(2, 3, 5)  # Quinto subplot
# Gera dados com distribuição normal (1000 valores, média=50, desvio=10)
dados = np.random.randn(1000) * 10 + 50
# Cria histograma com 30 caixas (bins), cor laranja e bordas pretas
plt.hist(dados, bins=30, color='orange', alpha=0.7, edgecolor='black')
plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.title("Histograma")

# Exemplo 6: Gráfico de área
plt.subplot(2, 3, 6)  # Sexto subplot
x_area = np.linspace(0, 10, 100)  # 100 pontos igualmente espaçados entre 0 e 10
y1_area = np.sin(x_area)  # Valores de seno
y2_area = np.cos(x_area)  # Valores de cosseno
# Preenche a área sob a curva do seno
plt.fill_between(x_area, y1_area, color="blue", alpha=0.3, label="Seno")
# Preenche a área sob a curva do cosseno
plt.fill_between(x_area, y2_area, color="red", alpha=0.3, label="Cosseno")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Gráfico de Área")
plt.legend()  # Adiciona legenda

# Ajusta o layout para evitar sobreposição
plt.tight_layout()
# Exibe todos os seis gráficos criados até agora
plt.show()

# Exemplo 7: Subplots mais elaborados com eixos explícitos
# Cria uma figura com 1 linha e 2 colunas de subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Gráfico à esquerda - múltiplas linhas
x_multi = np.linspace(0, 10, 100)  # 100 pontos entre 0 e 10
# Plota três funções diferentes no mesmo gráfico
axs[0].plot(x_multi, np.sin(x_multi), label='sin(x)', linewidth=2)
axs[0].plot(x_multi, np.cos(x_multi), label='cos(x)', linewidth=2)
axs[0].plot(x_multi, np.sin(x_multi) + np.cos(x_multi), label='sin(x)+cos(x)', linewidth=2)
axs[0].set_xlabel('x')  # Rótulo do eixo x
axs[0].set_ylabel('y')  # Rótulo do eixo y
axs[0].set_title('Múltiplas Funções')  # Título
axs[0].legend()  # Adiciona legenda
axs[0].grid(True, alpha=0.3)  # Adiciona grade

# Gráfico à direita - gráfico de caixa (boxplot)
# Cria três conjuntos de dados com distribuições normais diferentes
dados_box = [np.random.normal(0, std, 100) for std in range(1, 4)]
# Cria boxplot para os três conjuntos de dados
axs[1].boxplot(dados_box, labels=['Grupo 1', 'Grupo 2', 'Grupo 3'])
axs[1].set_title('Gráfico de Caixa (Boxplot)')
axs[1].set_ylabel('Valores')

# Ajusta o layout e exibe os gráficos
plt.tight_layout()
plt.show()

# Exemplo 8: Visualização 3D
from mpl_toolkits.mplot3d import Axes3D  # Importa toolkit para gráficos 3D

# Cria uma nova figura
fig = plt.figure(figsize=(10, 7))
# Adiciona um subplot com projeção 3D
ax = fig.add_subplot(111, projection='3d')

# Gera dados aleatórios para os três eixos
x_3d = np.random.standard_normal(100)
y_3d = np.random.standard_normal(100)
z_3d = np.random.standard_normal(100)

# Cria scatter plot 3D, colorindo os pontos pelo valor de z
ax.scatter(x_3d, y_3d, z_3d, c=z_3d, cmap='viridis', s=50, alpha=0.6)
ax.set_xlabel('Eixo X')  # Rótulo do eixo X
ax.set_ylabel('Eixo Y')  # Rótulo do eixo Y
ax.set_zlabel('Eixo Z')  # Rótulo do eixo Z
ax.set_title('Gráfico de Dispersão 3D')  # Título

# Exibe o gráfico 3D
plt.show()