import pygame
import sys
from assets.screenConfig import screen, font, filtro_preto, vardannImagem1, vardannImagem2, modeloBotao3, modeloBotao3Hover, setaPraTras, fontBold, paredeSangueVardann, vardannVigia
from assets.things import escrever_texto_animado
from resources.duel import duel
from assets.config import Char
from resources.final import final



BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)


def intro_vardann():
    Char.veioVardann = True
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    screen.blit(vardannImagem1, (0,0))
    screen.blit(filtro_preto, (0,0))
    pygame.display.update()
    pygame.mixer.music.unpause()
    if Char.language == "ptbr":
        escrever_texto_animado(f"{Char.Name} chega a majestosa fortaleza de Vardann.", font, BRANCO, 50, 50, 25, screen)
    else:
        escrever_texto_animado(f"{Char.Name} arrives at the majestic fortress of Vardann.", font, BRANCO, 50, 50, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1200)
    pygame.mixer.music.unpause()
    if Char.language == "ptbr":
        escrever_texto_animado("Algo na corte esta errado...", font, BRANCO, 50, 75, 25, screen)
    else:
        escrever_texto_animado("Something is wrong in the court...", font, BRANCO, 50, 75, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(2000)
    menu_vardann()

def menu_vardann():
    voltarVardann_rect = pygame.Rect(25, 25, 100, 100)
    opcao1_rect = pygame.Rect(245, 30, 300, 80)
    opcao2_rect = pygame.Rect(245, 130, 300, 80)
    opcao3_rect = pygame.Rect(245, 230, 300, 80)
    opcao4_rect = pygame.Rect(245, 330, 300, 80)
    if Char.language == "ptbr":
        opcao1 = fontBold.render("Patrulhar Arredores", True, (255, 255, 255))
        opcao2 = fontBold.render("Vigiar o Posto", True, (255, 255, 255))
        opcao3 = fontBold.render("Gerenciar Recursos", True, (255, 255, 255))
    else:
        opcao1 = fontBold.render("Patrol Surroundings", True, (255, 255, 255))
        opcao2 = fontBold.render("Watch the Post", True, (255, 255, 255))
        opcao3 = fontBold.render("Manage Resources", True, (255, 255, 255))
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if opcao1_rect.collidepoint(evento.pos):
                    patrulha()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if opcao2_rect.collidepoint(evento.pos):
                    vigias()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if opcao3_rect.collidepoint(evento.pos):
                    gerenciar_recursos()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if voltarVardann_rect.collidepoint(evento.pos):
                    from menus.areas import explorar
                    explorar()

        screen.blit(vardannImagem2, (0, 0))
        screen.blit(filtro_preto, (0, 0))
        screen.blit(modeloBotao3, (150, -130))
        screen.blit(modeloBotao3, (150, -30))
        screen.blit(modeloBotao3, (150, 70))
        screen.blit(setaPraTras, (25, 25))

        

        mouse_pos = pygame.mouse.get_pos()
        if opcao1_rect.collidepoint(mouse_pos):
            screen.blit(modeloBotao3Hover, (150, -130))
        if opcao2_rect.collidepoint(mouse_pos):
            screen.blit(modeloBotao3Hover, (150, -30))
        if opcao3_rect.collidepoint(mouse_pos):
            screen.blit(modeloBotao3Hover, (150, 70))
        screen.blit(opcao1, (275, 55))
        screen.blit(opcao2, (275, 156))
        screen.blit(opcao3, (275, 255))
        pygame.display.update()

def patrulha():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    if Char.fezPatrulha:
        screen.fill((0, 0, 0))
        pygame.display.update()
        if Char.language == "ptbr":
            escrever_texto_animado(f"{Char.Name} já patrulhou os arredores de Vardann.", font, BRANCO, 275, 200, 25, screen)
        else:
            escrever_texto_animado(f"{Char.Name} has already patrolled the surroundings of Vardann.", font, BRANCO, 275, 200, 25, screen)
        pygame.time.wait(1000)
        menu_vardann()
    Char.fezPatrulha = True
    screen.blit(paredeSangueVardann, (0, 0))
    screen.blit(filtro_preto, (0, 0))
    pygame.mixer.music.unpause()
    if Char.language == "ptbr":
        escrever_texto_animado(f"{Char.Name} patrulha os arredores de Vardann.", font, BRANCO, 50, 50, 25, screen)
    else:
        escrever_texto_animado(f"{Char.Name} patrols the surroundings of Vardann.", font, BRANCO, 50, 50, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1200)
    pygame.mixer.music.unpause()
    if Char.language == "ptbr":
        escrever_texto_animado("Ele encontra sinais de sabotagem nas muralhas.", font, BRANCO, 50, 80, 25, screen)
    else:
        escrever_texto_animado("He finds signs of sabotage on the walls.", font, BRANCO, 50, 80, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1000)
    pygame.mixer.music.unpause()
    if Char.language == "ptbr":
        escrever_texto_animado(f"{Char.Name} deve decidir como agir:", font, BRANCO, 50, 100, 25, screen)
    else:
        escrever_texto_animado(f"{Char.Name} must decide how to act:", font, BRANCO, 50, 100, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(2000)
    opcao1_rect = pygame.Rect(245, 30, 300, 80)
    opcao2_rect = pygame.Rect(245, 130, 300, 80)
    if Char.language == "ptbr":
        opcao1 = fontBold.render("Seguir rastros", True, (255, 255, 255))
        opcao2 = fontBold.render("Correr de medo", True, (255, 255, 255))
    else:
        opcao1 = fontBold.render("Follow tracks", True, (255, 255, 255))
        opcao2 = fontBold.render("Run in fear", True, (255, 255, 255))
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if opcao1_rect.collidepoint(evento.pos):
                    screen.blit(paredeSangueVardann, (0, 0))
                    screen.blit(filtro_preto, (0, 0))
                    pygame.display.update()
                    pygame.mixer.music.unpause()
                    if Char.language == "ptbr":
                        escrever_texto_animado(f"{Char.Name} segue os rastros e encontra um goblin sabotador.", font, BRANCO, 50, 50, 25, screen)
                    else:
                        escrever_texto_animado(f"{Char.Name} follows the tracks and finds a sabotaging goblin.", font, BRANCO, 50, 50, 25, screen)
                    pygame.mixer.music.pause()
                    pygame.time.wait(1200)
                    duel("Goblin", 50, 50, 0.7, 0.7, "Cavaleiroframe1.png", "mago", 5)
                    menu_vardann()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if opcao2_rect.collidepoint(evento.pos):
                    screen.blit(paredeSangueVardann, (0, 0))
                    screen.blit(filtro_preto, (0, 0))
                    pygame.display.update()
                    pygame.mixer.music.unpause()
                    if Char.language == "ptbr":
                        escrever_texto_animado(f"{Char.Name} corre de medo, mas um cavaleiro furioso o encontra.", font, BRANCO, 50, 50, 25, screen)
                    else:
                        escrever_texto_animado(f"{Char.Name} runs in fear, but an angry knight finds him.", font, BRANCO, 50, 50, 25, screen)
                    pygame.mixer.music.pause()
                    pygame.time.wait(1200)
                    duel("Cavaleiro", 50, 50, 0.7, 0.7, "Cavaleiroframe1.png", "espada", 5)
                    menu_vardann()
                    

        screen.blit(paredeSangueVardann, (0, 0))
        screen.blit(filtro_preto, (0, 0))
        screen.blit(modeloBotao3, (150, -130))
        screen.blit(modeloBotao3, (150, -30))

        

        mouse_pos = pygame.mouse.get_pos()
        if opcao1_rect.collidepoint(mouse_pos):
            screen.blit(modeloBotao3Hover, (150, -130))
        if opcao2_rect.collidepoint(mouse_pos):
            screen.blit(modeloBotao3Hover, (150, -30))
        screen.blit(opcao1, (275, 55))
        screen.blit(opcao2, (275, 156))
        pygame.display.update()

def vigias():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    if Char.fezVigiasVardann:
        screen.fill((0, 0, 0))
        pygame.display.update()
        pygame.mixer.music.unpause()
        if Char.language == "ptbr":
            escrever_texto_animado(f"{Char.Name} já ajudou os vigias de Vardann.", font, BRANCO, 275, 200, 25, screen)
        else:
            escrever_texto_animado(f"{Char.Name} has already helped the Vardann guards.", font, BRANCO, 275, 200, 25, screen)
        pygame.mixer.music.pause()
        pygame.time.wait(1000)
        menu_vardann()
    Char.fezVigiasVardann = True
    screen.blit(vardannVigia, (0,0))
    screen.blit(filtro_preto, (0,0))
    pygame.mixer.music.unpause()
    if Char.language == "ptbr":
        escrever_texto_animado(f"{Char.Name} ajuda os vigias e ouve rumores sobre o rei.", font, BRANCO, 50,50,25,screen)
    else:
        escrever_texto_animado(f"{Char.Name} helps the guards and hears rumors about the king.", font, BRANCO, 50,50,25,screen)
    pygame.mixer.music.pause()
    pygame.time.wait(2000)
    menu_vardann()



def gerenciar_recursos():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    if not Char.fezVigiasVardann and not Char.fezPatrulha:
        screen.fill((0, 0, 0))
        pygame.display.update()
        if Char.language == "ptbr":
            escrever_texto_animado(f"{Char.Name} precisa fazer outras opcoes.", font, BRANCO, 275, 200, 25, screen)
        else:
            escrever_texto_animado(f"{Char.Name} needs to make other things.", font, BRANCO, 275, 200, 25, screen)
        pygame.time.wait(1000)
        menu_vardann()
    if Char.fezGerenciar:
        screen.fill((0, 0, 0))
        pygame.display.update()
        if Char.language == "ptbr":
            escrever_texto_animado(f"{Char.Name} ja gerenciou os recursos de Vardann.", font, BRANCO, 275, 200, 25, screen)
        else:
            escrever_texto_animado(f"{Char.Name} has already managed the resources of Vardann.", font, BRANCO, 275, 200, 25, screen)
        pygame.time.wait(1000)
        menu_vardann()
    Char.fezGerenciar = True
    screen.blit(vardannImagem1, (0,0))
    screen.blit(filtro_preto, (0,0))
    pygame.mixer.music.unpause()
    if Char.language == "ptbr":
        escrever_texto_animado(f"{Char.Name} acessa os registros de suprimentos.", font, BRANCO,50,50,25,screen)
    else:
        escrever_texto_animado(f"{Char.Name} accesses the supply records.", font, BRANCO,50,50,25,screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1200)
    pygame.mixer.music.unpause()
    if Char.language == "ptbr":
        escrever_texto_animado("Descobre que o rei manipulou os numeros.", font,BRANCO,50,80,25,screen)
    else:
        escrever_texto_animado("Discovers that the king manipulated the numbers.", font,BRANCO,50,80,25,screen)
    pygame.mixer.music.pause()
    pygame.time.wait(2000)
    pygame.mixer.music.unpause()
    if Char.language == "ptbr":
        escrever_texto_animado(f"{Char.Name} decide enfrentar o rei em busca de justica", font,BRANCO,50,100,25,screen)
    else:
        escrever_texto_animado(f"{Char.Name} decides to confront the king in search of justice", font,BRANCO,50,100,25,screen)
    pygame.mixer.music.pause()
    pygame.time.wait(2000)
    duel("Rei", 50, 50, 0.3, 0.3, "Cavaleiroframe1.png", "mago", 10)
    final_batalha()
    



def final_batalha():
    Char.fezVardann = True
    opcao1_rect = pygame.Rect(245, 30, 300, 80)
    opcao2_rect = pygame.Rect(245, 130, 300, 80)
    if Char.language == "ptbr":
        opcao1 = fontBold.render("Desmascarar o rei", True, (255, 255, 255))
        opcao2 = fontBold.render("Eliminar o rei", True, (255, 255, 255))
    else:
        opcao1 = fontBold.render("Unmask the king", True, (255, 255, 255))
        opcao2 = fontBold.render("Eliminate the king", True, (255, 255, 255))
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if opcao1_rect.collidepoint(evento.pos):
                    final_paz()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if opcao2_rect.collidepoint(evento.pos):
                    final_vinganca()


        screen.blit(vardannImagem1, (0, 0))
        screen.blit(filtro_preto, (0, 0))
        screen.blit(modeloBotao3, (150, -130))
        screen.blit(modeloBotao3, (150, -30))

        

        mouse_pos = pygame.mouse.get_pos()
        if opcao1_rect.collidepoint(mouse_pos):
            screen.blit(modeloBotao3Hover, (150, -130))
        if opcao2_rect.collidepoint(mouse_pos):
            screen.blit(modeloBotao3Hover, (150, -30))
        screen.blit(opcao1, (275, 55))
        screen.blit(opcao2, (275, 156))
        pygame.display.update()
def final_paz():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    screen.fill(PRETO)
    pygame.mixer.music.unpause()
    if Char.language == "ptbr":
        escrever_texto_animado(f"{Char.Name} revela ao conselho que o rei era traidor.", font,BRANCO,50,50,25,screen)
        escrever_texto_animado("O povo o aclama e um novo governo é formado.", font,BRANCO,50,80,25,screen)
    else:
        escrever_texto_animado(f"{Char.Name} reveals to the council that the king was a traitor.", font,BRANCO,50,50,25,screen)
        escrever_texto_animado("The people acclaim him and a new government is formed.", font,BRANCO,50,80,25,screen)
    pygame.mixer.music.unpause()
    pygame.time.wait(2500)
    final()

def final_vinganca():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    screen.fill(PRETO)
    pygame.mixer.music.unpause()
    if Char.language == "ptbr":
        escrever_texto_animado(f"{Char.Name} elimina o rei em silencio.", font,BRANCO,50,50,25,screen)
        escrever_texto_animado("Ele assume o trono para restaurar justiça.", font,BRANCO,50,80,25,screen)
    else:
        escrever_texto_animado(f"{Char.Name} eliminates the king in silence.", font,BRANCO,50,50,25,screen)
        escrever_texto_animado("He takes the throne to restore justice.", font,BRANCO,50,80,25,screen)
    pygame.mixer.music.pause()
    pygame.time.wait(2500)
    final()

