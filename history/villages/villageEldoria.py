import curses
import time
from assets.config import Char
from assets.things import typedPrint
from menus.menu import menu
from assets.config import Config
from areas.tavern import tavern




def eldoriaIntro(stdscr):
    curses.curs_set(0)

    if Char.veioEldoria:
        eldoria(stdscr)
        return

    Char.villagesVisited += 1
    Char.veioEldoria = True
    Char.where = "Eldoria"

    stdscr.clear()
    altura, largura = stdscr.getmaxyx()

    textos = [
        f"Após uma longa jornada pelas trilhas poeirentas e sob o sol escaldante, finalmente {Char.Name} avistou Eldoria.",
        "Uma vila totalmente composta por malucos, com a personalidade extremamente forte.",
        f"Aqui, {Char.Name} pode acessar a Taverna."
    ]

    for texto in textos:
        stdscr.clear()
        typedPrint(stdscr, texto, altura // 2, (largura - len(texto)) // 2)
        time.sleep(2)

    eldoria(stdscr)


def eldoria(stdscr):
    from menus.areas import areas

    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)

    selecionado = 0
    opcoes = ["Voltar à praia", "Taverna"]

    while True:
        stdscr.clear()
        altura, largura = stdscr.getmaxyx()

        titulo = f"Você está atualmente em: {Char.where}"
        stdscr.addstr(1, (largura - len(titulo)) // 2, titulo)
        stdscr.addstr(3, 2, "[ESC] Voltar ao menu")

        for i, opcao in enumerate(opcoes):
            x = 4
            y = 5 + i
            if i == selecionado:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(y, x, f"> {opcao}")
                stdscr.attroff(curses.color_pair(2))
            else:
                stdscr.addstr(y, x, f"  {opcao}")

        stdscr.refresh()

        tecla = stdscr.getch()

        if tecla == curses.KEY_UP and selecionado > 0:
            selecionado -= 1
        elif tecla == curses.KEY_DOWN and selecionado < len(opcoes) - 1:
            selecionado += 1
        elif tecla == 27:  # ESC
            menu(stdscr)
            return
        elif tecla in [10, 13]:  # ENTER
            opcao = opcoes[selecionado]

            if opcao == "Voltar à praia":
                stdscr.clear()
                Char.where = "Praia"
                typedPrint(stdscr, "Voltando para a praia...", 5, 4, Config.speed)
                time.sleep(0.5)
                areas(stdscr)
                return

            elif opcao == "Taverna":
                stdscr.clear()
                typedPrint(stdscr, "Entrando na Taverna...", 5, 4, Config.speed)
                time.sleep(0.5)
                tavern(stdscr)
                return
