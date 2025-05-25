from assets.things import animar_texto
from menus.classSelection import escolhaClasse
import curses
import time
def menuInicial(stdscr):
    curses.curs_set(0)
    curses.start_color()

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Texto normal
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)   # Selecionado
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Título

    opcoes = ["Jogar", "Ver Saves", "Sair"]
    selecionado = 0

    altura, largura = stdscr.getmaxyx()
    titulo = "Beyond The Keep"
    x_titulo = largura // 2 - len(titulo) // 2
    ascii = """

                                                ____    _______   _  __
                                                |  _ \  |__   __| | |/ /
                                                | |_) |    | |    | ' / 
                                                |  _ <     | |    |  <  
                                                | |_) |    | |    | . \ 
                                                |____/     |_|    |_|\_\
                         
                         
"""

    # Animação do título uma única vez no início
    stdscr.clear()
    stdscr.border()
    animar_texto(stdscr, titulo, 1, x_titulo, curses.color_pair(3), delay=0.05)
    time.sleep(0.5)

    while True:
        stdscr.clear()
        stdscr.border()
        altura, largura = stdscr.getmaxyx()

        # Desenha título fixo (sem animação)
        # Título
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(2, largura // 2 - len("Beyond The Keep") // 2, "Beyond The Keep")
        stdscr.attroff(curses.color_pair(3))

        # ASCII fixo
        stdscr.addstr(3, largura // 2 - 17, "       ____    _______   _  __")
        stdscr.addstr(4, largura // 2 - 17, "      |  _ \\  |__   __| | |/ /")
        stdscr.addstr(5, largura // 2 - 17, "      | |_) |    | |    | ' / ")
        stdscr.addstr(6, largura // 2 - 17, "      |  _ <     | |    |  <  ")
        stdscr.addstr(7, largura // 2 - 17, "      | |_) |    | |    | . \\ ")
        stdscr.addstr(8, largura // 2 - 17, "      |____/     |_|    |_|\\_\\")

        # Desenha opções do menu
        for i, opcao in enumerate(opcoes):
            x = largura // 2 - len(opcao) // 2
            y = altura // 2 - len(opcoes) // 2 + i
            if i == selecionado:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(y, x, opcao)
                stdscr.attroff(curses.color_pair(2))
            else:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, opcao)
                stdscr.attroff(curses.color_pair(1))

        stdscr.refresh()
        tecla = stdscr.getch()

        if tecla == curses.KEY_UP and selecionado > 0:
            selecionado -= 1
        elif tecla == curses.KEY_DOWN and selecionado < len(opcoes) - 1:
            selecionado += 1
        elif tecla in [curses.KEY_ENTER, 10, 13]:
            if opcoes[selecionado] == "Jogar":
                escolhaClasse(stdscr)  # chama seu menu de seleção de classe
            elif opcoes[selecionado] == "Ver Saves":
                stdscr.clear()
                stdscr.border()
                msg = "Exibindo os saves (a implementar)..."
                stdscr.addstr(altura // 2, largura // 2 - len(msg) // 2, msg)
                stdscr.refresh()
                stdscr.getch()
            elif opcoes[selecionado] == "Sair":
                break
