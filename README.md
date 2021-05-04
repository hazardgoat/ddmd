# ddmd (discord dm deleter)
ddmd.py is a Python program for mass deleting Discord DM history.

It creates a macro and runs it a User determined number of times. It has a User enabled mode for overwriting messages with the character "x" prior to deletion, as well as a user enabled mode for entering custom screen coordinates.

You will need to install the PyAutoGUI library, which can be found here: https://pyautogui.readthedocs.io/en/latest/install.html

Operation:
Open ddmd.py in the command line and follow the on-screen instructions. During custom coordinate calibration, the User is asked to move their mouse to specific locations of the Discord application. This is because Discord deselects conversations after each hotkey deletion, so it is nessisary to reselect the conversation again. In order to ensure no selection mistakes and to keep things visually less destracting, during custom coordinates calibration the program prompts the User to set the "Friends" tab as the selection reset point. In practice, this can be anywhere in Discord so long as it isn't the traget conversation.

Troubleshooting:
1) If anyone messages you during the deletion process, that conversation will move to the top of the conversation list. You may need to reinitialize the program and reconfigure the coordinates if the conversation list order changes the target conversation's relative location.
2) An error that occasionally causes the program to misfunction is if it isn't able to start with your most recent message in the conversation visible on screen. This can happen if you forgot to scroll to the most recent message before initializing ddmd.py or if the program encounters a very long contiguous string of messages from the other person in the course of normal operation. To correct this error, end the active process, scroll up to your most recent message in the conversation, and reinitialize the program.
