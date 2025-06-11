import pygame
import sys
from assets.screenConfig import screen, font, filtro_preto, casteloZoom3, casteloZoom2, casteloZoom1, casteloZoom0, casteloPortaZoom1, casteloPortaZoom0, casteloPortaZoom2, casteloPrincipal, fontBold, botaoEldoriaInteragir, botaoEldoriaSair, botaoEldoriaExplorar, cavaleiro, npcEldoria, botaoOiEldoriaNpc, botaoOuroEldoriaNpc
from assets.things import escrever_texto_animado
from assets.things import fade_transicao
from resources.duel import duel
from assets.config import Char



# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (200, 50, 50)
AZUL = (50, 50, 200)
AMARELO = (200, 200, 50)
CINZA = (180, 180, 180)



def introEldoria():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    Char.veioEldoria = True
    screen.fill((0, 0, 0))
    pygame.display.update()
    pygame.mixer.music.unpause()
    escrever_texto_animado(f"{Char.Name} caminha bravamente em direcao ao castelo de Eldoria.", font, (255, 255 ,255), 50, 50, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1200)
    pygame.mixer.music.unpause()
    escrever_texto_animado("Apos horas de caminhada...", font, (255, 255, 255), 50, 75, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1200)
    pygame.mixer.music.unpause()
    escrever_texto_animado(f"{Char.Name} ja começa a sentir o ar frio do castelo.", font, (255 ,255, 255), 50, 100, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1200)


    fade_transicao(casteloZoom0, casteloZoom1)
    fade_transicao(casteloZoom1, casteloZoom2)
    fade_transicao(casteloZoom2, casteloZoom3)

    fade_transicao(casteloZoom3, casteloPortaZoom0)
    fade_transicao(casteloPortaZoom0, casteloPortaZoom1)
    fade_transicao(casteloPortaZoom1, casteloPortaZoom2)
    fade_transicao(casteloPortaZoom2, casteloPrincipal)

    screen.blit(filtro_preto, (0, 0))
    pygame.display.update()
    pygame.mixer.music.unpause()
    escrever_texto_animado("Logo apos sua chegada, um cavaleiro vem ate seu encontro", font, (255, 255, 255), 50, 50, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1000)
    pygame.mixer.music.unpause()
    escrever_texto_animado(f"CAVALEIRO: -Voce e {Char.Name} de Skalice ?", font, (255, 255, 255), 50, 75, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1000)
    pygame.mixer.music.unpause()
    escrever_texto_animado("-Sim, sou eu...", font, (255, 255, 255), 50, 100, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1000)
    pygame.mixer.music.unpause()
    escrever_texto_animado("CAVALEIRO: -Entre, esperavamos sua visita...", font, (255, 255, 255), 50, 125, 25, screen)
    pygame.mixer.music.pause()
    menuEldoria()

def menuEldoria():
    from menus.areas import explorar
    explorarEldoriaRect = pygame.Rect(325, 80, 150, 50)
    interagirEldoriaRect = pygame.Rect(325, 200, 150, 50)
    sairEldoriaRect = pygame.Rect(325, 320, 150, 50)
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if sairEldoriaRect.collidepoint(evento.pos):
                    explorar()
        screen.blit(casteloPrincipal, (0, 0))
        screen.blit(filtro_preto, (0, 0))

        screen.blit(botaoEldoriaExplorar, (275, -20))
        screen.blit(botaoEldoriaInteragir, (275, 100))
        screen.blit(botaoEldoriaSair, (275, 220))
        
        pos_mouse = pygame.mouse.get_pos()

        if explorarEldoriaRect.collidepoint(pos_mouse):
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                introDuelos()

        if interagirEldoriaRect.collidepoint(pos_mouse):
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if Char.conversouCarlinhoOuro:
                    screen.fill((0, 0, 0))
                    pygame.display.update()
                    escrever_texto_animado(f"{Char.Name} prometeu nao conversar com Carlinho.", font, (255, 255, 255), 275, 200, 25, screen)
                    pygame.time.wait(1000)
                    menuEldoria()
                interagirEldoria()

        if sairEldoriaRect.collidepoint(pos_mouse):
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                explorar()

        pygame.display.update()

def introDuelos():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    if Char.derrotouCavaleiroTreino:
        screen.fill((0, 0, 0))
        pygame.display.update()
        escrever_texto_animado(f"{Char.Name} já treinou com os cavaleiros.", font, (255, 255, 255), 275, 200, 25, screen)
        pygame.time.wait(1000)
        menuEldoria()
    from menus.areas import explorar
    screen.blit(casteloPrincipal, (0, 0))
    screen.blit(filtro_preto, (0, 0))
    screen.blit(cavaleiro, (0, 0))
    pygame.mixer.music.unpause()
    escrever_texto_animado("O que achou do castelo? hahaha!", font, (255, 255, 255), 375, 50, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1000)
    pygame.mixer.music.unpause()
    escrever_texto_animado("Nosso treinamento comeca em 60 minutos.", font, (255, 255, 255), 375, 75, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1500)
    pygame.mixer.music.unpause()
    escrever_texto_animado("Te espero la!", font, (255, 255, 255), 375, 100, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(3000)
    fixo = fontBold.render(" Minutos depois...", True, (255, 255, 255))
    for i in range(60):
        tempo = fontBold.render(f"{i}", True, (255, 255, 255))
        screen.blit(tempo, (310, 200))
        screen.blit(fixo, (335, 200))
        pygame.display.update()
        screen.fill((0,0,0))
        pygame.time.wait(60)
    duel("CavaleiroTreino", 40, 40, .5, .5, "Cavaleiroframe1.png", "espada", 5)
    Char.derrotouCavaleiroTreino = True
    explorar()


def interagirEldoria():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    rodando = True
    botaoOiRect = pygame.Rect(315, 290, 150, 45)
    botaoOuroRect = pygame.Rect(490, 290, 150, 45)
    screen.blit(casteloPrincipal, (0, 0))
    screen.blit(filtro_preto, (0, 0))
    screen.blit(npcEldoria, (0, 0))
    if not Char.conversouCarlinhoOi and not Char.conversouCarlinhoOuro:
        pygame.mixer.music.unpause()
        escrever_texto_animado("???: OLA!!!! BOM DIA!!! AAAAAAA!", font, (255, 255, 255), 375, 50, 25, screen)
        pygame.mixer.music.pause()
        pygame.time.wait(500)
        pygame.mixer.music.unpause()
        escrever_texto_animado("???: EU SOU O CARLINHO!", font, (255, 255, 255), 375, 75, 25, screen)
        pygame.mixer.music.pause()
        pygame.time.wait(1500)
        pygame.mixer.music.unpause()
        escrever_texto_animado("Carlinho: O QUE TE TRAZ AQUI?????", font, (255, 255, 255), 375, 100, 25, screen)
        pygame.mixer.music.pause()
        pygame.time.wait(3000)
    else:
        pygame.mixer.music.unpause()
        escrever_texto_animado("Carlinho: O QUE TE TRAZ AQUI?", font, (255, 255, 255), 375, 100, 25, screen)
        pygame.mixer.music.pause()
        pygame.time.wait(1500)
    pergunta = fontBold.render(f"O que {Char.Name} responde?", True, (255, 255, 255))
    while rodando:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(pergunta, (362, 225))
        screen.blit(botaoOiEldoriaNpc, (275, 200))
        screen.blit(botaoOuroEldoriaNpc, (450, 200))

        pos_mouse = pygame.mouse.get_pos()

        if botaoOiRect.collidepoint(pos_mouse):
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                rodando = False
                conversaCarlinhoOi()

        if botaoOuroRect.collidepoint(pos_mouse):
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                rodando = False
                conversaCarlinhoOuro()

        pygame.display.update()
    

def conversaCarlinhoOi():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    if Char.conversouCarlinhoOi:
        screen.fill((0, 0, 0))
        pygame.display.update()
        escrever_texto_animado(f"{Char.Name} ja fez essa interacao.", font, (255, 255, 255), 275, 200, 25, screen)
        pygame.time.wait(1000)
        interagirEldoria()
    Char.conversouCarlinhoOi = True
    screen.blit(casteloPrincipal, (0, 0))
    screen.blit(filtro_preto, (0, 0))
    screen.blit(npcEldoria, (0, 0))
    pygame.mixer.music.unpause()
    escrever_texto_animado("Carlinho: CALTHERA! PERIGO!!!", font, (255, 255, 255), 375, 50, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(500)
    pygame.mixer.music.unpause()
    escrever_texto_animado("Carlinho: CUIDADO POR LA.", font, (255, 255, 255), 375, 75, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(2000)
    interagirEldoria()

def conversaCarlinhoOuro():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    if Char.conversouCarlinhoOuro:
        screen.fill((0, 0, 0))
        pygame.display.update()
        escrever_texto_animado(f"{Char.Name} ja fez essa interacao.", font, (255, 255, 255), 275, 200, 25, screen)
        pygame.time.wait(1000)
        interagirEldoria()
    Char.conversouCarlinhoOuro = True
    screen.blit(casteloPrincipal, (0, 0))
    screen.blit(filtro_preto, (0, 0))
    screen.blit(npcEldoria, (0, 0))
    pygame.mixer.music.unpause()
    escrever_texto_animado("Carlinho: VOCE QUER OURO?? EU TENHO OURO!!", font, (255, 255, 255), 300, 50, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(500)
    pygame.mixer.music.unpause()
    escrever_texto_animado("Carlinho: MAS TUDO TEM UM PRECO.", font, (255, 255, 255), 300, 75, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(2000)
    pygame.mixer.music.unpause()
    escrever_texto_animado("Carlinho: NUNCA MAIS FALE COMIGO", font, (255, 255, 255), 300, 100, 25, screen)
    escrever_texto_animado("E EM TROCA, PEGUE 3 MOEDAS.", font, (255, 255, 255), 300, 115, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(2000)
    Char.coins += 3
    screen.fill((0, 0, 0))
    pygame.display.update()
    escrever_texto_animado(f"{Char.Name} ganhou 3 moedas.", font, (255, 255, 255), 275, 200, 25, screen)
    pygame.time.wait(1000)
    menuEldoria()

