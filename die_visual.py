from lib.die import Die
import pygal
''' Vamos cria um histograma que é um gráfico de barras quem mostra a frequência da ocorrência
    de determinados resultados. '''

# Cria um D6
die = Die() # Cria uma instância de Die com seis lados como default.

# Faz alguns lançamentos e armazena os resultados em uma lista.
results = []
for roll_num in range(1000): # Lançando o dado mil vezes e armazenamos o resultado de cada lançamento em uma lista.
    result = die.roll()
    results.append(result)

# Analisa os resultados.
frequencies = [] # Armazena o número de vezes que cada valor foi tirado.
for value in range(1, die.num_sides + 1): # Percorre os valores possíveis.
    frequency = results.count(value) # Conta quantas vezes cada número aparece em results
    frequencies.append(frequency) # Concatenamos o valor na lista frequencies.

# Visualiza os resultados.
hist = pygal.Bar() # Cria uma instância e armazena em hist.

# Definimos o atributo title, x_labels, y_labels, add e render_to_file.
hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = list(range(1, 7))
hist.x_title = 'Result'
hist.y_title = 'Frequency of result'

hist.add('D6', frequencies) # Acrescenta uma série de valores ao gráfico
hist.render_to_file('die_visual.svg') # Renderizamos o gráfico em um arquivo SVG, que espera
# um nome de arquivo com extensão .svg.
