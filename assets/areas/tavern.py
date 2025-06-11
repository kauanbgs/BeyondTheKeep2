from assets.screenConfig import screen, fontBold, botaoTavernaHover, botaoTaverna, setaPraTras, filtro_preto, pocaovida2, font, fontBold, pocaoforca2, fundoTaverna
from assets.config import Char
import pygame
import sys
from menus.gameMenu import gameMenu
from assets.things import escrever_texto_animado
from player.inventory import inventory



def tavern():
    rodando = True
    if Char.language == "ptbr":
        pocaoDeVida = fontBold.render("Pocao de Vida", True, (255, 255, 255))
    else:
        pocaoDeVida = fontBold.render("Health Potion", True, (255, 255, 255))
    infosPocaoVida = font.render(f"+{Char.aumentoVida}HP", True, (255, 255, 255))
    infosPocaoAtaque = font.render(f"+{Char.aumentoAtaque}ATK", True, (255, 255, 255))
    if Char.language == "ptbr":
        pocaoDeAtaque = fontBold.render(f"Pocao de Ataque", True, (255, 255, 255))
    else:
        pocaoDeAtaque = fontBold.render(f"Attack Potion", True, (255, 255, 255))
    voltarTaverna_rect = pygame.Rect(25, 25, 100, 100)
    pocaoAtaque_rect = pygame.Rect(80, 225, 250, 50)
    pocaoVida_rect = pygame.Rect(80, 300, 250, 50)
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
                        if Char.language == "ptbr":
                            escrever_texto_animado("Nao tem moedas suficientes.", font, (255, 255, 255), 275, 200, 25, screen)
                        else:
                            escrever_texto_animado("Not enough coins.", font, (255, 255, 255), 275, 200, 25, screen)
                        pygame.time.wait(1500)
                        tavern()
                    elif inventory[5] is not None:
                        screen.fill((0, 0, 0))
                        pygame.display.update()
                        if Char.language == "ptbr":
                            escrever_texto_animado("Nao ha espaco suficiente.", font, (255, 255, 255), 275, 200, 25, screen)
                        else:
                            escrever_texto_animado("Not enough space.", font, (255, 255, 255), 275, 200, 25, screen)
                        pygame.time.wait(1500)
                        tavern()

                    else:
                        Char.coins -= 5
                        screen.fill((0, 0, 0))
                        pygame.display.update()
                        if Char.language == "ptbr":
                            escrever_texto_animado("Comprou Pocao de vida!.", font, (255, 255, 255), 275, 200, 25, screen)
                        else:
                            escrever_texto_animado("Bought Health Potion!", font, (255, 255, 255), 275, 200, 25, screen)
                        pygame.time.wait(1500)
                        for i in range(len(inventory)):
                            if inventory[i] is None:
                                inventory[i] = "Pocaovida"
                                break
                if pocaoAtaque_rect.collidepoint(evento.pos):
                    if Char.coins < 3:
                        screen.fill((0, 0, 0))
                        pygame.display.update()
                        if Char.language == "ptbr":
                            escrever_texto_animado("Nao tem moedas suficientes.", font, (255, 255, 255), 275, 200, 25, screen)
                        else:
                            escrever_texto_animado("Not enough coins.", font, (255, 255, 255), 275, 200, 25, screen)
                        pygame.time.wait(1500)
                        tavern()
                    elif inventory[5] is not None:
                        screen.fill((0, 0, 0))
                        pygame.display.update()
                        if Char.language == "ptbr":
                            escrever_texto_animado("Nao ha espaco suficiente.", font, (255, 255, 255), 275, 200, 25, screen)
                        else:
                            escrever_texto_animado("Not enough space.", font, (255, 255, 255), 275, 200, 25, screen)
                        pygame.time.wait(1500)
                        tavern()
                    else:
                        Char.coins -= 3
                        screen.fill((0, 0, 0))
                        pygame.display.update()
                        if Char.language == "ptbr":
                            escrever_texto_animado("Comprou Pocao de Ataque!.", font, (255, 255, 255), 275, 200, 25, screen)
                        else:
                            escrever_texto_animado("Bought Attack Potion!", font, (255, 255, 255), 275, 200, 25, screen)
                        pygame.time.wait(1500)
                        for i in range(len(inventory)):
                            if inventory[i] is None:
                                inventory[i] = "Pocaovida"
                                break

        
        screen.blit(fundoTaverna, (0, 0))
        screen.blit(filtro_preto, (0, 0))
        screen.blit(botaoTaverna, (60, 125))
        screen.blit(botaoTaverna, (60, 200))
        gold_text = fontBold.render(f"GOLD:  {Char.coins}", True, (255, 255, 0))
        screen.blit(gold_text, (75, 190))
        mouse_pos = pygame.mouse.get_pos()
        if pocaoAtaque_rect.collidepoint(mouse_pos):
            screen.blit(botaoTavernaHover, (60, 125))
            screen.blit(infosPocaoAtaque, (400, 240))
        if pocaoVida_rect.collidepoint(mouse_pos):
            screen.blit(botaoTavernaHover, (60, 200))
            screen.blit(infosPocaoVida, (400, 315))
        screen.blit(pocaoDeVida, (150, 315))
        screen.blit(pocaoDeAtaque, (150, 240))
        screen.blit(pocaovida2, (50, 200))
        screen.blit(pocaoforca2, (50, 275))
        screen.blit(setaPraTras, (25, 25))

        
        pygame.display.update()
        

