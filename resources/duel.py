import pygame
import math
import sys
from assets.config import Char
from assets.screenConfig import screen, font, praiaBack, filtro_preto, mainClock, mago_frames_parado, mago_frames, praia, espada, cajado, fundo, botaoPlay, botaoPlayHover, botaoSaves, botaoSavesHover, botaoQuit, botaoQuitHover, fade_out, play_rect, quit_rect, saves_rect, casteloZoom3, casteloZoom2, casteloZoom1, casteloZoom0, casteloPortaZoom1, casteloPortaZoom0, casteloPortaZoom2, casteloPrincipal, backDuelo, aton, nextage, barraVida1de8, barraVida2de8, barraVida3de8, barraVida4de8, barraVida5de8, barraVida6de8, barraVida7de8, barraVida8de8, barraVidaInimigo1de8, barraVidaInimigo2de8, barraVidaInimigo3de8, barraVidaInimigo4de8, barraVidaInimigo5de8, barraVidaInimigo6de8, barraVidaInimigo7de8, barraVidaInimigo8de8

class Projetil:
    def __init__(self, x, y, velocidade):
        self.x = x
        self.y = y
        self.velocidade = velocidade
        self.raio = 6
        self.cor = (75, 150, 255)  # vermelho
        self.ativo = True

    def mover(self):
        self.x += self.velocidade
        if self.x > 800:  # saiu da tela
            self.ativo = False

    def desenhar(self, tela):
        pygame.draw.circle(tela, self.cor, (int(self.x), int(self.y)), self.raio)


def duel(enemyName, enemyHealth, enemyAttack, enemyDefense, enemyImage):
    rodando = True
    projeteis = []

    if Char.classplayer == 1:
        playerImage = aton
    else:
        playerImage = nextage

    player_x = 100
    player_y = 250
    player_speed = 1
    while rodando:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return
                if evento.key == pygame.K_SPACE and len(projeteis) == 0:
                    novo_proj = Projetil(player_x + 170, player_y + 100, 4)
                    projeteis.append(novo_proj)
                if evento.key == pygame.K_t:
                    Char.health -= 5

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player_x += player_speed
        if keys[pygame.K_a]:
            player_x -= player_speed


        
            
        # Desenhar fundo e jogador
        screen.blit(backDuelo, (0, 0))
        screen.blit(filtro_preto, (0, 0))
        screen.blit(playerImage, (player_x, player_y))
        screen.blit(aton, (player_x + 500, player_y + 60))

        # Atualizar e desenhar projéteis
        for p in projeteis:
            p.mover()
            p.desenhar(screen)

        # Remover projéteis fora da tela
        projeteis = [p for p in projeteis if p.ativo]

        if Char.health > 88:
            screen.blit(barraVida8de8, (-125, -290))
        elif Char.health > 77:
            screen.blit(barraVida7de8, (-125, -290))
        elif Char.health > 66:
            screen.blit(barraVida6de8, (-125, -290))
        elif Char.health > 55:
            screen.blit(barraVida5de8, (-125, -290))
        elif Char.health > 44:
            screen.blit(barraVida4de8, (-125, -290))
        elif Char.health > 33:
            screen.blit(barraVida3de8, (-125, -290))
        elif Char.health > 22:
            screen.blit(barraVida2de8, (-125, -290))
        elif Char.health > 11:
            screen.blit(barraVida1de8, (-125, -290))

        if enemyHealth > 88:
            screen.blit(barraVidaInimigo8de8, (325, -290))
        elif enemyHealth > 77:
            screen.blit(barraVidaInimigo7de8, (325, -290))
        elif enemyHealth > 66:
            screen.blit(barraVidaInimigo6de8, (325, -290))
        elif enemyHealth > 55:
            screen.blit(barraVidaInimigo5de8, (325, -290))
        elif enemyHealth > 44:
            screen.blit(barraVidaInimigo4de8, (325, -290))
        elif enemyHealth > 33:
            screen.blit(barraVidaInimigo3de8, (325, -290))
        elif enemyHealth > 22:
            screen.blit(barraVidaInimigo2de8, (325, -290))
        elif enemyHealth > 11:
            screen.blit(barraVidaInimigo1de8, (325, -290))

        pygame.display.update()

