#File made by: Kauan


import os, time
from assets.config import Char
from assets.things import typedPrint
from assets.config import Config
from menus.menu import menu
import curses


def intro(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.clear()
    stdscr.border()

    altura, largura = stdscr.getmaxyx()
    x = 2
    y = 2

    textosIntro1 = [
        "E aqui começa sua história...",
        "Talvez você quisesse se tornar uma lenda, alguém cujo nome seria gravado em canções e sussurrado em tavernas por séculos.",
        "Ou talvez sua ambição fosse um pouco mais simples: juntar ouro suficiente para se tornar rico e viver uma vida de prostitutas e bebidas.",
        f"Seja qual for o caso, você é {Char.Name}, de Skalice:"
    ]

    classe = "Um guerreiro, mestre da espada longa." if Char.classplayer == 1 else "Um mago, dominante do arcano."

    textosIntro2 = [
        "Seu caminho te trouxe até Eldoria, uma pequena vila, mas extremamente movimentada e cheia de aventuras.",
        "Todos os dias o sol se põe lentamente, e a lua brilha intensamente sobre as montanhas.",
        "Você caminha pelas ruas, observando o vilarejo ao seu redor. Nada fora do comum. Nada que indique que algo grande está prestes a acontecer.",
        "Mas talvez, isso dependa de você."
    ]

    # Mostra os textos
    for texto in textosIntro1:
        typedPrint(stdscr, texto, y, x)
        y += 2
        time.sleep(0.5)

    typedPrint(stdscr, classe, y, x)
    y += 2
    time.sleep(0.5)

    for texto in textosIntro2:
        typedPrint(stdscr, texto, y, x)
        y += 2
        time.sleep(0.5)

    stdscr.addstr(y + 1, x, "Pressione qualquer tecla para continuar...")
    stdscr.refresh()
    stdscr.getch()

    menu(stdscr)