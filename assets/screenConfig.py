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

praia = pygame.image.load("assets/images/praia.jpg")
praia = pygame.transform.scale(praia, (largura, altura))

praiaBack = pygame.image.load("assets/images/praiaBack.png")
praiaBack = pygame.transform.scale(praiaBack, (largura, altura))

explorarVilas = pygame.image.load("assets/images/explorarVilas.jpg")
explorarVilas = pygame.transform.scale(explorarVilas, (largura, altura))

backSemMarcacao = pygame.image.load("assets/images/backSemMarcacao.png")
backSemMarcacao = pygame.transform.scale(backSemMarcacao, (largura, altura))

backMarcacaoInventario1 = pygame.image.load("assets/images/backMarcacaoInventario1.png")
backMarcacaoInventario1 = pygame.transform.scale(backMarcacaoInventario1, (largura, altura))

backMarcacaoInventario2 = pygame.image.load("assets/images/backMarcacaoInventario2.png")
backMarcacaoInventario2 = pygame.transform.scale(backMarcacaoInventario2, (largura, altura))

backMarcacaoExplorar1 = pygame.image.load("assets/images/backMarcacaoExplorar1.png")
backMarcacaoExplorar1 = pygame.transform.scale(backMarcacaoExplorar1, (largura, altura))

backMarcacaoExplorar2 = pygame.image.load("assets/images/backMarcacaoExplorar2.png")
backMarcacaoExplorar2 = pygame.transform.scale(backMarcacaoExplorar2, (largura, altura))

persoBase = pygame.image.load("assets/images/persoBase.png")
persoBase = pygame.transform.scale(persoBase, (160, 160))

casteloZoom0 = pygame.image.load("assets/images/casteloZoom0.jpeg")
casteloZoom0 = pygame.transform.scale(casteloZoom0, (largura, altura))

casteloZoom1 = pygame.image.load("assets/images/casteloZoom1.jpg")
casteloZoom1 = pygame.transform.scale(casteloZoom1, (largura, altura))

casteloZoom2 = pygame.image.load("assets/images/casteloZoom2.jpg")
casteloZoom2 = pygame.transform.scale(casteloZoom2, (largura, altura))

casteloZoom3 = pygame.image.load("assets/images/casteloZoom3.jpg")
casteloZoom3 = pygame.transform.scale(casteloZoom3, (largura, altura))

casteloPortaZoom0 = pygame.image.load("assets/images/casteloPortaZoom0.jpeg")
casteloPortaZoom0 = pygame.transform.scale(casteloPortaZoom0, (largura, altura))

casteloPortaZoom1 = pygame.image.load("assets/images/casteloPortaZoom1.jpg")
casteloPortaZoom1 = pygame.transform.scale(casteloPortaZoom1, (largura, altura))

casteloPortaZoom2 = pygame.image.load("assets/images/casteloPortaZoom2.jpg")
casteloPortaZoom2 = pygame.transform.scale(casteloPortaZoom2, (largura, altura))

casteloPrincipal = pygame.image.load("assets/images/casteloPrincipal.jpeg")
casteloPrincipal = pygame.transform.scale(casteloPrincipal, (largura, altura))

apostasBack = pygame.image.load("assets/images/apostasBack.png")
apostasBack = pygame.transform.scale(apostasBack, (largura, altura))

fundoEldoria = pygame.image.load("assets/images/fundoEldoria.png")
fundoEldoria = pygame.transform.scale(fundoEldoria, (largura, altura))

persoAndando = pygame.image.load("assets/images/persoAndando.png")
persoAndando = pygame.transform.scale(persoAndando, (largura, altura))

botaoEldoriaSair = pygame.image.load("assets/images/botaoEldoriaSair.png")
botaoEldoriaSair = pygame.transform.scale(botaoEldoriaSair, (250, 250))

botaoEldoriaExplorar = pygame.image.load("assets/images/botaoEldoriaExplorar.png")
botaoEldoriaExplorar = pygame.transform.scale(botaoEldoriaExplorar, (250, 250))

botaoEldoriaInteragir = pygame.image.load("assets/images/botaoEldoriaInteragir.png")
botaoEldoriaInteragir = pygame.transform.scale(botaoEldoriaInteragir, (250, 250))

filtro_preto = pygame.Surface((800, 600)) 
filtro_preto.set_alpha(200) 
filtro_preto.fill((0, 0, 0)) 

frame1 = pygame.image.load(f"assets/images/backFrame1.jpg").convert_alpha()
frame1 = pygame.transform.scale(frame1, (largura, altura))



mago_frames_parado = [
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe1.png").convert_alpha(), (160, 160)),
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe2.png").convert_alpha(), (160, 160)),
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe3.png").convert_alpha(), (160, 160)),
    pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe4.png").convert_alpha(), (160, 160)),
    ]

mago_frames = [
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame1.png").convert_alpha(), (160, 160)),
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame2.png").convert_alpha(), (160, 160)),
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame3.png").convert_alpha(), (160, 160)),
    pygame.transform.scale(pygame.image.load("assets/images/magoFrame4.png").convert_alpha(), (160, 160)),
]

cavaleiro = pygame.image.load(f"assets/images/cavaleiro.png").convert_alpha()
cavaleiro = pygame.transform.scale(cavaleiro, (480, 480))

npcEldoria = pygame.image.load(f"assets/images/npcEldoria.png").convert_alpha()
npcEldoria = pygame.transform.scale(npcEldoria, (480, 480))

botaoOiEldoriaNpc = pygame.image.load(f"assets/images/botaoOiEldoriaNpc.png").convert_alpha()
botaoOiEldoriaNpc = pygame.transform.scale(botaoOiEldoriaNpc, (225, 225))

botaoOuroEldoriaNpc = pygame.image.load(f"assets/images/botaoOuroEldoriaNpc.png").convert_alpha()
botaoOuroEldoriaNpc = pygame.transform.scale(botaoOuroEldoriaNpc, (225, 225))

pocaovida = pygame.image.load("assets/images/pocaovida.png")
pocaovida = pygame.transform.scale(pocaovida, (250, 250))
pocaoforca = pygame.image.load("assets/images/pocaoforca.png")
pocaoforca = pygame.transform.scale(pocaoforca, (250, 250))
espada = pygame.image.load("assets/images/espada.png")
espada = pygame.transform.scale(espada, (250, 250))
cajado = pygame.image.load("assets/images/cajado.png")
cajado = pygame.transform.scale(cajado, (200, 200))

font = pygame.font.Font("assets/fonts/Minecraft.ttf", 16) 
fontBold = pygame.font.Font("assets/fonts/Minecraft.ttf", 22) 

backDuelo = pygame.image.load("assets/images/backDuelo.jpg")
backDuelo = pygame.transform.scale(backDuelo, (largura, altura))

nextage = pygame.image.load("assets/images/magoFrame1.png")
nextage = pygame.transform.scale(nextage, (250, 250))

aton = pygame.image.load("assets/images/aton.png")
aton = pygame.transform.scale(aton, (150, 150))

barraVida1de8 = pygame.image.load("assets/images/barraVida1de8.png")
barraVida1de8 = pygame.transform.scale(barraVida1de8, (600, 700))

barraVida2de8 = pygame.image.load("assets/images/barraVida2de8.png")
barraVida2de8 = pygame.transform.scale(barraVida2de8, (600, 700))

barraVida3de8 = pygame.image.load("assets/images/barraVida3de8.png")
barraVida3de8 = pygame.transform.scale(barraVida3de8, (600, 700))

barraVida4de8 = pygame.image.load("assets/images/barraVida4de8.png")    
barraVida4de8 = pygame.transform.scale(barraVida4de8, (600, 700))

barraVida5de8 = pygame.image.load("assets/images/barraVida5de8.png")
barraVida5de8 = pygame.transform.scale(barraVida5de8, (600, 700))

barraVida6de8 = pygame.image.load("assets/images/barraVida6de8.png")
barraVida6de8 = pygame.transform.scale(barraVida6de8, (600, 700))

barraVida7de8 = pygame.image.load("assets/images/barraVida7de8.png")
barraVida7de8 = pygame.transform.scale(barraVida7de8, (600, 700))

barraVida8de8 = pygame.image.load("assets/images/barraVida8de8.png")
barraVida8de8 = pygame.transform.scale(barraVida8de8, (600, 700))

barraVidaInimigo1de8 = pygame.image.load("assets/images/barraVidaInimigo1de8.png")
barraVidaInimigo1de8 = pygame.transform.scale(barraVidaInimigo1de8, (600, 700))

barraVidaInimigo2de8 = pygame.image.load("assets/images/barraVidaInimigo2de8.png")
barraVidaInimigo2de8 = pygame.transform.scale(barraVidaInimigo2de8, (600, 700))

barraVidaInimigo3de8 = pygame.image.load("assets/images/barraVidaInimigo3de8.png")
barraVidaInimigo3de8 = pygame.transform.scale(barraVidaInimigo3de8, (600, 700))

barraVidaInimigo4de8 = pygame.image.load("assets/images/barraVidaInimigo4de8.png")
barraVidaInimigo4de8 = pygame.transform.scale(barraVidaInimigo4de8, (600, 700))

barraVidaInimigo5de8 = pygame.image.load("assets/images/barraVidaInimigo5de8.png")
barraVidaInimigo5de8 = pygame.transform.scale(barraVidaInimigo5de8, (600, 700))

barraVidaInimigo6de8 = pygame.image.load("assets/images/barraVidaInimigo6de8.png")
barraVidaInimigo6de8 = pygame.transform.scale(barraVidaInimigo6de8, (600, 700))

barraVidaInimigo7de8 = pygame.image.load("assets/images/barraVidaInimigo7de8.png")
barraVidaInimigo7de8 = pygame.transform.scale(barraVidaInimigo7de8, (600, 700))

barraVidaInimigo8de8 = pygame.image.load("assets/images/barraVidaInimigo8de8.png")
barraVidaInimigo8de8 = pygame.transform.scale(barraVidaInimigo8de8, (600, 700))


def fade_out(velocidade=5, fundo = frame1):
    fade = pygame.Surface((largura, altura))
    fade.fill((0, 0, 0))
    for alpha in range(0, 255, velocidade):
        fade.set_alpha(alpha)
        screen.blit(fundo, (0, 0))
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(10)

click = False
