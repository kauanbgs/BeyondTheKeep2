from assets.screenConfig import screen, largura, altura, fontBold, filtro_preto, pocaovida, pocaoforca
from assets.config import Char
import pygame
import sys

def inventario():
    pygame.mixer.init()

    inventory_open_sound = pygame.mixer.Sound("assets/sounds/ziperabrindo.mp3")
    inventory_opened = False
    if not inventory_opened:
        inventory_open_sound.play()
        inventory_opened = True
    inventory_open_sound.set_volume(0.5)

    # Cores
    WHITE = (255, 255, 255)
    RED = (255, 100, 100)
    BLUE = (100, 150, 255)
    CYAN = (0, 255, 255)
    GRAY = (50, 50, 50)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)

    def inventory():
        # Carregar imagens
        background_img = pygame.image.load("assets/images/wallpaper.jpg").convert()
        background_img = pygame.transform.scale(background_img, (800, 450))
        player_img = pygame.image.load("assets/images/magoFrame1.png").convert_alpha()
        player_img = pygame.transform.scale(player_img, (300, 375))
        pocaoforca_img = pygame.image.load("assets/images/Pocaoforca.png").convert_alpha()
        pocaoforca_img = pygame.transform.scale(pocaoforca_img, (48, 48))
        pocaovida_img = pygame.image.load("assets/images/Pocaovida.png").convert_alpha()
        pocaovida_img = pygame.transform.scale(pocaovida_img, (48, 48))

        # Carregar imagens da barra de vida (barraVida1de8.png até barraVida8de8.png)
        life_bar_imgs = []
        for i in range(1, 9):
            img = pygame.image.load(f"assets/images/barraVida{i}de8.png").convert_alpha()
            img = pygame.transform.scale(img, (325, 290))
            life_bar_imgs.append(img)
        
        # Inventário
        inventory = ["Pocaoforca", "Pocaovida", None, None, None, None, None, None, None]
        selected_slot = 0

        # Slots
        slots = []
        slot_size = 64
        slot_margin = 20
        start_x = 250
        start_y = 300

        for row in range(3):
            for col in range(3):
                x = start_x + col * (slot_size + slot_margin)
                y = start_y + row * (slot_size + slot_margin)
                slots.append(pygame.Rect(x, y, slot_size, slot_size))

        # Loop principal
        clock = pygame.time.Clock()
        running = True

        while running:
            screen.blit(background_img, (0, 0))
            screen.blit(filtro_preto, (0, 0))

            # HUD - Layout reorganizado
            gold_text = fontBold.render(f"GOLD:  {Char.coins}", True, YELLOW)
            screen.blit(gold_text, (450, 20))

            lvl_text = fontBold.render(f"LVL: {Char.honor}", True, CYAN)
            screen.blit(lvl_text, (250, 20))

            # ATK (posição 250, 60)
            atk_text = fontBold.render(f"ATK {Char.attack_base}", True, RED)
            screen.blit(atk_text, (250, 60))

            # DEF abaixo do ATK (posição 250, 100)
            def_text = fontBold.render(f"DEF {Char.defense}", True, BLUE)
            screen.blit(def_text, (250, 100))

            # HP alinhado com DEF (450, 100) - desceu 40px em relação à posição anterior (450, 60)
            hp_text = fontBold.render(f"HP {Char.health}/{Char.max_health}", True, RED)
            screen.blit(hp_text, (450, 60))

            # Barra de vida ajustada para ficar abaixo do novo HP (450, 125)
            if Char.max_health > 0:
                vida_percentual = Char.health / Char.max_health
                index_vida = int(vida_percentual * 7)
                index_vida = max(0, min(7, index_vida))
                screen.blit(life_bar_imgs[index_vida], (320, -40))

            # Personagem
            screen.blit(player_img, (0, 100))

            # INVENTÁRIO
            for idx, slot in enumerate(slots):
                pygame.draw.rect(screen, CYAN if idx == selected_slot else WHITE, slot, 3 if idx == selected_slot else 1)
                if inventory[idx]:
                    if inventory[idx] == "Pocaoforca":
                        screen.blit(pocaoforca_img, (slot.x + 8, slot.y + 8))
                    elif inventory[idx] == "Pocaovida":
                        screen.blit(pocaovida_img, (slot.x + 8, slot.y + 8))
                    else:
                        item_text = fontBold.render(str(inventory[idx]), True, WHITE)
                        screen.blit(item_text, (slot.x + 5, slot.y + 20))

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_LEFT and selected_slot % 3 > 0:
                        selected_slot -= 1
                    elif event.key == pygame.K_RIGHT and selected_slot % 3 < 2:
                        selected_slot += 1
                    elif event.key == pygame.K_UP and selected_slot - 3 >= 0:
                        selected_slot -= 3
                    elif event.key == pygame.K_DOWN and selected_slot + 3 < len(slots):
                        selected_slot += 3
                    elif event.key == pygame.K_RETURN:
                        if inventory[selected_slot]:
                            print(f"Usou: {inventory[selected_slot]}")
                            inventory[selected_slot] = None

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        sys.exit()