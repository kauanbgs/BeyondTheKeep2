import pygame
import sys
from assets.screenConfig import screen, praiaBack, mainClock, backSemMarcacao, backMarcacaoInventario1, backMarcacaoInventario2, backMarcacaoExplorar1, backMarcacaoExplorar2, backMarcacaoTaverna1, backMarcacaoTaverna2
from player.inventory import inventario



def gameMenu():
    from menus.areas import explorar

    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/select.mp3")
    pygame.mixer.music.set_volume(0.20)
    

    inventario_rect = pygame.Rect(325, 30, 200, 150)
    explorar_rect = pygame.Rect(550, 100, 150, 150)
    taverna_rect = pygame.Rect(80, 125, 200, 150)
    botao_rect = pygame.Rect(340, 275, 50, 50)
    rodando = True
    selecionado_inventario = False
    selecionado_explorar = False
    selecionado_taverna = False

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if inventario_rect.collidepoint(evento.pos):
                    selecionado_inventario = not selecionado_inventario
                    selecionado_explorar = False  # Deseleciona o outro
                    selecionado_taverna = False  # Deseleciona o outro

                if explorar_rect.collidepoint(evento.pos):
                    selecionado_explorar = not selecionado_explorar
                    selecionado_inventario = False 
                    selecionado_taverna = False
                
                if taverna_rect.collidepoint(evento.pos):
                    selecionado_taverna = not selecionado_taverna
                    selecionado_inventario = False
                    selecionado_explorar = False

                if selecionado_inventario and botao_rect.collidepoint(evento.pos):
                    inventario()

                if selecionado_explorar and botao_rect.collidepoint(evento.pos):
                    explorar()

                if selecionado_taverna and botao_rect.collidepoint(evento.pos):
                    from assets.areas.tavern import tavern
                    tavern()

        pos_mouse = pygame.mouse.get_pos()

        # Fundo base
        screen.blit(backSemMarcacao, (0, 0))

        # Marcações de hover ou seleção
        if selecionado_inventario:
            screen.blit(backMarcacaoInventario2, (0, 0))
        elif inventario_rect.collidepoint(pos_mouse):
            screen.blit(backMarcacaoInventario1, (0, 0))
            pygame.mixer.music.play(1)
        if selecionado_explorar:  
            screen.blit(backMarcacaoExplorar2, (0, 0))
        elif explorar_rect.collidepoint(pos_mouse):
            screen.blit(backMarcacaoExplorar1, (0, 0))
            pygame.mixer.music.play(1)
        if selecionado_taverna:
            screen.blit(backMarcacaoTaverna2, (0, 0))
        elif taverna_rect.collidepoint(pos_mouse):
            screen.blit(backMarcacaoTaverna1, (0, 0))
            pygame.mixer.music.play(1)
        pygame.display.update()
        mainClock.tick(60)


