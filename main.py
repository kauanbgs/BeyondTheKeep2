import curses
import time

from menus.menu import menu  # só se precisar usar recursivamente
from menus.menuInicial import menuInicial  # só se precisar usar recursivamente
from areas.tavern import tavernIntro
from history.villages.villageVentogard import ventogardIntro
from areas.fundition import joinItens, showItens
from player.inventory import inventory
from areas.blacksmith import blacksmithIntro
from resources.duel import duel
from assets.things import DicesAnimation
from history.introduction import intro



curses.wrapper(menu)
