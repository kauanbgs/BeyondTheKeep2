# import pygame
# import math
# import sys

# <<<<<<< HEAD
# pygame.init()

# WIDTH, HEIGHT = 800, 400
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Duelos Mágicos")
# =======
# def duel():
#     from assets.config import Char
#     import random
# >>>>>>> 6df707ee969f364ae0b69945220cdc464f24c348

# clock = pygame.time.Clock()

# # Imagens
# player_img = pygame.image.load("assets/images/magoParado.gif").convert_alpha()
# player_img = pygame.transform.scale(player_img, (150, 150))

# enemy_img = pygame.image.load("assets/images/magoParado.gif").convert_alpha()
# enemy_img = pygame.transform.scale(enemy_img, (150, 150))

# <<<<<<< HEAD
# background = pygame.image.load("assets/images/background.jpg").convert()
# background = pygame.transform.scale(background, (WIDTH, HEIGHT))
# =======
#     mago_frames = [
#     pygame.transform.scale(pygame.image.load("assets/images/magoFrame1.png").convert_alpha(), (128, 128)),
#     pygame.transform.scale(pygame.image.load("assets/images/magoFrame2.png").convert_alpha(), (128, 128)),
#     pygame.transform.scale(pygame.image.load("assets/images/magoFrame3.png").convert_alpha(), (128, 128)),
#     pygame.transform.scale(pygame.image.load("assets/images/magoFrame4.png").convert_alpha(), (128, 128)),
# ]

#     mago_frames_parado = [
#     pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe1.png").convert_alpha(), (128, 128)),
#     pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe2.png").convert_alpha(), (128, 128)),
#     pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe3.png").convert_alpha(), (128, 128)),
#     pygame.transform.scale(pygame.image.load(f"assets/images/magoParadoframe4.png").convert_alpha(), (128, 128)),
#     ]
# >>>>>>> 6df707ee969f364ae0b69945220cdc464f24c348

# player_x, player_y = 200, HEIGHT - 190
# enemy_x, enemy_y = WIDTH - 200, HEIGHT - 190

# player_speed = 5

# class Magia:
#     def __init__(self, x, y, alvo_x, alvo_y, cor, dano, tipo='reta'):
#         self.x = x
#         self.y = y
#         self.alvo_x = alvo_x
#         self.alvo_y = alvo_y
#         self.cor = cor
#         self.dano = dano
#         self.tipo = tipo
#         self.fase = 'subindo' if tipo == 'ender_eye' else 'andando'
#         self.velocidade = 5

#     def mover(self):
#         if self.tipo == 'ender_eye':
#             if self.fase == 'subindo':
#                 self.y -= self.velocidade
#                 if self.y <= self.alvo_y - 100:
#                     self.fase = 'seguindo'
#             elif self.fase == 'seguindo':
#                 dx = self.alvo_x - self.x
#                 dy = self.alvo_y - self.y
#                 dist = math.hypot(dx, dy)
#                 if dist != 0:
#                     self.x += (dx / dist) * self.velocidade
#                     self.y += (dy / dist) * self.velocidade
#         elif self.tipo == 'reta':
#             dx = self.alvo_x - self.x
#             dy = self.alvo_y - self.y
#             dist = math.hypot(dx, dy)
#             if dist != 0:
#                 self.x += (dx / dist) * self.velocidade
#                 self.y += (dy / dist) * self.velocidade

# <<<<<<< HEAD
#     def desenhar(self, screen):
#         pygame.draw.circle(screen, self.cor, (int(self.x), int(self.y)), 8)

#     def saiu_da_tela(self, largura, altura):
#         return self.x < 0 or self.x > largura or self.y < 0 or self.y > altura
# =======
#     max_hp = 100

#     enemy_x = WIDTH - 200
#     enemy_y = HEIGHT - 110
#     enemy_hp = 100

#     # Velocidade
#     player_speed = 5
#     # Controle da animação
#     current_frame = 0
#     frame_timer = 0
#     frame_delay = 10  # troca de imagem a cada 10 frames
# >>>>>>> 6df707ee969f364ae0b69945220cdc464f24c348

# # Variáveis do jogo
# magias = []
# magia_selecionada = 0  # índice da magia selecionada
# magias_disponiveis = [
#     {'nome': 'Olho Etéreo', 'cor': (0, 0, 255), 'dano': 20, 'tipo': 'ender_eye'},
#     {'nome': 'Bola de Fogo', 'cor': (255, 0, 0), 'dano': 30, 'tipo': 'reta'}
# ]

# modo_selecao = False  # Se está no menu/modal de seleção

# running = True
# while running:
#     clock.tick(60)

# <<<<<<< HEAD
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# =======
#     def draw_health_bar(surface, x, y, w, h, hp, max_hp, color):
#         pygame.draw.rect(surface, (50, 50, 50), (x, y, w, h))  # fundo
#         hp_width = int(w * (hp / max_hp))
#         pygame.draw.rect(surface, color, (x, y, hp_width, h))  # vida
#         pygame.draw.rect(surface, (0, 0, 0), (x, y, w, h), 2)  # borda

#     # Loop principal
#     running = True
#     while running:
#         clock.tick(60)
#         screen.fill((255, 255, 255))  # Limpa a tela
# >>>>>>> 6df707ee969f364ae0b69945220cdc464f24c348

#         if modo_selecao:
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_UP:
#                     magia_selecionada = (magia_selecionada - 1) % len(magias_disponiveis)
#                 elif event.key == pygame.K_DOWN:
#                     magia_selecionada = (magia_selecionada + 1) % len(magias_disponiveis)
#                 elif event.key == pygame.K_RETURN:
#                     modo_selecao = False
#         else:
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_m:
#                     modo_selecao = True
#                 elif event.key == pygame.K_SPACE:
#                     if len(magias) == 0:
#                         magia_info = magias_disponiveis[magia_selecionada]
#                         magias.append(Magia(player_x + 75, player_y + 50, enemy_x + 75, enemy_y + 50,
#                                             magia_info['cor'], magia_info['dano'], magia_info['tipo']))

#                 # Movimento e animação
#         keys = pygame.key.get_pressed()
#         moving = False

#         if keys[pygame.K_q]:
#             Char.health = max(0, Char.health - 1)
#         if keys[pygame.K_e]:
#             enemy_hp = max(0, enemy_hp - 1)
#         if keys[pygame.K_d]:
#             player_x += player_speed
#             moving = True
#         if keys[pygame.K_a]:
#             player_x -= player_speed
#             moving = True

#         # Atualizar frame
#         frame_timer += 1
#         if frame_timer >= frame_delay:
#             frame_timer = 0
#             current_frame += 1

#         # Decide qual animação usar
#         if moving:
#             frame_list = mago_frames
#         else:
#             frame_list = mago_frames_parado

#         current_frame = current_frame % len(frame_list)

#         # Desenhar tudo
#         screen.blit(background, (0, 0))  # fundo
#         screen.blit(frame_list[current_frame], (player_x, player_y))  # player animado
#         screen.blit(enemy_img, (enemy_x, enemy_y))  # inimigo

#         # Barra de vida do jogador
#         draw_health_bar(screen, 50, 20, 200, 20, Char.health, max_hp, (0, 200, 0))

#         # Barra de vida do inimigo (lado direito)
#         draw_health_bar(screen, WIDTH - 250, 20, 200, 20, enemy_hp, max_hp, (200, 0, 0))

#         pygame.display.flip()

# <<<<<<< HEAD
#     # Atualiza magias
#     for magia in magias[:]:
#         magia.mover()
# =======
# >>>>>>> 6df707ee969f364ae0b69945220cdc464f24c348

#         if (enemy_x < magia.x < enemy_x + 150) and (enemy_y < magia.y < enemy_y + 150):
#             print(f"Acertou com {magia.tipo}!")
#             magias.remove(magia)

#         elif magia.saiu_da_tela(WIDTH, HEIGHT):
#             magias.remove(magia)

#     # Desenho
#     screen.blit(background, (0, 0))
#     screen.blit(player_img, (player_x, player_y))
#     screen.blit(enemy_img, (enemy_x, enemy_y))

#     for magia in magias:
#         magia.desenhar(screen)

#     # Se estiver no modo seleção, desenha o menu modal
#     if modo_selecao:
#         # Fundo semi-transparente
#         s = pygame.Surface((WIDTH, HEIGHT))
#         s.set_alpha(180)
#         s.fill((0, 0, 0))
#         screen.blit(s, (0, 0))

#         fonte = pygame.font.SysFont(None, 40)
#         texto_titulo = fonte.render("Escolha a magia", True, (255, 255, 255))
#         screen.blit(texto_titulo, (WIDTH // 2 - texto_titulo.get_width() // 2, 50))

#         # Lista de magias disponíveis
#         for i, magia in enumerate(magias_disponiveis):
#             cor = (255, 255, 0) if i == magia_selecionada else (255, 255, 255)
#             texto = fonte.render(magia['nome'], True, cor)
#             screen.blit(texto, (WIDTH // 2 - texto.get_width() // 2, 120 + i * 50))

#     pygame.display.flip()

# pygame.quit()
# sys.exit()
