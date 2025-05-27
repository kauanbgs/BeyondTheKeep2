#File made by: Kauan

# Colors:
# \033[30m Black \033[0m
# \033[31m Red \033[0m
# \033[32m Green \033[0m
# \033[33m Yellow \033[0m
# \033[34m Blue \033[0m
# \033[35m Magenta \033[0m
# \033[36m Cyan \033[0m
# \033[37m White \033[0m

# Bright colors:
# \033[90m Bright Black (Gray) \033[0m
# \033[91m Bright Red \033[0m
# \033[92m Bright Green \033[0m
# \033[93m Bright Yellow \033[0m
# \033[94m Bright Blue \033[0m
# \033[95m Bright Magenta \033[0m
# \033[96m Bright Cyan \033[0m
# \033[97m Bright White \033[0m


import curses
import time





def status(stdscr):
    from menus.menu import menu
    from assets.config import Char
    curses.curs_set(0)
    curses.start_color()

    # Definir cores
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)   # Vida
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)     # Ataque
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK) # Arma
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Moedas
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)   # Texto padrão

    while True:
        stdscr.clear()
        altura, largura = stdscr.getmaxyx()

        titulo = "Status do Personagem"
        stdscr.addstr(1, (largura - len(titulo)) // 2, titulo, curses.color_pair(6) | curses.A_BOLD)

        stdscr.addstr(3, 4, f"Nome: {Char.Name}", curses.color_pair(6))

        # Barra de vida
        # draw_bar(stdscr, 5, 4, Char.health, Char.max_health, 20, 1, "Vida")
        if Char.health > 90:
            stdscr.addstr(5, 4, f"Vida: [██████████] {Char.health}/100", curses.color_pair(1))
        elif Char.health > 80:
            stdscr.addstr(5, 4, f"Vida: [█████████ ] {Char.health}/100", curses.color_pair(1))
        elif Char.health > 70:
            stdscr.addstr(5, 4, f"Vida: [████████  ] {Char.health}/100", curses.color_pair(1))
        elif Char.health > 60:
            stdscr.addstr(5, 4, f"Vida: [███████   ] {Char.health}/100", curses.color_pair(1))
        elif Char.health > 50:
            stdscr.addstr(5, 4, f"Vida: [██████    ] {Char.health}/100", curses.color_pair(1))
        elif Char.health > 40:
            stdscr.addstr(5, 4, f"Vida: [█████     ] {Char.health}/100", curses.color_pair(1))
        elif Char.health > 30:
            stdscr.addstr(5, 4, f"Vida: [████      ] {Char.health}/100", curses.color_pair(1))
        elif Char.health > 20:
            stdscr.addstr(5, 4, f"Vida: [███       ] {Char.health}/100", curses.color_pair(1))
        elif Char.health > 10:
            stdscr.addstr(5, 4, f"Vida: [██        ] {Char.health}/100", curses.color_pair(1))
        else:
            stdscr.addstr(5, 4, f"Vida: [█         ] {Char.health}/100", curses.color_pair(1))



        # Dados adicionais
        stdscr.addstr(7, 4, f"Ataque: {Char.attack}", curses.color_pair(3))
        stdscr.addstr(8, 4, f"Arma: {Char.weapon}", curses.color_pair(4))
        stdscr.addstr(9, 4, f"Moedas: {Char.coins}", curses.color_pair(5))

        stdscr.addstr(11, 4, "[ENTER] - Voltar", curses.color_pair(6))

        stdscr.refresh()

        tecla = stdscr.getch()

        if tecla in [10, 13]:  # ENTER
            menu(stdscr)
            return
