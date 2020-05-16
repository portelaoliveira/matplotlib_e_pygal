import matplotlib.pyplot as plt

# Pontos individuais com scatter().
#plt.scatter(2, 4, s = 200) # O argumento S define o tamanho dos pontos usados para fazer o gráfico

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
''' Quando essas listas são passadas para scatter(), o matplotlib lê um valor de cada lista à medida 
    que plotar cada ponto. Os pontos a serem plotados são (1, 1), (2, 4), (3, 9).... '''
plt.scatter(x_values, y_values, s = 100)

# Define o título do gráfico e nomeia os eixos
plt.title('Square numbers', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square', fontsize = 14)

# Define o tamanho dos rótulos de marcações
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)

plt.show()

