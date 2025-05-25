import curses
import time
from assets.config import Char
from assets.things import classUpdate
from history.introduction import intro
from assets.things import typedPrint

def escolher_arma(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    altura, largura = stdscr.getmaxyx()

    opcoes = ["Espada gasta", "Cajado antigo"]
    selecionado = 0

    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)

    while True:
        stdscr.clear()
        titulo = "Escolha sua arma:"
        x_titulo = largura // 2 - len(titulo) // 2
        stdscr.addstr(2, x_titulo, titulo, curses.A_BOLD)

        for i, opcao in enumerate(opcoes):
            x = largura // 2 - len(opcao) // 2
            y = 5 + i
            if i == selecionado:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(y, x, opcao)
                stdscr.attroff(curses.color_pair(2))
            else:
                stdscr.addstr(y, x, opcao)

        stdscr.refresh()
        tecla = stdscr.getch()

        if tecla == curses.KEY_UP and selecionado > 0:
            selecionado -= 1
        elif tecla == curses.KEY_DOWN and selecionado < len(opcoes) - 1:
            selecionado += 1
        elif tecla in [curses.KEY_ENTER, 10, 13]:
            return selecionado 

def escolhaClasse(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)

    stdscr.clear()
    altura, largura = stdscr.getmaxyx()

    textoApresentação1 = ("Você desperta, sentindo a areia fria sob seu corpo e o som das ondas quebrando na praia. "
              "Ao abrir os olhos, percebe que está sozinho numa ilha deserta, cercado por uma densa floresta "
              "e um céu cinzento que promete tempestade.")
    textoApresentação2 = ("Enquanto tenta se levantar, algo chama sua atenção: duas armas repousam na areia, como se estivessem esperando por você."
              "A primeira é uma Espada gasta pelo tempo, mas ainda forte — a arma dos Guerreiros."
              "A segunda é um Cajado antigo, coberto de runas misteriosas — a arma dos Magos."
              "Sua vida, Seu destino começam agora!")
  
    typedPrint(stdscr, textoApresentação1, 2, 2)
    typedPrint(stdscr, textoApresentação2, 4, 2)
    time.sleep(2)


    arma_selecionada = escolher_arma(stdscr)

    if arma_selecionada == 0:
        Char.Name = "Aton"
    else:
        Char.Name = "Nextage"
    classUpdate()
    
    intro(stdscr)  # intro adaptada para curses


