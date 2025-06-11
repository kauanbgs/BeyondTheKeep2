import pygame
import sys
import time
from assets.things import escrever_texto_animado
from assets.config import Char
from assets.screenConfig import screen, font, filtro_preto, fontBoldGiga, fundoEldoria
from resources.final import final

import assets.things

def gameOver(enemyName):
    tempo_jogado = time.time() - assets.things.startTime

    minutos = int(tempo_jogado // 60)
    segundos = int(tempo_jogado % 60)

    gameOverTexto = fontBoldGiga.render("Game Over!", True, (255, 255, 255))
    screen.blit(fundoEldoria, (0, 0))
    screen.blit(filtro_preto, (0, 0))
    screen.blit(gameOverTexto, (200, 30))
    escrever_texto_animado(f"Voce foi derrotado por {enemyName}!", font, (255, 255, 255), 100, 150, 50, screen)
    escrever_texto_animado(f"{Char.Name} conseguiu juntar:", font, (255, 255, 255), 100, 200, 50, screen)
    escrever_texto_animado(f"{Char.coins} moedas de ouro!", font, (255, 255, 255), 100, 225, 50, screen)
    escrever_texto_animado(f"{Char.attack} de ataque!", font, (255, 255, 255), 100, 250, 50, screen)
    escrever_texto_animado(f"{Char.defense} de defesa!", font, (255, 255, 255), 100, 275, 50, screen)
    escrever_texto_animado(f"Jogou por {minutos} minutos e {segundos} segundos.", font, (255, 255, 255), 100, 300, 50, screen)
    escrever_texto_animado("Aperte espaco para finalizar o jogo.", font, (255, 255, 255), 100, 350, 50, screen)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    final()

