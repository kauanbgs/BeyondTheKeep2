#Coisas em geral que serao utilizadas ao longo do código
#General things that will be used throughout the code
import random
import time

import pygame
from assets.config import Char

from assets.screenConfig import screen

startTime = 0

def startTimer():
  global startTime
  startTime = time.time()



def classUpdate():
  if Char.Name == "Aton":
    Char.classplayer = 1
    Char.health = 100
    Char.mana = 50
    Char.attack = 1.5
  else:
    Char.classplayer = 2
    Char.health = 120
    Char.mana = 100
    Char.attack = 1.3



def escrever_texto_animado(texto, fonte, cor, x, y, velocidade, superficie):
    texto_renderizado = ''
    for letra in texto:
        texto_renderizado += letra
        render = fonte.render(texto_renderizado, True, cor)
        superficie.blit(render, (x, y))
        pygame.display.update()
        pygame.time.delay(velocidade)


def fade_transicao(imagem1, imagem2, duracao=300):
    clock = pygame.time.Clock()
    alpha = 0
    passo = 255 / (duracao / 10)

    overlay = pygame.Surface(screen.get_size()).convert()
    overlay.fill((0, 0, 0))

    screen.blit(imagem1, (0, 0))
    pygame.display.update()

    # Fade para preto
    while alpha < 255:
        overlay.set_alpha(alpha)
        screen.blit(imagem1, (0, 0))
        screen.blit(overlay, (0, 0))
        pygame.display.update()
        alpha += passo
        clock.tick(60)

    # Fade de preto para imagem2
    alpha = 255
    while alpha > 0:
        overlay.set_alpha(alpha)
        screen.blit(imagem2, (0, 0))
        screen.blit(overlay, (0, 0))
        pygame.display.update()
        alpha -= passo
        clock.tick(60)


def d20():
    return random.randint(1, 20)