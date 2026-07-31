import os
import sys
import time
import random
import threading

import keyboard
import pyautogui

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

    for ch in text:
        if stop_requested:
            break
        if ch == "\n":
            pyautogui.press("enter")
        else:
            pyautogui.write(ch)
        time.sleep(random.uniform(0.0005, 0.002))

    typing = False
    if stop_requested:
        print(f"{label} stopped.")
    else:
        print(f"{label} done.")

def start_program(text, label):
    if typing:
        print(f"{label} is already running. Press Shift+S to stop it.")
        return

    threading.Thread(target=type_text, args=(text, label), daemon=True).start()
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
        print("Stopping current typing...")
    else:
        print("Nothing is being typed right now.")


def exit_program():
    if typing:
        stop_requested = True
        print("Stopping typing and exiting...")
    else:
        print("Exiting...")

    keyboard.unhook_all_hotkeys()
    sys.exit(0)


keyboard.add_hotkey("shift+1", start_program1, suppress=True)
keyboard.add_hotkey("shift+2", start_program2, suppress=True)
keyboard.add_hotkey("shift+3", start_program3, suppress=True)
keyboard.add_hotkey("shift+4", start_program4, suppress=True)
keyboard.add_hotkey("shift+5", start_program5, suppress=True)
keyboard.add_hotkey("shift+s", stop_typing, suppress=True)
keyboard.add_hotkey("shift+q", exit_program, suppress=True)

print("Ready!")
print("Press Shift+1 -> Program 1")
print("Press Shift+2 -> Program 2")
print("Press Shift+3 -> Program 3")
print("Press Shift+4 -> Program 4")
print("Press Shift+5 -> Program 5")
print("Press Shift+S -> Stop current typing")
print("Press Shift+Q -> Exit the program")

keyboard.wait()
