# import pygame
# import sys
# from assets.screenConfig import screen, font, praiaBack, filtro_preto, mainClock, mago_frames_parado, mago_frames, praia, espada, cajado, fundo, botaoPlay, botaoPlayHover, botaoSaves, botaoSavesHover, botaoQuit, botaoQuitHover, fade_out, play_rect, quit_rect, saves_rect, apostasBack, altura, largura
# from resources.apostas.apostaCavalo import menuApostaCavalos

# BRANCO = (255, 255, 255)
# PRETO = (0, 0, 0)
# CINZA = (50, 50, 50)
# MARROM = (160, 82, 45)

# def apostasMenu(): 
#     # Lista de opções
#   opcoes = [
#       "Corrida de Cavalos",
#       "Aposta de Dados",
#       # "Luta de Gladiadores"
#   ]

#   # Função para criar os botões
#   def criar_botoes(opcoes):
#       botoes = []
#       espacamento = 20
#       largura_botao = 400
#       altura_botao = 60
#       y_inicial = (altura - (len(opcoes) * (altura_botao + espacamento))) // 2

#       for i, texto in enumerate(opcoes):
#           x = (largura - largura_botao) // 2
#           y = y_inicial + i * (altura_botao + espacamento)
#           rect = pygame.Rect(x, y, largura_botao, altura_botao)
#           botoes.append((texto, rect))

#       return botoes


#   # Desenhar os botões
#   def desenhar_botoes(botoes):
#       for texto, rect in botoes:
#           pygame.draw.rect(screen, MARROM, rect, border_radius=8)
#           render = font.render(texto, True, BRANCO)
#           texto_rect = render.get_rect(center=rect.center)
#           screen.blit(render, texto_rect)


#   # Verificar clique nos botões
#   def checar_clique(botoes, pos):
#       for i, (_, rect) in enumerate(botoes):
#           if rect.collidepoint(pos):
#               return i
#       return None


#   # Criar botões
#   botoes = criar_botoes(opcoes)


#   # Loop principal
#   while True:
#       screen.blit(apostasBack, (0, 0))
#       screen.blit(filtro_preto, (0, 0))

#       for evento in pygame.event.get():
#           if evento.type == pygame.QUIT:
#               pygame.quit()
#               sys.exit()

#           if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
#               pos = pygame.mouse.get_pos()
#               opcao_clicada = checar_clique(botoes, pos)
#               if opcao_clicada is not None:
#                   if opcao_clicada == 0:
#                       menuApostaCavalos()
#                       # Aqui você pode chamar a função da corrida de cavalos
#                   # elif opcao_clicada == 1:
#                       # print("Entrou na Aposta de Dados")
#                   # elif opcao_clicada == 2:
#                       # print("Entrou na Luta de Gladiadores")

#       desenhar_botoes(botoes)

#       pygame.display.flip()
        
