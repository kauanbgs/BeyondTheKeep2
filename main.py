import curses
import time

from menus.menu import menu 
from menus.menuInicial import menuInicial
from menus.menuInicial import Intro
from player.inventory import inventory
from history.introduction import intro
from menus.areas import areas
from history.villages.villageCalthera import calthera
from resources.duel import duel



# curses.wrapper(menu)
curses.wrapper(Intro)
# duel()
