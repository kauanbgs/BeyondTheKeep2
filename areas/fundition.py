#File made by: Kauan


from assets.itens import Itens
from player.status import Char
from player.inventory import inventory, inventoryItens
from assets.things import clearScreen
import time
from menus.menu import menu
from assets.things import updateStatus
from assets.things import typedPrint

def joinItens(item1, item2):
    global inventoryItens

    base = item1.replace(" - FUNDIVEL", "").strip()
    material = item2.replace(" - FUNDIVEL", "").strip()

    if base not in Itens.base_itens:
        clearScreen()
        typedPrint("Item base não encontrado.", 0.045)
        time.sleep(1)
        return False
    if material not in Itens.materials:
        clearScreen()
        typedPrint("Material não encontrado.", 0.045)
        time.sleep(1)
        return False

    if base == "Espada" and material == "Bola de slime":
        Char.weapon = "Espada Pegajosa"
    elif base == "Espada" and material == "Essencia de fogo":
        Char.weapon = "Espada Inflamável"
    elif base == "Espada" and material == "Escama de dragao":
        Char.weapon = "Espada Resistente"
    elif base == "Espada" and material == "Garra de lobo":
        Char.weapon = "Espada Afiada"
    elif base == "Espada" and material == "Pluma de fenix":
        Char.weapon = "Espada Magica"

    elif base == "Pocao de cura" and material == "Bola de slime":
        inventoryItens.append("Pocao Pegajosa de Cura")
        inventoryItens.remove(item1)
        inventoryItens.remove(item2)
        return True
    elif base == "Pocao de cura" and material == "Essencia de fogo":
        inventoryItens.append("Pocao Ardente de Cura")
        inventoryItens.remove(item1)
        inventoryItens.remove(item2)
        return True
    elif base == "Pocao de cura" and material == "Escama de dragao":
        inventoryItens.append("Pocao Resistente de Cura")
        inventoryItens.remove(item1)
        inventoryItens.remove(item2)
        return True
    elif base == "Pocao de cura" and material == "Garra de lobo":
        inventoryItens.append("Pocao Cortante de Cura")
        inventoryItens.remove(item1)
        inventoryItens.remove(item2)
        return True
    elif base == "Pocao de cura" and material == "Pluma de fenix":
        inventoryItens.append("Pocao Magica Regenerativa")
        inventoryItens.remove(item1)
        inventoryItens.remove(item2)
        return True

    elif base == "Pocao de mana" and material == "Bola de slime":
        inventoryItens.append("Pocao Pegajosa de Mana")
        inventoryItens.remove(item1)
        inventoryItens.remove(item2)
        return True
    elif base == "Pocao de mana" and material == "Essencia de fogo":
        inventoryItens.append("Pocao Energizante")
        inventoryItens.remove(item1)
        inventoryItens.remove(item2)
        return True
    elif base == "Pocao de mana" and material == "Escama de dragao":
        inventoryItens.append("Pocao Encantada")
        inventoryItens.remove(item1)
        inventoryItens.remove(item2)
        return True
    elif base == "Pocao de mana" and material == "Garra de lobo":
        inventoryItens.append("Pocao Aguçada de Mana")
        inventoryItens.remove(item1)
        inventoryItens.remove(item2)
        return True
    elif base == "Pocao de mana" and material == "Pluma de fenix":
        inventoryItens.append("Pocao de Mana Mística")
        inventoryItens.remove(item1)
        inventoryItens.remove(item2)
        return True

    elif base == "Pocao de forca" and material == "Bola de slime":
        inventoryItens.append("Pocao Flexível de Forca")
        inventoryItens.remove(item1)
        inventoryItens.remove(item2)
        return True
    elif base == "Pocao de forca" and material == "Essencia de fogo":
        inventoryItens.append("Pocao de Forca Ardente")
        inventoryItens.remove(item1)
        inventoryItens.remove(item2)
        return True
    elif base == "Pocao de forca" and material == "Escama de dragao":
        inventoryItens.append("Pocao de Forca Escamada")
        inventoryItens.remove(item1)
        inventoryItens.remove(item2)
        return True
    elif base == "Pocao de forca" and material == "Garra de lobo":
        inventoryItens.append("Pocao de Forca Selvagem")
        inventoryItens.remove(item1)
        inventoryItens.remove(item2)
        return True
    elif base == "Pocao de forca" and material == "Pluma de fenix":
        inventoryItens.append("Pocao de Forca Renascente")
        inventoryItens.remove(item1)
        inventoryItens.remove(item2)
        return True

    # Mensagem padrão caso não haja combinação
    print("Combinação inválida ou não implementada.")
    return False


def showItens():
  clearScreen()
  print("Escolha os itens para fundir:")
  print("[0] - Voltar")
  for i, item in enumerate(inventoryItens):
      fundivel = False

      if item in Itens.base_itens and Itens.base_itens[item]["fundivel"]:
        fundivel = True
      elif item in Itens.materials and Itens.materials[item]["fundivel"]:
        fundivel = True
      elif item in Itens.Itens_personalizados and Itens.Itens_personalizados[item]["fundivel"]:
        fundivel = True

      if fundivel:
        print(f"[{i + 1}] - {item} - FUNDIVEL")
      else:
        print(f"[{i + 1}] - {item}")
  option = input("Escolha o primeiro item: ")

  if not option.isdigit():
      clearScreen()
      print("Opção inválida!")
      time.sleep(1)
      showItens()
  else:
      option = int(option)

  if option == 0:
      menu()
  elif option > len(inventoryItens) or option < 0:
      clearScreen()
      print("Opção inválida!")
      time.sleep(1)
      showItens()
  else:
      item1 = inventoryItens[option - 1]

  option2 = input("Escolha o segundo item: ")

  if not option2.isdigit():
      clearScreen()
      print("Opção inválida!")
      time.sleep(1)
      showItens()
  else:
      option2 = int(option2)

  if option2 == 0:
      menu()
  elif option2 > len(inventoryItens) or option2 < 0:
      clearScreen()
      print("Opção inválida!")
      time.sleep(1)
      showItens()
  else:
      item2 = inventoryItens[option2 - 1]
      if joinItens(item1, item2):
          print(f"Você fundiu {item1} e {item2} com sucesso!")
      else:
          print("Falha ao fundir os itens.")
      time.sleep(2)
      showItens()


      
      

  
  
  