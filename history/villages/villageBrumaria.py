import pygame
import sys
from assets.screenConfig import screen, font, brumariaImagem1, brumariaImagem2,brumariaFerreiro,brumariaGuardas,brumariaCastelo,brumariaMorador,brumariaJulgamento,brumariaFinal
from assets.things import escrever_texto_animado
from assets.config import Char
from assets.screenConfig import  filtro_preto

Char.name = "Nextage"

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
DOURADO = (255, 215, 0)
CINZA = (50, 50, 50)

pygame.init()

# Estados das missões e pistas
fez_mercador = False
fez_castelo = False
fez_treinamento = False
fez_moradores = False
fez_julgamento = False

tem_pista_mercador = False
tem_pista_moradores = False

def desenhar_botao(texto, fonte, cor_texto, cor_fundo, rect, tela):
    pygame.draw.rect(tela, cor_fundo, rect)
    texto_surf = fonte.render(texto, True, cor_texto)
    texto_rect = texto_surf.get_rect(center=rect.center)
    tela.blit(texto_surf, texto_rect)

def introBrumaria():
    screen.blit(brumariaImagem1, (0, 0))
    screen.blit(filtro_preto,(0,0))
    pygame.display.update()
    escrever_texto_animado(f"{Char.name} chega a fria e sombria Brumaria. Seus muros sao altos", font, BRANCO, 50, 50, 25, screen)
    pygame.time.wait(1000)
    escrever_texto_animado("O ceu encoberto e a tensao e palpavel.", font, BRANCO, 50, 75, 25, screen)
    pygame.time.wait(1000)
    escrever_texto_animado("A cidade aguarda respostas.", font, BRANCO, 50, 100, 25, screen)
    pygame.time.wait(2000)
    menuBrumaria()

def menuBrumaria():
    global fez_mercador, fez_castelo, fez_treinamento, fez_moradores, fez_julgamento
    global tem_pista_mercador, tem_pista_moradores

    opcoes = [
        "Falar com o mercador mais proximo",
        "Ir ao castelo falar com o Lorde",
        "Treinar com os soldados no campo",
        "Conversar com os moradores",
        "Ir ao Tribunal"
    ]

    selecionado = 0
    rodando = True

    largura_botao = 500
    altura_botao = 40
    margem = 10
    x_botao = 50
    y_inicial = 50

    while rodando:
        screen.fill(PRETO)
        screen.blit(brumariaImagem2, (0, 0))
        screen.blit(filtro_preto,(0,0))

        for i, texto in enumerate(opcoes):
            texto_display = texto
            if i == 0 and fez_mercador:
                texto_display += " - FEITO"
            elif i == 1 and fez_castelo:
                texto_display += " - FEITO"
            elif i == 2 and fez_treinamento:
                texto_display += " - FEITO"
            elif i == 3 and fez_moradores:
                texto_display += " - FEITO"
            if i == 4 and not (tem_pista_mercador and tem_pista_moradores):
                texto_display += " (nao recomendado sem pistas suficientes)"

            if i == selecionado:
                cor_fundo = DOURADO
                cor_texto = BRANCO
            else:
                cor_fundo = CINZA
                cor_texto = BRANCO

            rect = pygame.Rect(x_botao, y_inicial + i * (altura_botao + margem), largura_botao, altura_botao)
            desenhar_botao(texto_display, font, cor_texto, cor_fundo, rect, screen)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    selecionado = (selecionado + 1) % len(opcoes)
                elif evento.key == pygame.K_UP:
                    selecionado = (selecionado - 1) % len(opcoes)
                elif evento.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                    if selecionado == 0 and not fez_mercador:
                        falar_mercador()
                        fez_mercador = True
                    elif selecionado == 1 and not fez_castelo:
                        ir_castelo()
                        fez_castelo = True
                    elif selecionado == 2 and not fez_treinamento:
                        campo_treinamento()
                        fez_treinamento = True
                    elif selecionado == 3 and not fez_moradores:
                        falar_moradores()
                        fez_moradores = True
                    elif selecionado == 4 and not fez_julgamento:
                        if tem_pista_mercador and tem_pista_moradores:
                            tribunalBrumaria_func()
                            fez_julgamento = True
                            rodando = False
                        else:
                            escrever_texto_animado("Voce nao tem pistas suficientes...", font, BRANCO, 50, 300, 25, screen)
                            pygame.time.wait(1500)
                    break

def falar_mercador():

    global tem_pista_mercador
    screen.fill(PRETO)
    screen.blit(brumariaFerreiro, (0, 0))
    screen.blit(filtro_preto,(0,0))
    escrever_texto_animado(f"{Char.name} se entra na ferraria de um homem nervoso.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado('"Voce... e de Skalice, nao?"', font, BRANCO, 50, 80, 25, screen)
    escrever_texto_animado('"Ouvi passos apressados na noite do crime... Depois, silencio."', font, BRANCO, 50, 110, 25, screen)
    tem_pista_mercador = True
    pygame.time.wait(1500)

def ir_castelo():
    screen.fill(PRETO)
    screen.blit(brumariaCastelo, (0, 0))
    screen.blit(filtro_preto,(0,0))
    escrever_texto_animado("Guardas escoltam Aton até o salao principal do castelo.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado('"Preciso de olhos confiaveis esta noite. Vigie meus corredores."', font, BRANCO, 50, 80, 25, screen)
    escrever_texto_animado("Durante a patrulha, Aton ve uma sombra e percebe que armaduras sumiram.", font, BRANCO, 50, 110, 25, screen)
    pygame.time.wait(1500)

def campo_treinamento():
    screen.fill(PRETO)
    screen.blit(brumariaGuardas,(0,0))
    screen.blit(filtro_preto,(0,0))
    escrever_texto_animado("Soldados treinam sob o vento gelido.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado('"Mostre-nos como se luta, cidadao de Skalice!"', font, BRANCO, 50, 80, 25, screen)
    escrever_texto_animado(f"{Char.name} vence o treino e ganha respeito.", font, BRANCO, 50, 110, 25, screen)
    pygame.time.wait(1500)

def falar_moradores():
    global tem_pista_moradores
    screen.fill(PRETO)
    screen.blit(brumariaMorador, (0, 0))
    screen.blit(filtro_preto,(0,0))
    escrever_texto_animado(f"{Char.name} caminha pelas ruas e ouve relatos.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado('"Ouvi barulhos pesados... Era um guarda, com botas."', font, BRANCO, 50, 80, 25, screen)
    escrever_texto_animado('"Vi um guarda sair da muralha... Usava capa."', font, BRANCO, 50, 110, 25, screen)
    tem_pista_moradores = True
    pygame.time.wait(1500)

def tribunalBrumaria_func():
    opcoes = [
        "Um guarda assassinou um campones",
        "Um guarda roubou itens do estoque",
        "Um guarda não fez seu turno noturno"
    ]

    selecionado = 0
    rodando = True

    largura_botao = 550
    altura_botao = 35
    margem = 10
    x_botao = 50
    y_inicial = 150

    # Escreve texto de introdução antes do loop
    screen.fill(PRETO)
    screen.blit(brumariaJulgamento,(0,0))
    screen.blit(filtro_preto,(0,0))
    escrever_texto_animado("O salao do castelo está lotado. O Lorde quer respostas.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado('"O que ocorreu em Brumaria?"', font, BRANCO, 50, 80, 25, screen)

    while rodando:
        # Desenha os botões
        for i, texto in enumerate(opcoes):
            if i == selecionado:
                cor_fundo = DOURADO
                cor_texto = BRANCO
            else:
                cor_fundo = CINZA
                cor_texto = BRANCO

            rect = pygame.Rect(x_botao, y_inicial + i * (altura_botao + margem), largura_botao, altura_botao)
            desenhar_botao(texto, font, cor_texto, cor_fundo, rect, screen)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    selecionado = (selecionado + 1) % len(opcoes)
                elif evento.key == pygame.K_UP:
                    selecionado = (selecionado - 1) % len(opcoes)
                elif evento.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                    if selecionado == 1:
                        screen.fill(PRETO)
                        screen.blit(filtro_preto,(0,0))
                        escrever_texto_animado('"Exatamente. Esta apto para julgar."', font, BRANCO, 50, 150, 25, screen)
                        pygame.time.wait(1500)
                        julgamento_final()
                        rodando = False
                    else:
                        screen.fill(PRETO)
                        screen.blit(filtro_preto,(0,0))
                        escrever_texto_animado("O Lorde nao parece convencido com essa acusacao.", font, BRANCO, 50, 150, 25, screen)
                        pygame.time.wait(1500)
                        menuBrumaria()
                        rodando = False
                    break

def julgamento_final():
    screen.fill(PRETO)
    screen.blit(brumariaFinal,(0,0))
    screen.blit(filtro_preto,(0,0))
    escrever_texto_animado(f"{Char.name} conclui seu julgamento e traz paz para Brumaria.", font, BRANCO, 50, 50, 25, screen)
    pygame.time.wait(1000)
    escrever_texto_animado("Agora essa vila aparenta ter mais vida ",font,BRANCO,50,75,25,screen)
    pygame.time.wait(2500)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    introBrumaria()
