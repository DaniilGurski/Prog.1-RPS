import colorama
import os 
import msvcrt

from colorama import Fore, Back, Style
from textwrap import dedent
from random import choice

colorama.init(autoreset = True)


class RPSgame:
    def __init__(self):
        self.win = self.losses = self.turns = 0
        self.rules = {"R": "S", "P":"R", "S":"P"}
        self.signs = {"R": 
             '''
   _________
  |   |  |  \__
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \____ROCK_____/

             ''',

             "P":
             '''
    __ __ __
   |  |  |  |__
   |¨¨|¨¨|¨¨|  |
__ |¨¨|¨¨|¨¨|¨¨|
\ \|  |  |  |¨¨|
|  \__         |
|              |
 \____PAPER____/

             ''',

             "S":
             '''
 __       __
 \  \   /  /
  \  \ /  /
   \  V  /__ __
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \__SCISSORS___/
             '''}


    def menu_screen(self):
        os.system("cls")

        # dedent removes included white space from multi-strings
        print(Fore.CYAN + dedent(
        r'''
         _____  ______  _____ 
        | ___ \ | ___ \/  ___|
        | |_/ / | |_/ /\ `--. 
        |    /  |  __/  `--. \
        | |\ \ _| |_   /\__/ /
        \_| \_(_)_(_)  \____/
        '''
        ))

        print(f"Coded by: Daniil (2023)\nSigns made by: Wrangman\nLogo made on: patorjk.com\n")

        print(f"{Fore.CYAN}Start game = enter\nReturn to menu from game = enter\nReset game = r\nExit = q")


    def display_choice(self, user, computer):
        os.system("cls")
        print(f"The computer chose: {self.signs[computer]}")
        print(f"You chose: {self.signs[user]}")


    def reset_game(self):
        self.win = self.losses = self.turns = 0


    def run(self):
        rules = self.rules
        underline = "-" * 30
        controls = list(rules.keys())

        print(f"{Fore.CYAN}(R)ock (P)aper (S)cissors: ", end="")
        user = msvcrt.getwch().upper()
        computer = choice(controls)


        # Handling input
        if user == "\r":
            return "menu"
        elif user == "Q":
            return "exit"
        elif user not in controls:
            os.system("cls")
            print(f"{Fore.YELLOW}Valid input requiered.")
            return


        # Revealing choice
        self.display_choice(user, computer)


        # Results
        if user == computer:
            print(f"{Fore.YELLOW}Tie.")
        elif rules[user] == computer:
            print(f"{Fore.GREEN}You made it.")
            self.win += 1
        else:
            print(f"{Fore.RED}You lost.")
            self.losses += 1
        self.turns += 1


        # Game stats 
        print(f"Wins: {self.win} | Losses: {self.losses} | Turns: {self.turns}\n{underline}")
        