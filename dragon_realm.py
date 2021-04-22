import random
import time

#Introduction goes here
def displayIntro():
    print('''You are in a land full of dragrons. In front of you, you see two caves. In one cave, the dragon is friendly
          and will share his treasure with you. The other dragon is greedy and hungry, and will eat you on sight.''')
    print()




#Player Chooses Cave - Funtion #2








#Game checks players response against random - Function #3










#If Statement about what happened in the cave



#Does the player want to play again with the the game asking for user input
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()