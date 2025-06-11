import pygame
import sys
from history.villages.villageEldoria import introEldoria
from history.villages.villageEldoria import menuEldoria
from history.villages.villageBrumaria import introBrumaria
from history.villages.villageBrumaria import menuBrumaria
from history.villages.villageVardann import intro_vardann
from assets.config import Char
from assets.screenConfig import screen, mainClock, explorarVilas, font
from assets.things import escrever_texto_animado

def explorar():
    from menus.gameMenu import gameMenu
    rodando = True
    voltarExplorar_rect = pygame.Rect(25, 25, 50, 50)
    vardann_rect = pygame.Rect(575, 275, 250, 250)
    brumaria_rect = pygame.Rect(375, 100, 150, 150)
    eldoria_rect = pygame.Rect(157, 290, 100, 100)

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
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if eldoria_rect.collidepoint(evento.pos):
                    if Char.veioEldoria:
                        menuEldoria()
                    introEldoria()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if vardann_rect.collidepoint(evento.pos):
                    if Char.fezVardann:
                        screen.fill((0, 0, 0))
                        escrever_texto_animado(f"{Char.Name} já completou Vardann.", font, (255, 255, 255), 275, 200, 25, screen)
                        pygame.time.wait(1000)
                        explorar()
                    if Char.veioVardann:
                        from history.villages.villageVardann import menu_vardann
                        menu_vardann()
                    intro_vardann()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if brumaria_rect.collidepoint(evento.pos):
                    if Char.fez_brumaria:
                        screen.fill((0, 0, 0))
                        escrever_texto_animado(f"{Char.Name} já completou Brumaria.", font, (255, 255, 255), 275, 200, 25, screen)
                        pygame.time.wait(1000)
                        explorar()
                    if Char.veioBrumaria:
                        menuBrumaria()
                    introBrumaria()
        screen.blit(explorarVilas, (0, 0))
        pygame.display.update()
        mainClock.tick(60)