#Esse arquivo representa o inventário do jogador, onde ele pode usar poções e ver suas estatísticas
#This file represents the player's inventory, where they can use potions and view their stats

import pygame
import sys
from assets.screenConfig import screen, fontBold, filtro_preto, molduraInventario, setaPraTras
from assets.config import Char

inventory = ["Pocaoforca", "Pocaovida", None, None, None, None]

def inventario():
    from menus.gameMenu import gameMenu

    inventory_open_sound = pygame.mixer.Sound("assets/sounds/ziperabrindo.mp3")
    inventory_open_sound.set_volume(0.5)
    inventory_open_sound.play()

    background_img = pygame.image.load("assets/images/wallpaper.jpg").convert()
    background_img = pygame.transform.scale(background_img, (800, 450))
    player_img = pygame.image.load("assets/images/magoFrame1.png").convert_alpha()
    player_img = pygame.transform.scale(player_img, (300, 300))
    pocaoforca_img = pygame.image.load("assets/images/Pocaoforca.png").convert_alpha()
    pocaoforca_img = pygame.transform.scale(pocaoforca_img, (100, 100))
    pocaovida_img = pygame.image.load("assets/images/Pocaovida.png").convert_alpha()
    pocaovida_img = pygame.transform.scale(pocaovida_img, (100, 100))

    item_rects = [
        pygame.Rect(260, 250, 90, 90),
        pygame.Rect(360, 250, 90, 90),
        pygame.Rect(460, 250, 90, 90),
        pygame.Rect(260, 350, 90, 90),
        pygame.Rect(360, 350, 90, 90),
        pygame.Rect(460, 350, 90, 90),
    ]
    
    voltarInventario_rect = pygame.Rect(25, 50, 100, 100)

    WHITE = (255, 255, 255)
    RED = (255, 100, 100)
    BLUE = (100, 150, 255)
    CYAN = (0, 255, 255)
    YELLOW = (255, 255, 0)


    running = True
    while running:
        screen.blit(background_img, (0, 0))
        screen.blit(filtro_preto, (0, 0))

        gold_text = fontBold.render(f"GOLD:  {Char.coins}", True, YELLOW)
        screen.blit(gold_text, (50, 20))

        atk_text = fontBold.render(f"ATK {Char.attack}", True, RED)
        screen.blit(atk_text, (250, 60))

        def_text = fontBold.render(f"DEF {Char.defense}", True, BLUE)
        screen.blit(def_text, (250, 100))

        hp_text = fontBold.render(f"HP {Char.health}/{Char.max_health}", True, RED)
        screen.blit(hp_text, (450, 60))

        lvl_text = fontBold.render(f"LVL: {Char.honor}", True, CYAN)
        screen.blit(lvl_text, (250, 20))

        screen.blit(player_img, (0, 150))
        screen.blit(setaPraTras, (25, 50))


        for i in range(6):
            x = 260 + (i % 3) * 100
            y = 250 + (i // 3) * 100

            screen.blit(molduraInventario, (x, y))

            item = inventory[i]
            if item == "Pocaoforca":
                screen.blit(pocaoforca_img, (x-5, y-5))
            elif item == "Pocaovida":
                screen.blit(pocaovida_img, (x-5, y-5))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if voltarInventario_rect.collidepoint(evento.pos):
                    gameMenu()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                pos_mouse = pygame.mouse.get_pos()
                for k in range(6):
                    if item_rects[k].collidepoint(pos_mouse):
                        item = inventory[k]
                        if item == "Pocaoforca":
                            Char.attack += Char.aumentoAtaque
                            inventory[k] = None
                        elif item == "Pocaovida":
                            Char.health += Char.aumentoVida
                            inventory[k] = None

            # Se quiser fechar inventário com ESC:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    gameMenu()

        pygame.display.update()
