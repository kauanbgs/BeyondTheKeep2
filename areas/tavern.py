import pygame
import sys

pygame.init()

# Configurações da janela
LARGURA, ALTURA = 800, 450
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Loja do Carlos")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (200, 50, 50)
AZUL = (50, 50, 200)
AMARELO = (200, 200, 50)
CIANO = (50, 200, 200)
MAGENTA = (200, 50, 200)
CINZA = (180, 180, 180)
CINZA_CLARO = (200, 200 ,200)
OURO = (255, 215, 0)
MARROM = (139, 69, 19)

# Fontes
fonte = pygame.font.Font("Minecraftia.ttf", 20)
fonte_pequena = pygame.font.Font("Minecraftia.ttf", 14)

relogio = pygame.time.Clock()

# Fundo
fundo1 = pygame.image.load("fundo1.jpeg").convert()
fundo1 = pygame.transform.scale(fundo1,(800,450))

# Inventário e loja
moedas = 50
inventario = {
    "Slime": 1,
    "Pó de Phoenix": 1,
    "Rocha Mística": 1,
    "Pedra Afiada": 1,
    "Essência Arcana": 1
}

espadas = [
    {"nome": "Espada de Madeira", "preco": 15},
    {"nome": "Espada de Pedra", "preco": 25},
    {"nome": "Espada de Ferro", "preco": 35},
    {"nome": "Espada de Ouro", "preco": 50},
    {"nome": "Espada de Diamante", "preco": 65},
]

pocoes = [
    {"nome": "Poção de Vida", "preco": 10},
    {"nome": "Poção de Mana", "preco": 15},
    {"nome": "Poção de Força", "preco": 25},
    {"nome": "Poção de Velocidade", "preco": 20},
]

armaduras = [
    {"nome": "Armadura de Cobre", "preco": 40},
    {"nome": "Armadura de Ferro", "preco": 60},
    {"nome": "Armadura de Ouro", "preco": 80},
    {"nome": "Armadura de Diamante", "preco": 100},
]

categorias = ['pocoes', 'espadas', 'armaduras']
categoria_index = 0
selecionado = 0

# Mensagem inicial
mensagem = "Carlos diz: Hola, como estás?"

# Função para combinar itens (espadas + item especial)
def combinar_itens(item1, item2):
    espadas_base = ["Espada de Madeira", "Espada de Pedra", "Espada de Ferro", "Espada de Ouro", "Espada de Diamante"]
    especiais = {
        "Slime": "Pegajosa",
        "Pó de Phoenix": "Inflamável",
        "Rocha Mística": "Resistente",
        "Pedra Afiada": "Afiada",
        "Essência Arcana": "Mágica"
    }

    # Tenta combinação de espada com item especial
    for espada in espadas_base:
        for especial, sufixo in especiais.items():
            if (item1 == espada and item2 == especial) or (item2 == espada and item1 == especial):
                return f"{espada} {sufixo}"

    # Verifica se são duas espadas iguais
    if item1 == item2 and item1 in espadas_base:
        return f"{item1} Melhorada"

    return None


# Variáveis para modo combinação de espadas
modo_combinacao = False
selecionados_combinacao = []
selecionado_combinacao = 0  # índice para navegar na lista de espadas no inventário

# Função para desenhar a interface
def desenhar_tela(itens, modo_combinacao):
    tela.fill(PRETO)  # Limpa a tela antes de desenhar tudo
    tela.blit(fundo1, (0, 0))  # desenha o fundo

    if not modo_combinacao:
        # Desenha título com moedas e categoria
        titulo_texto = f"Moedas: {moedas} | Categoria: {categorias[categoria_index].capitalize()}"
        titulo = fonte.render(titulo_texto, True, OURO)
        titulo_rect = pygame.Rect(15, 15, titulo.get_width()+30, titulo.get_height()+8)
        pygame.draw.rect(tela, CINZA, titulo_rect, border_radius=5)
        tela.blit(titulo, (titulo_rect.x + 10, titulo_rect.y + 5))

        # Desenha os itens da categoria com retângulo preenchido no selecionado e borda nos outros
        for i, item in enumerate(itens):
            nome = item["nome"]
            preco = item["preco"]
            cor = AZUL if categorias[categoria_index] == "pocoes" else VERMELHO if categorias[categoria_index] == "espadas" else MAGENTA

            fundo = pygame.Rect(40, 100 + i * 40, 400, 35)
            if i == selecionado:
                pygame.draw.rect(tela, CINZA, fundo, border_radius=8)
                pygame.draw.rect(tela, CINZA_CLARO, fundo, 3, border_radius=8)
            else:
                pygame.draw.rect(tela, CINZA, fundo, 1, border_radius=8)

            texto = fonte.render(f"{nome} - {preco} moedas", True, cor)
            tela.blit(texto, (fundo.x + 10, fundo.y + 5))

        # Inventário com fundo destacado
        y_inv = 75
        inv_fundo = pygame.Rect(490, y_inv - 10, 280, 300)
        pygame.draw.rect(tela, (30, 30, 30), inv_fundo, border_radius=8)
        tela.blit(fonte.render("Inventário:", True, CIANO), (500, y_inv))

        for i, (nome, qtd) in enumerate(inventario.items()):
            texto = fonte_pequena.render(f"{nome}: {qtd}", True, BRANCO)
            tela.blit(texto, (500, y_inv + 30 + i * 25))
    else:
        # No modo combinação: só mostra os itens do inventário para combinar e mensagem
        itens_combinacao = [item for item in inventario.keys() if (any(item.startswith(e["nome"]) for e in espadas) or item in ["Slime", "Pó de Phoenix", "Rocha Mística", "Pedra Afiada", "Essência Arcana"])]

        y_inv = 60
        inv_fundo = pygame.Rect(40, y_inv - 10, 440, 300)
        pygame.draw.rect(tela, (30, 35, 30), inv_fundo, border_radius=8)
        tela.blit(fonte.render("Selecione 2 itens para combinar:", True, CIANO), (50, y_inv))

        for i, nome_item in enumerate(itens_combinacao):
            cor_item = AMARELO if any(nome_item.startswith(e["nome"]) for e in espadas) else CIANO
            fundo_item = pygame.Rect(50, 100 + i * 30, 400, 25)
            if i == selecionado_combinacao:
                pygame.draw.rect(tela, CINZA, fundo_item, border_radius=5)
                pygame.draw.rect(tela, cor_item, fundo_item, 2, border_radius=5)
            else:
                pygame.draw.rect(tela, CINZA, fundo_item, 1, border_radius=5)
            texto_item = fonte_pequena.render(f"{nome_item} ({inventario[nome_item]})", True, cor_item)
            tela.blit(texto_item, (fundo_item.x + 10, fundo_item.y + 3))

    # Mensagem e instruções sempre aparecem
    instrucoes = "← →: Mudar Categoria | ↑ ↓: Navegar | Enter: Comprar | J: Menu Juntar | Q: Voltar"
    tela.blit(fonte_pequena.render(instrucoes, True, CINZA_CLARO), (20, ALTURA - 40))
    tela.blit(fonte_pequena.render(mensagem, True, BRANCO), (20, ALTURA - 60))

    pygame.display.flip()

# Tela inicial (apresentação do Carlos)
def apresentacao_carlos():
    tela.fill(PRETO)
    texto1 = fonte.render("ALGUEM APARECE...", True, VERMELHO)
    tela.blit(texto1, ((LARGURA - texto1.get_width()) // 2, ALTURA // 2 - 60))
    pygame.display.flip()
    pygame.time.wait(1000)

    tela.fill(PRETO)
    texto2 = fonte.render("Hola, cómo estás? Bienvenido a Taverna...", True, BRANCO)
    texto3 = fonte.render("Mi nombre é Carlos, o qué desejas comprar?", True, BRANCO)
    tela.blit(texto2, (100, ALTURA // 2 - 20))
    tela.blit(texto3, (100, ALTURA // 2 + 20))
    pygame.display.flip()
    pygame.time.wait(2000)

apresentacao_carlos()

rodando = True
while rodando:
    categoria = categorias[categoria_index]
    itens = pocoes if categoria == "pocoes" else espadas if categoria == "espadas" else armaduras

    desenhar_tela(itens, modo_combinacao)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if modo_combinacao:
                # Navegação no modo combinação
                itens_combinacao = [item for item in inventario.keys() if (any(item.startswith(e["nome"]) for e in espadas) or item in ["Slime", "Pó de Phoenix", "Rocha Mística", "Pedra Afiada", "Essência Arcana"])]
                if evento.key == pygame.K_UP:
                    selecionado_combinacao = (selecionado_combinacao - 1) % len(itens_combinacao) if itens_combinacao else 0
                elif evento.key == pygame.K_DOWN:
                    selecionado_combinacao = (selecionado_combinacao + 1) % len(itens_combinacao) if itens_combinacao else 0
                elif evento.key == pygame.K_RETURN:
                    item_escolhido = itens_combinacao[selecionado_combinacao] if itens_combinacao else None
                    if item_escolhido:
                        selecionados_combinacao.append(item_escolhido)
                        if len(selecionados_combinacao) == 2:
                            resultado = combinar_itens(selecionados_combinacao[0], selecionados_combinacao[1])
                            if resultado:
                                inventario[resultado] = inventario.get(resultado, 0) + 1
                                mensagem = f"Carlos diz: {resultado} criada!"
                                for i in selecionados_combinacao:
                                    inventario[i] -= 1
                                    if inventario[i] <= 0:
                                        del inventario[i]
                            else:
                                mensagem = "Carlos diz: Não dá para combinar esses itens."
                            selecionados_combinacao = []
                            modo_combinacao = False
                elif evento.key == pygame.K_ESCAPE or evento.key == pygame.K_j:
                    modo_combinacao = False
                    selecionados_combinacao = []
            else:
                # Navegação normal na loja
                if evento.key == pygame.K_LEFT:
                    categoria_index = (categoria_index - 1) % len(categorias)
                    selecionado = 0
                elif evento.key == pygame.K_RIGHT:
                    categoria_index = (categoria_index + 1) % len(categorias)
                    selecionado = 0
                elif evento.key == pygame.K_UP:
                    selecionado = (selecionado - 1) % len(itens)
                elif evento.key == pygame.K_DOWN:
                    selecionado = (selecionado + 1) % len(itens)
                elif evento.key == pygame.K_RETURN:
                    item_compra = itens[selecionado]
                    if moedas >= item_compra["preco"]:
                        moedas -= item_compra["preco"]
                        inventario[item_compra["nome"]] = inventario.get(item_compra["nome"], 0) + 1
                        mensagem = f"Carlos diz: Você comprou {item_compra['nome']}!"
                    else:
                        mensagem = "Carlos diz: Você não tem moedas suficientes."
                elif evento.key == pygame.K_j:
                    modo_combinacao = True
                    selecionados_combinacao = []
                    selecionado_combinacao = 0
                elif evento.key == pygame.K_q:
                    rodando = False

    relogio.tick(60)

pygame.quit()
sys.exit()
