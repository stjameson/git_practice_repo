# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Steve Jameson
# Creation Date: 05/15/2022
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
    cave = '' #Needs to get user input here.
	while cave != '1' and cave != '2': #Inconsistent use of tabs and spaces in indentation.
		print('Which cave will you go into? (1 or 2)')
		cave = input() #Defining cave twice and should be the chosenCave.

	return caves

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave): #should define 1 and 2 for if and else.
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!'

playAgain = 'yes' #Should get user input to select an option. Not define as always true.
while playAgain = 'yes' or playAgain = 'y':
	displayIntro()
	caveNumber = choosecave() #Late definition of CaveNumber
	checkCave(caveNumber) #Should be chosenCave.
    
	print('Do you want to play again? (yes or no)')
	playAgain = input() #This should be the definition and input function.
	if playAgain == "no": #Should be defined as "no" or "n" to keep consistency with "yes or y".
		print("Thanks for planing")

