import imageio
import pygame
import numpy as np
import sys
from assets.config import Char
from history.introduction import introJogo
from assets.screenConfig import screen, backFrame1, setaPraTras, filtro_preto, font, fontBold, fontBoldGiga
from menus.menu import menu

def menuConfig():
  voltarMenuConfig_rect = pygame.Rect(25, 50, 100, 100)
  ptbr_rect = pygame.Rect(250, 170, 100, 20)
  en_rect = pygame.Rect(250, 190, 100, 20)
  facil_rect = pygame.Rect(450, 170, 100, 20)
  medio_rect = pygame.Rect(450, 190, 100, 20)
  dificil_rect = pygame.Rect(450, 210, 100, 20)
  
  if Char.language == "ptbr":
      configuracoes = fontBoldGiga.render("Configurações", True, (255, 255, 255))
      linguagem = fontBold.render("Linguagem", True, (255, 255, 255))
      ptbr = font.render("Portugues", True, (255, 255, 255))
      en = font.render("Ingles", True, (170, 170, 170))
      dificuldade = fontBold.render("Dificuldade", True, (255, 255, 255))
      facil = font.render("Facil", True, (255, 255, 255))
      medio = font.render("Medio", True, (170, 170, 170))
      dificil = font.render("Dificil", True, (170, 170, 170))
  else:
      configuracoes = fontBoldGiga.render("Settings", True, (255, 255, 255))
      linguagem = fontBold.render("Language", True, (255, 255, 255))
      ptbr = font.render("Portuguese", True, (170, 170, 170))
      en = font.render("English", True, (255, 255, 255))
      dificuldade = fontBold.render("Difficulty", True, (255, 255, 255))
      facil = font.render("Easy", True, (255, 255, 255))
      medio = font.render("Medium", True, (170, 170, 170))
      dificil = font.render("Hard", True, (170, 170, 170))

  rodando = True
  while rodando:
    
    screen.blit(backFrame1, (0, 0))
    screen.blit(filtro_preto, (0, 0))
    screen.blit(setaPraTras, (25, 50))
    screen.blit(configuracoes, (250, 30))
    screen.blit(linguagem, (252, 140))
    screen.blit(ptbr, (250, 170))
    screen.blit(en, (250, 190))
    screen.blit(dificuldade, (450, 140))
    screen.blit(facil, (450, 170))
    screen.blit(medio, (450, 190))
    screen.blit(dificil, (450, 210))


    for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if voltarMenuConfig_rect.collidepoint(evento.pos):
                    menu()
                if ptbr_rect.collidepoint(evento.pos):
                    Char.language = "ptbr"
                    linguagem = fontBold.render("Linguagem", True, (255, 255, 255))
                    dificuldade = fontBold.render("Dificuldade", True, (255, 255, 255))
                    ptbr = font.render("Portugues", True, (255, 255, 255))
                    en = font.render("Ingles", True, (170, 170, 170))
                    facil = font.render("Facil", True, (170, 170, 170))
                    medio = font.render("Medio", True, (170, 170, 170))
                    dificil = font.render("Dificil", True, (170, 170, 170))
                if en_rect.collidepoint(evento.pos):
                    Char.language = "en"
                    linguagem = fontBold.render("Language", True, (255, 255, 255))
                    dificuldade = fontBold.render("Difficulty", True, (255, 255, 255))
                    ptbr = font.render("Portuguese", True, (170, 170, 170))
                    en = font.render("English", True, (255, 255, 255))
                    facil = font.render("Easy", True, (170, 170, 170))
                    medio = font.render("Medium", True, (170, 170, 170))
                    dificil = font.render("Hard", True, (170, 170, 170))
                if facil_rect.collidepoint(evento.pos):
                    Char.dificuldade = 1
                    if Char.language == "ptbr":
                        facil = font.render("Facil", True, (255, 255, 255))
                        medio = font.render("Medio", True, (170, 170, 170))
                        dificil = font.render("Dificil", True, (170, 170, 170))
                    else:
                      facil = font.render("Easy", True, (255, 255, 255))
                      medio = font.render("Medium", True, (170, 170, 170))
                      dificil = font.render("Hard", True, (170, 170, 170))
                if medio_rect.collidepoint(evento.pos):
                    Char.dificuldade = 2
                    if Char.language == "ptbr":
                        facil = font.render("Facil", True, (170, 170, 170))
                        medio = font.render("Medio", True, (255, 255, 255))
                        dificil = font.render("Dificil", True, (170, 170, 170))
                    else:
                      facil = font.render("Easy", True, (170, 170, 170))
                      medio = font.render("Medium", True, (255, 255, 255))
                      dificil = font.render("Hard", True, (170, 170, 170))
                if dificil_rect.collidepoint(evento.pos):
                    Char.dificuldade = 3
                    if Char.language == "ptbr":
                        facil = font.render("Facil", True, (170, 170, 170))
                        medio = font.render("Medio", True, (170, 170, 170))
                        dificil = font.render("Dificil", True, (255, 255, 255))
                    else:
                      facil = font.render("Easy", True, (170, 170, 170))
                      medio = font.render("Medium", True, (170, 170, 170))
                      dificil = font.render("Hard", True, (255, 255, 255))

            
    pygame.display.update()