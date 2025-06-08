from assets.screenConfig import screen, largura, altura, fontBold, filtro_preto
from assets.config import Char
import pygame
import sys

weaponsInventory = []

def inventario():
    # Inicializa o mixer de som
    pygame.mixer.init()

    # Carrega o som de abertura do inventário
    inventory_open_sound = pygame.mixer.Sound("assets/sounds/ziperabrindo.mp3")
    inventory_opened = False
    if not inventory_opened:
        inventory_open_sound.play()
        inventory_opened = True
    inventory_open_sound.set_volume(0.5)  # Valor entre 0.0 e 1.0

    # Cores
    WHITE = (255, 255, 255)
    RED = (255, 100, 100)
    BLUE = (100, 150, 255)
    CYAN = (0, 255, 255)
    GRAY = (50, 50, 50)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)

    # Carregar imagens
    background_img = pygame.image.load("assets/images/wallpaper.jpg").convert()
    background_img = pygame.transform.scale(background_img, (800, 450))
    player_img = pygame.image.load("assets/images/magoFrame1.png").convert_alpha()
    player_img = pygame.transform.scale(player_img, (300, 375))

    # Dados do personagem
    level = 1
    hp = 0
    max_hp = 0
    mp = 0
    max_mp = 0
    atk = 1.3
    max_atk = 0
    defense = 0
    max_def = 0

    # Inventário: 3x3 (apenas Poção)
    inventory = ["Poção", None, None, None, None, None, None, None, None]
    selected_slot = 0

    # Configuração dos slots
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

        # HUD
        gold_text = fontBold.render(f"GOLD:  {Char.coins}", True, YELLOW)
        screen.blit(gold_text, (50, 20))

        lvl_text = fontBold.render(f"LVL: {Char.honor}", True, CYAN)
        screen.blit(lvl_text, (250, 20))

        hp_text = fontBold.render(f"HP {Char.health}/{Char.max_health}", True, RED)
        mp_text = fontBold.render(f"MP {mp}/{max_mp}", True, BLUE)
        atk_text = fontBold.render(f"ATK {Char.attack_base}", True, RED)
        def_text = fontBold.render(f"DEF {Char.defense}", True, BLUE)

        screen.blit(hp_text, (250, 60))
        screen.blit(atk_text, (450, 60))
        screen.blit(mp_text, (250, 100))
        screen.blit(def_text, (450, 100))

        # Personagem
        screen.blit(player_img, (0, 100))

        # INVENTÁRIO
        for idx, slot in enumerate(slots):
            if idx == selected_slot:
                pygame.draw.rect(screen, CYAN, slot, 3)
            else:
                pygame.draw.rect(screen, WHITE, slot, 1)

            if inventory[idx]:
                item_text = fontBold.render(inventory[idx], True, WHITE)
                screen.blit(item_text, (slot.x + 5, slot.y + 20))

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    if selected_slot % 3 > 0:
                        selected_slot -= 1
                elif event.key == pygame.K_RIGHT:
                    if selected_slot % 3 < 2:
                        selected_slot += 1
                elif event.key == pygame.K_UP:
                    if selected_slot - 3 >= 0:
                        selected_slot -= 3
                elif event.key == pygame.K_DOWN:
                    if selected_slot + 3 < len(slots):
                        selected_slot += 3
                elif event.key == pygame.K_RETURN:
                    if inventory[selected_slot]:
                        print(f"Usou: {inventory[selected_slot]}")
                        inventory[selected_slot] = None

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()
