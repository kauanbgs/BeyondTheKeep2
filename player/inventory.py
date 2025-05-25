import curses
import time

inventoryItens = ["Pocao de mana", "Escama de dragao"]  # Lista de exemplo
weaponsInventory = []  # Se quiser, usa depois

def inventory(stdscr):
    from assets.itens import Itens
    from menus.menu import menu
    from assets.things import updateStatus

    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Texto normal
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)   # Selecionado

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

        # Mostra os itens
        for i, item in enumerate(inventoryItens):
            utilizavel = False
            if item in Itens.base_itens and Itens.base_itens[item]["utilizavel"]:
                utilizavel = True
            elif item in Itens.materials and Itens.materials[item]["utilizavel"]:
                utilizavel = True
            elif item in Itens.Itens_personalizados and Itens.Itens_personalizados[item]["utilizavel"]:
                utilizavel = True

            texto = f"{item} {'- UTILIZÁVEL' if utilizavel else ''}"
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
        elif tecla == 27:  # ESC
            menu(stdscr)
            return
        elif tecla in [10, 13]:  # Enter
            item = inventoryItens[selecionado]
            utilizavel = False
            if item in Itens.base_itens and Itens.base_itens[item]["utilizavel"]:
                utilizavel = True
            elif item in Itens.materials and Itens.materials[item]["utilizavel"]:
                utilizavel = True
            elif item in Itens.Itens_personalizados and Itens.Itens_personalizados[item]["utilizavel"]:
                utilizavel = True

            if utilizavel:
                stdscr.clear()
                msg = f"Você usou: {item}. Status atualizado."
                stdscr.addstr(altura//2, (largura - len(msg))//2, msg)
                stdscr.refresh()
                updateStatus(item)
                inventoryItens.remove(item)
                time.sleep(1)

                if not inventoryItens:
                    menu(stdscr)
                    return
                # Continua no inventário (sem chamar novamente)
            else:
                stdscr.clear()
                msg = f"{item} não é utilizável."
                stdscr.addstr(altura//2, (largura - len(msg))//2, msg)
                stdscr.refresh()
                time.sleep(1)
