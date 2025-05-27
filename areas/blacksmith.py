import curses
import time
from assets.itens import Itens
from assets.config import Char
from assets.config import Config
from assets.things import typedPrint
from menus.menu import menu
from player.inventory import weaponsInventory


def blacksmithIntro(stdscr):
    curses.curs_set(0)

    if Char.veioFerreiro:
        blacksmith(stdscr)
        return

    Char.veioFerreiro = True
    Char.where = "Ferreiro"

    typedPrint("Hola, joven! Bienvenido al herrero!\n", Config.speed)
    typedPrint("Tengo varias opciones de armas.\n", Config.speed)
    time.sleep(2)
    blacksmith(stdscr)


def blacksmith(stdscr):
    curses.curs_set(0)
    selecionado = 0

    itens = Itens.blacksmith
    opcoes = ["Voltar"] + [f"{item['nome']} | {item['preco']} moedas | +{item['dano']} ATK" for item in itens]

    while True:
        stdscr.clear()
        altura, largura = stdscr.getmaxyx()

        titulo = "Bienvenido al herrero!"
        saldo = f"Tienes {Char.coins} monedas!"

        stdscr.addstr(1, (largura - len(titulo)) // 2, titulo)
        stdscr.addstr(3, (largura - len(saldo)) // 2, saldo)

        stdscr.addstr(5, 2, "[ESC] Voltar ao menu")

        for i, opcao in enumerate(opcoes):
            x = 4
            y = 7 + i
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
            if selecionado == 0:
                typedPrint("Saindo do ferreiro...\n", Config.speed)
                time.sleep(0.5)
                menu(stdscr)
                return
            else:
                item = itens[selecionado - 1]
                if Char.coins >= item["preco"]:
                    Char.coins -= item["preco"]
                    weaponsInventory.append(item["nome"])
                    typedPrint(f"Claro, claro! Aquí está tu {item['nome']}!\n", Config.speed)
                    time.sleep(1)
                else:
                    typedPrint("Você não tem moedas suficientes!\n", Config.speed)
                    time.sleep(1)
