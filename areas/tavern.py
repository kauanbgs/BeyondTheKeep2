from assets.config import Char
import curses
from assets.things import typedPrint
import time
from menus.menu import menu



textosIntro2 = [
        "Ao chegar em Eldoria, você sente o cheiro de aventura no ar. O vilarejo é pequeno, mas vibrante.",
        "A taverna local, 'A Taverna do Dragão', é o coração da vila. Aqui, histórias são contadas e alianças são formadas.",
        "Você entra na taverna e é recebido por um caloroso sorriso do taverneiro.",
    ]

def tavernIntro():
    if Char.veioTaverna:
        tavern()
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)

    stdscr.clear()
    stdscr.border()

    altura, largura = stdscr.getmaxyx()
    x = 2
    y = 2

    # Mostra os textos
    for texto in textosIntro2:
        typedPrint(stdscr, texto, y, x)
        y += 2
        time.sleep(0.5)

    stdscr.addstr(y + 1, x, "Pressione qualquer tecla para continuar...")
    stdscr.refresh()
    stdscr.getch()

    menu(stdscr)

def tavern():
    stdscr = curses.initscr()
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)

    stdscr.clear()
    stdscr.border()

    altura, largura = stdscr.getmaxyx()
    x = 2
    y = 2

    typedPrint(stdscr, "Você está na Taverna do Dragão.", y, x)
    y += 2

    menu(stdscr)