import time
import pygame

def duel():
    from assets.config import Char
    import random

    pygame.init()

    # Configurações da janela
    WIDTH, HEIGHT = 600, 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Duelos Mágicos")

    clock = pygame.time.Clock()

    mago_frames = [
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame1.png").convert_alpha(), (128, 128)),
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame2.png").convert_alpha(), (128, 128)),
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame3.png").convert_alpha(), (128, 128)),
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame4.png").convert_alpha(), (128, 128)),
]

    mago_frames_parado = [
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe1.png").convert_alpha(), (128, 128)),
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe2.png").convert_alpha(), (128, 128)),
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe3.png").convert_alpha(), (128, 128)),
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe4.png").convert_alpha(), (128, 128)),
    ]

    enemy_img = pygame.image.load("assets/images/Mago.png").convert_alpha()
    enemy_img = pygame.transform.scale(enemy_img, (120, 120))

    background = pygame.image.load("assets/images/floresta.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))


    # Posição inicial do jogador
    player_x = 200
    player_y = HEIGHT - 110  # chão

    max_hp = 100

    enemy_x = WIDTH - 200
    enemy_y = HEIGHT - 110
    enemy_hp = 100

    # Velocidade
    player_speed = 5
    # Controle da animação
    current_frame = 0
    frame_timer = 0
    frame_delay = 10  # troca de imagem a cada 10 frames



    # Cores
    WHITE = (255, 255, 255)

    def draw_health_bar(surface, x, y, w, h, hp, max_hp, color):
        pygame.draw.rect(surface, (50, 50, 50), (x, y, w, h))  # fundo
        hp_width = int(w * (hp / max_hp))
        pygame.draw.rect(surface, color, (x, y, hp_width, h))  # vida
        pygame.draw.rect(surface, (0, 0, 0), (x, y, w, h), 2)  # borda

    # Loop principal
    running = True
    while running:
        clock.tick(60)
        screen.fill((255, 255, 255))  # Limpa a tela

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

                # Movimento e animação
        keys = pygame.key.get_pressed()
        moving = False

        if keys[pygame.K_q]:
            Char.health = max(0, Char.health - 1)
        if keys[pygame.K_e]:
            enemy_hp = max(0, enemy_hp - 1)
        if keys[pygame.K_d]:
            player_x += player_speed
            moving = True
        if keys[pygame.K_a]:
            player_x -= player_speed
            moving = True

        # Atualizar frame
        frame_timer += 1
        if frame_timer >= frame_delay:
            frame_timer = 0
            current_frame += 1

        # Decide qual animação usar
        if moving:
            frame_list = mago_frames
        else:
            frame_list = mago_frames_parado

        current_frame = current_frame % len(frame_list)

        # Desenhar tudo
        screen.blit(background, (0, 0))  # fundo
        screen.blit(frame_list[current_frame], (player_x, player_y))  # player animado
        screen.blit(enemy_img, (enemy_x, enemy_y))  # inimigo

        # Barra de vida do jogador
        draw_health_bar(screen, 50, 20, 200, 20, Char.health, max_hp, (0, 200, 0))

        # Barra de vida do inimigo (lado direito)
        draw_health_bar(screen, WIDTH - 250, 20, 200, 20, enemy_hp, max_hp, (200, 0, 0))

        pygame.display.flip()


    pygame.quit()
    sys.exit()
