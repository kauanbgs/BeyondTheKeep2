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


#Makes the print like an 'typing' print. You can change the speed by going on 'assets/config.py at the config class'
def typedPrint(stdscr, texto, y, x, delay=0.03):
    altura, largura = stdscr.getmaxyx()
    stdscr.move(y, x)
    stdscr.refresh()
    for char in texto:
        
        if x >= largura - 1:
            y += 1
            x = 0
            stdscr.move(y, x)
        stdscr.addstr(y, x, char)
        stdscr.refresh()
        time.sleep(delay)
        x += 1

def animar_texto(stdscr, texto, y, x, atributo=0, delay=0.05):
    for i, letra in enumerate(texto):
        stdscr.addstr(y, x + i, letra, atributo)
        stdscr.refresh()
        time.sleep(delay)

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

def updateStatus(stdscr, item):

    curses.curs_set(0)
    stdscr.clear()
    altura, largura = stdscr.getmaxyx()

    msg = ""

    if item == "Pocao de Vida":
        Char.health += 10
        msg = f"Você recuperou 10 de vida. Vida atual: {Char.health}"
    elif item == "Pocao de Ataque":
        Char.attack += 0.5
        msg = f"Você ganhou 0.5 de ataque. Ataque atual: {Char.attack}"
    else:
        msg = "Esse item não tem efeito."

    stdscr.addstr(altura//2, (largura - len(msg))//2, msg)
    stdscr.refresh()
    time.sleep(1.5)

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


   