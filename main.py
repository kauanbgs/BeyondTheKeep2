import curses
import time

from menus.menuInicial import menuInicial  
# from player.inventory import inventory
# from history.introduction import intro
# from menus.areas import areas
# from history.villages.villageCalthera import calthera



curses.wrapper(menuInicial)