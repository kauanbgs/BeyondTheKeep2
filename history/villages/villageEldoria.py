#File made by: Kauan

from player.status import Char
import os
import time

from assets.things import typedPrint
from menus.menu import menu
from assets.config import Config
from assets.config import Char
from areas.tavern import tavern

def eldoriaIntro():
  if Char.veioEldoria:
    eldoria()
  Char.villagesVisited += 1
  clearScreen( )
  typedPrint(f"Após uma longa jornada pelas trilhas poeirentas e sob o sol escaldante, finalmente {Char.Name} avistou Eldoria.\n", Config.speed)
  typedPrint("Uma vila totalmente composta por malucos, com a personalidade extremamente forte.\n", Config.speed)
  time.sleep(1)
  print("")
  typedPrint(f"Aqui, {Char.Name} pode acessar a Taverna.\n", Config.speed)
  time.sleep(2.5)
  eldoria()

  
  


def eldoria():
  Char.veioEldoria = True
  Char.where = "Eldoria"
  clearScreen()
  print(f"Você está atualmente em: {Char.where}\n")
  print("[0] - Voltar a praia")
  print("[1] - Taverna")
  option = input("Escolha uma opção: ")

  if not option.isdigit():
    clearScreen()
    print("Opção inválida!")
    time.sleep(1)
    eldoria()
  else:
    option = int(option)
  
  if option not in [0, 1]:
    clearScreen()
    print("Opção não existente.")
    time.sleep(1)
    eldoria()

  elif option == 0:
    clearScreen()
    typedPrint("Voltando a praia...", Config.speed)
    time.sleep(.3)
    menu()
  elif option == 1:
    clearScreen()
    typedPrint("Entrando na taverna...", Config.speed)
    time.sleep(.3)
    tavern()


