import pyautogui #macro control library
import time
from tqdm import tqdm #progress bar library

print('Screen', pyautogui.size()) #print users screen resolution

#check user input for valid message deletion quota loop
while True:
    iterations = input('Number of messages to delete [default is 50]: ')
    if len(iterations) < 1:
        iterations = '50'
    try:
        iterations = int(iterations) #checks user input for an integer
    except:
        print('Error:', iterations, 'is not a number')
        continue
    break

#check user input for valid message edit mode setting loop
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

subCount = 0
pyautogui.click(1, 1)   #moves mouse to upper left hand corner and selects app

#message deletion loop
for i in tqdm (range (iterations),  #updates a progress bar for each message deletion cycle
                desc="Deleting",
                ascii=False, ncols=75):
    pyautogui.click(220, 120)   #moves mouse to Friends tab and clicks right
    pyautogui.click(220, 280)   #moves mouse to conversation and clicks right

    while subCount < (2 - modeCorrect):
        subCount += 1
        pyautogui.typewrite(['up'])
        pyautogui.hotkey('ctrlleft', 'a')
        time.sleep(1)
        #sleep is used in this program to prevent it from executing commands
        #faster than discord will accept them

        if editMode in ('y', 'yes', 'Yes'):
            if gateStatus == True:
                pyautogui.typewrite(['backspace', 'x', 'enter'])
                gateStatus ^= t
                time.sleep(1)
                continue
            else:
                gateStatus ^= t

        pyautogui.typewrite(['backspace', 'enter'])
        pyautogui.typewrite(['enter'])
        time.sleep(1)

    subCount = 0

print('Finished:', iterations, 'messages deleted')
