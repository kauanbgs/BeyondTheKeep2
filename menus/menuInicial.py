from assets.things import animar_texto
from menus.classSelection import escolhaClasse
import curses
import time
import pygame
def menuInicial():

    pygame.init()

    # Configurações da janela
    WIDTH, HEIGHT = 600, 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Menu Inicial")

    clock = pygame.time.Clock()

    mago_frames = [
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame1.png").convert_alpha(), (160, 160)),
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame2.png").convert_alpha(), (160, 160)),
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame3.png").convert_alpha(), (160, 160)),
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame4.png").convert_alpha(), (160, 160)),
    ]

    mago_frames_parado = [
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe1.png").convert_alpha(), (160, 160)),
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe2.png").convert_alpha(), (160, 160)),
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe3.png").convert_alpha(), (160, 160)),
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe4.png").convert_alpha(), (160, 160)),
    ]

    background = pygame.image.load("assets/images/praia.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))


    # Posição inicial do jogador
    player_x = 200
    player_y = HEIGHT - 130  # chão

      # Velocidade
    player_speed = 5
    # Controle da animação
    current_frame = 0
    frame_timer = 0
    frame_delay = 10  # troca de imagem a cada 10 frames


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

        pygame.display.flip()


    pygame.quit()
    sys.exit()
