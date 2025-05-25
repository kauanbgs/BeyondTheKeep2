import curses
import time

from menus.menu import menu  # só se precisar usar recursivamente
from menus.menuInicial import menuInicial  # só se precisar usar recursivamente
from player.inventory import inventory
from history.introduction import intro
from menus.areas import areas



curses.wrapper(areas)
