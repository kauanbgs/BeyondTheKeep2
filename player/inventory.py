import curses
import time

inventoryItens = ["Pocao de Vida", "Pocao de Ataque", "Pocao de Vida"]
weaponsInventory = []


def inventory(stdscr):
    from menus.menu import menu
    from assets.things import updateStatus

    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)

    selecionado = 0

    while True:
        stdscr.clear()
        altura, largura = stdscr.getmaxyx()

        if not inventoryItens:
            msg = "Seu inventário está vazio. Pressione qualquer tecla para voltar."
            stdscr.addstr(altura//2, (largura - len(msg))//2, msg)
            stdscr.refresh()
            stdscr.getch()
            menu(stdscr)
            return

        stdscr.addstr(1, 2, "Seu inventário:")
        stdscr.addstr(2, 2, "[ESC] Voltar")

        for i, item in enumerate(inventoryItens):
            texto = item
            x = 4
            y = 4 + i

            if i == selecionado:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(y, x, texto)
                stdscr.attroff(curses.color_pair(2))
            else:
                stdscr.addstr(y, x, texto)

        stdscr.refresh()

        tecla = stdscr.getch()
        if tecla == curses.KEY_UP and selecionado > 0:
            selecionado -= 1
        elif tecla == curses.KEY_DOWN and selecionado < len(inventoryItens) - 1:
            selecionado += 1
        elif tecla == 27:
            menu(stdscr)
            return
        elif tecla in [10, 13]:
            item = inventoryItens[selecionado]
            stdscr.clear()
            msg = f"Você usou: {item}. Status atualizado."
            stdscr.addstr(altura//2, (largura - len(msg))//2, msg)
            stdscr.refresh()

            updateStatus(stdscr, item)
            inventoryItens.remove(item)
            time.sleep(1)

            if not inventoryItens:
                menu(stdscr)
                return
