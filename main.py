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

    player_name = input(Fore.CYAN+"What's your name? ")
    time.sleep(1)

    print (Fore.WHITE + f"Hello, {player_name}, you find yourself in a weird forest")
    time.sleep(1)

    print(Fore.BLACK+"Make choices to navigate through the adventure")
    time.sleep(1)


def make_choice(question, options, score_change):
    print(Fore.MAGENTA + Style.DIM + question)
    for i, option in enumerate(options, 1):
        print(f"{i}.{option}")

    while True:
        try:
            choice = int(input(Fore.CYAN + Style.DIM + "Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                # Update global score variable
                global player_score
                player_score += score_change[choice - 1]
                return choice
            else:
                print(Fore.RED + Style.BRIGHT + "Invalid choice! Try again")
        except ValueError:
            print(Fore.LIGHTRED_EX + Style.DIM + "Invalid input. Enter a number.")

def forest_path():
    print("You come across a fork in the path")
    time.sleep(1)
    choice = make_choice("Which part do you take?", ["Go left", "Go right"], [1, -1])

    if choice == 1: 
        print(Fore.GREEN + "You encounter a friendly squirrel. It leads you to safety")
    else:
        print(Fore.RED + "Oh no you stumble into a spider web and get trapped.")

def mountain_climb():
    print(Fore.BLACK + Style.NORMAL + "You reach a steep mountain. What do you do?")
    time.sleep(1)
    choice = make_choice("How do you climb it?", ["Use a rope", "Climb without equipment"], [1, -1])

    if choice == 1: 
        print(Fore.GREEN + "Smart Choice! The rope helps you climb safely.")
    else:
        print(Fore.RED + "Uh-oh! Climbing without equipment is risky. You slip, but luckily, you catch yourself")

def mystical_cave():
    print(Fore.BLACK + "You discover a mystical cave filled with glowing crystals.")
    time.sleep(1)

    choice = make_choice(Fore.CYAN + "What do you do?", ["Enter a cave", "Continue with journey"], [1, -1])
    time.sleep(1)

    if choice == 1: 
        print(Fore.GREEN + "The cave is enchanted! You gain magical powers.")
    else:
        print(Fore.RED + "An evil witch casts a spell on you but a kind fair helps you up.")

def river_crossing():
    print(Fore.BLACK + "You reach a wide river blocking your way.")
    time.sleep(1)

    choice = make_choice(Fore.CYAN + "How do you cross it?", ["Build a raft", "Swim across"], [1, -1])
    time.sleep(1)

    if choice == 1: 
        print(Fore.GREEN + "Great idea! You successfully build a raft and cross the river")
    else:
        print(Fore.RED + "Oh no! Swimming across was a bad idea. You struggle but manage to reach the other side")

def hidden_treasure():
    print(Fore.BLACK + "You stumble upon a hidden treasure chest.")
    time.sleep(1)

    choice = make_choice(Fore.CYAN + "What do you do?", ["Open the chest", "Leave it alone"], [1, -1])
    time.sleep(1)

    if choice == 1: 
        print(Fore.GREEN + "Congratulations! You find valuable treasures inside the chest.")
    else:
        print(Fore.RED + "You decide to leave the chest untouched.")


def play_game():
    introduction()

    # Start of the adventure
    forest_path()
    mountain_climb()
    mystical_cave()
    river_crossing()
    hidden_treasure()

if __name__ == "__main__":
    play_game()
