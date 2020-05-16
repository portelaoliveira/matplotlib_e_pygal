import matplotlib.pyplot as plt

# Pontos individuais com scatter().
#plt.scatter(2, 4, s = 200) # O argumento S define o tamanho dos pontos usados para fazer o gráfico

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
''' Quando essas listas são passadas para scatter(), o matplotlib lê um valor de cada lista à medida 
    que plotar cada ponto. Os pontos a serem plotados são (1, 1), (2, 4), (3, 9).... '''
plt.scatter(x_values, y_values, c = (0, 0, 0.8), edgecolors = 'none', s = 40) # O argumento edgecolor remove o contorno dos pontos.
# O argumento c = 'red' define as cores dos pontos.
# Passando uma tupla para o argumento C, por exemplo, c = (0, 0, 0.8), personalizamos 
# as cores em um modelo RGB  (vermelho, verde e azul). Utilizamops valores entre 0 e 1.
# Os valores próximos a 0 geram cores escuras enquanto valores mais próximos de 1 produzem cores mais claras.

# Define o título do gráfico e nomeia os eixos
plt.title('Square numbers', fontsize = 24)
plt.xlabel('Value', fontsize = 14)
plt.ylabel('Square', fontsize = 14)

# Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000]) # Valores mínimos e máximos para o eixo x e para o eixo y.

plt.show()