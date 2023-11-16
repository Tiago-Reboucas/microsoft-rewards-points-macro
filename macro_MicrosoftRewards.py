import pyautogui as gui
import pyperclip
import time
import random
import keyboard
import threading
import signal


# Handle exit signal
def handler(signum, frame):
    pass

signal.signal(signal.SIGINT, handler)

# Pause/Continue
def pause_resume():
    global pause, event

    if pause:
        pause = False
        event.set()
        print("Resuming...")
    else:
        pause = True
        event.clear()
        print(f"Macro paused. Press <{pause_hotkey.upper()}> to resume.")


pause_hotkey = "ctrl + i"
keyboard.add_hotkey(pause_hotkey, pause_resume)
pause = False
finished = False

def rd():
    return random.uniform(0.9, 1.1)


# Repeated process
count = 1
def macro_start(event):
    global search ,pause, count, finished, error

    error = 0
    while len(search) > 0:
        if pause: break

        # Check if its in the right spot
        time.sleep(2*rd())
        event.wait()
        gui.doubleClick(search_pos[0], search_pos[1])
        time.sleep(0.2*rd())
        gui.hotkey('ctrl', 'c')
        time.sleep(0.1*rd())
        old_search = pyperclip.paste()
        event.wait()

        if old_search == "" or old_search is None or len(old_search) > len(search):
            time.sleep(0.5*rd())
            gui.write(search+'x')
            error += 1
            if error == 5:
                print("\r\n====TO MANY ERRORS====\r\n")
                input()
                finished = True
                break
        event.wait()

        if old_search == search:
            search = search[:len(search)-1]
        
        # Do the search
        if len(search) > 0:
            time.sleep(0.5*rd())
            gui.click(search_pos[0], search_pos[1])
            time.sleep(0.5*rd())
            gui.press('backspace')
            time.sleep(0.1*rd())
            gui.press('enter')
            count += 1
            event.wait()

    if pause is False and finished is False: 
        # Open Rewards
        time.sleep(0.5)
        gui.click(url_pos[0], url_pos[1])
        time.sleep(0.5)
        gui.press('r')
        time.sleep(0.5)
        gui.press('enter')
        event.wait()

        # Open Daily set
        time.sleep(3)
        gui.press('down')
        time.sleep(0.5)
        gui.press('down')
        time.sleep(0.5)
        event.wait()
        gui.click(daily_pos1[0], daily_pos1[1])
        time.sleep(2.5*rd())
        gui.hotkey('ctrl', 'w')
        # gui.click(closeTab_pos[0], closeTab_pos[1])
        time.sleep(1*rd())
        event.wait()
        gui.click(daily_pos2[0], daily_pos2[1])
        time.sleep(2.5*rd())
        gui.hotkey('ctrl', 'w')
        # gui.click(closeTab_pos[0], closeTab_pos[1])
        time.sleep(1*rd())
        event.wait()
        gui.click(daily_pos3[0], daily_pos3[1])

        # End of Macro
        errors = "erro" if error == 1 else "errors"
        print(f"\r\n---Macro Finished---\r\nTotal of {count} searches\r\nEncountered {error} {errors}\r\nTook {time.time() - time_0:.2f}s")
        input()


# Check mouse position
def check_mouse_position():
    time.sleep(2)
    print(f"({gui.position()[0]}, {gui.position()[1]})")

    while True:
        again = input("Check positon again? (y/n) ")
        if again.lower() == 'n': return False
        else: return True

################################# UNCOMMENT THE THREE LINES BELLOW TO CHECK MOUSE POSITION #################################
again = True
while again is True:
    again = check_mouse_position()
##########################################################################################################################

# ----- Positions -----
# ############### Edit the lines bellow with your positions ###############
# Browser Position on your toolbar
browser_pos = (510, 1058)

# First search position when a "new tab" is opened on Microsoft Edge
search_pos1 = (1083, 148)

# Search bar position on Bing website (OBS: mouse position must be after the "search" string)
search_pos = (527, 111)

# URL search bar position (where you input websites addresses)
url_pos = (480, 48)

# Daily set positions
daily_pos1 = (586, 855)
daily_pos2 = (1168, 855)
daily_pos3 = (1575, 855)

# Close Tab position (used only if your tabs are not closing with "ctrl+w", then uncomment lines 103 and 109)
closeTab_pos = (554, 15)
# --------------------

# Set the "search" value
search = "tttttuuuuuvvvvvwwwwwxxxxxyyyyyzzzz"
searches = input(f"Press <{pause_hotkey.upper()}> at any time to pause/continue the macro.\nHow many searches? ")

if searches != "":
    if input("Search type 1 or 2? ") == "2":
        search = "hhhhhiiiiijjjjjkkkkklllllmmmmmnnnn"
    
    search = search[:int(searches)]

time_0 = time.time()

# Start first steps of the macro
# Open browser
time.sleep(1)
gui.click(browser_pos[0], browser_pos[1])

# Click os search bar
time.sleep(2)
gui.click(search_pos1[0], search_pos1[1])

# Insert full search
gui.typewrite(search)
gui.press('enter')


# Threading
event = threading.Event()
event.set()
t = threading.Thread(target=macro_start, args=(event,))
t.start()
