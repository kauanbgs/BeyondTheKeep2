#File made by: Kauan

import pygame

#Main settings of pygame

mainClock = pygame.time.Clock()
pygame.init()

#---------------------------------------------------------------------#
largura = 800 #PLEASE DONT CHANGE THIS!
altura = 450 #PLEASE DONT CHANGE THIS!
#---------------------------------------------------------------------#


pygame.display.set_caption("Beyond The Keep")
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
cajado = pygame.image.load("assets/images/cajado.png")
cajado = pygame.transform.scale(cajado, (200, 200))

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
