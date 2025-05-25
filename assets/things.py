#File made by: Kauan
import curses
import random
import os
import time
from assets.config import Char
from assets.config import Config
from assets.itens import Village
from assets.itens import Flashback
from player.inventory import inventory
from player.inventory import weaponsInventory
from assets.itens import Itens

startTime = 0

#Starts an timer (it will be used on the saved games, at the game over and at the final page.)
def startTimer():
  global tempoComeco
  startTime = time.time()

#Just clear the screen, based on your OS.
def clearScreen():
  if os.name == 'nt':  # Windows
    os.system('cls')
  else:  # Linux ou macOS
    os.system('clear')

#Makes the print like an 'typing' print. You can change the speed by going on 'assets/config.py at the config class'
def typedPrint(stdscr, texto, y, x, delay=0.03):
    altura, largura = stdscr.getmaxyx()
    stdscr.move(y, x)
    stdscr.refresh()
    for char in texto:
        # Evita imprimir fora da tela na horizontal
        if x >= largura - 1:
            y += 1
            x = 0
            stdscr.move(y, x)
        stdscr.addstr(y, x, char)
        stdscr.refresh()
        time.sleep(delay)
        x += 1

def animar_texto(stdscr, texto, y, x, atributo=0, delay=0.05):
    for i, letra in enumerate(texto):
        stdscr.addstr(y, x + i, letra, atributo)
        stdscr.refresh()
        time.sleep(delay)

def classUpdate():
  if Char.Name == "Aton":
    Char.classplayer = 1
    Char.health = 100
    Char.mana = 50
    Char.attack = 1.5
    weaponsInventory.append("Espada gasta")
  else:
    Char.classplayer = 2
    Char.health = 120
    Char.mana = 100
    Char.attack = 1.3
    weaponsInventory.append("Cajado antigo")

def updateStatus(item):
    from assets.itens import Itens
    from player.status import Char  # Imagino que seja onde estão os atributos do personagem

    dados = {}
    if item in Itens.base_itens:
        dados = Itens.base_itens[item]
    elif item in Itens.Itens_personalizados:
        dados = Itens.Itens_personalizados[item]
    else:
        return "Item inválido para uso."

    mensagens = []

    if "cura" in dados:
        Char.health += dados["cura"]
        mensagens.append(f"Você ganhou {dados['cura']} de vida! Vida atual: {Char.health}")
    if "mana" in dados:
        Char.mana += dados["mana"]
        mensagens.append(f"Você recuperou {dados['mana']} de mana! Mana atual: {Char.mana}")
    if "forca" in dados:
        Char.attack += dados["forca"]
        mensagens.append(f"Você ganhou {dados['forca']} de força! Força atual: {Char.attack}")

    if not mensagens:
        mensagens.append("Esse item não teve efeito.")

    return "\n".join(mensagens)

def flashback():
    if not Flashback.flashbacks:
        return "Não existem mais flashbacks."
    
    choice = random.choice(Flashback.flashbacks)
    Flashback.flashbacks.remove(choice)
    return choice

def revealChar(npc_name, initial_text, final_text, speed=0.045):
    clearScreen()
    print("???: ", end="")
    typedPrint(initial_text + "\n", speed)
    
    print("???: ", end="")
    typedPrint(f"Meu nome é {npc_name}", speed)
    
    time.sleep(1)
    clearScreen()
    
    print(f"{npc_name}: {initial_text}")
    print(f"{npc_name}: Meu nome é {npc_name}, ", end="")
    typedPrint(final_text + "\n", speed)
    time.sleep(2)

def revealChar2(npc_name, initial_text, final_text, speed=0.045):
    clearScreen()
    print("???: ", end="")
    typedPrint(initial_text + "\n", speed)
    
    print("???: ", end="")
    typedPrint(f"Mi nombre é {npc_name}", speed)
    
    time.sleep(1)
    clearScreen()
    
    print(f"{npc_name}: {initial_text}")
    print(f"{npc_name}: Mi nombre é {npc_name}, ", end="")
    typedPrint(final_text + "\n", speed)
    time.sleep(2)

def updateStatus(item):
  from player.inventory import inventory, inventoryItens

  clearScreen()

  dados = {}
  if item in Itens.base_itens:
    dados = Itens.base_itens[item]
  elif item in Itens.Itens_personalizados:
    dados = Itens.Itens_personalizados[item]
  else:
    print("Item inválido para uso.")
    time.sleep(1)
    inventory()
    return

  inventoryItens.remove(item)

  efeito_aplicado = False

  if "cura" in dados:
    Char.health += dados["cura"]
    print(f"Você ganhou {dados['cura']} de vida! Sua vida atual é: {Char.health}")
    efeito_aplicado = True
  if "mana" in dados:
    Char.mana += dados["mana"]
    print(f"Você recuperou {dados['mana']} de mana! Sua mana atual é: {Char.mana}")
    efeito_aplicado = True
  if "forca" in dados:
    Char.attack += dados["forca"]
    print(f"Você ganhou {dados['forca']} de força! Sua força atual é: {Char.attack}")
    efeito_aplicado = True

  if not efeito_aplicado:
    print("Esse item não teve efeito.")

  time.sleep(2)
  inventory()

def weaponThings():
  print(f"Sua arma atual é: {Char.weapon}")
  print("[0] - Voltar")
  print("[1] - Guardar")
  print("[2] - Vender")
  option = input("Escolha uma opção: ")

  if not option.isdigit():
    clearScreen()
    print("Opção inválida!")
    time.sleep(1)
    weaponThings()
  else:
    option = int(option)

  if option == 0:
    clearScreen()
    print("Voltando...")
    time.sleep(1)
    return
  elif option == 1:
    clearScreen()
    typedPrint("Guardando arma...", Config.speed)
    time.sleep(1)
    if Char.classplayer == 1:
      weaponsInventory.append((Char.weapon))
      Char.weapon = "Espada gasta"
    else:
      weaponsInventory.append((Char.weapon))
      Char.weapon = "Cajado antigo"
    refreshDamage()

def refreshDamage():
    base = Char.attack_base  # ataque base do personagem
    
    if Char.weapon == "Espada de Madeira":
        Char.attack = base + 0.5
    elif Char.weapon == "Espada de Prata":
        Char.attack = base + 1.0
    elif Char.weapon == "Espada de Ouro":
        Char.attack = base + 1.5
    elif Char.weapon == "Espada de Platina":
        Char.attack = base + 2.0
    elif Char.weapon == "Espada de Diamante":
        Char.attack = base + 2.5

    # Personalizadas - manualmente
    elif Char.weapon == "Espada de Madeira Pegajosa":
        Char.attack = base + 0.6
    elif Char.weapon == "Espada de Madeira Inflamavel":
        Char.attack = base + 0.7
    elif Char.weapon == "Espada de Madeira Resistente":
        Char.attack = base + 0.8
    elif Char.weapon == "Espada de Madeira Afiada":
        Char.attack = base + 1.0
    elif Char.weapon == "Espada de Madeira Magica":
        Char.attack = base + 1.3

    elif Char.weapon == "Espada de Prata Pegajosa":
        Char.attack = base + 1.5
    elif Char.weapon == "Espada de Prata Inflamavel":
        Char.attack = base + 1.8
    elif Char.weapon == "Espada de Prata Resistente":
        Char.attack = base + 2.0
    elif Char.weapon == "Espada de Prata Afiada":
        Char.attack = base + 2.3
    elif Char.weapon == "Espada de Prata Magica":
        Char.attack = base + 2.5

    elif Char.weapon == "Espada de Ouro Pegajosa":
        Char.attack = base + 2.8
    elif Char.weapon == "Espada de Ouro Inflamavel":
        Char.attack = base + 3.0
    elif Char.weapon == "Espada de Ouro Resistente":
        Char.attack = base + 3.2
    elif Char.weapon == "Espada de Ouro Afiada":
        Char.attack = base + 3.4
    elif Char.weapon == "Espada de Ouro Magica":
        Char.attack = base + 3.5

    elif Char.weapon == "Espada de Platina Pegajosa":
        Char.attack = base + 3.7
    elif Char.weapon == "Espada de Platina Inflamavel":
        Char.attack = base + 3.8
    elif Char.weapon == "Espada de Platina Resistente":
        Char.attack = base + 4.0
    elif Char.weapon == "Espada de Platina Afiada":
        Char.attack = base + 4.2
    elif Char.weapon == "Espada de Platina Magica":
        Char.attack = base + 4.5

    elif Char.weapon == "Espada de Diamante Pegajosa":
        Char.attack = base + 4.8
    elif Char.weapon == "Espada de Diamante Inflamavel":
        Char.attack = base + 5.0
    elif Char.weapon == "Espada de Diamante Resistente":
        Char.attack = base + 5.2
    elif Char.weapon == "Espada de Diamante Afiada":
        Char.attack = base + 5.4
    elif Char.weapon == "Espada de Diamante Magica":
        Char.attack = base + 5.5

    else:
        Char.attack = base
  
def tools():
    clearScreen()
    print("=== Equipamento ===")
    print("[0] - Voltar")
    print(f"Arma equipada: {Char.weapon}")

    print("\n=== Armas no inventário ===")
    armas_disponiveis = []

    for i in weaponsInventory:
        if i != Char.weapon:
            armas_disponiveis.append(i)

    for index, arma in enumerate(armas_disponiveis):
        print(f"[{index + 1}] - {arma}")

    print("")
    option = input("Escolha um item para equipar: ")

    if not option.isdigit():
        clearScreen()
        print("Opção inválida!")
        time.sleep(1)
        clearScreen()
        tools()
    else:
        option = int(option)

        if option == 0:
            clearScreen()
            return

        if 1 <= option <= len(armas_disponiveis):
            Char.weapon = armas_disponiveis[option - 1]
            clearScreen()
            print(f"Você equipou: {Char.weapon}")
            refreshDamage()
            time.sleep(1)
            clearScreen()
        else:
            clearScreen
            print("Opção inválida!")
            time.sleep(1)
            clearScreen()
            tools()

def DicesAnimation():
    for i in range(15):
      print("O dado rolou: ", end='')
      print(f"{random.randint(1, 20)}")
      time.sleep(0.1)
      clearScreen()
    print()

def d20():
   ree = random.randint(1, 20)
   return ree
      
def attackAnimation():
    jogador = ["você", " o ", "/|\\ 🗡", "/_\\"]
    inimigo  = ["   inimigo", "     o ", "  🖊 /|\\", "____/_\\"]

    clearScreen()
    print(f"""
    ______________________________________
    |                                     |
    |                   ATAQUE!           |
    |                                     |
    |            {jogador[0]}         {inimigo[0]}  |
    |            {jogador[1]}           {inimigo[1]}    |
    |            {jogador[2]}         {inimigo[2]}    |
    |____________{jogador[3]}___________{inimigo[3]}____|
    """)
    time.sleep(.5)
    clearScreen()
    print(f"""
    ______________________________________
    |                                     |
    |                   ATAQUE!           |
    |                                     |
    |               {jogador[0]}      {inimigo[0]}  |
    |               {jogador[1]}        {inimigo[1]}    |
    |               {jogador[2]}      {inimigo[2]}    |
    |_______________{jogador[3]}________{inimigo[3]}____|
    """)
    time.sleep(.5)
    clearScreen()
    print(f"""
    ______________________________________
    |                                     |
    |                   ATAQUE!           |
    |                                     |
    |                  {jogador[0]}   {inimigo[0]}  |
    |                  {jogador[1]}     {inimigo[1]}    |
    |                  {jogador[2]}   {inimigo[2]}    |
    |__________________{jogador[3]}_____{inimigo[3]}____|
    """)

    time.sleep(.5)
    clearScreen()

    print(f"""
    ______________________________________
    |                                     |
    |                   ATAQUE!           |
    |                                     |
    |                    {jogador[0]} {inimigo[0]}  |
    |                    {jogador[1]}   {inimigo[1]}    |
    |                    {jogador[2]} {inimigo[2]}    |
    |____________________{jogador[3]}___{inimigo[3]}____|
    """)

    time.sleep(.5)
    clearScreen()

    print(f"""
    ______________________________________
    |                                     |
    |                   ATAQUE!           |
    |                                     |
    |                      {jogador[0]}{inimigo[0]} |
    |                      {jogador[1]}  {inimigo[1]} 🩸|
    |                      {jogador[2]}{inimigo[2]}   |
    |______________________{jogador[3]}__{inimigo[3]}___|
    """)
    time.sleep(2)

def magicAttackAnimation(ascii):
    jogador = ["você", " o ", f"/|\\ {ascii}", "/_\\"]
    inimigo = ["   inimigo", "     o ", "  🖊 /|\\", "____/_\\"]

    clearScreen()
    print(f"""
    ______________________________________
    |                                     |
    |               MAGIA LANÇADA!        |
    |                                     |
    |            {jogador[0]}         {inimigo[0]}  |
    |            {jogador[1]}           {inimigo[1]}    |
    |            {jogador[2]}         {inimigo[2]}    |
    |____________{jogador[3]}___________{inimigo[3]}____|
    """)
    time.sleep(0.5)
    clearScreen()

    print(f"""
    ______________________________________
    |                                     |
    |               MAGIA LANÇADA!        |
    |                                     |
    |               {jogador[0]}      {inimigo[0]}  |
    |               {jogador[1]}        {inimigo[1]}    |
    |               {jogador[2]}      {inimigo[2]}    |
    |_______________{jogador[3]}________{inimigo[3]}____|
    """)
    time.sleep(0.5)
    clearScreen()

    print(f"""
    ______________________________________
    |                                     |
    |               MAGIA LANÇADA!        |
    |                                     |
    |                  {jogador[0]}   {inimigo[0]}  |
    |                  {jogador[1]}     {inimigo[1]}    |
    |                  {jogador[2]}   {inimigo[2]}    |
    |__________________{jogador[3]}_____{inimigo[3]}____|
    """)
    time.sleep(0.5)
    clearScreen()

    print(f"""
    ______________________________________
    |                                     |
    |               MAGIA LANÇADA!        |
    |                                     |
    |                    {jogador[0]} {inimigo[0]}  |
    |                    {jogador[1]}   {inimigo[1]}    |
    |                    {jogador[2]} {inimigo[2]}    |
    |____________________{jogador[3]}___{inimigo[3]}____|
    """)
    time.sleep(0.5)
    clearScreen()

    print(f"""
    ______________________________________
    |                                     |
    |               MAGIA LANÇADA!        |
    |                                     |
    |                      {jogador[0]}{inimigo[0]} |
    |                      {jogador[1]}  {inimigo[1]} 🩸|
    |                      {jogador[2]}{inimigo[2]}   |
    |______________________{jogador[3]}__{inimigo[3]}___|
    """)
    time.sleep(2)
    clearScreen()


