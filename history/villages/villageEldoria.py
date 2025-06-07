import pygame
import sys
import os
from assets.screenConfig import screen, font, praiaBack, filtro_preto, mainClock, mago_frames_parado, mago_frames, praia, espada, cajado, fundo, botaoPlay, botaoPlayHover, botaoSaves, botaoSavesHover, botaoQuit, botaoQuitHover, fade_out, play_rect, quit_rect, saves_rect, backFrames, casteloZoom3, casteloZoom2, casteloZoom1, casteloZoom0, casteloPortaZoom1, casteloPortaZoom0, casteloPortaZoom2, casteloPrincipal, fontBold, altura, largura, fundoEldoria, persoAndando, botaoEldoriaInteragir, botaoEldoriaSair, botaoEldoriaExplorar
from assets.things import escrever_texto_animado
from assets.things import fade_transicao
from menus.areas import explorar
from assets.config import Char


# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (200, 50, 50)
AZUL = (50, 50, 200)
AMARELO = (200, 200, 50)
CINZA = (180, 180, 180)



def introEldoria():
    screen.blit(persoAndando, (0, 0))
    pygame.display.update()
    escrever_texto_animado("Aton caminha bravamente em direcao ao castelo de Eldoria.", font, (0, 0, 0), 50, 50, 25, screen)
    pygame.time.wait(1200)
    escrever_texto_animado("Apos horas de caminhada...", font, (0, 0 ,0), 50, 75, 25, screen)
    pygame.time.wait(1200)
    escrever_texto_animado("Aton ja começa a sentir o ar frio do castelo.", font, (0, 0 ,0), 50, 100, 25, screen)
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
    escrever_texto_animado("Logo apos sua chegada, um cavaleiro vem ate seu encontro", font, (255, 255, 255), 50, 50, 25, screen)
    pygame.time.wait(1000)
    escrever_texto_animado(f"CAVALEIRO: -Voce e {Char.Name} de Skalice ?", font, (255, 255, 255), 50, 75, 25, screen)
    pygame.time.wait(1000)
    escrever_texto_animado("-Sim, sou eu...", font, (255, 255, 255), 50, 100, 25, screen)
    pygame.time.wait(1000)
    escrever_texto_animado("CAVALEIRO: -Entre, esperavamos sua visita...", font, (255, 255, 255), 50, 125, 25, screen)
    menuEldoria()

def menuEldoria():
    explorarEldoriaRect = pygame.Rect(325, 80, 150, 50)
    interagirEldoriaRect = pygame.Rect(325, 200, 150, 50)
    sairEldoriaRect = pygame.Rect(325, 320, 150, 50)
    rodando = True
    selecionado_inventario = False
    selecionado_explorar = False

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
        
        pygame.display.update()

# def acao_aldeoes():
#     mostrar_texto_animado("Você conversa com os aldeões e ouve rumores de uma criatura nas montanhas.", 60, 380, font, CINZA, delay=20)
#     pygame.time.wait(800)

# def executar_acao(acao):
#     if acao == "sair":
#         pygame.quit()
#         sys.exit()
#     elif acao == "explorar":
#         acao_explorar()
#     elif acao == "aldeoes":
#         acao_aldeoes()

# # Mostra introdução antes de entrar no loop
# eldoria_introducao()

# # Loop principal
# rodando = True
# while rodando:
#     screen.blit(casteloPrincipal, (0, 0))

#     if introducao:
#         desenhar_botoes()
#         desenhar_instrucao()

#     pygame.display.update()

#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             rodando = False
#         elif introducao and evento.type == pygame.KEYDOWN:
#             if evento.key == pygame.K_q:
#                 executar_acao("sair")
#             elif evento.key == pygame.K_UP:
#                 botao_selecionado = (botao_selecionado - 1) % len(botoes)
#             elif evento.key == pygame.K_DOWN:
#                 botao_selecionado = (botao_selecionado + 1) % len(botoes)
#             elif evento.key == pygame.K_RETURN:
#                 executar_acao(botoes[botao_selecionado]["acao"])
#         elif introducao and evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
#             acao = checar_clique_botoes(evento.pos)
#             if acao:
#                 executar_acao(acao)

#     mainClock.tick(60)

# pygame.quit()
# sys.exit()