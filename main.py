#Imports
from termcolor import colored
from random import randint
import time, sys
import math

#Variables

playerScore = 0
cpuScore = 0
rToR = 0
rToP = 0
rToS = 0
pToP = 0
pToS = 0
pToR = 0
sToS = 0
sToP = 0
sToR = 0
preMove = "n/a"
curMove = ""
robotMove = ""
afterS = [sToS, sToP, sToR]
highestS = max(afterS)
afterP = [pToR, pToS, pToP]
highestP = max(afterP)
afterR = [rToR, rToS, rToP]
highestR = max(afterR)
scorePlus = ""


#Functions
def skip():
    print('')


def time_print(text, delay=0.06):  #Letter By Letter
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print
    skip()


def acessAIDCS():
    while True:
        openData = input()
        if (openData == "AIDCS"):
            print("\033c")
            print("Player Score:", playerScore)
            skip()
            time.sleep(.5)
            print("Computer Score:", cpuScore)
            skip()
            time.sleep(.5)
            print("Rock to Rock:", rToR)
            skip()
            time.sleep(.5)
            print("Rock to Paper:", rToP)
            skip()
            time.sleep(.5)
            print("Rock to Scizors:", rToS)
            skip()
            time.sleep(.5)
            print("Paper to Paper:", pToP)
            skip()
            time.sleep(.5)
            print("Paper to Rock:", pToR)
            skip()
            time.sleep(.5)
            print("Paper to Scizors:", pToS)
            skip()
            time.sleep(.5)
            print("Scizors to Scizors:", sToS)
            skip()
            time.sleep(.5)
            print("Scizors to Rock:", sToR)
            skip()
            time.sleep(.5)
            print("Scizors to Paper:", sToP)


def cpuMove():
    eqaulVal = 0
    global robotMove
    global curMove
    if (curMove == "Scizors"):
        if (preMove == "Scizors"):
            global sToS
            sToS += 1
        elif (preMove == "Rock"):
            global rToS
            rToS += 1
        elif (preMove == "Paper"):
            global pToS
            pToS += 1
    elif (curMove == "Rock"):
        if (preMove == "Scizors"):
            global sToR
            sToR += 1
        elif (preMove == "Rock"):
            global rToR
            rToR += 1
        elif (preMove == "Paper"):
            global pToR
            pToR += 1
    elif (curMove == "Paper"):
        if (preMove == "Scizors"):
            global sToP
            sToP += 1
        elif (preMove == "Rock"):
            global rToP
            rToP += 1
        elif (preMove == "Paper"):
            global pToP
            pToP += 1

    afterS = [sToS, sToP, sToR]
    highestS = max(afterS)
    if (afterS[0] == highestS):
        highestS = "sToS"
    elif (afterS[1] == highestS):
        highestS = "sToP"
    elif (afterS[2] == highestS):
        highestS = "sToR"
    afterP = [pToR, pToS, pToP]
    highestP = max(afterP)
    if (afterP[0] == highestP):
        highestP = "pToR"
    elif (afterS[1] == highestS):
        highestP = "pToS"
    elif (afterS[2] == highestS):
        highestP = "pToP"
    afterR = [rToR, rToS, rToP]
    highestR = max(afterR)
    if (afterR[0] == highestR):
        highestR = "rToR"
    elif (afterR[1] == highestR):
        highestR = "rToS"
    elif (afterR[2] == highestR):
        highestR = "rToP"

    if (preMove == "Rock"):
        if (highestR == "rToR"):
            eqaulVal += 1
        elif (highestR == "rToP"):
            eqaulVal += 1
        elif (highestR == "rToS"):
            eqaulVal += 1
        if (eqaulVal == 1):
            if (highestR == "rToR"):
                robotMove = "Paper"
            elif (highestR == "rToP"):
                robotMove = "Scizors"
            elif (highestR == "rToS"):
                robotMove = "Rock"
        else:
            for x in range(4):
                randomChoice = randint(1, 3)
            if (randomChoice == 1):
                robotMove = "Rock"
            elif (randomChoice == 2):
                robotMove = "Scizors"
            elif (randomChoice == 3):
                robotMove = "Paper"
            else:
                print(
                    colored(
                        "<There is an error, please make sure you dont mess with values>",
                        "red"))
                time.sleep(3)
                quit()

    elif (preMove == "Paper"):
        if (highestP == "pToP"):
            eqaulVal += 1
        elif (highestP == "pToR"):
            eqaulVal += 1
        elif (highestP == "pToS"):
            eqaulVal += 1
        if (eqaulVal == 1):
            if (highestP == "pToR"):
                robotMove = "Paper"
            elif (highestP == "pToP"):
                robotMove = "Scizors"
            elif (highestP == "pToS"):
                robotMove = "Rock"
        else:
            for x in range(4):
                randomChoice = randint(1, 3)
            if (randomChoice == 1):
                robotMove = "Rock"
            elif (randomChoice == 2):
                robotMove = "Scizors"
            elif (randomChoice == 3):
                robotMove = "Paper"
            else:
                print(
                    colored(
                        "<There is an error, please make sure you dont mess with values>",
                        "red"))
                time.sleep(3)
                quit()
    elif (preMove == "Scizors"):
        if (highestS == "sToS"):
            eqaulVal += 1
        elif (highestS == "sToR"):
            eqaulVal += 1
        elif (highestS == "sToP"):
            eqaulVal += 1
        if (eqaulVal == 1):
            if (highestS == "sToR"):
                robotMove = "Paper"
            elif (highestS == "sToP"):
                robotMove = "Scizors"
            elif (highestS == "sToS"):
                robotMove = "Rock"
        else:
            for x in range(4):
                randomChoice = randint(1, 3)
            if (randomChoice == 1):
                robotMove = "Rock"
            elif (randomChoice == 2):
                robotMove = "Scizors"
            elif (randomChoice == 3):
                robotMove = "Paper"
            else:
                print(
                    colored(
                        "<There is an error, please make sure you dont mess with values>",
                        "red"))
                time.sleep(3)
                quit()
    elif (preMove == "n/a"):
        for x in range(4):
            randomChoice = randint(1, 3)
            if (randomChoice == 1):
                robotMove = "Rock"
            elif (randomChoice == 2):
                robotMove = "Scizors"
            elif (randomChoice == 3):
                robotMove = "Paper"
            else:
                print(
                    colored(
                        "<There is an error, please make sure you dont mess with values>",
                        "red"))
                time.sleep(3)
                quit()
    else:
        print(
            colored(
                "<There is an error, please make sure you dont mess with values>",
                "red"))
        time.sleep(3)
        quit()
    print(robotMove)


def findWinner():
    global playerScore
    global cpuScore
    global scorePlus
    if (robotMove == "Scizors"):
        if (curMove == "Scizors"):
            scorePlus = "No One"
        elif (curMove == "Rock"):
            scorePlus = "Player"
            playerScore += 1
        elif (curMove == "Paper"):
            scorePlus = "CPU"
            cpuScore += .5
    elif (robotMove == "Rock"):
        if (curMove == "Rock"):
            scorePlus = "No One"
        elif (curMove == "Scizors"):
            scorePlus = "CPU"
            cpuScore += .5
        elif (curMove == "Paper"):
            scorePlus = "Player"
            playerScore += .5
    elif (robotMove == "Paper"):
        if (curMove == "Paper"):
            scorePlus = "No One"
        elif (curMove == "Scizors"):
            scorePlus = "Player"
            playerScore += .5
        elif (curMove == "Rock"):
            scorePlus = "CPU"
            cpuScore += 1


#Main Loop
while True:
    time_print(colored("Rock, Paper, Scizors Machine Learning Bot", "blue"))
    time.sleep(1)
    skip()
    print(colored("[1]Play", "cyan"))
    print(colored("[2]About", "cyan"))
    time.sleep(1)
    skip()
    mainMenuChoice = input(colored("   >>>", "green"))
    if (mainMenuChoice == "1"):
        print("\033c")
        time.sleep(1)
        break
    elif (mainMenuChoice == "2"):
        print("\033c")
        time_print(
            colored(
                "This is a Machine Learning Bot that learns the patterns of your moves and uses them to its advantage.",
                "cyan"))
        time.sleep(3)
        skip()
        time_print(colored("Done Reading? Press any key to escape.", "yellow"))
        time.sleep(1)
        skip()
        finishReading = input(colored("   >>>", "green"))
        time.sleep(1)
        break
    else:
        time.sleep(1)
        print("\033c")
        time_print(colored("<Please type in a valid choice>", "red"))
        time.sleep(1)
        print("\033c")

while True:
    print("\033c")
    print(playerScore, "-", cpuScore)
    skip()
    print(colored("[1]Rock", "cyan"))
    print(colored("[2]Paper", "cyan"))
    print(colored("[3]Scizors", "cyan"))
    skip()
    time.sleep(.5)
    moveChoice = input(colored("   >>>", "green"))
    if (moveChoice == "1"):
        curMove = "Rock"
        cpuMove()
        print("\033c")
        time.sleep(1)
        print(colored(f"\nComputer Move: {robotMove}", "blue"))
        time.sleep(1)
        findWinner()
        print(colored(f"\nPoint goes to {scorePlus}", "blue"))
        time.sleep(1)
        print("\033c")
        preMove = "Rock"
    elif (moveChoice == "2"):
        curMove = "Paper"
        cpuMove()
        print("\033c")
        print(colored(f"\nComputer Move: {robotMove}", "blue"))
        time.sleep(1)
        findWinner()
        print(colored(f"\nPoint goes to {scorePlus}", "blue"))
        time.sleep(1)
        print("\033c")
        findWinner()
        preMove = "Paper"
    elif (moveChoice == "3"):
        curMove = "Scizors"
        cpuMove()
        print("\033c")
        print(colored(f"\nComputer Move: {robotMove}", "blue"))
        time.sleep(1)
        findWinner()
        print(colored(f"\nPoint goes to {scorePlus}", "blue"))
        time.sleep(1)
        print("\033c")
        findWinner()
        preMove = "Scizors"
    else:
        time.sleep(.5)
        print(colored("<That was not a valid choice>", "red"))
        time.sleep(2)
    if (cpuScore == 15):
        print("\033c")
        time.sleep(.5)
        print(
            colored("Oh no! Looks like the Machine Learning Bot beat you!",
                    "red"))
        time.sleep(.5)
        acessAIDCS()
        break
    elif (playerScore == 15):
        print("\033c")
        time.sleep(.5)
        print(
            colored(
                "Wow! It looks like you just beat the Machine Learning Bot!",
                "green"))
        time.sleep(.5)
        acessAIDCS()
        break
