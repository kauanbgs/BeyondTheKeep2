import curses
import time
from assets.things import typedPrint, randomVillage
from assets.config import Config, Char
from menus.menu import menu
from history.villages.villageEldoria import eldoriaIntro
from history.villages.villageBrumaria import brumariaIntro
from history.villages.villageVentogard import ventogardIntro
from history.villages.villageSkaldenheim import skaldenheim


def areas(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Normal
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)   # Selecionado

    selecionado = 0

    while True:
        stdscr.clear()
        altura, largura = stdscr.getmaxyx()

        opcoes = ["Voltar à praia", "Procurar vila"]
        if Char.veioEldoria:
            opcoes.append("Eldoria - TAVERNA")
        if Char.veioBrumaria:
            opcoes.append("Brumaria - FERREIRO")
        if Char.veioVentogard:
            opcoes.append("Ventogard - MEMÓRIAS")

        titulo = f"Você está em: {Char.where if Char.where else 'Placa de Sinalização'}"
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
                typedPrint("Voltando para a praia...\n", Config.speed)
                time.sleep(0.5)
                menu(stdscr)
                return

            elif opcao == "Procurar vila":
                stdscr.clear()
                vila = randomVillage()

                typedPrint(f"Você encontrou {vila}!\n", Config.speed)
                time.sleep(0.5)

                if vila == "Eldoria":
                    eldoriaIntro(stdscr)
                elif vila == "Brumaria":
                    brumariaIntro(stdscr)
                elif vila == "Ventogard":
                    ventogardIntro(stdscr)
                elif vila == "Skaldenheim":
                    skaldenheim(stdscr)
                return

            elif opcao == "Eldoria - TAVERNA":
                if Char.veioEldoria:
                    stdscr.clear()
                    typedPrint(f"{Char.Name} está indo para Eldoria...\n", Config.speed)
                    time.sleep(0.5)
                    eldoriaIntro(stdscr)
                else:
                    msg = "Você ainda não desbloqueou Eldoria."
                    stdscr.addstr(altura//2, (largura - len(msg))//2, msg)
                    stdscr.refresh()
                    time.sleep(2)

            elif opcao == "Brumaria - FERREIRO":
                if Char.veioBrumaria:
                    stdscr.clear()
                    typedPrint(f"{Char.Name} está indo para Brumaria...\n", Config.speed)
                    time.sleep(0.5)
                    brumariaIntro(stdscr)
                else:
                    msg = "Você ainda não desbloqueou Brumaria."
                    stdscr.addstr(altura//2, (largura - len(msg))//2, msg)
                    stdscr.refresh()
                    time.sleep(2)

            elif opcao == "Ventogard - MEMÓRIAS":
                if Char.veioVentogard:
                    stdscr.clear()
                    typedPrint(f"{Char.Name} está indo para Ventogard...\n", Config.speed)
                    time.sleep(0.5)
                    ventogardIntro(stdscr)
                else:
                    msg = "Você ainda não desbloqueou Ventogard."
                    stdscr.addstr(altura//2, (largura - len(msg))//2, msg)
                    stdscr.refresh()
                    time.sleep(2)
