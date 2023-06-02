import pygame as pg
import random
from pygame.locals import *

# função para alinhar a posição da fruta com a posição da cobra
def alinha_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10) # divisão inteira

def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pg.init()   # inicializa todos os módulos do pygame importados

# testamos se os módulos foram inicializados com sucesso
if not(pg.get_init()):  # 'get_init()' retorna True se os módulos foram inicializados
    print("Inicialização dos módulos não teve sucesso")

# inicializa o display; passamos uma tupla com dois valores, que são o tamanho da tela (Ox e Oy)
screen = pg.display.set_mode((600, 600))

# a variável 'imagem' salva o caminho do ícone
imagem = pg.image.load("cobra-icone.png")
pg.display.set_icon(imagem) # definimos como ícone a imagem salva anteriormente

# indicamos o título do programa
pg.display.set_caption("Jogo da Cobrinha")

# a cobra é uma lista de segmentos; abaixo, temos três tuplas que vão indicar
# cada ponto (ou seja, as coordenadas) onde estão localizados os três segmentos da cobra
cobra = [(200, 200), (210, 200), (220, 200)]
cobra_skin = pg.Surface((10, 10))
cobra_skin.fill((64, 218, 145))

fruta_posicao = alinha_random()
fruta = pg.Surface((10, 10))
fruta.fill((255, 0, 0))

minha_direcao = LEFT

clock = pg.time.Clock()

# todo jogo tem um laço infinito
while 1:

    clock.tick(15)

    # pegamos os eventos de mudança
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()   # desinicializa todos os módulos pygame que foram inicializados anteriormente

        if event.type == KEYDOWN:
            if event.key == K_UP:
                minha_direcao = UP
            if event.key == K_DOWN:
                minha_direcao = DOWN
            if event.key == K_LEFT:
                minha_direcao = LEFT
            if event.key == K_RIGHT:
                minha_direcao = RIGHT
        
    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])

    if colisao(cobra[0], fruta_posicao):
        fruta_posicao = alinha_random()
        cobra.append((0, 0))
    
    if minha_direcao == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)

    if minha_direcao == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    
    if minha_direcao == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    
    if minha_direcao == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])

    # limpar tela; preto em RGB
    screen.fill((0, 0, 0))

    screen.blit(fruta, fruta_posicao)

    for posicao in cobra:
        screen.blit(cobra_skin, posicao)

    pg.display.update()