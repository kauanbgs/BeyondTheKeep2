import pygame
import sys
from assets.screenConfig import screen, font, filtro_preto,brumariaImagem1,brumariaImagem2
from assets.things import escrever_texto_animado, draw_text
from assets.config import Char

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

pygame.init()

fez_mercador = False
fez_castelo = False
fez_treinamento = False
fez_moradores = False
fez_julgamento = False

tem_pista_mercador = False
tem_pista_moradores = False

def introBrumaria():
    screen.blit(brumariaImagem1,(0, 0))
    pygame.display.update()
    escrever_texto_animado("Aton chega à fria e sombria Brumaria. Seus muros são altos, o céu encoberto e a tensão é palpável.", font, PRETO, 50, 50, 25, screen)
    pygame.time.wait(1000)
    escrever_texto_animado("A cidade aguarda respostas.", font, PRETO, 50, 80, 25, screen)
    pygame.time.wait(1000)
    menuBrumaria()

def menuBrumaria():
    global fez_mercador, fez_castelo, fez_treinamento, fez_moradores, fez_julgamento
    global tem_pista_mercador, tem_pista_moradores

    opcoes = [
        "Falar com o mercador mais próximo",
        "Ir ao castelo falar com o Lorde",
        "Treinar com os soldados no campo",
        "Conversar com os moradores",
        "Ir ao Tribunal"
    ]

    # Controla qual opção está selecionada (índice)
    selecionado = 0
    rodando = True

    while rodando:
        screen.fill((0, 0, 0))

        # Exibe as opções com destaque na selecionada
        for i, texto in enumerate(opcoes):
            # Texto com "- FEITO" se a tarefa foi feita
            feito = False
            if i == 0 and fez_mercador:
                texto_display = texto + " - FEITO"
                feito = True
            elif i == 1 and fez_castelo:
                texto_display = texto + " - FEITO"
                feito = True
            elif i == 2 and fez_treinamento:
                texto_display = texto + " - FEITO"
                feito = True
            elif i == 3 and fez_moradores:
                texto_display = texto + " - FEITO"
                feito = True
            else:
                texto_display = texto

            # Se for a opção 4 (Tribunal) e pistas não suficientes, mostra aviso
            if i == 4 and not (tem_pista_mercador and tem_pista_moradores):
                texto_display += " (não recomendado sem pistas suficientes)"

            cor = BRANCO
            # Destaca opção selecionada
            if i == selecionado:
                cor = (255, 215, 0)  # dourado

            draw_text(f"> {texto_display}", font, cor, screen, 50, 50 + i * 40)

        pygame.display.update()

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    selecionado = (selecionado + 1) % len(opcoes)
                elif evento.key == pygame.K_UP:
                    selecionado = (selecionado - 1) % len(opcoes)
                elif evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER:
                    # Lógica para cada opção
                    if selecionado == 0 and not fez_mercador:
                        falar_mercador()
                        fez_mercador = True
                    elif selecionado == 1 and not fez_castelo:
                        ir_castelo()
                        fez_castelo = True
                    elif selecionado == 2 and not fez_treinamento:
                        campo_treinamento()
                        fez_treinamento = True
                    elif selecionado == 3 and not fez_moradores:
                        falar_moradores()
                        fez_moradores = True
                    elif selecionado == 4 and not fez_julgamento:
                        if tem_pista_mercador and tem_pista_moradores:
                            tribunalBrumaria_func()
                            fez_julgamento = True
                            rodando = False
                        else:
                            escrever_texto_animado("Você não tem pistas suficientes...", font, PRETO, 50, 300, 25, screen)
                            pygame.time.wait(1500)
                    # Após fazer uma ação, atualiza o menu para refletir alterações
                    break

def falar_mercador():
    global tem_pista_mercador
    screen.fill((0, 0, 0))
    escrever_texto_animado("Aton se aproxima de um mercador nervoso.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado('"Você... é de Skalice, não é?"', font, BRANCO, 50, 80, 25, screen)
    escrever_texto_animado('"Ouvi passos apressados na noite do crime... Depois, silêncio."', font, BRANCO, 50, 110, 25, screen)
    tem_pista_mercador = True
    pygame.time.wait(1500)

def ir_castelo():
    screen.fill((0, 0, 0))
    escrever_texto_animado("Guardas escoltam Aton até o salão principal do castelo.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado('"Preciso de olhos confiáveis esta noite. Vigie meus corredores."', font, BRANCO, 50, 80, 25, screen)
    escrever_texto_animado("Durante a patrulha, Aton vê uma sombra e percebe que armaduras sumiram.", font, BRANCO, 50, 110, 25, screen)
    pygame.time.wait(1500)

def campo_treinamento():
    screen.fill((0, 0, 0))
    escrever_texto_animado("Soldados treinam sob o vento gélido.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado('"Mostre-nos como se luta, espadachim de Skalice!"', font, BRANCO, 50, 80, 25, screen)
    escrever_texto_animado("Aton vence o treino e ganha respeito.", font, BRANCO, 50, 110, 25, screen)
    pygame.time.wait(1500)

def falar_moradores():
    global tem_pista_moradores
    screen.fill((0, 0, 0))
    escrever_texto_animado("Aton caminha pelas ruas e ouve relatos.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado('"Ouvi barulhos pesados... Era um guarda, com botas."', font, BRANCO, 50, 80, 25, screen)
    escrever_texto_animado('"Vi um guarda sair da muralha... Usava capa."', font, BRANCO, 50, 110, 25, screen)
    tem_pista_moradores = True
    pygame.time.wait(1500)

def tribunalBrumaria_func():
    screen.fill((0, 0, 0))
    escrever_texto_animado("O salão do castelo está lotado. O Lorde quer respostas.", font, BRANCO, 50, 50, 25, screen)
    escrever_texto_animado('"O que ocorreu em Brumaria?"', font, BRANCO, 50, 80, 25, screen)
    opcoes = [
        "Um guarda assassinou um camponês",
        "Um guarda roubou itens do estoque",
        "Um guarda não fez seu turno noturno"
    ]

    selecionado = 0
    rodando = True

    while rodando:
        # Reescreve as opções para destacar a selecionada
        y_base = 120
        for i, texto in enumerate(opcoes):
            cor = BRANCO
            if i == selecionado:
                cor = (255, 215, 0)
                texto = "> " + texto
            draw_text(texto, font, cor, screen, 50, y_base + i * 30)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    selecionado = (selecionado + 1) % len(opcoes)
                elif evento.key == pygame.K_UP:
                    selecionado = (selecionado - 1) % len(opcoes)
                elif evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER:
                    if selecionado == 1:
                        escrever_texto_animado('"Exatamente. Está apto para julgar."', font, BRANCO, 50, 220, 25, screen)
                        pygame.time.wait(1000)
                        julgamento_final()
                        rodando = False
                    else:
                        escrever_texto_animado("O Lorde não parece convencido. Reúna mais provas.", font, BRANCO, 50, 250, 25, screen)
                        pygame.time.wait(1500)
                        rodando = False
                    break

def julgamento_final():
    rodando = True
    opcoes = ["Condenar", "Absolver"]
    selecionado = 0

    while rodando:
        screen.fill((30, 30, 30))
        screen.blit(filtro_preto, (0, 0))
        escrever_texto_animado('"O que deseja fazer com o acusado?"', font, BRANCO, 50, 50, 25, screen)

        y_base = 200
        for i, texto in enumerate(opcoes):
            cor = BRANCO
            if i == selecionado:
                cor = (255, 215, 0)
                texto = "> " + texto
            draw_text(texto, font, cor, screen, 275, y_base + i * 60)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    selecionado = (selecionado + 1) % len(opcoes)
                elif evento.key == pygame.K_UP:
                    selecionado = (selecionado - 1) % len(opcoes)
                elif evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER:
                    julgamento_resultado(selecionado == 0)
                    rodando = False
                    break

def julgamento_resultado(condena):
    screen.fill((0, 0, 0))
    if condena:
        escrever_texto_animado("A sala vibra em aplausos. Justiça é feita.", font, BRANCO, 50, 50, 25, screen)
        Char.honra += 1
    else:
        escrever_texto_animado("Crimes voltam a acontecer... Aton perde honra diante do reino.", font, BRANCO, 50, 50, 25, screen)
        Char.honra -= 1
    pygame.time.wait(2000)
    escrever_texto_animado("Aton parte para Vardann, uma ilha montanhosa ameaçada por bandidos.", font, BRANCO, 50, 90, 25, screen)
    pygame.time.wait(3000)
