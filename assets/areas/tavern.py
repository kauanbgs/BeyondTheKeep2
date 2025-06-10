from assets.screenConfig import screen, largura, altura, fontBold, botaoTavernaHover, botaoTaverna, filtro_preto, pocaovida2, font, fontBold, pocaoforca2, fundoTaverna
from assets.config import Char
import pygame
import sys
from menus.gameMenu import gameMenu
from assets.things import escrever_texto_animado



def tavern():
    rodando = True
    pocaoDeVida = fontBold.render("Pocao de Vida", True, (255, 255, 255))
    pocaoDeAtaque = fontBold.render("Pocao de Ataque", True, (255, 255, 255))
    voltarTaverna_rect = pygame.Rect(25, 25, 100, 100)
    pocaoVida_rect = pygame.Rect(80, 225, 250, 50)
    pocaoAtaque_rect = pygame.Rect(80, 300, 250, 50)
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if voltarTaverna_rect.collidepoint(evento.pos):
                    gameMenu()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if pocaoVida_rect.collidepoint(evento.pos):
                    if Char.coins < 5:
                        screen.fill((0, 0, 0))
                        pygame.display.update()
                        escrever_texto_animado("Aton nao tem moedas suficientes.", font, (255, 255, 255), 275, 200, 25, screen)
                        pygame.time.wait(1500)
                        tavern()
                    else:
                        Char.coins -= 5
                        #DAR APPEND NO INVENTARIO AQUI
                if pocaoAtaque_rect.collidepoint(evento.pos):
                    if Char.coins < 3:
                        screen.fill((0, 0, 0))
                        pygame.display.update()
                        escrever_texto_animado("Aton nao tem moedas suficientes.", font, (255, 255, 255), 275, 200, 25, screen)
                        pygame.time.wait(1500)
                        tavern()
                    else:
                        Char.coins -= 3
                        #DAR APPEND NO INVENTARIO AQUI

        
        screen.blit(fundoTaverna, (0, 0))
        screen.blit(filtro_preto, (0, 0))
        screen.blit(botaoTaverna, (70, 140))
        screen.blit(botaoTaverna, (70, 220))
        # screen.blit(botaoTavernaHover, (70, 230))
        screen.blit(pocaoDeVida, (150, 320))
        screen.blit(pocaoDeAtaque, (150, 240))
        screen.blit(pocaovida2, (50, 200))
        screen.blit(pocaoforca2, (50, 275))
        
        pygame.display.update()
        

