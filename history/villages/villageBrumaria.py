import pygame
import sys
from assets.screenConfig import screen, font,fontBold, brumariaImagem2,brumariaFerreiro,brumariaCastelo,brumariaMorador,brumariaJulgamento,brumariaFinal, modeloBotao, modeloBotaoHover, modeloBotao2, modeloBotao2Hover, setaPraTras
from assets.things import escrever_texto_animado
from assets.config import Char
from assets.screenConfig import  filtro_preto


# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
DOURADO = (255, 215, 0)
CINZA = (50, 50, 50)

def introBrumaria():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    Char.veioBrumaria = True
    screen.fill((0, 0, 0))
    pygame.display.update()
    pygame.mixer.music.unpause()
    escrever_texto_animado(f"{Char.Name} chega a fria e sombria Brumaria. Seus muros sao altos,", font, BRANCO, 50, 50, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1000)
    pygame.mixer.music.unpause()
    escrever_texto_animado("O ceu encoberto e a tensao e palpavel.", font, BRANCO, 50, 75, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1000)
    pygame.mixer.music.unpause()
    escrever_texto_animado("A cidade aguarda respostas.", font, BRANCO, 50, 100, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(2000)
    menuBrumaria()


def menuBrumaria():
    voltarBrumaria_rect = pygame.Rect(25, 25, 100, 100)
    opcao1_rect = pygame.Rect(245, 30, 300, 80)
    opcao2_rect = pygame.Rect(245, 130, 300, 80)
    opcao3_rect = pygame.Rect(245, 230, 300, 80)
    opcao4_rect = pygame.Rect(245, 330, 300, 80)
    opcao1 = fontBold.render("Falar com o mercador", True, (255, 255, 255))
    opcao2 = fontBold.render("Ir ao castelo", True, (255, 255, 255))
    opcao3 = fontBold.render("Falar com moradores", True, (255, 255, 255))
    opcao4 = fontBold.render("Ir ao Tribunal", True, (255, 255, 255))
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if opcao1_rect.collidepoint(evento.pos):
                    if not Char.fez_mercador:
                        falar_mercador()
                    else:
                        screen.fill((0, 0, 0))
                        escrever_texto_animado(f"{Char.Name} ja falou com o mercador.", font, BRANCO, 50, 50, 25, screen)
                        pygame.time.wait(1500)

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if opcao2_rect.collidepoint(evento.pos):
                    if not Char.fez_castelo:
                        ir_castelo()
                    else:
                        screen.fill((0, 0, 0))
                        escrever_texto_animado(f"{Char.Name} ja foi ao castelo.", font, BRANCO, 50, 50, 25, screen)
                        pygame.time.wait(1500)

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if opcao3_rect.collidepoint(evento.pos):
                    if not Char.falou_moradores:
                        falar_moradores()
                    else:
                        screen.fill((0, 0, 0))
                        escrever_texto_animado(f"{Char.Name} ja falou com os moradores.", font, BRANCO, 50, 50, 25, screen)
                        pygame.time.wait(1500)
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if opcao4_rect.collidepoint(evento.pos):
                    if Char.fez_castelo and Char.falou_moradores and Char.fez_mercador:
                        tribunalBrumaria()
                    else:
                        screen.fill((0, 0, 0))
                        escrever_texto_animado(f"{Char.Name} nao coletou todas as dicas disponiveis.", font, BRANCO, 50, 50, 25, screen)
                        pygame.time.wait(1500)
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if voltarBrumaria_rect.collidepoint(evento.pos):
                    from menus.areas import explorar
                    explorar()

        screen.blit(brumariaImagem2, (0, 0))
        screen.blit(filtro_preto, (0, 0))
        screen.blit(modeloBotao, (150, -130))
        screen.blit(modeloBotao, (150, -30))
        screen.blit(modeloBotao, (150, 70))
        screen.blit(modeloBotao, (150, 170))
        screen.blit(setaPraTras, (25, 25))

        

        mouse_pos = pygame.mouse.get_pos()
        if opcao1_rect.collidepoint(mouse_pos):
            screen.blit(modeloBotaoHover, (150, -130))
        if opcao2_rect.collidepoint(mouse_pos):
            screen.blit(modeloBotaoHover, (150, -30))
        if opcao3_rect.collidepoint(mouse_pos):
            screen.blit(modeloBotaoHover, (150, 70))
        if opcao4_rect.collidepoint(mouse_pos):
            screen.blit(modeloBotaoHover, (150, 170))
        screen.blit(opcao1, (275, 55))
        screen.blit(opcao2, (275, 156))
        screen.blit(opcao3, (275, 255))
        screen.blit(opcao4, (275, 355))
        pygame.display.update()
    

def falar_mercador():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    Char.fez_mercador = True
    screen.fill(PRETO)
    screen.blit(brumariaFerreiro, (0, 0))
    screen.blit(filtro_preto,(0,0))
    pygame.mixer.music.unpause()
    escrever_texto_animado(f"{Char.Name} entra na ferraria de um homem nervoso.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado('"Voce... e de Skalice, nao?"', font, BRANCO, 50, 80, 25, screen)
    escrever_texto_animado('"Ouvi passos apressados na noite do crime... Depois, silencio."', font, BRANCO, 50, 110, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1500)
    Char.tem_pista_mercador = True
    pygame.time.wait(1500)

def ir_castelo():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    Char.fez_castelo = True
    screen.fill(PRETO)
    screen.blit(brumariaCastelo, (0, 0))
    screen.blit(filtro_preto,(0,0))
    pygame.mixer.music.unpause()
    escrever_texto_animado("Guardas escoltam Aton até o salao principal do castelo.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado('"Preciso de olhos confiaveis esta noite. Vigie meus corredores."', font, BRANCO, 50, 80, 25, screen)
    escrever_texto_animado("Durante a patrulha, Aton ve uma sombra e percebe que armaduras sumiram.", font, BRANCO, 50, 110, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1500)

def falar_moradores():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    Char.falou_moradores = True
    screen.fill(PRETO)
    screen.blit(brumariaMorador, (0, 0))
    screen.blit(filtro_preto,(0,0))
    pygame.mixer.music.unpause()
    escrever_texto_animado(f"{Char.Name} caminha pelas ruas e ouve relatos.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado('"Ouvi barulhos pesados... Era um guarda, com botas."', font, BRANCO, 50, 80, 25, screen)
    escrever_texto_animado('"Vi um guarda sair da muralha... Usava capa."', font, BRANCO, 50, 110, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1500)
    
def tribunalBrumaria():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    opcao1_rect = pygame.Rect(245, 30, 300, 80)
    opcao2_rect = pygame.Rect(245, 130, 300, 80)
    opcao3_rect = pygame.Rect(245, 230, 300, 80)
    opcao1 = fontBold.render("Guarda matou alguem", True, (255, 255, 255))
    opcao2 = fontBold.render("Guarda roubou itens", True, (255, 255, 255))
    opcao3 = fontBold.render("Guarda nao fez turno", True, (255, 255, 255))
    rodando = True
    screen.blit(brumariaJulgamento,(0,0))
    screen.blit(filtro_preto,(0,0))
    pygame.mixer.music.unpause()
    escrever_texto_animado("O salao do castelo esta lotado. O Lorde quer respostas.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado('"O que ocorreu em Brumaria?"', font, BRANCO, 50, 80, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1500)
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if opcao1_rect.collidepoint(evento.pos):
                    screen.fill(PRETO)
                    screen.blit(filtro_preto,(0,0))
                    pygame.mixer.music.unpause()
                    escrever_texto_animado("O Lorde nao parece convencido com essa acusacao.", font, BRANCO, 50, 150, 25, screen)
                    pygame.mixer.music.pause()
                    pygame.time.wait(1500)
                    menuBrumaria()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if opcao2_rect.collidepoint(evento.pos):
                    screen.fill(PRETO)
                    screen.blit(filtro_preto,(0,0))
                    pygame.mixer.music.unpause()
                    escrever_texto_animado(f'"Exatamente, {Char.Name}! PRENDAM-O!"', font, BRANCO, 50, 150, 25, screen)
                    pygame.mixer.music.pause()
                    pygame.time.wait(2500)
                    julgamento_final()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if opcao3_rect.collidepoint(evento.pos):
                    screen.fill(PRETO)
                    screen.blit(filtro_preto,(0,0))
                    pygame.mixer.music.unpause()
                    escrever_texto_animado("O Lorde nao parece convencido com essa acusacao.", font, BRANCO, 50, 150, 25, screen)
                    pygame.mixer.music.pause()
                    pygame.time.wait(1500)
                    menuBrumaria()


        screen.blit(brumariaJulgamento, (0, 0))
        screen.blit(filtro_preto, (0, 0))
        screen.blit(modeloBotao2, (150, -130))
        screen.blit(modeloBotao2, (150, -30))
        screen.blit(modeloBotao2, (150, 70))

        

        mouse_pos = pygame.mouse.get_pos()
        if opcao1_rect.collidepoint(mouse_pos):
            screen.blit(modeloBotao2Hover, (150, -130))
        if opcao2_rect.collidepoint(mouse_pos):
            screen.blit(modeloBotao2Hover, (150, -30))
        if opcao3_rect.collidepoint(mouse_pos):
            screen.blit(modeloBotao2Hover, (150, 70))
        screen.blit(opcao1, (275, 55))
        screen.blit(opcao2, (275, 156))
        screen.blit(opcao3, (275, 255))
        pygame.display.update()


def julgamento_final():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/tecladoDigitando.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.15)
    pygame.mixer.music.pause()
    from menus.gameMenu import gameMenu
    Char.fez_brumaria = True
    screen.fill(PRETO)
    screen.blit(brumariaFinal,(0,0))
    screen.blit(filtro_preto,(0,0))
    pygame.mixer.music.unpause()
    escrever_texto_animado(f"{Char.Name} conclui seu julgamento e traz paz para Brumaria.", font, BRANCO, 50, 50, 25, screen)
    pygame.mixer.music.pause()
    pygame.time.wait(1000)
    pygame.mixer.music.unpause()
    escrever_texto_animado("Agora essa vila aparenta ter mais vida. ",font,BRANCO,50,75,25,screen)
    pygame.mixer.music.pause()
    pygame.time.wait(2500)
    gameMenu()

