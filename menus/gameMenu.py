import pygame
import sys
from history.introduction import intro
from assets.screenConfig import screen, font, praiaBack, filtro_preto, mainClock, mago_frames_parado, mago_frames, praia, espada, cajado, fundo, botaoPlay, botaoPlayHover, botaoSaves, botaoSavesHover, botaoQuit, botaoQuitHover, fade_out, play_rect, quit_rect, saves_rect, backSemMarcacao, backMarcacaoInventario1, backMarcacaoInventario2


def gameMenu():
    inventario_rect = pygame.Rect(325, 60, 200, 150)
    botao_rect = pygame.Rect(340, 275, 50, 50)
    rodando = True
    selecionado_inventario = False

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if inventario_rect.collidepoint(evento.pos):
                    selecionado_inventario = not selecionado_inventario

                if selecionado_inventario and botao_rect.collidepoint(evento.pos):
                    # Aqui seria a troca de tela, não só um blit
                    abrirPraia()  # <-- Você precisa criar essa função para a praia

        pos_mouse = pygame.mouse.get_pos()

        if selecionado_inventario:
            screen.blit(backMarcacaoInventario2, (0, 0))  # Estado selecionado
        elif inventario_rect.collidepoint(pos_mouse):
            screen.blit(backMarcacaoInventario1, (0, 0))  # Hover
        else:
            screen.blit(backSemMarcacao, (0, 0))          # Normal

        pygame.display.update()
        mainClock.tick(60)


def abrirPraia():
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False  # Volta para o menu

        screen.blit(praiaBack, (0, 0))
        pygame.display.update()
        mainClock.tick(60)
