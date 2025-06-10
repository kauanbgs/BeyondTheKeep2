import pygame
import sys
from assets.screenConfig import screen, font, filtro_preto, vardannImagem1, vardannImagem2,vardannPatrulha,vardannVigia,vardannGnomo,avancouVardann
from assets.things import escrever_texto_animado
from resources.duel import duel

pygame.init()

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Estado para rastrear quais cenas o jogador já viu
estado_vardann = {
    "fez_patrulha": False,
    "fez_vigias": False,
    "fez_gerenciar": False
}

def desenhar_botao(texto, x, y, largura, altura, selecionado):
    cor_fundo = (60, 60, 60) if not selecionado else (255, 215, 0)
    cor_texto = BRANCO if not selecionado else PRETO
    pygame.draw.rect(screen, cor_fundo, (x, y, largura, altura), border_radius=10)
    pygame.draw.rect(screen, BRANCO, (x, y, largura, altura), 2, border_radius=10)
    txt = font.render(texto, True, cor_texto)
    rect = txt.get_rect(center=(x + largura // 2, y + altura // 2))
    screen.blit(txt, rect)

def intro_vardann():
    screen.blit(vardannImagem1, (0,0))
    screen.blit(filtro_preto, (0,0))
    pygame.display.update()
    escrever_texto_animado("Aton chega à majestosa fortaleza de Vardann.", font, BRANCO, 50, 50, 25, screen)
    pygame.time.wait(1200)
    escrever_texto_animado("Algo na corte está errado...", font, BRANCO, 50, 75, 25, screen)
    pygame.time.wait(2000)
    menu_vardann()

def menu_vardann():
    opcoes = ["Patrulhar os arredores", "Trabalhar com os vigias",
              "Gerenciar recursos do posto"]
    selecionado = 0
    rodando = True

    while rodando:
        screen.blit(vardannImagem2, (0,0))
        screen.blit(filtro_preto, (0,0))
        for i, texto in enumerate(opcoes):
            # Bloqueia "Gerenciar" até as outras duas feitas
            enabled = not (i == 2 and not (estado_vardann["fez_patrulha"] and estado_vardann["fez_vigias"]))
            cor = (150,150,150) if not enabled else None
            draw_sel = (i == selecionado) and enabled
            desenhar_botao(texto, 100, 150 + i*70, 600, 50, draw_sel)
            if not enabled:
                # overlay para indicar desativado
                s = pygame.Surface((600,50)); s.set_alpha(150); s.fill((0,0,0))
                screen.blit(s, (100, 150 + i*70))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key in [pygame.K_DOWN, pygame.K_UP]:
                    delta = 1 if evento.key == pygame.K_DOWN else -1
                    novo = (selecionado + delta) % len(opcoes)
                    # só seleciona se habilitado
                    if not (novo == 2 and not (estado_vardann["fez_patrulha"] and estado_vardann["fez_vigias"])):
                        selecionado = novo
                elif evento.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                    if selecionado == 0:
                        patrulha()
                    elif selecionado == 1:
                        vigias()
                    elif selecionado == 2:
                        gerenciar_recursos()
                    rodando = False

def patrulha():
    selected = 0
    opcoes = ["Seguir rastros", "Voltar sem investigar"]
    screen.blit(vardannPatrulha, (0,0))
    screen.blit(filtro_preto, (0,0))
    escrever_texto_animado("Na patrulha, Aton vê sinais de sabotagem nas muralhas.", font, BRANCO, 50, 50, 25, screen)
    pygame.time.wait(1000)

    rodando = True
    while rodando:
        screen.blit(vardannPatrulha, (0,0))
        screen.blit(filtro_preto, (0,0))
        for i, t in enumerate(opcoes):
            desenhar_botao(t, 100, 150 + i*70, 600, 50, i==selected)
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    selected = (selected+1)%len(opcoes)
                elif e.key == pygame.K_UP:
                    selected = (selected-1)%len(opcoes)
                elif e.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                    rodando = False
    estado_vardann["fez_patrulha"] = True
    if selected == 0:
        duelo_anao()
    else:
        duelo_gnomo()

def vigias():
    screen.blit(vardannVigia, (0,0))
    screen.blit(filtro_preto, (0,0))
    escrever_texto_animado("Aton ajuda os vigias e ouve rumores sobre o rei.", font, BRANCO, 50,50,25,screen)
    pygame.time.wait(2000)
    estado_vardann["fez_vigias"] = True
    final_vardann()

def duelo_gnomo():
    screen.blit(vardannGnomo, (0,0))
    screen.blit(filtro_preto, (0,0))
    escrever_texto_animado("Aton e os vigias enfrentam um gnomo infiltrado.", font, BRANCO,50,50,25,screen)
    pygame.time.wait(1200)
    escrever_texto_animado("Eles prevalecem e ganham confiança.", font,BRANCO,50,80,25,screen)
    pygame.time.wait(2000)
    final_vardann()

def duelo_anao():
    screen.blit(vardannGnomo, (0,0))
    screen.blit(filtro_preto, (0,0))
    escrever_texto_animado("Aton segue rastros e encontra um anão sabotador.", font, BRANCO,50,50,25,screen)
    pygame.time.wait(1200)
    escrever_texto_animado("Ele derrota o inimigo e ganha 6 moedas.", font,BRANCO,50,80,25,screen)
    pygame.time.wait(2000)
    final_vardann()

def gerenciar_recursos():
    screen.blit(vardannImagem1, (0,0))
    screen.blit(filtro_preto, (0,0))
    escrever_texto_animado("Aton acessa os registros de suprimentos.", font, BRANCO,50,50,25,screen)
    pygame.time.wait(1200)
    escrever_texto_animado("Descobre que o rei manipulou os numeros.", font,BRANCO,50,80,25,screen)
    pygame.time.wait(2000)
    escrever_texto_animado("Aton decide enfrentar o rei em busca de justica", font,BRANCO,50,100,25,screen)
    pygame.time.wait(2000)
    estado_vardann["fez_gerenciar"] = True
    final_batalha()

def final_vardann():
    screen.blit(avancouVardann, (0,0))
    screen.blit(filtro_preto, (0,0))    
    escrever_texto_animado("As missoes fortalecem a defesa de Vardann.", font,BRANCO,50,50,25,screen)
    pygame.time.wait(1500)
    menu_vardann()

def final_batalha():
    duel("CavaleiroTreino", 100, 100, 1, 1, "Cavaleiroframe1.png", "espada", 3)
    opcoes = ["Desmascarar o rei diante da corte", "Eliminar o rei em segredo"]
    selecionado = 0
    screen.fill(PRETO)
    escrever_texto_animado("Aton está perto de revelar a traição real...", font,BRANCO,50,50,25,screen)

    rodando = True
    while rodando:
        screen.fill(PRETO)
        for i, t in enumerate(opcoes):
            desenhar_botao(t,100,150 + i*70,600,50,i==selecionado)
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    selecionado = (selecionado+1)%len(opcoes)
                elif e.key == pygame.K_UP:
                    selecionado = (selecionado-1)%len(opcoes)
                elif e.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                    rodando = False

    if selecionado == 0:
        final_paz()
    else:
        final_vinganca()

def final_paz():
    screen.fill(PRETO)
    escrever_texto_animado("Aton revela ao conselho que o rei era traidor.", font,BRANCO,50,50,25,screen)
    escrever_texto_animado("O povo o aclama e um novo governo é formado.", font,BRANCO,50,80,25,screen)
    pygame.time.wait(2500)
    pygame.quit()
    sys.exit()

def final_vinganca():
    screen.fill(PRETO)
    escrever_texto_animado("Aton elimina o rei em silencio.", font,BRANCO,50,50,25,screen)
    escrever_texto_animado("Ele assume o trono para restaurar justiça.", font,BRANCO,50,80,25,screen)
    pygame.time.wait(2500)
    pygame.quit()
    sys.exit()

# Início
