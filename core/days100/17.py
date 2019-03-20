import random
import time

def displayIntro():
    print('You are in land full of Dragons.')
    time.sleep(2)
    print('In front of you, you see two caves. In one cave the Dragon is friendly and will share his treasure with you.'
          'The other dragon is greedy and hungry, and will eat you alive.' '\n')

def chooseCave():
    cave = " "
    while cave != '1' and cave != '2':
        print('which cave will you go into? (1 or 2)')
        cave = input()

    return cave


def checkCave(chosenCave):
    print('you approached the cave')
    time.sleep(2)
    print('it is dark and spooky...')
    time.sleep(2)
    print('A large Dragon jumps in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if(chosenCave == str(friendlyCave)):
        print('Gives you his treasure!')
    else:
        print('gobbles you in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()

    caveNumber = chooseCave()

    checkCave(caveNumber)

    print('do you want to play again? (yes or no)')
    playAgain = input()

