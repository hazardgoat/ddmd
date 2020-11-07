import pyautogui    #macro control library
import time
from tqdm import tqdm   #progress bar library

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
    editMode = input('Edit mode? y/n: ')
    if len(editMode) < 1:
        editMode = 'n'
        print('editMode off')
    elif editMode not in ('y', 'yes', 'Yes', 'n', 'no', 'No'):
        print('Invalid input: Please enter y or n')
        continue
    if editMode not in ('y', 'yes', 'Yes'):
        modeCorrect = 1
    else:
        modeCorrect = 0
    break

#default screen coordinates
xa = 220    #Friends tab x default coordinate
ya = 120    #Friends tab y default coordinate
xb = 220    #conversation tab x default coordinate
yb = 280    #conversation tab y default coordinate
print('Screen', pyautogui.size())   #print users screen resolution
print('Default screen coordinates', (xa, xb),'and', (xb, yb))

#checks user input for valid custom coordinate mode setting
while True:
    ccMode = input('Custom screen coordinates? y/n: ')
    if len(ccMode) < 1:
        ccMode = 'n'
        print('ccMode off')
    elif ccMode not in ('y', 'yes', 'Yes', 'n', 'no', 'No'):
        print('Invalid input: Please enter y or n')
        continue
    elif ccMode in ('n', 'no', 'No'):
        break
    else:
        while True:    #starts loops asking for user to input screen coordinates
            xa = input('Friends tab X coordinate: ')
            try:
                xa = int(xa)
            except:
                print('Invalid input:', xa, 'is not a number')
                continue
            while True:
                ya = input('Friends tab Y coordinate: ')
                try:
                    ya = int(ya)
                except:
                    print('Invalid input:', ya, 'is not a number')
                    continue
                while True:
                    xb = input('Conversation tab X coordinate: ')
                    try:
                        xb = int(xb)
                    except:
                        print('Invalid input:', xb, 'is not a number')
                        continue
                    while True:
                        yb = input('Conversation tab Y coordinate: ')
                        try:
                            yb = int(yb)
                        except:
                            print('Invalid input:', yb, 'is not a number')
                            continue
                        break
                    break
                break
            break
        break
    break

#logic gate for when edit mode is turned on
gateOpen = True
gateClosed = False
t = gateOpen ^ gateClosed
gateStatus = gateOpen

count = 0
pyautogui.click(1, 1)   #moves mouse to upper left hand corner and selects app

#message deletion loop
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
