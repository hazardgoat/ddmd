#Use this program to dial in the screen coordinates you need to make ddmd.py run properly. 

#Run sctest.py with the Discord desktop application in fullscreen mode or with the window
#stretching top to bottom of your screen and moved all the way to the left. Make sure that
#the upper left corner of the Discord application window is visible while other programs are
#running. Take note of where the mouse cursor moves and edit the coordinates in this code as 
#nessisary until the mouse cursor moves to the #Friends list tab and then the target conversation. 
#Once you have the correct coordinates, use them when prompted by ddmd.py. If you'd like them to 
#be the default, edit them into ddmd.py

#You will need to install the pyautogui library, which can be found here: 
#https://pyautogui.readthedocs.io/en/latest/install.html

import pyautogui

print('Screen', pyautogui.size()) #displays your screen resolution
pyautogui.click(1,1)
pyautogui.click(220, 120, duration = 1)
pyautogui.click(220, 280, duration = 1)
