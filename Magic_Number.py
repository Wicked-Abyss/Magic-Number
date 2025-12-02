###   Utilities ###

# The imports are Python keywords that tells Python to load modules, libraries, and packages into your file so you can use their respective functions, classes, variables, etc.
import time
import random
from colorama import Fore, init

# This is my clear function. It allows me to type clear() for the terminal to look clean and uncluttered
def clear():
    print("\033c")

# This is the auto reset function for colorama, I don't trust it so I added a manual one as well
init(autoreset=True)

# Sleep options(These functions allow me to slow down the rate of code that's being spit out):
def time1():
    time.sleep(1)
def time2():
    time.sleep(2)
def time3():
    time.sleep(3)
def time4():
    time.sleep(4)

# Color options (These variables are simple little color options if I choose to embed them):
Red = Fore.RED
Green = Fore.GREEN
Cyan = Fore.CYAN
Blue = Fore.BLUE
Reset = Fore.RESET
###################
## Everything above the # is all the shortcuts and utilities I need in this file

clear()


print("Hello, welcome to your first" + Blue + " mini-game!")

time2()

# The input variable snags the user's name and stores it for safe keeping
Input = input('May I get your name?\n---> ')

time1()

print('Hi ' + Input + ', this first mini-game will be Magic Number!')

time2()

# This input variable is very picky as it only accepts integer responses from the user
Number = int(input('\nPick a number between 1 and 3. What is the magic number, ' + Input + '?\n---> '))

# This variable names the generator that randomly chooses numbers 1-3
Magic_Number = random.randint(1,3)

# If the user guesses correctly, it passes them and reveals the magic number. If not, it proceeds the user into a while loop until the user eventually guesses correctly
if Number == Magic_Number:
    print('Computing answer...')
    
    time3()

    print(Fore.GREEN + "Yay! You guessed right! The number was " + str(Magic_Number) + '!')
else:
    time1()

    print(Fore.RED + 'Sorry, the magic number was ' + str(Magic_Number) + ' :(')

time2()

# This variable is sort of the anchor for this while loop. 
# As long as the user always types y, then the loop will stay active. If anything other than y is entered, it stops the while loop
Again = input('Would you like to try again ' + Input + '?\n---> y or n: ')
while Again == 'y':
    
    # A solution to a tricky problem was putting the generator inside the while loop so it randomizes the numbers everytime the loop is ran through
    # Otherwise, when you make a generator outside of a while loop, it won't actually make a random choice until you throw it through something like a while loop that can restart
    # the randomization each time the run button is pressed
    Magic_Number = random.randint(1,3)
    
    time1()

    Number = int(input('Pick a number between 1 and 3. What is the magic number, ' + Input + '?\n---> '))
    
    # Determines if the user guessed the magic number correctly or not when inside the while loop. If the user passes, it breaks the loop. Otherwise, it will stay active
    if Number == Magic_Number:
        print('Computing answer...')
        
        time3()

        print("Yay! You guessed right! The number was: " + Green + str(Magic_Number) + '!')
        break
    else:
        time1()

        print('Sorry, the magic number was ' + Fore.RED + str(Magic_Number) + ' :(')

## The code above works as expected and displays use of input, conditional statements, while loops, variables, 
#concatenation, and proper use of the time function to prevent code clutter as well as the random function.##