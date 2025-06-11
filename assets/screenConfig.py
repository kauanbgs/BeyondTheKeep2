
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

botaoConfig = pygame.image.load("assets/images/botaoConfig.png")
botaoConfig = pygame.transform.scale(botaoConfig, (450, 450))

botaoQuit = pygame.image.load("assets/images/botaoQuit.png")
botaoQuit = pygame.transform.scale(botaoQuit, (450, 450))


botaoPlayHover = pygame.image.load("assets/images/botaoPlayHover.png")
botaoPlayHover = pygame.transform.scale(botaoPlayHover, (450, 450))

botaoConfigHover = pygame.image.load("assets/images/botaoConfigHover.png")
botaoConfigHover = pygame.transform.scale(botaoConfigHover, (450, 450))

botaoQuitHover = pygame.image.load("assets/images/botaoQuitHover.png")
botaoQuitHover = pygame.transform.scale(botaoQuitHover, (450, 450))

play_rect = pygame.Rect(160 + 125, -160 + 175, 200, 100)
saves_rect = pygame.Rect(0 + 125, -160 + 175, 200, 100)
quit_rect = pygame.Rect(320 + 125, -160 + 175, 200, 100)

praia = pygame.image.load("assets/images/praia.jpg")
praia = pygame.transform.scale(praia, (largura, altura))

praiaBack = pygame.image.load("assets/images/praiaBack.png")
praiaBack = pygame.transform.scale(praiaBack, (largura, altura))

backFrame1 = pygame.image.load("assets/images/backFrame1.jpg")
backFrame1 = pygame.transform.scale(backFrame1, (largura, altura))

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

backMarcacaoTaverna1 = pygame.image.load("assets/images/backMarcacaoTaverna1.png")
backMarcacaoTaverna1 = pygame.transform.scale(backMarcacaoTaverna1, (largura, altura))

backMarcacaoTaverna2 = pygame.image.load("assets/images/backMarcacaoTaverna2.png")
backMarcacaoTaverna2 = pygame.transform.scale(backMarcacaoTaverna2, (largura, altura))

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

botaoEldoriaLeft = pygame.image.load("assets/images/botaoEldoriaLeft.png")
botaoEldoriaLeft = pygame.transform.scale(botaoEldoriaLeft, (250, 250))

botaoEldoriaExplore = pygame.image.load("assets/images/botaoEldoriaExplore.png")
botaoEldoriaExplore = pygame.transform.scale(botaoEldoriaExplore, (250, 250))

botaoEldoriaInteract = pygame.image.load("assets/images/botaoEldoriaInteract.png")
botaoEldoriaInteract = pygame.transform.scale(botaoEldoriaInteract, (250, 250))

fundoEldoria = pygame.image.load("assets/images/fundoEldoria.png")
fundoEldoria = pygame.transform.scale(fundoEldoria, (largura, altura))

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

pocaovida2 = pygame.image.load("assets/images/pocaovida.png")
pocaovida2 = pygame.transform.scale(pocaovida2, (100, 100))
pocaoforca2 = pygame.image.load("assets/images/pocaoforca.png")
pocaoforca2 = pygame.transform.scale(pocaoforca2, (100, 100))

espada = pygame.image.load("assets/images/espada.png")
espada = pygame.transform.scale(espada, (250, 250))
cajado = pygame.image.load("assets/images/cajado.png")
cajado = pygame.transform.scale(cajado, (200, 200))

font = pygame.font.Font("assets/fonts/Minecraft.ttf", 16) 
fontBold = pygame.font.Font("assets/fonts/Minecraft.ttf", 22) 
fontBoldGiga = pygame.font.Font("assets/fonts/Minecraft.ttf", 75) 

backDuelo = pygame.image.load("assets/images/backDuelo.jpg")
backDuelo = pygame.transform.scale(backDuelo, (largura, altura))

nextage = pygame.image.load("assets/images/magoFrame1.png")
nextage = pygame.transform.scale(nextage, (250, 250))

aton = pygame.image.load("assets/images/aton.png")
aton = pygame.transform.scale(aton, (250, 250))

atonEspada3 = pygame.image.load("assets/images/atonEspada3.png")
atonEspada3 = pygame.transform.scale(atonEspada3, (250, 250))

atonEspada4 = pygame.image.load("assets/images/atonEspada4.png")
atonEspada4 = pygame.transform.scale(atonEspada4, (250, 250))

atonEspada5 = pygame.image.load("assets/images/atonEspada5.png")
atonEspada5 = pygame.transform.scale(atonEspada5, (250, 250))

atonEspada6 = pygame.image.load("assets/images/atonEspada6.png")
atonEspada6 = pygame.transform.scale(atonEspada6, (250, 250))

cavaleiroFrame1 = pygame.image.load("assets/images/Cavaleiroframe1.png")
cavaleiroFrame1 = pygame.transform.scale(cavaleiroFrame1, (500, 500))

cavaleiroFrame2 = pygame.image.load("assets/images/Cavaleiroframe2.png")
cavaleiroFrame2 = pygame.transform.scale(cavaleiroFrame2, (500, 500))

cavaleiroFrame3 = pygame.image.load("assets/images/Cavaleiroframe3.png") 
cavaleiroFrame3 = pygame.transform.scale(cavaleiroFrame3, (500, 500))

cavaleiroFrame4 = pygame.image.load("assets/images/Cavaleiroframe4.png")
cavaleiroFrame4 = pygame.transform.scale(cavaleiroFrame4, (500, 500))

cavaleiroFrame5 = pygame.image.load("assets/images/Cavaleiroframe5.png")
cavaleiroFrame5 = pygame.transform.scale(cavaleiroFrame5, (500, 500))

cavaleiroFrame6 = pygame.image.load("assets/images/Cavaleiroframe6.png")
cavaleiroFrame6 = pygame.transform.scale(cavaleiroFrame6, (500, 500))

goblinMago = pygame.image.load("assets/images/goblinMago.png")

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

rei = pygame.image.load("assets/images/rei.png")
rei = pygame.transform.scale(rei, (200, 200))

botaoTaverna = pygame.image.load("assets/images/botaoTaverna.png")
botaoTaverna = pygame.transform.scale(botaoTaverna, (330, 250))

botaoTavernaHover = pygame.image.load("assets/images/botaoTavernaHover.png")
botaoTavernaHover = pygame.transform.scale(botaoTavernaHover, (330, 250))

fundoTaverna = pygame.image.load("assets/images/fundoTaverna.jpeg")
fundoTaverna = pygame.transform.scale(fundoTaverna, (largura, altura))

cavaleiroEspada1 = pygame.image.load("assets/images/cavaleiroEspada1.png")
cavaleiroEspada1 = pygame.transform.scale(cavaleiroEspada1, (180, 180))

cavaleiroEspada2 = pygame.image.load("assets/images/cavaleiroEspada2.png")
cavaleiroEspada2 = pygame.transform.scale(cavaleiroEspada2, (180, 180))

brumariaImagem1 = pygame.image.load("assets/images/Brumaria1.png")
brumariaImagem1 = pygame.transform.scale(brumariaImagem1,(largura,altura))

brumariaImagem2 = pygame.image.load("assets/images/Brumaria2.png")
brumariaImagem2 = pygame.transform.scale(brumariaImagem2,(largura,altura))

brumariaFerreiro = pygame.image.load("assets/images/BrumariaFerreiro.png")
brumariaFerreiro = pygame.transform.scale(brumariaFerreiro,(largura,altura))

brumariaGuardas = pygame.image.load("assets/images/BrumariaTreino.png")
brumariaGuardas = pygame.transform.scale(brumariaGuardas,(largura,altura))

brumariaCastelo = pygame.image.load("assets/images/BrumariaCastelo.png")
brumariaCastelo = pygame.transform.scale(brumariaCastelo,(largura,altura))

brumariaMorador = pygame.image.load("assets/images/BrumariaMorador.png")
brumariaMorador = pygame.transform.scale(brumariaMorador, (largura,altura))

brumariaJulgamento = pygame.image.load("assets/images/BrumariaJulgamento.png")
brumariaJulgamento = pygame.transform.scale(brumariaJulgamento, (largura,altura))

brumariaFinal = pygame.image.load("assets/images/BrumariaFinal.png")
brumariaFinal = pygame.transform.scale(brumariaFinal, (largura,altura))

vardannImagem1 = pygame.image.load("assets/images/Vardann1.png")
vardannImagem1 = pygame.transform.scale(vardannImagem1, (largura,altura))

vardannImagem2 = pygame.image.load("assets/images/Vardann2.png")
vardannImagem2 = pygame.transform.scale(vardannImagem2, (largura,altura))

vardannVigia = pygame.image.load("assets/images/VardannVigia.png")
vardannVigia = pygame.transform.scale(vardannVigia, (largura,altura))

setaPraTras = pygame.image.load("assets/images/setaPraTras.png")
setaPraTras = pygame.transform.scale(setaPraTras, (100, 100))

molduraInventario = pygame.image.load("assets/images/molduraInventario.png")
molduraInventario = pygame.transform.scale(molduraInventario, (90, 90))

modeloBotao = pygame.image.load("assets/images/modeloBotao.png")
modeloBotao = pygame.transform.scale(modeloBotao, (500, 400))

modeloBotaoHover = pygame.image.load("assets/images/modeloBotaoHover.png")
modeloBotaoHover = pygame.transform.scale(modeloBotaoHover, (500, 400))

modeloBotao2 = pygame.image.load("assets/images/modeloBotao2.png")
modeloBotao2 = pygame.transform.scale(modeloBotao2, (500, 400))

modeloBotao2Hover = pygame.image.load("assets/images/modeloBotao2Hover.png")
modeloBotao2Hover = pygame.transform.scale(modeloBotao2Hover, (500, 400))

modeloBotao3 = pygame.image.load("assets/images/modeloBotao3.png")
modeloBotao3 = pygame.transform.scale(modeloBotao3, (500, 400))

modeloBotao3Hover = pygame.image.load("assets/images/modeloBotao3Hover.png")
modeloBotao3Hover = pygame.transform.scale(modeloBotao3Hover, (500, 400))

paredeSangueVardann = pygame.image.load("assets/images/paredeSangueVardann.jpg")
paredeSangueVardann = pygame.transform.scale(paredeSangueVardann, (largura, altura))

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
