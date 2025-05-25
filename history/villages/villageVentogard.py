# #File made by: Kauan

# from player.status import Char
# import os
# import time
# from assets.things import typedPrint
# from menus.menu import menu
# from assets.config import Config
# from assets.config import Char
# from areas.tavern import tavern
# # 

# def ventogardIntro():
#   if Char.veioVentogard:
#     ventogard()
#   Char.villagesVisited += 1
#   clearScreen( )
#   typedPrint(f"O vento mostrou certa direção... calma, o vento?\n", Config.speed)
#   typedPrint("Aqui, a força da natureza assopra flashbacks. Que tal conhecer mais sua história?\n", Config.speed)
#   time.sleep(1)
#   print("")
#   typedPrint(f"Aqui, {Char.Name} pode acessar memórias.\n", Config.speed)
#   time.sleep(2.5)
#   ventogard()


# def ventogard():
#   Char.veioBrumaria = True
#   Char.where = "Brumaria"
#   clearScreen()
#   print(f"Você está atualmente em: {Char.where}\n")
#   print("[0] - Voltar a praia")
#   print("[1] - Procurar memórias")
#   option = input("Escolha uma opção: ")

#   if not option.isdigit():
#     clearScreen()
#     print("Opção inválida!")
#     time.sleep(1)
#     ventogard()
#   else:
#     option = int(option)
  
#   if option not in [0, 1]:
#     clearScreen()
#     print("Opção não existente.")
#     time.sleep(1)
#     ventogard()

#   elif option == 0:
#     clearScreen()
#     typedPrint("Voltando a praia...", Config.speed)
#     time.sleep(.3)
#     menu()
#   elif option == 1:
#     clearScreen()
#     typedPrint("Você sente...\n", Config.speed)
#     time.sleep(1)
#     print("--------------FLASHBACK--------------")
#     typedPrint(flashback(), Config.speed)
#     time.sleep(4)
#     ventogard()

    
    


