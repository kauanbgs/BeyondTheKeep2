#File made by: Kauan


from player.status import Char
import os
import time
from assets.things import clearScreen
from assets.config import Config
from assets.config import Char
from menus.menu import menu
from assets.things import randomVillage
from history.villages.villageEldoria import eldoriaIntro
from history.villages.villageBrumaria import brumariaIntro
from history.villages.villageVentogard import ventogardIntro
from history.villages.villageSkaldenheim import skaldenheim


def areas():

  from assets.things import typedPrint

  clearScreen()
  Char.where = "Placa de Sinalização"
  print(f"Você está atualmente em: {Char.where}\n")
  print("Você pode ir para: ")
  print("[0] - Voltar a praia")
  print("[1] - Procurar vila")
  if Char.veioEldoria:
    print("[2] - Eldoria - TAVERNA")
  if Char.veioBrumaria:
    print("[3] - Brumaria - FERREIRO")
  if Char.veioVentogard:
    print("[4] - Ventogard - MEMÓRIAS")
    
  option = input("Escolha uma opção: ")

  if not option.isdigit():
    clearScreen()
    print("Opção inválida!")
    time.sleep(1)
    areas()
  else:
    option = int(option)

  if option == 0:
    clearScreen()
    typedPrint("voltando para a praia...\n", Config.speed)
    time.sleep(0.5)
    menu()
    
  
  if option == 1:
    clearScreen()
    if randomVillage() == "Eldoria":
      typedPrint("Você encontrou Eldoria!\n", Config.speed)
      time.sleep(0.5)
      eldoriaIntro()
    if randomVillage() == "Brumaria":
      typedPrint("Você encontrou Brumaria!\n", Config.speed)
      time.sleep(0.5)
      brumariaIntro()
    if randomVillage() == "Ventogard":
      typedPrint("Você encontrou Ventogard!\n", Config.speed)
      time.sleep(0.5)
      ventogardIntro()
    if randomVillage() == "Skaldenheim":
      typedPrint("Você encontrou Skaldenheim!\n", Config.speed)
      time.sleep(0.5)
      skaldenheim()

  elif option == 2:
    if Char.veioEldoria:
      clearScreen()
      typedPrint(f"{Char.Name} está indo para Eldoria...\n", Config.speed)
      time.sleep(0.5)
      eldoriaIntro()
    else:
      clearScreen()
      print(f"{Char.name} ainda não desbloqueou isso.")
      time.sleep(2)
      areas()

  elif option == 3:
    if Char.veioBrumaria:
      clearScreen()
      typedPrint(f"{Char.Name} está indo para Brumaria...\n", Config.speed)
      time.sleep(0.5)
      brumariaIntro()
    else:
      clearScreen()
      print(f"{Char.name} ainda não desbloqueou isso.")
      time.sleep(2)
      areas()

  elif option == 3:
    if Char.veioVentogard:
      clearScreen()
      typedPrint(f"{Char.Name} está indo para Ventogard...\n", Config.speed)
      time.sleep(0.5)
      brumariaIntro()
    else:
      clearScreen()
      print(f"{Char.name} ainda não desbloqueou isso.")
      time.sleep(2)
      areas()
    

  
  else:
    clearScreen()
    print("Opção não existente.")
    time.sleep(1)
    areas()