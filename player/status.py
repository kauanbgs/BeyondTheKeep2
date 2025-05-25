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


import os, time
from assets.config import Char
from assets.things import clearScreen
from menus.menu import menu

#Just print the status.
def status():
    clearScreen()
    print(f"Nome: {Char.Name}")
    print(f"\033[32mVida:\033[0m {Char.health}")
    print(f"\033[36mMana:\033[0m {Char.mana}")
    print(f"\033[31mAtaque:\033[0m {Char.attack}")
    print(f"\033[35mArma:\033[0m {Char.weapon}")
    print(f"\033[33mMoedas:\033[0m {Char.coins}")
    print("")
    while True:
      print("[0] - Voltar")
      option = int(input("Você escolheu: "))
      
      if option != 0:
          print("Resposta inválida.")
          time.sleep(1)
          continue
      elif option == 0:
        menu()