import pygame
import sys
from assets.screenConfig import screen, praiaBack, mainClock, backSemMarcacao, backMarcacaoInventario1, backMarcacaoInventario2, backMarcacaoExplorar1, backMarcacaoExplorar2



def gameMenu():
    from menus.areas import explorar
    inventario_rect = pygame.Rect(325, 30, 200, 150)
    explorar_rect = pygame.Rect(550, 100, 150, 150)
    botao_rect = pygame.Rect(340, 275, 50, 50)
    rodando = True
    selecionado_inventario = False
    selecionado_explorar = False

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if inventario_rect.collidepoint(evento.pos):
                    selecionado_inventario = not selecionado_inventario
                    selecionado_explorar = False  # Deseleciona o outro

                if explorar_rect.collidepoint(evento.pos):
                    selecionado_explorar = not selecionado_explorar
                    selecionado_inventario = False  # Deseleciona o outro

                if selecionado_inventario and botao_rect.collidepoint(evento.pos):
                    abrirPraia()  # Aqui entraria o inventário

                if selecionado_explorar and botao_rect.collidepoint(evento.pos):
                    explorar()  # Aqui entraria a exploração

        pos_mouse = pygame.mouse.get_pos()

        # Fundo base
        screen.blit(backSemMarcacao, (0, 0))

        # Marcações de hover ou seleção
        if selecionado_inventario:
            screen.blit(backMarcacaoInventario2, (0, 0))
        elif inventario_rect.collidepoint(pos_mouse):
            screen.blit(backMarcacaoInventario1, (0, 0))

        if selecionado_explorar:
            screen.blit(backMarcacaoExplorar2, (0, 0))
        elif explorar_rect.collidepoint(pos_mouse):
            screen.blit(backMarcacaoExplorar1, (0, 0))

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

