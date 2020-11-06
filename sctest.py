#Use this program to dial in the screen coordinates you need to make ddmd.py run properly
#Run sctest.py with discord in fullscreen mode. Make note of where the mouse cursor moves
#and edit the coordinates in this code as nessisary until the mouse cursor gos where you want it.
#Once you have the correct coordinates, edit them into ddmd.py

#You will need to install the pyautogui library, which can be found here: 
#https://pyautogui.readthedocs.io/en/latest/install.html

import pyautogui

print('Screen', pyautogui.size()) #displays your screen resolution
pyautogui.click(1,1)
pyautogui.click(220, 120, duration = 1)
pyautogui.click(220, 280, duration = 1)
