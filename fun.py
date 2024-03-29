
import time # to make the code interactive
from colorama import Fore, Style, init # color text on the terminal

#launch colorama
init(autoreset = True)

player_score = 0

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


def valentine_day():
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

    print("Today's edition is")
    time.sleep(1)

    print("...")
    time.sleep(1)

    print("...")
    time.sleep(1)

    print("Valentine's Day!!")
    time.sleep(1)

    print("Mimii alert: Have fun now!")
    time.sleep(1)



    question = make_choice("Valentine's day was named after a saint, yes or no? ", ["Yes", "No"], [1, -1])
    if question == 1: 
        print(Fore.GREEN + "Yes you are right, You get one point!")
    elif question == "Mimii" :
        print("The Saint is the patron saint of love and kindness")
    else:
        print(Fore.RED + "Sorry to disappoint you, but you are wrong.")
        print("Mimii alert: Don't hesitate to call on me for help, all you need to say is Mimii")

    question = make_choice("What's the main colour of Valentine's Day", ["Red", "Pink"], [1, -1]) 
    if question == 1:
        print("Yes, well done, you get one point")
    elif question == "Mimii":
        print("Which colour do you often see people wear when it's Valentine's day?")
    else:
        print("Sorry it's red, try again next time!")
    
    question = make_choice("When is Valentine's day?", ["Feb 14th", "Feb 15th"], [1, -1])
    if question == 1:
        print("Well done! You get one point")
    elif question == "Mimii":
        print("If it's Feb 7th, then, valentine's day would be in a week.")
    else:
        print("Did you actually get that wrong? Come on, I hope this is a joke!")
    
    question = make_choice("Which food is gifted commonly on Valentine's day?", ["Chocolate", "Sweet"], [1, -1])
    if question == 1:
        print("I knew you would get it! You get one point")
    elif question == "Mimii":
        print("The answer has a len of 9")
    else:
        ("Seriously! How do you not know?")

    print("This simple Valentine's Day Questionnaire has come to an end.")
    print("Did you enjoy this questionnaire?")
    print("Happy Early Valentine's Day!")
    
valentine_day()
