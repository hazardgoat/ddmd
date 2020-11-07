# ddmd (discord dm deleter)
ddmd is a Python program for mass deleting Discord DM history.

It creates a macro and runs it a user determined number of times. It has a user enabled mode for overwriting messages with the character "x" prior to deletion, as well as a user enabled mode for entering custom screen coordinates.

You will need to install the PyAutoGUI library, which can be found here: https://pyautogui.readthedocs.io/en/latest/install.html

Operation:
Run sctest.py to dial in the exact screen coordinates needed to make ddmd.py work properly for your screen size and resolution.
Use these coordinates for the custom coordinates prompt, or edit them into your ddmd.py file to make them the default. Open the Discord desktop application and set the window to full screen, or at least make the window stretch top to bottom on your screen and move it all the way to the left. Make sure that the upper left-hand corner is visible while other applications are open, and make sure that the private conversation you want to delete messages from is at the top of the conversations list (i.e your most recent DM). Select that conversation and scroll to where your most recent message starts if it is currently off screen, otherwise leave it where it is. Now run ddmd.

You will see the screen flash back and forth between the conversation and the Friends tab (this is normal). The tabs are switched back and forth because Discord wont accept the "up arrow" selection hotkey more than once without leaving the current conversation and returning. The Friends tab was chosen because it is always present and less visually disruptive than other choices when switching back and forth between it and the conversation.

Troubleshooting:
1) If any messages you during the deletion process, that conversation will move up the conversation list as it is the most recent. You will need to reinitialize the program and either reconfigure the coordinates or make the desired conversation the most recent.
2) An error that occasionally causes the program to misfunction is if it isn't able to start with your most recent message in the conversation visible on screen. To correct this if it occurs, scroll up to your most recent message in the conversation and reinitialize the program.
