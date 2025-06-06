# import pygame
# import sys
# import random
# from assets.config import Char
# from history.introduction import intro
# from assets.screenConfig import screen, font, praiaBack, filtro_preto, mainClock, mago_frames_parado, mago_frames, praia, espada, cajado, fundo, botaoPlay, botaoPlayHover, botaoSaves, botaoSavesHover, botaoQuit, botaoQuitHover, fade_out, play_rect, quit_rect, saves_rect, largura, altura


# def menuApostaCavalos(): 

#   font_pequena = pygame.font.Font("assets/fonts/Minecraft.ttf", 16)
#   font_media = pygame.font.Font("assets/fonts/Minecraft.ttf", 28)

#   BRANCO = (255, 255, 255)
#   MARROM = (139, 69, 19)
#   AZUL = (70, 130, 200)
#   AZUL_CLARO = (100, 170, 250)
#   VERDE = (0, 200, 0)
#   VERDE_CLARO = (0, 255, 0)
#   CINZA = (50, 50, 50)

#   valor_aposta = 10
#   cavalo_selecionado = None

#   # Lista base de cavalos e suas chances
#   todos_cavalos = {
#       "Relâmpago": 50,
#       "Tempestade": 25,
#       "Ventania": 5,
#       "Furacão": 15,
#       "Trovão": 10,
#       "Vento Sul": 20,
#       "Chuva de Prata": 30
#   }

#   # Número de cavalos que vão aparecer no menu
#   quantidade_cavalos_menu = 3

#   def gerar_cavalos_aleatorios():
#       # Seleciona aleatoriamente 3 cavalos da lista base, sem repetição
#       selecionados = random.sample(list(todos_cavalos.items()), quantidade_cavalos_menu)
#       # Cria um dicionário com esses cavalos
#       return dict(selecionados)

#   def criar_botoes_cavalos(cavalos):
#       botoes = []
#       espacamento = 20
#       largura_botao = 400
#       altura_botao = 50
#       y_inicial = 100

#       nomes = list(cavalos.keys())

#       for i, nome in enumerate(nomes):
#           x = (largura - largura_botao) // 2
#           y = y_inicial + i * (altura_botao + espacamento)
#           rect = pygame.Rect(x, y, largura_botao, altura_botao)
#           botoes.append((nome, rect))
#       return botoes

#   def criar_botoes_aposta():
#       menos = pygame.Rect(200, 320, 50, 50)
#       mais = pygame.Rect(550, 320, 50, 50)
#       iniciar = pygame.Rect((largura - 300) // 2, 380, 300, 60)
#       return menos, mais, iniciar

#   def desenhar_tela(cavalos, botoes_cavalos, menos, mais, iniciar):
#       screen.fill((30, 30, 30))

#       titulo = font_media.render("Menu de Aposta - Cavalos", True, BRANCO)
#       screen.blit(titulo, ((largura - titulo.get_width()) // 2, 20))

#       texto_saldo = font_pequena.render(f"Saldo: ${Char.coins}", True, BRANCO)
#       screen.blit(texto_saldo, (30, 30))

#       mouse_pos = pygame.mouse.get_pos()
#       for i, (nome, rect) in enumerate(botoes_cavalos):
#           if cavalo_selecionado == i:
#               cor = VERDE
#           elif rect.collidepoint(mouse_pos):
#               cor = AZUL_CLARO
#           else:
#               cor = AZUL

#           pygame.draw.rect(screen, cor, rect, border_radius=8)
#           pygame.draw.rect(screen, BRANCO, rect, 2, border_radius=8)

#           texto = font_pequena.render(nome, True, BRANCO)
#           screen.blit(texto, texto.get_rect(center=rect.center))

#       pygame.draw.rect(screen, CINZA, menos, border_radius=8)
#       pygame.draw.rect(screen, CINZA, mais, border_radius=8)

#       menos_texto = font_media.render("-", True, BRANCO)
#       mais_texto = font_media.render("+", True, BRANCO)
#       screen.blit(menos_texto, menos_texto.get_rect(center=menos.center))
#       screen.blit(mais_texto, mais_texto.get_rect(center=mais.center))

#       texto_aposta = font_media.render(f"Aposta: ${valor_aposta}", True, BRANCO)
#       screen.blit(texto_aposta, ((largura - texto_aposta.get_width()) // 2, 330))

#       cor_iniciar = VERDE_CLARO if iniciar.collidepoint(mouse_pos) else VERDE
#       pygame.draw.rect(screen, cor_iniciar, iniciar, border_radius=8)
#       pygame.draw.rect(screen, BRANCO, iniciar, 2, border_radius=8)

#       texto_iniciar = font_pequena.render("Iniciar Corrida", True, BRANCO)
#       screen.blit(texto_iniciar, texto_iniciar.get_rect(center=iniciar.center))

#   def iniciar_corrida(cavalos):
#       if cavalo_selecionado is None:
#           print("Selecione um cavalo!")
#           return

#       if valor_aposta > Char.coins:
#           print("Saldo insuficiente!")
#           return

#       nomes = list(cavalos.keys())
#       chances = list(cavalos.values())

#       vencedor = random.choices(nomes, weights=chances, k=1)[0]

#       print(f"O cavalo vencedor é: {vencedor}")

#       selecionado = nomes[cavalo_selecionado]

#       if selecionado == vencedor:
#           ganho = valor_aposta * 2
#           Char.coins += ganho
#           print(f"Você ganhou ${ganho}!")
#       else:
#           Char.coins -= valor_aposta
#           print(f"Você perdeu ${valor_aposta}!")

#   cavalos_atuais = gerar_cavalos_aleatorios()
#   botoes_cavalos = criar_botoes_cavalos(cavalos_atuais)
#   menos, mais, iniciar = criar_botoes_aposta()

#   click = False

#   while True:
#       desenhar_tela(cavalos_atuais, botoes_cavalos, menos, mais, iniciar)

#       for event in pygame.event.get():
#           if event.type == pygame.QUIT:
#               pygame.quit()
#               sys.exit()

#           if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#               pos = pygame.mouse.get_pos()

#               for i, (_, rect) in enumerate(botoes_cavalos):
#                   if rect.collidepoint(pos):
#                       cavalo_selecionado = i

#               if menos.collidepoint(pos):
#                   if valor_aposta > 1:
#                       valor_aposta -= 1

#               if mais.collidepoint(pos):
#                   if valor_aposta + 1 <= Char.coins:
#                       valor_aposta += 1

#               if iniciar.collidepoint(pos):
#                   iniciar_corrida(cavalos_atuais)
#                   # Depois de corrida, gera novos cavalos pro próximo jogo:
#                   cavalos_atuais = gerar_cavalos_aleatorios()
#                   botoes_cavalos = criar_botoes_cavalos(cavalos_atuais)
#                   cavalo_selecionado = None

#       pygame.display.flip()
#       pygame.time.Clock().tick(60)
