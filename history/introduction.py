import pygame
import sys
from assets.config import Char
from assets.things import draw_text
from assets.things import escrever_texto_animado
from assets.things import classUpdate
from assets.screenConfig import screen, font, praiaBack, filtro_preto, mainClock, mago_frames_parado, mago_frames, praia, espada, cajado, fundo, botaoPlay, botaoPlayHover, botaoSaves, botaoSavesHover, botaoQuit, botaoQuitHover, fade_out, play_rect, quit_rect, saves_rect



def introTexto():
    screen.fill((0, 0, 0))
    escrever_texto_animado("E aqui começa sua historia...", font, (255, 255, 255), 0, 25, 25, screen)
    escrever_texto_animado("Talvez voce quisesse se tornar uma lenda, alguem cujo nome seria gravado em cancoes", font, (255, 255, 255), 0, 50, 25, screen)
    escrever_texto_animado("e sussurrado em tavernas por seculos.", font, (255, 255, 255), 0, 75, 25, screen)
    escrever_texto_animado("Ou talvez sua ambicao fosse um pouco mais simples:", font, (255, 255, 255), 0, 100, 25, screen)
    escrever_texto_animado("juntar ouro suficiente para se tornar rico.", font, (255, 255, 255), 0, 125, 25, screen)
    escrever_texto_animado(f"Seja qual for o caso, voce e {Char.Name}, de Skalice:", font, (255, 255, 255), 0, 150, 25, screen)
    if Char.Name == "Aton":
        escrever_texto_animado(f"Um guerreiro, mestre da espada e professor de esgrima.", font, (255, 255, 255), 0, 175, 25, screen)
    else:
        escrever_texto_animado(f"Um mago, mestre das artes arcanas e professor de magia.", font, (255, 255, 255), 0, 175, 25, screen)
    escrever_texto_animado("E sua jornada está apenas começando.", font, (255, 255, 255), 0, 200, 25, screen)
    pygame.display.update()
    areas()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return
      


def intro():
    screen.blit(praiaBack, (0, 0))
    screen.blit(filtro_preto, (0, 0))
    escrever_texto_animado("Voce acorda, tonto e desnorteado, em uma praia qualquer.", font, (255, 255, 255), 0, 50, 25, screen)
    escrever_texto_animado("Em ambos os seus lados pairam duas armas sobre o ar.", font, (255, 255, 255), 0, 75, 25, screen)
    escrever_texto_animado("A primeira e um:", font, (255, 255, 255), 0, 100, 25, screen)
    escrever_texto_animado("CAJADO ANTIGO", font, (255, 0, 0), 0, 125, 75, screen)
    escrever_texto_animado("A segunda e uma:", font, (255, 255, 255), 0, 150, 25, screen)
    escrever_texto_animado("ESPADA GASTA", font, (255, 0, 0), 0, 175, 75, screen)
    escrever_texto_animado("Voce deve escolher uma delas para continuar sua jornada.", font, (255, 255, 255), 0, 200, 50, screen)
    pygame.time.delay(2000)
    
 
    frame_index = 0
    frame_timer = 0
    frame_delay = 200
    player_x, player_y = 340, 320
    player_speed = 5
    current_frame = 0


    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return

        frame_timer += mainClock.get_time()
        if frame_timer >= frame_delay:
            frame_timer = 0
            frame_index = (frame_index + 1) % len(mago_frames_parado)


        # Movimento e animação
        keys = pygame.key.get_pressed()
        moving = False

        if keys[pygame.K_d]:
            player_x += player_speed
            moving = True
        if keys[pygame.K_a]:
            player_x -= player_speed
            moving = True
            
        if frame_timer >= frame_delay:
            frame_timer = 0
            current_frame += 1

        if moving:
            frame_list = mago_frames
        else:
            frame_list = mago_frames_parado

        current_frame = current_frame % len(frame_list)

        # Define a Rect for the player and the sword for collision detection
        player_rect = pygame.Rect(player_x, player_y, 128, 128)
        if player_rect.colliderect(pygame.Rect(650, 250, 250, 250)):
            Char.Name = "Aton"
            classUpdate()
            introTexto()            
        if player_rect.colliderect(pygame.Rect(-100, 250, 250, 250)):
            Char.Name = "Nextage"
            classUpdate()
            introTexto()


        screen.blit(praia, (0, 0))
        screen.blit(frame_list[current_frame], (player_x, player_y))
        screen.blit(espada, (600, 250))
        screen.blit(cajado, (50, 250))
        
        pygame.display.update()
        mainClock.tick(60)


