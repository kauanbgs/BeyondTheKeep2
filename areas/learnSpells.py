#File made by: Kauan

from assets.itens import Itens
from player.status import Char
from assets.config import Config
from assets.things import typedPrint
from menus.menu import menu
from assets.things import clearScreen
from assets.things import revealChar2
from player.inventory import inventory, weaponsInventory

def learnSpellsIntro():
  if Char.veioFeiticeiro:
    learnSpells()
  revealChar2("\033[33mFeiticeiro\033[0m", "Olá, muahahahaha!", "PLOFT E PLIFTTTT! MAGIAS!!!!!!!!!!!!!!")
  learnSpells()

def learnSpells():
  Char.veioFeiticeiro = True
  Char.where = "Feiticeiro"

