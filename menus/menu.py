import imageio
import pygame
import numpy as np
import sys
from history.introduction import introJogo
from assets.screenConfig import screen, mainClock, botaoPlay, botaoPlayHover, botaoSaves, botaoSavesHover, botaoQuit, botaoQuitHover, fade_out, play_rect, quit_rect, saves_rect


def menu():
    reader = imageio.get_reader("assets/videos/videoBack.mp4")
    frames = [np.array(frame) for frame in reader]  # carrega todos os frames na memória
    reader.close()

    total_frames = len(frames)
    frame_index = 0
    direcao = 1
    fps = 30 
    rodando = True

    # Música de fundo
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/musicaMenu.mp3")
    pygame.mixer.music.set_volume(0.08)
    pygame.mixer.music.play(-1)

    while rodando:
        dt = mainClock.tick(fps)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Desenha frame atual do vídeo
        frame = frames[frame_index]
        surface = pygame.surfarray.make_surface(np.transpose(frame, (1, 0, 2)))
        surface = pygame.transform.scale(surface, screen.get_size())  # ← ajusta o tamanho do vídeo
        screen.blit(surface, (0, 0))

        # Avança ou volta frame para fazer looping "ping-pong"
        frame_index += direcao
        if frame_index >= total_frames - 1:
            direcao = -1
        elif frame_index <= 0:
            direcao = 1

        # Botões
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
                sys.exit()
        else:
            screen.blit(botaoQuit, (320, -160))

        pygame.display.update()