import sys
from os import system
from time import sleep
from random import choice

def revealPrint(s):
    """
    Takes a string as an argument and prints it out letter by letter everu 0.01 of a second
    and jumps to the next line
    """
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(1/100)

def clear():
    """
    lazy function to clear the whole terminal
    because i do not want to type the whole os.system('clear') lol
    change clear to cls if on windows
    """
    system('clear')

def game():
    while True:
        # defining user choice and computer choice
        choices = ["rock", "paper", "scissors"]
        computer = choice(choices)
        
        # clearing the terminal
        clear()

        # announcing the game
        revealPrint("Hello! Let's play rock paper scissors")
        sleep(1.5)
        clear()
        revealPrint("You have the following options.")
        revealPrint("Rock | Paper | Scissors")

        # asking user input
        while True:
            user_input = input("--> ").lower()
            if user_input not in choices:
                revealPrint("Unvalid input.")
                revealPrint("Please try again.")
                continue
            else:
                break

        # displaying both inputs
        revealPrint(f"you played {user_input} against {computer}")
        sleep(0.5)

        # win lose logic
        if user_input == computer:
            revealPrint("It's a tie")
        elif user_input == "rock" and computer == "scissors":
            revealPrint("You win!")
        elif user_input == "paper" and computer == "rock":
            revealPrint("You win!")
        elif user_input == "scissors" and computer == "paper":
            revealPrint("You win!")
        else:
            revealPrint("You lost!")

        # asking user for rematch
        yesNo = ["yes", "no"]
        revealPrint("would you like to play again?")

        while True:
            rematch = input("--> ").lower()
            if rematch not in yesNo:
                revealPrint("Unvalid input.")
                revealPrint("Please try again.")
                continue
            else:
                clear()
                break

        if rematch == "yes":
            continue
        else:
            break

if __name__ == "__main__":
    game()
