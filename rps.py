'''
RPS.PY: Rock papper scissors game

__author__  = "Daniil Gurski"
__version__ = "1.0.0"
__email__   = "daniil.gurski@elev.ga.ntig.se"
'''

from gameclass import RPSgame

import os
import msvcrt
import colorama

game = RPSgame()

while True:
    game.menu_screen()
    key = msvcrt.getwch().upper()

    if key == "\r":
        os.system("cls")
        colorama.init(autoreset=False)
        while True:
            state = game.run()

            if state == "menu":
                break
            elif state == "exit":
                exit()
                
    elif key == "R":
        game.reset_game()

    elif key == "Q":
        exit()