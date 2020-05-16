import matplotlib.pyplot as plt 
from lib.random_walk import RandomWalk

# Cria um passeio aleatório e plota os pontos
''' Todo passeio aleatório é diferente, e é divertido explorar os vários padrões que podem ser gerados.
    Uma maneira de usar o código anterios para gerar vários passeios sem a necessidade de executar o 
    programa diversas vezes é colocá-lo em um laço while, assim:
 '''

while True:
    # Cria um passeio aleatório e plota os pontos.
    rw = RandomWalk()
    rw.fill_walk()
    # Define o tamanho da janela de plotagem.
    plt.figure(dpi = 128, figsize = (10, 6) )
    ''' A função figure() controla a largura, a altura, a resolução e a cor de fundo do gráfico. '''
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors = 'none', s = 15)
    # Enfatiza o primeiro e o último ponto.
    plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)
    # remove os eixos.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = ' '
    while keep_running not in 'YN':
        keep_running = str(input('Make another walk? [Y/N]: ')).strip().upper()[0]
    if keep_running == 'N':
        break
