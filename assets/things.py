#File made by: Kauan
import curses
import random
import os
import time

import pygame
from assets.config import Char
from assets.config import Config
from assets.itens import Village
from assets.itens import Flashback
from player.inventory import inventory
from player.inventory import weaponsInventory
from assets.itens import Itens

startTime = 0

#Starts an timer (it will be used on the saved games, at the game over and at the final page.)
def startTimer():
  global tempoComeco
  startTime = time.time()



def classUpdate():
  if Char.Name == "Aton":
    Char.classplayer = 1
    Char.health = 100
    Char.mana = 50
    Char.attack = 1.5
    weaponsInventory.append("Espada gasta")
  else:
    Char.classplayer = 2
    Char.health = 120
    Char.mana = 100
    Char.attack = 1.3
    weaponsInventory.append("Cajado antigo")

def randomVillage():
    if not Village.village_names:
        return "Você não pode mais visitar vilas."
    
    choice = random.choice(Village.village_names)
    Village.village_names.remove(choice)
    return choice


def draw_text(text, font, color, surface, x, y):
    textobject = font.render(text, 1, color)
    textrect = textobject.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobject, textrect)

def escrever_texto_animado(texto, fonte, cor, x, y, velocidade, superficie):
    texto_renderizado = ''
    for letra in texto:
        texto_renderizado += letra
        render = fonte.render(texto_renderizado, True, cor)
        superficie.blit(render, (x, y))
        pygame.display.update()
        pygame.time.delay(velocidade)


   