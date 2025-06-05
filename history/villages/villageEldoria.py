import pygame
import sys
import os

# Importa o Char de outro diretório
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from assets.config import Char

# Inicia Pygame
pygame.init()
LARGURA, ALTURA = 800, 450
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Eldoria")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (200, 50, 50)
AZUL = (50, 50, 200)
AMARELO = (200, 200, 50)
CINZA = (180, 180, 180)

# Fontes
fonte = pygame.font.Font("Minecraftia.ttf", 20)
fonte_pequena = pygame.font.Font("Minecraftia.ttf", 14)

# Relógio
relogio = pygame.time.Clock()

# Carrega os fundos
fundo1_img = pygame.image.load("fundo1_eldoria.png").convert()
fundo1_img = pygame.transform.scale(fundo1_img, (800, 450))
fundo2_img = pygame.image.load("fundo2_eldoria.png").convert()
fundo2_img = pygame.transform.scale(fundo2_img, (800, 450))
fundo3_img = pygame.image.load("fundo3_eldoria.jpeg").convert()
fundo3_img = pygame.transform.scale(fundo3_img, (800,450))
fundo4_img = pygame.image.load("fundo4_eldoria.jpeg").convert()
fundo4_img = pygame.transform.scale(fundo4_img, (800, 450))
fundo5_img = pygame.image.load("fundo5_eldoria.jpeg").convert()
fundo5_img = pygame.transform.scale(fundo5_img, (800, 450))

fundo_ativo = fundo1_img

# Estado
Char.name = "Aton"
introducao = False
botao_selecionado = 0

# Dados dos botões
botoes = [
    {"texto": "Explorar", "cor": CINZA, "acao": "explorar"},
    {"texto": "Falar com os aldeões", "cor": CINZA, "acao": "aldeoes"},
    {"texto": "Sair (Q)", "cor": CINZA, "acao": "sair"},
]

# Funções
def desenhar_instrucao():
    instrucao = "Use ↑ ↓ para navegar, Enter para selecionar, Q para sair"
    render = fonte_pequena.render(instrucao, True, BRANCO)
    tela.blit(render, (10, ALTURA - 25))

def desenhar_botoes():
    largura, altura = 300, 50
    espacamento = 30
    x = (LARGURA - largura) // 2
    y_inicio = 100

    for i, botao in enumerate(botoes):
        y = y_inicio + i * (altura + espacamento)
        rect = pygame.Rect(x, y, largura, altura)
        pygame.draw.rect(tela, botao["cor"], rect, border_radius=10)

        if i == botao_selecionado:
            pygame.draw.rect(tela, PRETO, rect, 4, border_radius=10)

        txt = fonte.render(botao["texto"], True, PRETO)
        txt_rect = txt.get_rect(center=(x + largura // 2, y + altura // 2))
        tela.blit(txt, txt_rect)
        botao["rect"] = rect

def mostrar_texto_animado(texto, x, y, fonte, cor, delay=30):
    superficie_texto = ""
    for letra in texto:
        superficie_texto += letra
        render = fonte.render(superficie_texto, True, cor)
        tela.blit(fundo_ativo, (0, 0))
        tela.blit(render, (x, y))
        pygame.display.update()
        pygame.time.wait(delay)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def eldoria_introducao():
    global introducao, fundo_ativo
    pygame.display.update()
    tela.blit(fundo_ativo, (0, 0))
    mostrar_texto_animado("Aton caminha bravamente em direção à vila de Eudoria", 80, 80, fonte, PRETO)
    pygame.time.wait(1000)
    mostrar_texto_animado("Após longas horas de caminhadas...", 80, 80, fonte, PRETO)
    pygame.time.wait(1000)
    
    tela.blit(fundo3_img, (0,0))
    pygame.display.update()
    fundo_ativo = fundo3_img
    mostrar_texto_animado("Aton já começa a sentir o ar frio da vila", 80, 80, fonte, CINZA)
    pygame.time.wait(1000)   
    

   
    tela.blit(fundo4_img, (0,0))
    pygame.display.update()
    fundo_ativo = fundo4_img
    mostrar_texto_animado("Logo após sua chegada, um cavaleiro vem até seu encontro", 80, 80, fonte, CINZA)
    pygame.time.wait(1000)
    
    
    tela.blit(fundo5_img, (0,0))
    fundo_ativo = fundo5_img
    pygame.display.update()
    mostrar_texto_animado(f"-Você é {Char.name} de Skalice ?", 80, 80, fonte, AZUL)
    pygame.time.wait(1000)

    mostrar_texto_animado("-Sim, sou eu...", 80, 80, fonte, BRANCO)
    pygame.time.wait(1000)
    mostrar_texto_animado("-Ótimo, ouvimos muito sobre você", 80, 80, fonte, AZUL)
    pygame.time.wait(1000)
    mostrar_texto_animado("-Entre, esperávamos sua visita...", 80, 80, fonte, AZUL)
    pygame.time.wait(1000)
    fundo_ativo = fundo2_img
    introducao = True

def checar_clique_botoes(pos):
    for botao in botoes:
        if botao.get("rect") and botao["rect"].collidepoint(pos):
            return botao["acao"]
    return None

def intro_castelo():
    tela.blit(fundo3_img, (0,0))
    pygame.time.wait(1000)   
    tela.blit(fundo4_img, (0,0))
    pygame.time.wait(1000)
    tela.blit(fundo5_img, (0,0))
    pygame.time.wait(1000)

def acao_explorar():
    mostrar_texto_animado("Você acaba indo explorar dentro do castelo...", 60, 150, fonte, CINZA, delay=20)
    pygame.time.wait(800)
    mostrar_texto_animado(f"No caminho {Char.name} acaba encontrando um dos cavaleiros", 20, 150, fonte, CINZA, delay = 20)
    pygame.time.wait(800)
    mostrar_texto_animado(f"-Ei {Char.name},você acha de participar do nosso treino?", 60, 150,fonte,CINZA, delay = 20)
    pygame.time.wait(800)
    



def acao_aldeoes():
    mostrar_texto_animado("Você conversa com os aldeões e ouve rumores de uma criatura nas montanhas.", 60, 380, fonte_pequena, CINZA, delay=20)
    pygame.time.wait(800)

def executar_acao(acao):
    if acao == "sair":
        pygame.quit()
        sys.exit()
    elif acao == "explorar":
        acao_explorar()
    elif acao == "aldeoes":
        acao_aldeoes()

# Mostra introdução antes de entrar no loop
eldoria_introducao()

# Loop principal
rodando = True
while rodando:
    tela.blit(fundo_ativo, (0, 0))

    if introducao:
        desenhar_botoes()
        desenhar_instrucao()

    pygame.display.update()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif introducao and evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_q:
                executar_acao("sair")
            elif evento.key == pygame.K_UP:
                botao_selecionado = (botao_selecionado - 1) % len(botoes)
            elif evento.key == pygame.K_DOWN:
                botao_selecionado = (botao_selecionado + 1) % len(botoes)
            elif evento.key == pygame.K_RETURN:
                executar_acao(botoes[botao_selecionado]["acao"])
        elif introducao and evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            acao = checar_clique_botoes(evento.pos)
            if acao:
                executar_acao(acao)

    relogio.tick(60)

pygame.quit()
sys.exit()