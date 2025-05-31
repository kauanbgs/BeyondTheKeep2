from assets.things import typedPrint
from menus.classSelection import escolhaClasse
import curses
import time
import pygame

def Intro(stdscr):
    curses.initscr
    curses.start_color()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Texto normal
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)   # Selecionado
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Título

    textoApresentação1 = ("Você desperta, sentindo a areia fria sob seu corpo e o som das ondas quebrando na praia. "
              "Ao abrir os olhos, percebe que está sozinho numa ilha deserta, cercado por uma densa floresta "
              "e um céu cinzento que promete tempestade.")
    textoApresentação2 = ("Enquanto tenta se levantar, algo chama sua atenção: duas armas repousam na areia, como se estivessem esperando por você."
              "A primeira é uma Espada gasta pelo tempo, mas ainda forte — a arma dos Guerreiros."
              "A segunda é um Cajado antigo, coberto de runas misteriosas — a arma dos Magos."
              "Sua vida, Seu destino começam agora!")

    altura, largura = stdscr.getmaxyx()
    titulo = "Beyond The Keep"
    x_titulo = largura // 2 - len(titulo) // 2

    typedPrint(stdscr, textoApresentação1, 2, 2)
    typedPrint(stdscr, textoApresentação2, 4, 2)
    # Animação do título uma única vez no início
    stdscr.clear()
    stdscr.border()
    time.sleep(0.5)

    stdscr.endwin()
    menuInicial()

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
