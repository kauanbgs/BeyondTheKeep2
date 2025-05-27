import os 
import time
import curses

from _curses import
from menus.menu import menu


def inventario:
    print("Digite [0] para voltar!")
    print("[1] - Usar item 1")
    print("[2] - Usar item 2")
    print("[3] - Usar item 3")

    compra = int(input("Sua escolha: "))
    if compra == 0:
        print("Você escolheu voltar!")
        menu():

