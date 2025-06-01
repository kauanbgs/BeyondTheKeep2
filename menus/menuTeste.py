import pygame
import sys
from assets.config import Char
from assets.things import draw_text
from assets.things import escrever_texto_animado
from assets.things import classUpdate

mainClock = pygame.time.Clock()
pygame.init()
largura = 800
altura = 450
pygame.display.set_caption("Menu teste")
screen = pygame.display.set_mode((largura, altura))

fundo = pygame.image.load("assets/images/wallpaper.jpg")
fundo = pygame.transform.scale(fundo, (largura, altura))

botaoPlay = pygame.image.load("assets/images/botaoPlay.png")
botaoPlay = pygame.transform.scale(botaoPlay, (450, 450))

botaoSaves = pygame.image.load("assets/images/botaoSaves.png")
botaoSaves = pygame.transform.scale(botaoSaves, (450, 450))

botaoQuit = pygame.image.load("assets/images/botaoQuit.png")
botaoQuit = pygame.transform.scale(botaoQuit, (450, 450))


botaoPlayHover = pygame.image.load("assets/images/botaoPlayHover.png")
botaoPlayHover = pygame.transform.scale(botaoPlayHover, (450, 450))

botaoSavesHover = pygame.image.load("assets/images/botaoSavesHover.png")
botaoSavesHover = pygame.transform.scale(botaoSavesHover, (450, 450))

botaoQuitHover = pygame.image.load("assets/images/botaoQuitHover.png")
botaoQuitHover = pygame.transform.scale(botaoQuitHover, (450, 450))

play_rect = pygame.Rect(160 + 125, -160 + 175, 200, 100)
saves_rect = pygame.Rect(0 + 125, -160 + 175, 200, 100)
quit_rect = pygame.Rect(320 + 125, -160 + 175, 200, 100)

praia = pygame.image.load("assets/images/praia.png")
praia = pygame.transform.scale(praia, (largura, altura))

praiaBack = pygame.image.load("assets/images/praiaBack.png")


filtro_preto = pygame.Surface((800, 600)) 
filtro_preto.set_alpha(200) 
filtro_preto.fill((0, 0, 0)) 




mago_frames_parado = [
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe1.png").convert_alpha(), (128, 128)),
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe2.png").convert_alpha(), (128, 128)),
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe3.png").convert_alpha(), (128, 128)),
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe4.png").convert_alpha(), (128, 128)),
    ]

mago_frames = [
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame1.png").convert_alpha(), (128, 128)),
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame2.png").convert_alpha(), (128, 128)),
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame3.png").convert_alpha(), (128, 128)),
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame4.png").convert_alpha(), (128, 128)),
]

espada = pygame.image.load("assets/images/espada.png")
espada = pygame.transform.scale(espada, (250, 250))

font = pygame.font.Font("assets/fonts/Minecraft.ttf", 16) 

def fade_out(velocidade=5):
    fade = pygame.Surface((largura, altura))
    fade.fill((0, 0, 0))
    for alpha in range(0, 255, velocidade):
        fade.set_alpha(alpha)
        screen.blit(fundo, (0, 0))
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(10)

click = False

def intro():
    screen.blit(praiaBack, (0, 0))
    screen.blit(filtro_preto, (0, 0))
    escrever_texto_animado("Voce acorda, tonto e desnorteado, em uma praia qualquer.", font, (255, 255, 255), 0, 50, 25, screen)
    escrever_texto_animado("Em ambos os seus lados pairam duas armas sobre o ar.", font, (255, 255, 255), 0, 75, 25, screen)
    escrever_texto_animado("A primeira e um:", font, (255, 255, 255), 0, 100, 25, screen)
    escrever_texto_animado("CAJADO ANTIGO", font, (255, 0, 0), 0, 125, 75, screen)
    escrever_texto_animado("A segunda e uma:", font, (255, 255, 255), 0, 150, 25, screen)
    escrever_texto_animado("ESPADA GASTA", font, (255, 0, 0), 0, 175, 75, screen)
    escrever_texto_animado("Voce deve escolher uma delas para continuar sua jornada.", font, (255, 255, 255), 0, 200, 50, screen)
    pygame.time.delay(2000)
    
 
    frame_index = 0
    frame_timer = 0
    frame_delay = 200
    player_x, player_y = 340, 320
    player_speed = 5
    current_frame = 0


    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return

        frame_timer += mainClock.get_time()
        if frame_timer >= frame_delay:
            frame_timer = 0
            frame_index = (frame_index + 1) % len(mago_frames_parado)


        # Movimento e animação
        keys = pygame.key.get_pressed()
        moving = False

        if keys[pygame.K_d]:
            player_x += player_speed
            moving = True
        if keys[pygame.K_a]:
            player_x -= player_speed
            moving = True
            
        if frame_timer >= frame_delay:
            frame_timer = 0
            current_frame += 1

        if moving:
            frame_list = mago_frames
        else:
            frame_list = mago_frames_parado

        current_frame = current_frame % len(frame_list)

        # Define a Rect for the player and the sword for collision detection
        player_rect = pygame.Rect(player_x, player_y, 128, 128)
        if player_rect.colliderect(pygame.Rect(650, 250, 250, 250)):
            Char.Name = "Aton"
            classUpdate()
            introTexto()            
        if player_rect.colliderect(pygame.Rect(-100, 250, 250, 250)):
            Char.Name = "Nextage"
            classUpdate()
            introTexto()


        screen.blit(praia, (0, 0))
        screen.blit(frame_list[current_frame], (player_x, player_y))
        screen.blit(espada, (600, 250))
        screen.blit(espada, (50, 250))
        
        pygame.display.update()
        mainClock.tick(60)




def introTexto():
    screen.fill((0, 0, 0))
    escrever_texto_animado("E aqui começa sua historia...", font, (255, 255, 255), 0, 25, 25, screen)
    escrever_texto_animado("Talvez voce quisesse se tornar uma lenda, alguem cujo nome seria gravado em cancoes", font, (255, 255, 255), 0, 50, 25, screen)
    escrever_texto_animado("e sussurrado em tavernas por seculos.", font, (255, 255, 255), 0, 75, 25, screen)
    escrever_texto_animado("Ou talvez sua ambicao fosse um pouco mais simples:", font, (255, 255, 255), 0, 100, 25, screen)
    escrever_texto_animado("juntar ouro suficiente para se tornar rico.", font, (255, 255, 255), 0, 125, 25, screen)
    escrever_texto_animado(f"Seja qual for o caso, voce e {Char.Name}, de Skalice:", font, (255, 255, 255), 0, 150, 25, screen)
    if Char.Name == "Aton":
        escrever_texto_animado(f"Um guerreiro, mestre da espada e professor de esgrima.", font, (255, 255, 255), 0, 175, 25, screen)
    else:
        escrever_texto_animado(f"Um mago, mestre das artes arcanas e professor de magia.", font, (255, 255, 255), 0, 175, 25, screen)
    escrever_texto_animado("E sua jornada está apenas começando.", font, (255, 255, 255), 0, 200, 25, screen)
    pygame.display.update()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return
      

# Loop principal
def menu(): 
  rodando = True
  while rodando:
      for evento in pygame.event.get():
          if evento.type == pygame.QUIT:
              rodando = False

      # Desenha o background
      screen.blit(fundo, (0, 0))


      pos_mouse = pygame.mouse.get_pos()

      if play_rect.collidepoint(pos_mouse):
          screen.blit(botaoPlayHover, (160, -160))
          if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
              rodando = False
              fade_out()
              intro()
      else:
          screen.blit(botaoPlay, (160, -160))

      if saves_rect.collidepoint(pos_mouse):
          screen.blit(botaoSavesHover, (0, -160))
      else:
          screen.blit(botaoSaves, (0, -160))

      if quit_rect.collidepoint(pos_mouse):
          screen.blit(botaoQuitHover, (320, -160))
          if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
              rodando = False
              pygame.quit()
      else:
          screen.blit(botaoQuit, (320, -160))

      pygame.display.update()

menu()


    