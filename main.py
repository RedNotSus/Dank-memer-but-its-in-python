import time
import sys

from gameplay import Game
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"


st = 0
def sp(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(st)
  print()


yes = ['YES', 'yes', 'Yes', 'y', 'Y']
no = ['NO', 'no', 'No', 'n', 'N'] 
all_choices = ['NO', 'no', 'No', 'n', 'N', 'YES', 'yes', 'Yes', 'y', 'Y']

def mainSkeleton():
    choice()


def running():
    Game().play()

def choice():
    choice = True
    while choice:
        user_knowing = input(f"{magenta}Do you know how to play the game?(y/n):\n>> ")
        while user_knowing in all_choices:
            if user_knowing in yes:
                sp(f"\n{bright_cyan}OK, let's continue.....")
                running()
                choice = False
                break
            if user_knowing in no:
                sp(f"\n{bright_white}This is a game about life. You can work on a job, hunt, fish, shop, sell, rob, buy multipliers, to increase money and much much more! Enjoy. ")
                running()
                choice = False
                break
        else:
            print(f"\n{red}Invalid Input")

mainSkeleton()