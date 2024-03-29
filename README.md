# ddmd (discord dm deleter)
ddmd.py is a Python script macro for mass deleting Discord DM history.

It creates a macro and runs it a User determined number of times. It has a User enabled mode for overwriting messages with the character "x" prior to deletion, as well as a User enabled mode for entering custom screen coordinates.

Users will need to install the PyAutoGUI library, which can be found here: https://pyautogui.readthedocs.io/en/latest/install.html

Operation:
1) Open ddmd.py in the command line and follow the on-screen instructions. 

Notes:
1) During custom coordinate calibration, the User is asked to move their mouse to specific locations of the Discord application. This is because Discord deselects conversations after each hotkey deletion, so it is nessisary to reselect the conversation again. In order to ensure no selection mistakes and to keep things visually less destracting, during custom coordinates calibration the program prompts the User to set the "Friends" tab as the selection reset point. In practice, this can be anywhere in Discord so long as it isn't the traget conversation.
2) The message edit mode is not reccomended for most Users. Enabling the message edit mode will result in spamming a conversation with the letter "x" if no more messages exist to delete or the program is otherwise tripped up.

Troubleshooting:
1) If anyone sends a message during the deletion process, that conversation will move to the top of the conversation list. It may be nessisary to reinitialize the program and reconfigure the coordinates if the conversation list order changes the target conversation's relative location.
2) An error that occasionally causes the program to misfunction is if it isn't able to start with the User's most recent message in the conversation visible on screen. This can happen if the User forgot to scroll to the most recent message before initializing ddmd.py or if the program encounters a very long contiguous string of messages from the other person in the course of normal operation. To correct this error, end the active process, scroll up to the User's most recent message in the conversation, and reinitialize the program.
