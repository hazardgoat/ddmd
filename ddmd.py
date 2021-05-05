import pyautogui    #macro control library
import sys
import time
from tqdm import tqdm   #progress bar library

print('')
print('DDMD is a python macro that automates mass deletion of Discord messages.')
print('')

#check user input for valid message deletion quota
while True:
    iterations = input('Number of messages to delete: ')
    if len(iterations) < 1:
        iterations = 100
    try:
        iterations = int(iterations)    #checks user input for an integer
    except:
        print('Invalid input:', iterations, 'is not a number')
        continue
    break

#check user input for valid message edit mode setting
while True:
    editMode = input('Edit messages before deletion? y/n: ')
    if len(editMode) < 1:
        editMode = 'n'
    elif editMode not in ('y', 'yes', 'Yes', 'n', 'no', 'No'):
        print('Invalid input: Please enter y or n')
        continue
    if editMode not in ('y', 'yes', 'Yes'):
        modeCorrect = 1
        print('editMode off')
    else:
        modeCorrect = 0
        print('editMode on')
    break

#default screen coordinates
xa = 220    #Friends tab x default coordinate
ya = 120    #Friends tab y default coordinate
xb = 220    #conversation tab x default coordinate
yb = 330    #conversation tab y default coordinate
print('')
print('Screen', pyautogui.size())   #print users screen resolution
print('Default screen coordinates', (xa, xb),'and', (xb, yb))

#checks user input for valid custom coordinate mode setting
while True:
    ccMode = input('Custom screen coordinates? (recommended for first time users) y/n: ')
    if len(ccMode) < 1:
        ccMode = 'y'
    elif ccMode not in ('y', 'yes', 'Yes', 'n', 'no', 'No'):
        print('Invalid input: Please enter y or n')
        continue
    elif ccMode in ('n', 'no', 'No'):
        print('ccMode off')
        break
    if ccMode == 'y':
        print('ccMode on')
        xa = None
        ya = None
        xb = None
        yb = None
        counter = 0

        print('')
        print('Position cursor over the "Friends" tab in Discord and then press Ctrl-C.')
        print('')

        while xa == None or ya == None or xb == None or yb == None:
            try:
                x, y = pyautogui.position()
                positionStr = '(' + str(x) + ', ' + str(y) + ')'
                print(positionStr, end='')
                print('\b' * len(positionStr), end='')
            except KeyboardInterrupt:
                counter = counter + 1
                if counter == 1:
                    print('\b' * len(positionStr), end='')
                    print('"Friends" tab coordinates are:', positionStr)
                    xa = x
                    ya = y
                    print('')
                    print('Next, position the cursor over the desired conversation and press Ctrl-C.')
                if counter == 2:
                    print('\b' * len(positionStr), end='')
                    print('Conversation tab coordinates are:', positionStr)
                    print('')
                    xb = x
                    yb = y
    break

#logic gate for when edit mode is turned on
gateOpen = True
gateClosed = False
t = gateOpen ^ gateClosed
gateStatus = gateOpen

count = 0
#pyautogui.click(1, 1)   #moves mouse to upper left hand corner and selects app

#message deletion loop
while True:
    beginDeletion = input('Start deleting messages? y/n: ')
    if len(beginDeletion) < 1:
        pass
    elif beginDeletion not in ('y', 'yes', 'Yes', 'n', 'no', 'No'):
        print('Invalid input: Please enter y or n')
        continue
    elif beginDeletion in ('n', 'no', 'No'):
        print('Exiting')
        exit()
    break

try:
    print('To exit program, select the command line window and press Ctrl-C.')
    for i in tqdm (range (iterations), desc="Deleting", ascii=False):
        pyautogui.click(xa, ya)   #moves mouse to Friends tab and clicks right
        pyautogui.click(xb, yb)   #moves mouse to conversation tab and clicks right

        while count < (2 - modeCorrect):
            count += 1
            pyautogui.typewrite(['up'])    #up arrow key
            pyautogui.hotkey('ctrlleft', 'a')   #left ctrl+a key combination
            time.sleep(1)   #sleep used to prevent execution of commands faster than discord will accept them

            if editMode in ('y', 'yes', 'Yes'):
                if gateStatus == True:
                    pyautogui.typewrite(['backspace', 'x', 'enter'])    #backspace key then x key then enter key
                    gateStatus ^= t    #toggles the logic gate
                    time.sleep(1)
                    continue
                else:
                    gateStatus ^= t

            pyautogui.typewrite(['backspace', 'enter'])    #backspace key then enter key
            pyautogui.typewrite(['enter'])     #enter key (seperate commant because it executes too fast for discord)
            time.sleep(1)

        count = 0

    print('Finished:', iterations, 'messages deleted')
except KeyboardInterrupt:
    print('Exiting')
    exit()
    
