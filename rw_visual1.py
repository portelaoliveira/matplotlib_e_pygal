import matplotlib.pyplot as plt 
from lib.random_walk1 import RandomWalk

''' Movimento molecular. Simula o percurso de um grão de pólem na superfície de um agota de água. '''

while True:
    # Cria um passeio aleatório e plota os pontos.
    rw = RandomWalk(5000)
    rw.fill_walk()
     # Define o tamanho da janela de plotagem.
    plt.figure(dpi = 128, figsize = (10, 6) )
    plt.plot(rw.x_values, rw.y_values, linewidth = 0.8)
    # Enfatiza o primeiro e o último ponto.
    plt.scatter(0, 0, c = 'green', edgecolors = 'none', s = 150)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 150)
    # remove os eixos.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = ' '
    while keep_running not in 'YN':
        keep_running = str(input('Make another walk? [Y/N]: ')).strip().upper()[0]
    if keep_running == 'N':
        break
