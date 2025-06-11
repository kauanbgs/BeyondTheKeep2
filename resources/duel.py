#Esse arquive representa o sistema de duelo no jogo, onde o jogador pode lutar contra inimigos
#This file represents the duel system in the game, where the player can fight against enemies.


import pygame
import sys
from assets.things import escrever_texto_animado
from assets.config import Char
from assets.screenConfig import screen, font, backDuelo, aton, rei, nextage, barraVida1de8, barraVida2de8, barraVida3de8, barraVida4de8, barraVida5de8, barraVida6de8, barraVida7de8, barraVida8de8, barraVidaInimigo1de8, barraVidaInimigo2de8, barraVidaInimigo3de8, barraVidaInimigo4de8, barraVidaInimigo5de8, barraVidaInimigo6de8, barraVidaInimigo7de8, barraVidaInimigo8de8, atonEspada3, atonEspada4, atonEspada5, atonEspada6, cavaleiroFrame2, cavaleiroFrame3, cavaleiroFrame4, cavaleiroFrame5, cavaleiroFrame6, goblinMago, cavaleiro, cavaleiroEspada1, cavaleiroEspada2
from assets.things import d20
from resources.gameOver import gameOver

def desenhar_barra_vida(vida_atual, vida_maxima, x, y, tipo):
    parte = vida_atual / vida_maxima
    if tipo == "player":
        if parte > 7/8:
            screen.blit(barraVida8de8, (x, y))
        elif parte > 6/8:
            screen.blit(barraVida7de8, (x, y))
        elif parte > 5/8:
            screen.blit(barraVida6de8, (x, y))
        elif parte > 4/8:
            screen.blit(barraVida5de8, (x, y))
        elif parte > 3/8:
            screen.blit(barraVida4de8, (x, y))
        elif parte > 2/8:
            screen.blit(barraVida3de8, (x, y))
        elif parte > 1/8:
            screen.blit(barraVida2de8, (x, y))
        elif parte > 0:
            screen.blit(barraVida1de8, (x, y))
    elif tipo == "inimigo":
        if parte > 7/8:
            screen.blit(barraVidaInimigo8de8, (x, y))
        elif parte > 6/8:
            screen.blit(barraVidaInimigo7de8, (x, y))
        elif parte > 5/8:
            screen.blit(barraVidaInimigo6de8, (x, y))
        elif parte > 4/8:
            screen.blit(barraVidaInimigo5de8, (x, y))
        elif parte > 3/8:
            screen.blit(barraVidaInimigo4de8, (x, y))
        elif parte > 2/8:
            screen.blit(barraVidaInimigo3de8, (x, y))
        elif parte > 1/8:
            screen.blit(barraVidaInimigo2de8, (x, y))
        elif parte > 0:
            screen.blit(barraVidaInimigo1de8, (x, y))


class Projetil: #Classe para o projétil do jogador
    def __init__(self, x, y, velocidade): #atributos do projétil
        self.x = x
        self.y = y
        self.velocidade = velocidade
        self.raio = 6
        self.cor = (75, 150, 255)  # vermelho
        self.ativo = True

    def mover(self): #mover o projétil
        self.x += self.velocidade
        if self.x > 800:  # saiu da tela
            self.ativo = False

    def colidir(self, enemy_x): #Verifica se eixo X do projetil colidiu com o eixo X do inimigo
        if self.x > enemy_x + 175:
            self.ativo = False
            return Char.attack * d20()
        return 0

    def desenhar(self, tela): #Formula para desenhar o projétil
        pygame.draw.circle(tela, self.cor, (int(self.x), int(self.y)), self.raio)


def duel(enemyName, enemyHealth, enemyMaxHealth, enemyAttack, enemyDefense, enemyImage, enemyType, coinsForWin):
    
    class ProjetilInimigo:
        def __init__(self, x, y, velocidade):
            self.x = x
            self.y = y
            self.velocidade = velocidade
            self.raio = 6
            self.cor = (255, 100, 100)  # cor diferente do jogador
            self.ativo = True

        def mover(self):
            self.x -= self.velocidade  # vai da direita pra esquerda
            if self.x < 0:
                self.ativo = False

        def colidir(self, player_x):
            if self.x > player_x - 60 and self.x < player_x + 60:
                self.ativo = False
                return enemyAttack * d20() - Char.defense
            return 0

        def desenhar(self, tela):
            pygame.draw.circle(tela, self.cor, (int(self.x), int(self.y)), self.raio)

    pygame.mixer.init()
    som_espada = pygame.mixer.Sound("assets/sounds/espadaAtacando.mp3")
    som_espada.set_volume(0.15)
    som_magia = pygame.mixer.Sound("assets/sounds/somMagia.mp3")
    som_magia.set_volume(0.08)
    global musica
    musica = d20()
    if musica <= 16:
        pygame.mixer.music.load("assets/sounds/musicaBatalha.mp3")
        pygame.mixer.music.set_volume(0.15)
    elif musica > 7 and musica <= 12:
        pygame.mixer.music.load("assets/sounds/musicaBatalha2.mp3")
        pygame.mixer.music.set_volume(0.03) #Algumas musicas são mais altas, entao abaixei o volume
    else:
        pygame.mixer.music.load("assets/sounds/musicaBatalha3.mp3")
        pygame.mixer.music.set_volume(0.02) #Algumas musicas são mais altas, entao abaixei o volume
    pygame.mixer.music.play(-1) #Toca a musica em loop


    #Aumenta os atributos do inimigo de acordo com a dificuldade
    if Char.dificuldade == 1:
        enemyHealth += 10
        enemyAttack += 0.1
    elif Char.dificuldade == 2:
        enemyHealth += 20
        enemyAttack += 0.2
    elif Char.dificuldade == 3:
        enemyHealth += 30
        enemyAttack += 0.3
    
    projeteis_inimigo = [] 
    tempo_ultimo_ataque_mago = 0
    cooldown_mago = 1500
    projeteis = []

    if Char.classplayer == 1:
        playerImage = aton
        player_x = 100
        player_y = 250
    else:
        playerImage = nextage
        player_x = 100
        player_y = 250

    tempoCooldownMago = 0
    espada_cooldown = 0
    cooldownAtaqueEspadaInimigo = 0
    enemy_x = 500
    enemy_y = 25
    if enemyName == "Cavaleiro": #Cada imagem tem um tamanho diferente e está em um lugar diferente do tamanho, então é necessario ajustar a posição para cada inimigo.
        enemy_x = 350
        enemy_y = 90
    enemyImage = pygame.image.load(f"assets/images/{enemyImage}").convert_alpha()
    enemyImage = pygame.transform.scale(enemyImage, (250, 250))

    if enemyName == "Cavaleiro":
        enemyImage = pygame.transform.scale(enemyImage, (500, 500))
    player_speed = 1.5

    if enemyName == "Goblin":
        enemyImage = pygame.transform.scale(goblinMago, (500, 500))
        enemy_x = 350
        enemy_y = 117

    if enemyName == "CavaleiroTreino":
        enemyImage = pygame.transform.scale(cavaleiro, (180, 180))
        enemy_x = 350
        enemy_y = 290

    if enemyName == "Rei":
        enemyImage = pygame.transform.scale(rei, (230, 230))
        enemy_x = 350
        enemy_y = 255

    while Char.health > 0 and enemyHealth > 0:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return
                if evento.key == pygame.K_SPACE: #Espaço para atacar
                    if Char.classplayer == 1 and espada_cooldown == 0: #Esse tanto de blit é para fazer a animação do ataque com espada
                        som_espada.play()
                        espada_cooldown = 45
                        screen.blit(backDuelo, (0, 0))
                        desenhar_barra_vida(Char.health, Char.max_health, -125, -290, "player")
                        desenhar_barra_vida(enemyHealth, enemyMaxHealth, 325, -290, "inimigo")
                        screen.blit(enemyImage, (enemy_x, enemy_y))
                        screen.blit(atonEspada3, (player_x, player_y))
                        pygame.display.update()
                        pygame.time.wait(15)

                        screen.blit(backDuelo, (0, 0))
                        desenhar_barra_vida(Char.health, Char.max_health, -125, -290, "player")
                        desenhar_barra_vida(enemyHealth, enemyMaxHealth, 325, -290, "inimigo")
                        screen.blit(enemyImage, (enemy_x, enemy_y))
                        screen.blit(atonEspada4, (player_x, player_y))
                        pygame.display.update()
                        pygame.time.wait(15)

                        screen.blit(backDuelo, (0, 0))
                        desenhar_barra_vida(Char.health, Char.max_health, -125, -290, "player")
                        desenhar_barra_vida(enemyHealth, enemyMaxHealth, 325, -290, "inimigo")
                        screen.blit(enemyImage, (enemy_x, enemy_y))
                        screen.blit(atonEspada5, (player_x, player_y))
                        pygame.display.update()
                        pygame.time.wait(15)

                        screen.blit(backDuelo, (0, 0))
                        desenhar_barra_vida(Char.health, Char.max_health, -125, -290, "player")
                        desenhar_barra_vida(enemyHealth, enemyMaxHealth, 325, -290, "inimigo")
                        screen.blit(enemyImage, (enemy_x, enemy_y))
                        screen.blit(atonEspada6, (player_x, player_y))
                        pygame.display.update()
                        pygame.time.wait(15)
                        if player_x > enemy_x - 150 and player_x < enemy_x + 150: #Se o jogador está perto o suficiente do inimigo, ele recebe dano
                            enemyHealth -= Char.attack * d20()
                    elif Char.classplayer == 2:
                        if len(projeteis) == 0 and tempoCooldownMago == 0:
                            tempoCooldownMago = 150
                            novo_proj = Projetil(player_x + 170, player_y + 100, 4) #Cria um novo projétil
                            projeteis.append(novo_proj) #Adiciona o projétil à lista de projéteis
                
        #Se o inimigo é um mago, ele ataca com magia
        if enemyType == "mago":
            tempo_atual = pygame.time.get_ticks()
            if tempo_atual - tempo_ultimo_ataque_mago > cooldown_mago:
                som_magia.play()
                if enemyName == "Goblin":
                    novo_proj = ProjetilInimigo(enemy_x + 175, enemy_y + 237, 3)
                    projeteis_inimigo.append(novo_proj)
                    tempo_ultimo_ataque_mago = tempo_atual
                else:
                    novo_proj = ProjetilInimigo(enemy_x, enemy_y + 100, 3)
                    projeteis_inimigo.append(novo_proj)
                    tempo_ultimo_ataque_mago = tempo_atual

        # Se o inimigo é um espadachim, ele ataca com espada
        elif enemyType == "espada":
            if enemyName == "Cavaleiro":
                if cooldownAtaqueEspadaInimigo == 0:
                    som_espada.play()

                    screen.blit(backDuelo, (0, 0))
                    desenhar_barra_vida(Char.health, Char.max_health, -125, -290, "player")
                    desenhar_barra_vida(enemyHealth, enemyMaxHealth, 325, -290, "inimigo")
                    screen.blit(enemyImage, (enemy_x, enemy_y))
                    screen.blit(playerImage, (player_x, player_y))
                    pygame.display.update()
                    pygame.time.wait(15)

                    screen.blit(backDuelo, (0, 0))
                    desenhar_barra_vida(Char.health, Char.max_health, -125, -290, "player")
                    desenhar_barra_vida(enemyHealth, enemyMaxHealth, 325, -290, "inimigo")
                    screen.blit(cavaleiroFrame2, (enemy_x, enemy_y))
                    screen.blit(playerImage, (player_x, player_y))
                    pygame.display.update()
                    pygame.time.wait(15)

                    screen.blit(backDuelo, (0, 0))
                    desenhar_barra_vida(Char.health, Char.max_health, -125, -290, "player")
                    desenhar_barra_vida(enemyHealth, enemyMaxHealth, 325, -290, "inimigo")
                    screen.blit(cavaleiroFrame3, (enemy_x, enemy_y))
                    screen.blit(playerImage, (player_x, player_y))
                    pygame.display.update()
                    pygame.time.wait(15)

                    screen.blit(backDuelo, (0, 0))
                    desenhar_barra_vida(Char.health, Char.max_health, -125, -290, "player")
                    desenhar_barra_vida(enemyHealth, enemyMaxHealth, 325, -290, "inimigo")
                    screen.blit(cavaleiroFrame4, (enemy_x, enemy_y))
                    screen.blit(playerImage, (player_x, player_y))
                    pygame.display.update()
                    pygame.time.wait(15)

                    screen.blit(backDuelo, (0, 0))
                    desenhar_barra_vida(Char.health, Char.max_health, -125, -290, "player")
                    desenhar_barra_vida(enemyHealth, enemyMaxHealth, 325, -290, "inimigo")
                    screen.blit(cavaleiroFrame5, (enemy_x, enemy_y))
                    screen.blit(playerImage, (player_x, player_y))
                    pygame.display.update()
                    pygame.time.wait(15)

                    screen.blit(backDuelo, (0, 0))
                    desenhar_barra_vida(Char.health, Char.max_health, -125, -290, "player")
                    desenhar_barra_vida(enemyHealth, enemyMaxHealth, 325, -290, "inimigo")
                    screen.blit(cavaleiroFrame6, (enemy_x, enemy_y))
                    screen.blit(playerImage, (player_x, player_y))
                    pygame.display.update()
                    pygame.time.wait(15)

                    cooldownAtaqueEspadaInimigo = 120

                    if player_x + 150 > enemy_x and player_x - 150 < enemy_x:
                        dano = enemyAttack * d20() - Char.defense
                        if dano > 0:
                            Char.health -= dano

            elif enemyName == "CavaleiroTreino":
                if cooldownAtaqueEspadaInimigo == 0:
                    som_espada.play()

                    screen.blit(backDuelo, (0, 0))
                    desenhar_barra_vida(Char.health, Char.max_health, -125, -290, "player")
                    desenhar_barra_vida(enemyHealth, enemyMaxHealth, 325, -290, "inimigo")
                    screen.blit(enemyImage, (enemy_x, enemy_y))
                    screen.blit(playerImage, (player_x, player_y))
                    pygame.display.update()
                    pygame.time.wait(15)

                    screen.blit(backDuelo, (0, 0))
                    desenhar_barra_vida(Char.health, Char.max_health, -125, -290, "player")
                    desenhar_barra_vida(enemyHealth, enemyMaxHealth, 325, -290, "inimigo")
                    screen.blit(cavaleiroEspada1, (enemy_x, enemy_y))
                    screen.blit(playerImage, (player_x, player_y))
                    pygame.display.update()
                    pygame.time.wait(15)

                    screen.blit(backDuelo, (0, 0))
                    desenhar_barra_vida(Char.health, Char.max_health, -125, -290, "player")
                    desenhar_barra_vida(enemyHealth, enemyMaxHealth, 325, -290, "inimigo")
                    screen.blit(cavaleiroEspada2, (enemy_x, enemy_y))
                    screen.blit(playerImage, (player_x, player_y))
                    pygame.time.wait(15)

                    cooldownAtaqueEspadaInimigo = 160

                    if player_x + 220 > enemy_x and player_x - 220 < enemy_x: #Só da o dano se o jogador estiver perto o suficiente do inimigo
                        dano = enemyAttack * d20() - Char.defense
                        print(dano)
                        if dano > 0:
                            Char.health -= dano
        #Se o inimigo é um mago, ele vai pra frente se a vida está alta e pra trás se a vida está baixa.
        if enemyType == "mago":
            if Char.health >= Char.health * 0.75:
                if enemyHealth >= enemyMaxHealth * 0.75:
                    enemy_x += 0.5
                else:
                    enemy_x -= 0.5
            
            elif Char.health >= Char.health * 0.5:
                if enemyHealth >= enemyMaxHealth * 0.5:
                    enemy_x += 0.75
                else:
                    enemy_x -= 0.75
            elif Char.health >= Char.health * 0.25:
                if enemyHealth >= enemyMaxHealth * 0.25:
                    enemy_x += 1
                else:
                    enemy_x -= 1
        #Se o inimigo é um espadachim, ele vai pra frente se o jogador está longe e pra trás se o jogador está perto, para acertar com a espada.
        elif enemyType == "espada":
            if player_x - 100 < enemy_x:
                enemy_x -= 0.5
            elif player_x + 100 > enemy_x:
                enemy_x += 0.5
        
                    
        #Logica de movimentação
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            player_x += player_speed
        if keys[pygame.K_a]:
            player_x -= player_speed

        #Verifica se o jogador está no limite da tela, e se ele for sair o "trava", apenas sempre voltando a variavel X para o maximo permitido
        if player_x < -50:
            player_x = -50
        if player_x > 800 - 175:
            player_x = 800 - 175
        if enemy_x < -50:
            enemy_x = -50
        if enemy_x > 800 - 175:
            enemy_x = 800 - 175
        if enemyName == "Cavaleiro":
            if enemy_x < 100:
                enemy_x = 100
            if enemy_x > 700:
                enemy_x = 700
            if player_x > enemy_x + 130:
                player_x = enemy_x + 130
        if enemyName == "CavaleiroTreino":
            if enemy_x < 100:
                enemy_x = 100
            if enemy_x > 700:
                enemy_x = 700
            if player_x > enemy_x - 50:
                player_x = enemy_x - 50
        if enemyName == "Goblin":
            if enemy_x < 100:
                enemy_x = 100
            if enemy_x > 525:
                enemy_x = 525
            if player_x > enemy_x + 80:
                player_x = enemy_x + 80
        


        
            
        # Desenhar fundo e jogador
        screen.blit(backDuelo, (0, 0))
        screen.blit(playerImage, (player_x, player_y))
        screen.blit(enemyImage, (enemy_x, enemy_y))

        #Projeteis do jogador
        for p in projeteis: #Para cada projétil na lista de projéteis
                p.mover() #Move o projétil
                p.desenhar(screen)#Desenha o projétil
                dano = p.colidir(enemy_x) #Calcula o dano se o projétil colidiu com o inimigo
                enemyHealth -= dano #Diminui a vida do inimigo
        
        for p in projeteis_inimigo:
            p.mover()
            p.desenhar(screen)
            dano = p.colidir(player_x)
            Char.health -= dano

        projeteis_inimigo = [p for p in projeteis_inimigo if p.ativo] #verifica se o projétil do inimigo ainda está ativo

        


        projeteis = [p for p in projeteis if p.ativo]


        desenhar_barra_vida(Char.health, Char.max_health, -125, -290, "player")
        desenhar_barra_vida(enemyHealth, enemyMaxHealth, 325, -290, "inimigo")
        
        if espada_cooldown > 0:
            espada_cooldown -= 1
        if cooldownAtaqueEspadaInimigo > 0:
            cooldownAtaqueEspadaInimigo -= 1
        if tempoCooldownMago > 0:
            tempoCooldownMago -= 1

        pygame.display.update()


    if Char.health <= 0:
        pygame.mixer.music.stop()
        gameOver(enemyName)


    elif enemyHealth <= 0:
        pygame.mixer.music.stop()
        screen.fill((0, 0, 0))
        Char.coins += coinsForWin
        escrever_texto_animado(f"{Char.Name} derrotou {enemyName}, e ganhou {coinsForWin} moedas!", font, (255, 255, 255), 100, 100, 50, screen)
        pygame.display.update()
        pygame.time.wait(3000)




    

