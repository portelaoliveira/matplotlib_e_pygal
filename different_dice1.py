from lib.die import Die
import pygal
''' Vamos cria um histograma que é um gráfico de barras quem mostra a frequência da ocorrência
    de determinados resultados. '''

# Cria um D6 e um D10.
die_1 = Die(8) # Cria uma instância de Die passando como argumento oito lados.
die_2 = Die(8) # Cria uma instância de Die passando como argumento oito lados.

# Faz alguns lançamentos e armazena os resultados em uma lista.
results = []
for roll_num in range(100000): # Lançando o dado mil vezes e armazenamos o resultado de cada lançamento em uma lista.
    result = die_1.roll() + die_2.roll() # Soma dos dois dados em cada lançamento.
    results.append(result)

# Analisa os resultados.
frequencies = [] # Armazena o número de vezes que cada valor foi tirado.
max_result = die_1.num_sides + die_2.num_sides # Maior resultado possível da soma é (12) e o menor é (2).
for value in range(2, max_result + 1): # Percorre os valores possíveis.
    frequency = results.count(value) # Conta quantas vezes cada número aparece em results
    frequencies.append(frequency) # Concatenamos o valor na lista frequencies.

# Visualiza os resultados.
hist = pygal.Bar() # Cria uma instância e armazena em hist.

# Definimos o atributo title, x_labels, y_labels, add e render_to_file.
hist.title = 'Results of rolling two D8 dice 100000 times.'
hist.x_labels = list(range(2, max_result + 1))
hist.x_title = 'Result'
hist.y_title = 'Frequency of result'

hist.add('D8 + D8', frequencies) # Acrescenta uma série de valores ao gráfico
hist.render_to_file('different1_dice_visual.svg') # Renderizamos o gráfico em um arquivo SVG, que espera
# um nome de arquivo com extensão .svg.
