##This program seeks to test the probability
##problem presented on the forum as follows
##
##If an item is randomly generated inside of any given box
##of a set of 3 boxes and the user is asked for a box selection
##does the probability of the user having selected the correct box
##remain the same, or increase, when the user is given the option
##to switch choices after the box not containing the object has been
##removed from the selection pool

import random




# box class
class Box:
    def __init__(self):
        self.__hasItem = False
        self.isValidChoice = True

    def showHasItem(self):
        return self.__hasItem

    def doesHaveItem(self):
        self.__hasItem = True

    def resetItemFalse(self):
        self.__hasItem = False

    def inValidChoice(self):
        self.isValidChoice = False

    def resetToValidChoice(self):
        self.isValidChoice = True

    

def main():
    #execute test with switching enabled
    box1 = Box()
    box2 = Box()
    box3 = Box()

    

    #   outside loop loops twice for tests
    #   once nonswitching, once switching
    for ii in range(0, 2):
        # resets values 
        numberOfTests = 0
        correctChoices = 0
        correctBox = False

        # changes doesSwitch depending on which loop
        # iteration is happening
        if ii == 0:
            doesSwitch = False
        else:
            doesSwitch = True
            
        userBox = getUserBox(doesSwitch)

        for i in range(0, 10000):

            # initially set all boxes to not have item
            # all boxes to be valid choices
            # correct box value to be false

            noBoxHasItem(box1, box2, box3)
            resetValidChoices(box1, box2, box3)
            correctBox = False

            # generates item number for item box
            itemBox = random.randint(1,3)


            # sets box object value of correlating box to
            # represent box having item
            
            if itemBox == 1:
                box1.doesHaveItem()
            elif itemBox == 2:
                box2.doesHaveItem()
            elif itemBox == 3:
                box3.doesHaveItem()
            

            # if switching protocol executes switching protocol
            if doesSwitch:
                inValidateChoices(itemBox, userBox, box1, box2, box3)
                userBox = switchUserBox(userBox, box1, box2, box3)
        
            # checks if user box is the same box as the item box
            correctBox = checkIfCorrectBox(userBox, box1, box2, box3)

            numberOfTests = numberOfTests + 1

            if correctBox == True:
                correctChoices = correctChoices + 1
        
            


            
        
        winPercent = getWinPercent(correctChoices, numberOfTests)
        printResults(numberOfTests, winPercent)

        

        if doesSwitch:
            switchWinPercent = winPercent
        else:
            nonSwitchWinPercent = winPercent

    printComparison(switchWinPercent, nonSwitchWinPercent)



def printComparison(switch, nonSwitch):
    print('The success percentage while switching boxes was')
    print(str(switch)+ ' while the success percentage was')
    print(str(nonSwitch) + ' for the nonswitching trial')


    if switch > nonSwitch:
        switchWins()
    else:
        nonSwitchWins()

def switchWins():
    print('For this cycle Switching boxes was the better choice')

def nonSwitchWins():
    print('For this cycle it was better not to switch')



def getUserBox(switching):
    if switching:
        userBox = int(input('Input User choice 1-3 for switching trial '))
    else:
        userBox = int(input('Input User choice 1-3 for non switching trial '))

    return userBox
    

def printResults(numberOfTests, winPercent):
    print(str(numberOfTests)+' Number of tests were run')
    print('The user box was the same box as was containing the item ' + str(winPercent)+ ' percent of the time')
    print('')


def getWinPercent(correctChoices, numberOfTests):
    winPercent = correctChoices / numberOfTests
    return winPercent
        

def checkIfCorrectBox(userBox, box1, box2, box3,):
    correctBox = False
    if userBox == 1 and box1.showHasItem():
        correctBox = True
    elif userBox == 2 and box2.showHasItem():
        correctBox = True
    elif userBox == 3 and box3.showHasItem():
        correctBox = True
    return correctBox


def switchUserBox(userBox, box1, box2, box3):
    if userBox == 1:
        if box2.isValidChoice:
            userBox = 2
        else:
            userBox = 3
    elif userBox == 2:
        if box1.isValidChoice:
            userBox = 1
        else:
            userBox = 3
    elif userBox == 3:
        if box1.isValidChoice:
            userBox = 1
        else:
            userBox = 2
    return userBox

def inValidateChoices(itemBox, userBox, box1, box2, box3):
    if itemBox != 1 and userBox != 1:
        box1.isValidChoice = False
    elif itemBox != 2 and userBox != 2:
        box2.isValidChoice = False
    elif itemBox != 3 and userBox != 3:
        box3.isValidChoice = False


def noBoxHasItem(box1, box2, box3):
    box1.resetItemFalse()
    box2.resetItemFalse()
    box3.resetItemFalse()

def resetValidChoices(box1, box2, box3):
    box1.resetToValidChoice()
    box2.resetToValidChoice()
    box3.resetToValidChoice()
    


main()

    
    
