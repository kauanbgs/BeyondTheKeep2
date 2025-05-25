from player.status import Char
import os
import time
from assets.things import clearScreen
from assets.things import typedPrint
from menus.menu import menu
from assets.config import Config
from assets.config import Char
from areas.tavern import tavern
from areas.learnSpells import learnSpells

def ravenspireIntro():
  if Char.veioRavenspire:
    ravenspire()
  Char.villagesVisited += 1
  clearScreen( )
  typedPrint(f"{Char.Name}, depois de perceber que precisava de conhecimento, encontrou Ravenspire.\n", Config.speed)
  typedPrint("Uma cidade mágica, com aura extremamente confortante e cheia de de surpresas.\n", Config.speed)
  time.sleep(1)
  print("")
  typedPrint(f"Aqui, {Char.Name} pode aprender magias.\n", Config.speed)
  time.sleep(2.5)
  ravenspire()


def ravenspire():
  Char.veioRavenspire = True
  Char.where = "Ravenspire"
  clearScreen()
  print(f"Você está atualmente em: {Char.where}\n")
  print("[0] - Voltar a praia")
  print("[1] - Feiticeiro")
  option = input("Escolha uma opção: ")

  if not option.isdigit():
    clearScreen()
    print("Opção inválida!")
    time.sleep(1)
    ravenspire()
  else:
    option = int(option)
  
  if option not in [0, 1]:
    clearScreen()
    print("Opção não existente.")
    time.sleep(1)
    ravenspire()

  elif option == 0:
    clearScreen()
    typedPrint("Voltando a praia...", Config.speed)
    time.sleep(.3)
    menu()
  elif option == 1:
    clearScreen()
    typedPrint("Encontrando o feiticeiro", Config.speed)
    time.sleep(.3)
    learnSpells()


