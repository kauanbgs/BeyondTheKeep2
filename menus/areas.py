import curses
import time
from assets.things import randomVillage
from assets.config import Config, Char
from menus.menu import menu
from history.villages.villageEldoria import eldoriaIntro
from history.villages.villageBrumaria import brumariaIntro
from history.villages.villageCalthera import caltheraIntro


def areas(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)

    selecionado = 0

    while True:
        stdscr.clear()
        altura, largura = stdscr.getmaxyx()

        opcoes = ["Procurar vila", "Voltar à praia"]
        if Char.veioEldoria:
            opcoes.append("Eldoria - TAVERNA")
        if Char.veioBrumaria:
            opcoes.append("Brumaria - FERREIRO")
        if Char.veioCalthera:
            opcoes.append("Calthera - DUELOS")

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
                stdscr.addstr(altura // 2, (largura - len("Voltando para a praia...")) // 2, "Voltando para a praia...")
                stdscr.refresh()
                time.sleep(0.8)
                menu(stdscr)
                return

            elif opcao == "Procurar vila":
                stdscr.clear()
                vila = randomVillage()

                mensagem = f"Você encontrou {vila}!"
                stdscr.addstr(altura // 2, (largura - len(mensagem)) // 2, mensagem)
                stdscr.refresh()
                time.sleep(1)

                if vila == "Eldoria":
                    eldoriaIntro(stdscr)
                elif vila == "Brumaria":
                    brumariaIntro(stdscr)
                elif vila == "Calthera":
                    caltheraIntro(stdscr)
                return

            elif opcao == "Eldoria - TAVERNA":
                if Char.veioEldoria:
                    stdscr.clear()
                    msg = f"{Char.Name} está indo para Eldoria..."
                    stdscr.addstr(altura // 2, (largura - len(msg)) // 2, msg)
                    stdscr.refresh()
                    time.sleep(0.8)
                    eldoriaIntro(stdscr)
                else:
                    msg = "Você ainda não desbloqueou Eldoria."
                    stdscr.addstr(altura // 2, (largura - len(msg)) // 2, msg)
                    stdscr.refresh()
                    time.sleep(2)

            elif opcao == "Brumaria - FERREIRO":
                if Char.veioBrumaria:
                    stdscr.clear()
                    msg = f"{Char.Name} está indo para Brumaria..."
                    stdscr.addstr(altura // 2, (largura - len(msg)) // 2, msg)
                    stdscr.refresh()
                    time.sleep(0.8)
                    brumariaIntro(stdscr)
                else:
                    msg = "Você ainda não desbloqueou Brumaria."
                    stdscr.addstr(altura // 2, (largura - len(msg)) // 2, msg)
                    stdscr.refresh()
                    time.sleep(2)
            elif opcao == "Calthera - DUELOS":
                if Char.veioBrumaria:
                    stdscr.clear()
                    msg = f"{Char.Name} está indo para Brumaria..."
                    stdscr.addstr(altura // 2, (largura - len(msg)) // 2, msg)
                    stdscr.refresh()
                    time.sleep(0.8)
                    brumariaIntro(stdscr)
                else:
                    msg = "Você ainda não desbloqueou Brumaria."
                    stdscr.addstr(altura // 2, (largura - len(msg)) // 2, msg)
                    stdscr.refresh()
                    time.sleep(2)
