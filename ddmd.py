import pyautogui
import time
import re

print('Screen', pyautogui.size())   #print users screen resolution

#check user input for valid message deletion quota
while True:
    iterations = input('Number of messages to delete [default is 50]: ')
    if len(iterations) < 1:
        iterations = 50
    try:
        iterations = int(iterations)
    except ValueError:
        print('Error:', iterations, 'is not a number')
        continue
    break

#check user input for valid message edit mode setting
while True:
    editMode = input('Edit mode? y/n [default is n]: ')
    if len(editMode) < 1:
        editMode = 'n'
    elif editMode not in ('y', 'yes', 'Yes', 'n', 'no', 'No'):
        print('Unknown input: Please enter y or n')
        continue
    if editMode not in ('y', 'yes', 'Yes'):
        modeCorrect = 1
    else:
        modeCorrect = 0
    break

#logic gate for when edit mode is turned on
gateOpen = True
gateClosed = False
t = gateOpen ^ gateClosed
gateStatus = gateOpen

mainCount = 0   #count of how many times message deletion loop has run
subCount = 0    #count used to moderate message deletion loop runs when edit mode on vs off, as it needs to cycle through twice in the main loop when edit mode is on
pyautogui.click(1, 1)   #moves mouse to upper left hand corner and selects app

while mainCount < iterations:
    pyautogui.click(220, 100)   #moves mouse to Friends tab and left-clicks
    pyautogui.click(220, 220)   #moves mouse to conversation and left-clicks

    while subCount < (2 - modeCorrect):
        subCount += 1
        pyautogui.typewrite(['up'])
        pyautogui.hotkey('ctrlleft', 'a')
        time.sleep(1)   #sleeps are used to prevent execution of commands faster than discord will accept them

        if editMode in ('y', 'yes', 'Yes'):
            if gateStatus == True:
                pyautogui.typewrite(['backspace', 'x', 'enter'])
                gateStatus ^= t   #toggles logic gate so next time around it will delete the message rather than overwrite it
                time.sleep(1)
                continue
            else:
                gateStatus ^= t   #toggles logic gate so next time around it will overwrite the message rather than delete it

        pyautogui.typewrite(['backspace', 'enter'])
        pyautogui.typewrite(['enter'])
        time.sleep(1)

    subCount = 0
    mainCount += 1

print('Finished:', iterations, 'messages deleted')
