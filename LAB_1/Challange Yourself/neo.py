# made by kunal ugale with ai but idia was mine

import os
import sys
import time
import threading

try:
    import keyboard
except ImportError:
    keyboard = None

import pyautogui

# Speed optimizations
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

base_dir = os.path.dirname(os.path.abspath(__file__))


def load_program(filename):
    with open(os.path.join(base_dir, filename), "r", encoding="utf-8") as f:
        return f.read().strip()


program1 = load_program("Q1_Answer.txt")
program2 = load_program("Q2_Answer.txt")
program3 = load_program("Q3_Answer.txt")
program4 = load_program("Q4_Answer.txt")
program5 = load_program("Q5_Answer.txt")

typing = False
stop_requested = False


def type_text(text, label):
    global typing, stop_requested

    typing = True
    stop_requested = False

    print(f"Typing {label} starts in 3 seconds...")
    time.sleep(3)

    if stop_requested:
        typing = False
        return

    try:
        # Extremely fast typing
        keyboard.write(text, delay=0)

    except Exception as e:
        print("Error:", e)

    typing = False

    if stop_requested:
        print(f"{label} stopped.")
    else:
        print(f"{label} done.")


def start_program(text, label):
    if typing:
        print(f"{label} is already running. Press Shift+S to stop it.")
        return

    threading.Thread(
        target=type_text,
        args=(text, label),
        daemon=True
    ).start()

    print(f"{label} started. Press Shift+S to stop.")


def start_program1():
    start_program(program1, "Program 1")


def start_program2():
    start_program(program2, "Program 2")


def start_program3():
    start_program(program3, "Program 3")


def start_program4():
    start_program(program4, "Program 4")


def start_program5():
    start_program(program5, "Program 5")


def stop_typing():
    global stop_requested

    if typing:
        stop_requested = True
        if keyboard is not None:
            keyboard.release('shift')
        print("Stopping current typing...")
    else:
        print("Nothing is being typed right now.")


def exit_program():
    global stop_requested

    stop_requested = True

    print("Exiting...")

    if keyboard is not None:
        keyboard.unhook_all_hotkeys()
    sys.exit(0)


def register_hotkeys():
    if keyboard is None:
        print("The 'keyboard' package is required. Install it with: pip install keyboard")
        return

    if sys.platform == "darwin":
        combos_1 = ["shift+1", "command+1"]
        combos_2 = ["shift+2", "command+2"]
        combos_3 = ["shift+3", "command+3"]
        combos_4 = ["shift+4", "command+4"]
        combos_5 = ["shift+5", "command+5"]
        combos_stop = ["shift+s", "command+s"]
        combos_exit = ["shift+q", "command+q"]
    else:
        combos_1 = ["shift+1", "ctrl+1"]
        combos_2 = ["shift+2", "ctrl+2"]
        combos_3 = ["shift+3", "ctrl+3"]
        combos_4 = ["shift+4", "ctrl+4"]
        combos_5 = ["shift+5", "ctrl+5"]
        combos_stop = ["shift+s", "ctrl+s"]
        combos_exit = ["shift+q", "ctrl+q"]

    for combo in combos_1:
        keyboard.add_hotkey(combo, start_program1, suppress=True)
    for combo in combos_2:
        keyboard.add_hotkey(combo, start_program2, suppress=True)
    for combo in combos_3:
        keyboard.add_hotkey(combo, start_program3, suppress=True)
    for combo in combos_4:
        keyboard.add_hotkey(combo, start_program4, suppress=True)
    for combo in combos_5:
        keyboard.add_hotkey(combo, start_program5, suppress=True)
    for combo in combos_stop:
        keyboard.add_hotkey(combo, stop_typing, suppress=True)
    for combo in combos_exit:
        keyboard.add_hotkey(combo, exit_program, suppress=True)


register_hotkeys()

print("Ready!")
print("Press Shift+1 or Command+1 / Ctrl+1 -> Program 1")
print("Press Shift+2 or Command+2 / Ctrl+2 -> Program 2")
print("Press Shift+3 or Command+3 / Ctrl+3 -> Program 3")
print("Press Shift+4 or Command+4 / Ctrl+4 -> Program 4")
print("Press Shift+5 or Command+5 / Ctrl+5 -> Program 5")
print("Press Shift+S or Command+S / Ctrl+S -> Stop current typing")
print("Press Shift+Q or Command+Q / Ctrl+Q -> Exit the program")

keyboard.wait() if keyboard is not None else print("Keyboard support is unavailable in this environment.")

# made by kunal ugale with ai but idia was mine
