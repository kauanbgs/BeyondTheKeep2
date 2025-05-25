import curses
import time
from player.status import Char
from assets.things import typedPrint
from menus.menu import menu
from assets.config import Config


def caltheraIntro(stdscr):
    curses.curs_set(0)

    if Char.veioCalthera:
        calthera(stdscr)
        return

    Char.villagesVisited += 1
    Char.veioCalthera = True
    Char.where = "Calthera"

    stdscr.clear()
    altura, largura = stdscr.getmaxyx()

    textos = [
        f"Depois de muito tempo caminhando, {Char.Name} avistou Calthera.",
        "Uma vila conhecida pelos duelos intrigantes e perigosos, onde os mais fortes guerreiros se reúnem.",
        f"Aqui, {Char.Name} pode acessar os combates."
    ]

    for texto in textos:
        stdscr.clear()
        typedPrint(stdscr, texto, altura // 2, (largura - len(texto)) // 2, Config.speed)
        time.sleep(2)

    calthera(stdscr)


def calthera(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)

    selecionado = 0
    opcoes = ["Voltar à praia", "Duelar"]

    while True:
        stdscr.clear()
        altura, largura = stdscr.getmaxyx()

        titulo = f"Você está atualmente em: {Char.where}"
        stdscr.addstr(1, (largura - len(titulo)) // 2, titulo, curses.color_pair(1))
        stdscr.addstr(3, 2, "[ESC] Voltar ao menu", curses.color_pair(1))

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
                menu(stdscr)
                return

            elif opcao == "Duelar":
                stdscr.clear()
                typedPrint(stdscr, "Indo duelar...", 5, 4, Config.speed)
                time.sleep(0.5)
                # Aqui você deve chamar a função que controla o sistema de duelo
                # Exemplo (se existir): duelIntro(stdscr)
                # Se não existir, volta pro menu provisoriamente:
                menu(stdscr)
                return
