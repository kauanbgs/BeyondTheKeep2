# #File made by: Kauan

# from player.status import Char
# import os
# import time

# from assets.things import typedPrint
# from menus.menu import menu
# from assets.config import Config
# from assets.config import Char
# from areas.tavern import tavern


# def eldoriaIntro():
#   if Char.veioSkaldenheim:
#     skaldenheim()
#   Char.villagesVisited += 1
#   clearScreen( )
#   typedPrint(f"Uau! Quantas cores e combinações. uma ilha colorida, ao olhar para o lado, {Char.Name} observa uma placa dizendo: \n", Config.speed)
#   typedPrint("Que tal fabricar seus próprios equipamentos?\n", Config.speed)
#   time.sleep(1)
#   print("")
#   typedPrint(f"Aqui, {Char.Name} pode acessar a Fundição.\n", Config.speed)
#   time.sleep(2.5)
#   skaldenheim()

  
  


# def skaldenheim():
#   Char.veioSkaldenheim = True
#   Char.where = "Skaldenheim"
#   clearScreen()
#   print(f"Você está atualmente em: {Char.where}\n")
#   print("[0] - Voltar a praia")
#   print("[1] - Fundição")
#   option = input("Escolha uma opção: ")

#   if not option.isdigit():
#     clearScreen()
#     print("Opção inválida!")
#     time.sleep(1)
#     skaldenheim()
#   else:
#     option = int(option)
  
#   if option not in [0, 1]:
#     clearScreen()
#     print("Opção não existente.")
#     time.sleep(1)
#     skaldenheim()

#   elif option == 0:
#     clearScreen()
#     typedPrint("Voltando a praia...", Config.speed)
#     time.sleep(.3)
#     menu()
#   elif option == 1:
#     clearScreen()
#     typedPrint("Indo à fundição...", Config.speed)
#     time.sleep(.3)
#     joinItens()


