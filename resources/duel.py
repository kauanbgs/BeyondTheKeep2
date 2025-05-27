import time
import pygame

def duel():

    import random

    pygame.init()

    # Configurações da janela
    WIDTH, HEIGHT = 600, 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Duelos Mágicos")

    clock = pygame.time.Clock()

    player_img = pygame.image.load("assets/images/Mago.png").convert_alpha()
    player_img = pygame.transform.scale(player_img, (120, 120))

    enemy_img = pygame.image.load("assets/images/Mago.png").convert_alpha()
    enemy_img = pygame.transform.scale(enemy_img, (120, 120))

    background = pygame.image.load("assets/images/floresta.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))


    # Posição inicial do jogador
    player_x = 200
    player_y = HEIGHT - 110  # chão

    enemy_x = WIDTH - 200
    enemy_y = HEIGHT - 110

    # Velocidade
    player_speed = 5



    # Cores
    WHITE = (255, 255, 255)

    # Loop principal
    running = True
    while running:
        clock.tick(60)  # FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))  # Fundo
        screen.blit(player_img, (player_x, player_y))
        screen.blit(enemy_img, (enemy_x, enemy_y))
        pygame.display.flip()

        pygame.display.flip()  # mostra tudo

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_x -= player_speed
        if keys[pygame.K_d]:
            player_x += player_speed

        

    pygame.quit()
    sys.exit()
