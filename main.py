import curses
import time

from menus.menu import menu  # só se precisar usar recursivamente
from menus.menuInicial import menuInicial  # só se precisar usar recursivamente
from player.inventory import inventory
from history.introduction import intro
from menus.areas import areas
from history.villages.villageCalthera import calthera
from resources.duel import duel



# curses.wrapper(menu)
curses.wrapper(menuInicial)
