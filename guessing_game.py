"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

answer = random.randint(1,10)
attempts = 1


print("Welcome to the the number guessing game!\n")

while True:
	try:
		guess = int(input("I'm thinking of a number between 1 and 10... \n Can you guess the number?  "))	
	except ValueError:
		print("Oh no! That's not a valid value. Try again...")
	else:
		
		while guess != answer:		
			if guess > answer:
				guess = int(input("It's lower...Guess again!  "))
				attempts = attempts + 1
			elif guess < answer:
				guess = int(input("It's higher...Try again!  "))
				attempts = attempts +1
			elif guess == answer:	
				break
	break
print("Got it! Nice work!\n It took you {} attempts to guess the number".format(attempts))
print("GAME OVER!")

# Kick off the program by calling the start_game function.
start_game()
