# #File made by: Kauan

# from player.status import Char
# import os
# import time

# from assets.things import typedPrint
# from menus.menu import menu
# from assets.config import Config
# from assets.config import Char
# from areas.tavern import tavern
# from areas.blacksmith import blacksmith

# def brumariaIntro():
#   if Char.veioBrumaria:
#     brumaria()
#   Char.villagesVisited += 1
#   clearScreen( )
#   typedPrint(f"Depois de muito tempo caminhando, {Char.Name} avistou Brumaria.\n", Config.speed)
#   typedPrint("Onde as mais belas armas das dez vilas são formadas, bem vindo à terra da forja!\n", Config.speed)
#   time.sleep(1)
#   print("")
#   typedPrint(f"Aqui, {Char.Name} pode acessar o Ferreiro.\n", Config.speed)
#   time.sleep(2.5)
#   brumaria()


# def brumaria():
#   Char.veioBrumaria = True
#   Char.where = "Brumaria"
#   clearScreen()
#   print(f"Você está atualmente em: {Char.where}\n")
#   print("[0] - Voltar a praia")
#   print("[1] - Ferreiro")
#   option = input("Escolha uma opção: ")

#   if not option.isdigit():
#     clearScreen()
#     print("Opção inválida!")
#     time.sleep(1)
#     brumaria()
#   else:
#     option = int(option)
  
#   if option not in [0, 1]:
#     clearScreen()
#     print("Opção não existente.")
#     time.sleep(1)
#     brumaria()

#   elif option == 0:
#     clearScreen()
#     typedPrint("Voltando a praia...", Config.speed)
#     time.sleep(.3)
#     menu()
#   elif option == 1:
#     clearScreen()
#     typedPrint("Encontrando o ferreiro...", Config.speed)
#     time.sleep(.3)
#     blacksmith()


