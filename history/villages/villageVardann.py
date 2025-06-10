import pygame
import sys
from assets.screenConfig import screen, font, filtro_preto, vardannImagem1, vardannImagem2
from assets.things import escrever_texto_animado

pygame.init()

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

estado_vardann = {
    "escolheu": None,
    "patrulha_opcao": None,
    "final_decisao": None
}

def intro_vardann():
    screen.blit(vardannImagem1, (0, 0))
    screen.blit(filtro_preto,(0,0))
    pygame.display.update()
    escrever_texto_animado("Aton chega à imponente fortaleza de Vardann.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado("O ceu encoberto e a tensao e palpavel.", font, BRANCO, 50, 75, 25, screen)
    pygame.time.wait(1000)
    menu_vardann()

def menu_vardann():
    opcoes = [
        "Patrulhar os arredores",
        "Trabalhar com os vigias",
        "Gerenciar recursos do posto"
    ]
    selecionado = 0
    rodando = True

    while rodando:
        screen.blit(vardannImagem2, (0, 0))
        screen.blit(filtro_preto,(0,0))
        for i, texto in enumerate(opcoes):
            cor = BRANCO if i != selecionado else (255, 215, 0)
            pygame.draw.rect(screen, cor, (100, 150 + i*70, 600, 50), 2)
            escrever_texto_animado(texto, font, cor, 120, 160 + i*70, 25, screen)

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
                    estado_vardann["escolheu"] = selecionado
                    if selecionado == 0:
                        patrulha()
                    elif selecionado == 1:
                        vigias()
                    elif selecionado == 2:
                        gerenciar_recursos()
                    rodando = False

def patrulha():
    opcoes = ["Seguir os rastros", "Relatar aos guardas"]
    selecionado = 0
    screen.fill(PRETO)
    escrever_texto_animado("Durante a patrulha, Aton encontra rastros suspeitos...", font, BRANCO, 50, 50, 25, screen)
    pygame.time.wait(500)

    while True:
        for i, texto in enumerate(opcoes):
            cor = BRANCO if i != selecionado else (255, 215, 0)
            pygame.draw.rect(screen, cor, (100, 150 + i*70, 600, 50), 2)
            escrever_texto_animado(texto, font, cor, 120, 160 + i*70, 25, screen)

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
                    estado_vardann["patrulha_opcao"] = selecionado
                    if selecionado == 0:
                        duelo_anao()
                    else:
                        duelo_gnomo()
                    return

def duelo_gnomo():
    screen.fill(PRETO)
    escrever_texto_animado("Aton alerta os guardas e enfrenta um gnomo invasor.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado("Com coragem, vence o duelo e ganha a confiança da guarda.", font, BRANCO, 50, 80, 25, screen)
    pygame.time.wait(2000)
    final_vardann()

def duelo_anao():
    screen.fill(PRETO)
    escrever_texto_animado("Aton segue os rastros e encontra um anão hostil.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado("Após um duelo árduo, Aton sai vitorioso e recebe 6 moedas.", font, BRANCO, 50, 80, 25, screen)
    pygame.time.wait(2000)
    final_vardann()

def vigias():
    screen.fill(PRETO)
    escrever_texto_animado("Aton colabora com os vigias e reforça a segurança de Vardann.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado("Seu senso estratégico impressiona os superiores.", font, BRANCO, 50, 80, 25, screen)
    pygame.time.wait(2000)
    final_vardann()

def gerenciar_recursos():
    screen.fill(PRETO)
    escrever_texto_animado("Aton percebe que suprimentos estão desaparecendo.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado("Investigando, ele descobre um traidor: Blackhand.", font, BRANCO, 50, 80, 25, screen)
    pygame.time.wait(2000)
    final_batalha()

def final_vardann():
    screen.fill(PRETO)
    escrever_texto_animado("Vardann está a salvo graças a Aton.", font, BRANCO, 50, 50, 25, screen)
    pygame.time.wait(1500)
    final_batalha()

def final_batalha():
    opcoes = [
        "Voltar para Skalice com Blackhand",
        "Matar Blackhand e vingar seus amigos"
    ]
    selecionado = 0
    screen.fill(PRETO)
    escrever_texto_animado("Com Blackhand capturado, Aton encara sua decisão final.", font, BRANCO, 50, 50, 25, screen)

    while True:
        for i, texto in enumerate(opcoes):
            cor = BRANCO if i != selecionado else (255, 215, 0)
            pygame.draw.rect(screen, cor, (100, 150 + i*70, 600, 50), 2)
            escrever_texto_animado(texto, font, cor, 120, 160 + i*70, 25, screen)
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
                    if selecionado == 0:
                        final_paz()
                    else:
                        final_vinganca()
                    return

def final_paz():
    screen.fill(PRETO)
    escrever_texto_animado("Aton retorna a Skalice. É celebrado com um banquete.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado("Sua jornada o torna uma lenda viva entre os seus.", font, BRANCO, 50, 80, 25, screen)
    pygame.time.wait(2500)
    pygame.quit()
    sys.exit()

def final_vinganca():
    screen.fill(PRETO)
    escrever_texto_animado("Aton derrota Blackhand num duelo clandestino.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado("Depois, abandona as armas e vive como senhor sábio no campo.", font, BRANCO, 50, 80, 25, screen)
    pygame.time.wait(2500)
    pygame.quit()
    sys.exit()

# Para iniciar a vila Vardann
intro_vardann()
