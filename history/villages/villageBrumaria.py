import curses
import time
from assets.config import Char
from assets.things import typedPrint
from menus.menu import menu
from assets.config import Config
from areas.blacksmith import blacksmithIntro


def brumariaIntro(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)   # Selecionado

    if Char.veioBrumaria:
        brumaria(stdscr)
        return

    Char.villagesVisited += 1
    Char.veioBrumaria = True
    Char.where = "Brumaria"

    stdscr.clear()
    altura, largura = stdscr.getmaxyx()

    textos = [
        f"Depois de muito tempo caminhando, {Char.Name} avistou Brumaria.",
        "Onde as mais belas armas das dez vilas são formadas, bem vindo à terra da forja!",
        f"Aqui, {Char.Name} pode acessar o Ferreiro."
    ]

    for texto in textos:
        stdscr.clear()
        typedPrint(stdscr, texto, altura // 2, (largura - len(texto)) // 2, Config.speed)
        stdscr.refresh()
        time.sleep(2)

    brumaria(stdscr)


def brumaria(stdscr):

    from menus.areas import areas


    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)   # Selecionado

    selecionado = 0
    opcoes = ["Voltar à praia", "Ferreiro"]

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
                typedPrint(stdscr, "Voltando para a praia...", altura // 2, (largura - len("Voltando para a praia...")) // 2, Config.speed)
                time.sleep(1)
                areas(stdscr)
                return

            elif opcao == "Ferreiro":
                stdscr.clear()
                typedPrint(stdscr, "Indo ao Ferreiro...", altura // 2, (largura - len("Indo ao Ferreiro...")) // 2, Config.speed)
                time.sleep(1)
                blacksmithIntro(stdscr)
                return
