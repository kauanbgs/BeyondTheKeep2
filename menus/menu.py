import pygame
import sys
from history.introduction import intro
from assets.configTela import screen, font, praiaBack, filtro_preto, mainClock, mago_frames_parado, mago_frames, praia, espada, cajado, fundo, botaoPlay, botaoPlayHover, botaoSaves, botaoSavesHover, botaoQuit, botaoQuitHover, fade_out, play_rect, quit_rect, saves_rect

def menu(): 
  rodando = True
  while rodando:
      for evento in pygame.event.get():
          if evento.type == pygame.QUIT:
              rodando = False

      # Desenha o background
      screen.blit(fundo, (0, 0))


      pos_mouse = pygame.mouse.get_pos()

      if play_rect.collidepoint(pos_mouse):
          screen.blit(botaoPlayHover, (160, -160))
          if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
              rodando = False
              fade_out()
              intro()
      else:
          screen.blit(botaoPlay, (160, -160))

      if saves_rect.collidepoint(pos_mouse):
          screen.blit(botaoSavesHover, (0, -160))
      else:
          screen.blit(botaoSaves, (0, -160))

      if quit_rect.collidepoint(pos_mouse):
          screen.blit(botaoQuitHover, (320, -160))
          if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
              rodando = False
              pygame.quit()
      else:
          screen.blit(botaoQuit, (320, -160))

      pygame.display.update()
