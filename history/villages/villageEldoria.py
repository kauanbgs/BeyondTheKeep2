import pygame
import sys
import os
from assets.screenConfig import screen, font, praiaBack, filtro_preto, mainClock, mago_frames_parado, mago_frames, praia, espada, cajado, fundo, botaoPlay, botaoPlayHover, botaoSaves, botaoSavesHover, botaoQuit, botaoQuitHover, fade_out, play_rect, quit_rect, saves_rect, backFrames, casteloZoom3, casteloZoom2, casteloZoom1, casteloZoom0, casteloPortaZoom1, casteloPortaZoom0, casteloPortaZoom2, casteloPrincipal, fontBold, altura, largura, fundoEldoria, persoAndando
from assets.things import escrever_texto_animado
from assets.things import fade_transicao

# Importa o Char de outro diretório
from assets.config import Char


# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (200, 50, 50)
AZUL = (50, 50, 200)
AMARELO = (200, 200, 50)
CINZA = (180, 180, 180)



# def eldoria_introducao():
#     global introducao
#     pygame.display.update()
#     screen.blit(fundoEldoria, (0, 0))
#     mostrar_texto_animado("Aton caminha bravamente em direção à vila de Eudoria", 80, 80, fontBold, PRETO)
#     pygame.time.wait(1000)
#     mostrar_texto_animado("Após longas horas de caminhadas...", 80, 80, fontBold, PRETO)
#     pygame.time.wait(1000)
    
#     screen.blit(casteloZoom0, (0,0))
#     pygame.display.update()
#     mostrar_texto_animado("Aton já começa a sentir o ar frio da vila", 80, 80, fontBold, CINZA)
#     pygame.time.wait(1000)   
    

   
    # screen.blit(casteloPortaZoom1, (0,0))
    # pygame.display.update()
    # mostrar_texto_animado("Logo após sua chegada, um cavaleiro vem até seu encontro", 80, 80, fontBold, CINZA)
    # pygame.time.wait(1000)
    
    
    # screen.blit(casteloPrincipal, (0,0))
    # pygame.display.update()
    # mostrar_texto_animado(f"-Você é {Char.name} de Skalice ?", 80, 80, fontBold, AZUL)
    # pygame.time.wait(1000)

    # mostrar_texto_animado("-Sim, sou eu...", 80, 80, fontBold, BRANCO)
    # pygame.time.wait(1000)
    # mostrar_texto_animado("-Ótimo, ouvimos muito sobre você", 80, 80, fontBold, AZUL)
    # pygame.time.wait(1000)
    # mostrar_texto_animado("-Entre, esperávamos sua visita...", 80, 80, fontBold, AZUL)
    # pygame.time.wait(1000)
    # introducao = True



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

# def acao_explorar():
#     mostrar_texto_animado("Você acaba indo explorar dentro do castelo...", 60, 150, fontBold, CINZA, delay=20)
#     pygame.time.wait(800)
#     mostrar_texto_animado(f"No caminho {Char.name} acaba encontrando um dos cavaleiros", 20, 150, fontBold, CINZA, delay = 20)
#     pygame.time.wait(800)
#     mostrar_texto_animado(f"-Ei {Char.name},você acha de participar do nosso treino?", 60, 150,fontBold,CINZA, delay = 20)
#     pygame.time.wait(800)
    



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