import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Dados
x = np.array([1, 2, 3, 4, 5])
y = x * 2
y2 = x * x

# Criar figura com dois subplots lado a lado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Primeiro subplot: Gráfico simples de linha
ax1.plot(x, y)
ax1.set_xlabel("Valores de X")
ax1.set_ylabel("Valores de Y")
ax1.set_title("Gráfico de Linha Simples: y = 2x")
ax1.grid(True, alpha=0.3)

# Segundo subplot: Gráfico com múltiplas linhas e estilos
ax2.plot(x, y, "*:r", linewidth=3, markersize=10, label="y = 2x")
ax2.plot(x, y2, "s--g", linewidth=3, markersize=10, label="y = x²")
ax2.set_xlabel("Valores de X")
ax2.set_ylabel("Valores de Y")
ax2.set_title("Gráfico com Múltiplas Linhas e Estilos")
ax2.legend()
ax2.grid(True, alpha=0.3)

# Ajustar layout e mostrar
plt.tight_layout()
plt.show()

# Outra forma de Criar subplots
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.subplot(1, 2, 1)
plt.plot(x, y,"*:r",linewidth=3)
plt.subplot(1, 2, 2)
plt.plot(x, y2,"*:r",linewidth=3)
plt.show()

# Grafico de dispersão
dfPaises = pd.read_csv("paises.csv", delimiter=";")
print(dfPaises.head(3))

# Limpando possíveis espaços nos nomes das colunas
dfPaises.columns = dfPaises.columns.str.strip()

# Pegando os 6 maiores países em área
dfMaioresPaises = dfPaises.nlargest(6, "Area (sq. mi.)")

# Gráfico de dispersão: Área x População
plt.figure(figsize=(10,6))
plt.scatter(dfMaioresPaises["Area (sq. mi.)"], dfMaioresPaises["Population"], color="blue", s=100)

# Adicionando os nomes dos países no gráfico
for i, row in dfMaioresPaises.iterrows():
    plt.text(row["Area (sq. mi.)"], row["Population"], row["Country"], fontsize=9, ha="right")

plt.xlabel("Área (sq. mi.)")
plt.ylabel("População")
plt.title("6 Maiores Países em Área")
plt.grid(False)
plt.show()

# Grafico Bar (Barras)
dfMaioresGDP = dfPaises.nlargest(5, "GDP ($ per capita)")
print(dfMaioresGDP["Country"])
plt.figure(figsize=(10,6))
plt.bar(dfMaioresGDP["Country"], dfMaioresGDP["GDP ($ per capita)"], color="green")
plt.xlabel("País")
plt.ylabel("PIB per capita ($)")
plt.title("Top 5 Países com Maior PIB per Capita")
plt.xticks(rotation=45)  # Inclina os nomes para caber melhor
plt.show()

# Criando o gráfico de barras horizontais
plt.figure(figsize=(10,6))
bars = plt.barh(dfMaioresGDP["Country"], dfMaioresGDP["GDP ($ per capita)"],
                color=plt.cm.viridis(range(len(dfMaioresGDP))))

# Adicionando valores ao lado das barras
for bar in bars:
    plt.text(bar.get_width() + 500,  # desloca um pouco para direita
             bar.get_y() + bar.get_height()/2,
             f"{bar.get_width():,.0f}",  # formata número com separador
             va="center", fontsize=9)

# Melhorias visuais
plt.xlabel("PIB per capita ($)", fontsize=12)
plt.ylabel("País", fontsize=12)
plt.title("Top 5 Países com Maior PIB per Capita", fontsize=14, fontweight="bold")
plt.grid(axis="x", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# Grafico em Pizza (Pie Chart)
dfNoCoast = dfPaises[dfPaises["Coastline (coast/area ratio)"]==0]
print(dfNoCoast["Country"])

qtNoCoast = len(dfNoCoast)
qtCoast = len(dfPaises)- qtNoCoast

# Dados para o gráfico
valores = [qtNoCoast, qtCoast]
labels = ["Sem Litoral", "Com Litoral"]
cores = ["#ff9999", "#66b3ff"]  # cores suaves

# Gráfico de Pizza
plt.figure(figsize=(6,6))
plt.pie(valores, labels=labels, autopct="%.1f%%", startangle=90, colors=cores, explode=(0.05, 0))
plt.title("Distribuição de Países com e sem Litoral", fontsize=14, fontweight="bold")
plt.show()

plt.figure(figsize=(6,6))
plt.pie(
    [qtNoCoast, qtCoast],
    labels=["Sem Litoral", "Com Litoral"],
    autopct="%.1f%%",
    startangle=140,
    colors=plt.cm.Pastel1.colors,  # paleta pastel
    shadow=True
)
plt.title("Distribuição de Países (Paleta Pastel)", fontsize=14, fontweight="bold")
plt.show()
