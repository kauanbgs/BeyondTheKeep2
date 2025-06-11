#Esse arquivo representa a tela final do jogo, onde os créditos são exibidos
#This file represents the final screen of the game, where the credits are displayed

import pygame
import sys
from assets.screenConfig import screen, font, filtro_preto, vardannVigia
from assets.config import Char



def final():
  pygame.mixer.init()
  pygame.mixer.music.load("assets/sounds/musicaApresentacao.mp3")
  pygame.mixer.music.play(1)
  pygame.mixer.music.set_volume(.15)
  if Char.language == "ptbr":
    creditos = [
        "                Beyond The Keep",
        "Desenvolvido por Kauan, Rafael e Davi",
        "",
        "",
        "Narrativa: Kauan, Rafael, Davi",
        "",
        "",
        "Programacao: Kauan, Rafael, Davi",
        "",
        "",
        "Level Design / Dificuldade: Kauan"
        "",
        ""
        "Vila Brumaria: Rafael",
        "Vila Eldoria: Kauan",
        "Vila Vardann: Rafael",
        "",
        "",
        "Introducao: Kauan",
        "Duelo: Kauan",
        "GameOver: Kauan",
        "",
        "",
        "Menus: Kauan",
        "Taverna: Rafael",
        "Inventario:",
        ""
        "",
        "Creditos: Kauan",
        "Final: Rafael",
        "QA: Kauan, Rafael, Davi",

        "Design: Kauan, LeonardoAI, RaphaelAI",
        "Design de personagens:",
        "Animacoes de personagens:",
        "Videos: Kauan",
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
  else:
    creditos = [
          "                Beyond The Keep",
          "Developed by Kauan, Rafael and Davi",
          "",
          "",
          "Narrative: Kauan, Rafael, Davi",
          "",
          "",
          "Programming: Kauan, Rafael, Davi",
          "",
          "",
          "Level Design / Difficulty: Kauan"
          "",
          ""
          "Brumaria Village: Rafael",
          "Eldoria Village: Kauan,",
          "Vardann Village: Rafael,",
          "",
          "",
          "Introduction: Kauan",
          "Duel: Kauan",
          "GameOver: Kauan",
          "",
          "",
          "Menus: Kauan",
          "Tavern: Rafael",
          "Inventory: Davi",
          ""
          "",
          "Credits: Kauan",
          "QA: Kauan, Rafael, Davi",

          "Design: Kauan, Davi, LeonardoAI, RaphaelAI",
          "Character Design:Davi, Kauan",
          "Character Animations: Davi",
          "Videos: Kauan",
          "",
          ""
          "Sound: Kauan, Pixabay"
          "",
          ""
          "Soundtrack: Kauan, Pixabay",
          "",
          "",
          "Tools:",
          "Python, Pygame, Vscode, Photoshop, Piskel, Libresprite, Github, Trello",
          "",
          "",
          "Inspired by:",
          "Game Of Thrones, Kingdom Come: Deliverance.",
          "",
          "",
          "Special Thanks:",
          "Professors: Euller and Adriano",
          "",
          "",
          "Made with bugs, but with love.",
          "",
          "Thank you for playing Beyond The Keep!"
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


  
