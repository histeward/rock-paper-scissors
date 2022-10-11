# rock-paper-scissors
A simple terminal game I wanted to write that I had on my bucket list for ages

**Packages**
```python
import sys
from os import system
from time import sleep
from random import choice
```
* I used the `sys` library to write that cool letter by letter reveal function instead of using a normal `print` statement
* from the `os` library import `system` to clear the terminal for a clean look
* from the `time` library import the `sleep` function so it won't feel like lighting mcqueen in your terminal printing out lines
* from the `random` library import the `choice` functinon to make the computer choose a random answer

**2 functions just for show and laziness**
The slow reveal function and the lazy clearing the terminal function. 
```python
def revealPrint(s):
    """
    Takes a string as an argument, prints it out letter by letter every 100s of a second and jumps to the next line
    """
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(1/100)

def clear():
    """
    lazy function to clear the terminal because i did not want type the whole os.system('clear') lol
    """
    system('clear') # If you are on windows change clear to cls
```

**Now the actual game**
```python
def game():
    while True:

        # Defining user choices and the computers choice
        choices = ["rock", "paper", "scissors"]
        computer = choice(choices)

        # Clearing out the terminal for a clean look
        clear()
        
        # Announcing the game in a cool way
        revealPrint("Hello there! Welcome to Rock Paper Scissors!")
        sleep(1.5)
        clear()

        # Asking for user input
        revealPrint("You have the following options.")
        revealPrint("Rock, paper or scissors. Type your answer below and press enter.")
        user_input = input().lower()

        # Making sure user input is valid
        while True:
            if user_input not in choices:
                clear()
                revealPrint("Invalid input, please try again")
                revealPrint('Please enter either rock, paper or scissors')
                user_input = input().lower()
            elif user_input in choices:
                clear()
                break

        # Telling the coices of the user and the computer
        revealPrint(f"You chose {user_input} and the computer chose {computer}")
        sleep(1.5)
         
        # Validating who won and lost
        if user_input == computer:
            revealPrint("It's a tie")
        elif user_input == "rock":
            if computer == "scissors":
                revealPrint("you win")
                sleep(1.5)
            else:
                revealPrint("you lost")
                sleep(1.5)
        elif user_input == "paper":
            if computer == "rock":
                revealPrint("you win")
                sleep(1.5)
            else:
                revealPrint("you lost")
                sleep(1.5)
        elif user_input == "scissors":
            if computer == "paper":
                revealPrint("you win")
                sleep(1.5)
            else:
                revealPrint("you lost")
                sleep(1.5)
        
        _ = ['yes', 'no'] # list to validate user input choice
        revealPrint("would you like to play again yes or no?") 
        rematch = input()

        # User input validation for rematch
        while True:
            if rematch.lower() not in _:
                revealPrint("unvalid input, please enter either yes or no.")
                rematch = input()
            elif True:
                break

        if rematch.lower() != "yes":
            revealPrint("Thank you for playing and till next time!")
            sleep(1.5)
            clear()
            break
```
And don't forget the `if __name__ == "__main__":` at the end
```python
if __name__ == "__main__":
    game()
```
