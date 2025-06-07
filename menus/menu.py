import pygame
import sys
from history.introduction import introJogo
from assets.screenConfig import screen, font, praiaBack, filtro_preto, mainClock, mago_frames_parado, mago_frames, praia, espada, cajado, fundo, botaoPlay, botaoPlayHover, botaoSaves, botaoSavesHover, botaoQuit, botaoQuitHover, fade_out, play_rect, quit_rect, saves_rect, backFrames, casteloZoom3, casteloZoom2, casteloZoom1, casteloZoom0, casteloPortaZoom1, casteloPortaZoom0, casteloPortaZoom2, casteloPrincipal

def menu(): 
  pygame.mixer.init()
  pygame.mixer.music.load("assets/sounds/musicaMenu.mp3")
  frame_timer = 0
  frame_index = 0
  frame_delay = 150
  direcao = 1
  rodando = True
  pygame.mixer.music.play(-1)
  pygame.mixer.music.set_volume(.08)
  while rodando:
      dt = mainClock.tick(60)
      for evento in pygame.event.get():
          if evento.type == pygame.QUIT:
              rodando = False

      frame_timer += dt
      if frame_timer >= frame_delay:
            frame_timer = 0
            frame_index += direcao

            if frame_index == 13:  # chegou no último frame, muda direção
                direcao = -1
            elif frame_index == 1:  # chegou no primeiro frame, muda direção
                direcao = 1

        # Desenha o frame atual (supondo que backFrames esteja indexado de 0)
        # Se backFrames[0] é frame 1, backFrames[12] é frame 13
      screen.blit(backFrames[frame_index - 1], (0, 0))


      pos_mouse = pygame.mouse.get_pos()

      if play_rect.collidepoint(pos_mouse):
          screen.blit(botaoPlayHover, (160, -160))
          if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
              rodando = False
              pygame.mixer.music.stop()
              fade_out()
              introJogo()
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
              pygame.mixer.music.stop()
              pygame.quit()
      else:
          screen.blit(botaoQuit, (320, -160))

      pygame.display.update()




