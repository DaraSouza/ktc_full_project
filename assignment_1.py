# Import dependencies
# A dependency is a library or module that our code needs to function

import time # to make the code interactive
from colorama import Fore, Style, init # color text on the terminal

#launch colorama
init(autoreset = True)

player_score = 0

def introduction():
    # Welcome the player
    time.sleep(1)

    print(Fore.MAGENTA+"Welcome to Python Adventure!")
    time.sleep(1)

    player_name = input(Fore.CYAN+"What's your name?")
    time.sleep(1)

    print(Fore.WHITE + f"Hello, {player_name}, you find yourself in a weird forest")
    time.sleep(1)

    print(Fore.BLACK+"Make choices to navigate through the adventure")
    time.sleep(1)

    favourite_animal = input(Fore.BLUE+"What is your favourite animal? ")
    time.sleep(1)

    print(f"Awww! {favourite_animal} is so cute!")

introduction()