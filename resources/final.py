import pygame
import sys
from assets.screenConfig import screen, font, filtro_preto, vardannVigia



def final():
  pygame.mixer.init()
  pygame.mixer.music.load("assets/sounds/musicaApresentacao.mp3")
  pygame.mixer.music.play(-1)
  pygame.mixer.music.set_volume(.15)
  creditos = [
        "                Beyond The Keep",
        "Desenvolvido por Kauan, Rafael e Davi",
        "",
        "",
        "Narrativa: Kauan, Rafael e Davi, CHATGPT",
        "",
        "",
        "Programacao: Kauan, Rafael e Davi",
        "",
        "",
        "Level Design / Dificuldade: Kauan"
        "",
        ""
        "Vila Brumaria: Rafael",
        "Vila Eldoria: Kauan",
        "Vila Vardann: Davi",
        "",
        "",
        "Introducao: Kauan",
        "Duelo: Kauan",
        "GameOver: Kauan",
        "",
        "",
        "Menus: Kauan",
        "Taverna: Rafael",
        "Inventario: Davi",
        ""
        "",
        "Creditos: Kauan",
        "Final: Rafael",
        "QA: Kauan, Davi, Rafael",

        "Design: Kauan, Davi, Rafael, LeonardoAI, RaphaelAI",
        "Design de personagens: Davi",
        "Animacoes: Kauan, Davi",
        "",
        ""
        "Som: Kauan, Pixabay"
        "",
        ""
        "Trilha sonora: Kauan, Pixabay",
        "",
        "",
        "Ferramentas:",
        "Python, Pygame, Vscode, Photoshop, Piskel, Libresprite, Github, Trello",
        "",
        "",
        "Inspirado por:",
        "Game Of Thrones, Kingdom Come: Deliverance.",
        "",
        "",
        "Agradecimentos especiais:",
        "Professores: Euller e Adriano",
        "",
        "",
        "Feito com bugs, mas com amor.",
        "",
        "Obrigado por jogar Beyond The Keep!"
    ]
  y = 450
  x = 250

  while True:
    screen.blit(vardannVigia, (0,0))
    screen.blit(filtro_preto, (0,0))
    for i, texto in enumerate(creditos):
      linha = font.render(texto, True, (255, 255, 255))
      screen.blit(linha, (x, y + i * 30))

    y -= 1
    pygame.display.update()
    pygame.time.wait(20)
    if y < -1600:
      pygame.quit()
      sys.exit()


  
