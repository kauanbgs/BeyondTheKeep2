#File made by: Kauan

from assets.itens import Itens
from player.status import Char
from assets.config import Config
from assets.things import typedPrint
from menus.menu import menu
from assets.things import clearScreen
from assets.things import revealChar2
from player.inventory import inventory, weaponsInventory

import time
import os

def blacksmithIntro():
  if Char.veioFerreiro:
    blacksmith()
  revealChar2("\033[33mPero\033[0m", "Hola, joven! Bienvenido al herrero!", "tengo varias opciones de armas.")
  blacksmith()

def blacksmith():
  Char.foiFerreiro = True
  Char.where = "Ferreiro"


  print("Bienvenido al herrero!")
  clearScreen()
  print(f"Tienes {Char.coins} monedas!")
  print("[0] - Voltar")
  print(f"[1] - {Itens.blacksmith[0]["nome"]}  | {Itens.blacksmith[0]["preco"]} moedas  | +{Itens.blacksmith[0]["dano"]}ATK")
  print(f"[2] - {Itens.blacksmith[1]["nome"]}    | {Itens.blacksmith[1]["preco"]} moedas | +{Itens.blacksmith[1]["dano"]}ATK")
  print(f"[3] - {Itens.blacksmith[2]["nome"]}     | {Itens.blacksmith[2]["preco"]} moedas | +{Itens.blacksmith[2]["dano"]}ATK")
  print(f"[4] - {Itens.blacksmith[3]["nome"]}  | {Itens.blacksmith[3]["preco"]} moedas | +{Itens.blacksmith[3]["dano"]}ATK")
  print(f"[5] - {Itens.blacksmith[4]["nome"]} | {Itens.blacksmith[4]["preco"]} moedas | +{Itens.blacksmith[4]["dano"]}ATK")
  option = input("Escolha uma opção: ")

  if not option.isdigit():
    clearScreen
    print("Opção inválida!")
    time.sleep(1)
    clearScreen
    blacksmith()
  else:
    option = int(option)

  if option == 0:
    clearScreen
    print("Saindo do ferreiro...")
    time.sleep(1)
    menu()

  elif option == 1:
    if Char.coins >= Itens.blacksmith[0]["preco"]:
      clearScreen()
      typedPrint(f"claro, claro! aquí está tu {Itens.blacksmith[0]["nome"]}!", Config.speed)
      Char.coins -= Itens.blacksmith[0]["preco"]
      weaponsInventory.append(Itens.blacksmith[0]["nome"])
      time.sleep(1)
      blacksmith()
    else:
      clearScreen()
      typedPrint("Você não tem moedas suficientes!", Config.speed)
      time.sleep(1)
      blacksmith()
  elif option == 2:
    if Char.coins >= Itens.blacksmith[1]["preco"]:
      clearScreen()
      typedPrint(f"claro, claro! aquí está tu {Itens.blacksmith[0]["nome"]}!", Config.speed)
      Char.coins -= Itens.blacksmith[1]["preco"]
      weaponsInventory.append(Itens.blacksmith[1]["nome"])
      time.sleep(1)
      blacksmith()
    else:
      clearScreen()
      typedPrint("Você não tem moedas suficientes!", Config.speed)
      time.sleep(1)
      blacksmith()
  elif option == 3:
    if Char.coins >= Itens.blacksmith[2]["preco"]:
      clearScreen()
      typedPrint(f"claro, claro! aquí está tu {Itens.blacksmith[2]["nome"]}!", Config.speed)
      Char.coins -= Itens.blacksmith[2]["preco"]
      weaponsInventory.append(Itens.blacksmith[2]["nome"])
      time.sleep(1)
      blacksmith()
    else:
      clearScreen()
      typedPrint("Você não tem moedas suficientes!", Config.speed)
      time.sleep(1)
      blacksmith()
  elif option == 4:
    if Char.coins >= Itens.blacksmith[3]["preco"]:
      clearScreen()
      typedPrint(f"claro, claro! aquí está tu {Itens.blacksmith[3]["nome"]}!", Config.speed)
      Char.coins -= Itens.blacksmith[3]["preco"]
      weaponsInventory.append(Itens.blacksmith[3]["nome"])
      time.sleep(1)
      blacksmith()
    else:
      clearScreen()
      typedPrint("Você não tem moedas suficientes!", Config.speed)
      time.sleep(1)
      blacksmith()
  elif option == 5:
    if Char.coins >= Itens.blacksmith[4]["preco"]:
      clearScreen()
      typedPrint(f"claro, claro! aquí está tu {Itens.blacksmith[4]["nome"]}!", Config.speed)
      Char.coins -= Itens.blacksmith[4]["preco"]
      weaponsInventory.append(Itens.blacksmith[4]["nome"])
      time.sleep(1)
      blacksmith()
    else:
      clearScreen()
      typedPrint("Você não tem moedas suficientes!", Config.speed)
      time.sleep(1)
      blacksmith()

  else:
    clearScreen
    print("Opção inválida!")
    time.sleep(2)
    blacksmith()
