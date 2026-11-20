# ddmd (Discord DM deleter)

ddmd deletes your own messages from a Discord direct message conversation. It starts with your newest message and works back to the oldest, and it leaves the other person's messages alone. It deletes pictures and files as well as text.

ddmd runs on a Mac with the Discord desktop app. It deletes each message the same way you would by hand, by opening the message's menu and choosing Delete Message.

Deleted messages can't be brought back, so make sure you want them gone before you start.

## What you need

- A Mac
- The Discord desktop app, signed in and set to English
- Python 3
- Permission for your terminal app to control your computer (see Setup)

## Setup

1. Download `ddmd.py` and install the Python packages it uses.

   ```
   pip install pyautogui tqdm pyobjc-framework-applicationservices
   ```

2. Let your terminal app control your computer. Open System Settings, go to Privacy & Security, then Accessibility, and turn on the app you'll run ddmd from (for example Terminal). If that app was already open, quit it and open it again.

## How to use it

1. Open Discord and go to the conversation you want to clear.
2. Scroll all the way to the bottom so your newest messages are loaded. ddmd works backwards from where Discord is scrolled, so anything newer than that gets skipped.
3. Leave the message box empty.
4. In your terminal, go to the folder with `ddmd.py` and run it.

   ```
   python ddmd.py
   ```

5. Type how many messages to delete and press Enter. If you press Enter without a number, it deletes 100.
6. Type `y` and press Enter to start.

ddmd takes about 3 seconds per message, so 1,000 messages take about 45 minutes. While it runs, leave the mouse and keyboard alone. ddmd uses them to work Discord, and using them yourself can get in its way and make it stop.

If your screen locks, ddmd can't keep going. For a long run, open a second terminal window and run `caffeinate -d` to keep the screen on. Press Ctrl-C in that window when you're done.

To stop ddmd early, switch to its terminal window and press Ctrl-C.

## When it stops

When ddmd finishes, it prints how many messages it deleted. If it gets to the start of the conversation first, it stops there.

If something in Discord doesn't look the way ddmd expects, such as a menu that didn't open, it stops and prints a line starting with "Stopped:" that says what went wrong. Fix that and run ddmd again. It picks up with your newest remaining message.

The pip install line is for people who don't use conda. Your own setup still works as before (conda activate ddmd).
