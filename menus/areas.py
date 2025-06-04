import pygame
import sys

from assets.screenConfig import screen, font, praiaBack, filtro_preto, mainClock, mago_frames_parado, mago_frames, praia, espada, cajado, fundo, botaoPlay, botaoPlayHover, botaoSaves, botaoSavesHover, botaoQuit, botaoQuitHover, fade_out, play_rect, quit_rect, saves_rect, backSemMarcacao, backMarcacaoInventario1, backMarcacaoInventario2, backMarcacaoExplorar1, backMarcacaoExplorar2, explorarVilas

def explorar():
    from menus.gameMenu import gameMenu
    rodando = True
    voltarExplorar_rect = pygame.Rect(25, 25, 50, 50)
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False  # Volta para o menu
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if voltarExplorar_rect.collidepoint(evento.pos):
                    gameMenu()
        screen.blit(explorarVilas, (0, 0))
        pygame.display.update()
        mainClock.tick(60)