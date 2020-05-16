import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5] # Valores de entrada
squares = [1, 4, 9, 16, 25] # Valores de saída

# O parâmetro linewidth controla a espessura da linha gerada por plot.
plt.plot(input_values, squares, linewidth = 5)  
# Define o título do gráfico e nomeia os eixos.
plt.title('Square Numbers', fontsize = 24) # Função title define o título do gráfico.
# A o parâmetro fontsize controla o tamanho do texto no gráfico.
# As funções xlabel e ylabel permite definir títulos em cada um dos eixos.
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square of value', fontsize = 14)

# Define o tamanho dos rótulos das marcações dos eixos.
plt.tick_params(axis = 'both', labelsize = 14) # A função tick_parms estiliza as marcações nos eixos.
# O argumento axis afeta as marcações no eixo x e y.
# O argumento labelsize deine o tamanho dos rótulos das marcações.

plt.show() # Abre o visualizador do matplotlib e exibe o gráfico.
