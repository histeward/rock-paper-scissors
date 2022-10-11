# rock-paper-scissors
A simple terminal game I wanted to write that I had on my bucket list for ages

**packages**
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

