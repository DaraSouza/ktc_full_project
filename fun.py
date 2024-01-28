
import time # to make the code interactive
from colorama import Fore, Style, init # color text on the terminal

#launch colorama
init(autoreset = True)

player_score = 0

def introduction():
    print("Welcome to the internet!")
    time.sleep(1)

    user_name = input("Hello user, what is your name? ")
    time.sleep(1)

    print(f"Hello, {user_name} have a look around.")
    time.sleep(1)
    
    print("My name is Mimii, I appear a lot of times to guide you!")
    time.sleep(1)

    print("My notifications pop up in this format. Mimii Alert" )
    time.sleep(1)

    print("Mimii Alert: The game is starting")


introduction()


