"""
Selection Saver
---------------
Select text with your mouse (like you would to copy it), then press
Ctrl+1, Ctrl+2, Ctrl+3, Ctrl+4, or Ctrl+5.

Each key saves the currently selected text into its own file:
    selection_1.txt
    selection_2.txt
    selection_3.txt
    selection_4.txt
    selection_5.txt

Pressing the same number again OVERWRITES that file with the new selection.
Press Esc to stop the program.

SETUP
-----
1. Install dependencies:
       pip install keyboard pyperclip

   On Linux you also need a clipboard tool for pyperclip to work:
       sudo apt install xclip

2. Run the script. On Windows/Linux, global hotkeys usually need
   elevated permissions:
       Windows: run your terminal "as Administrator"
       Linux:   sudo python3 selection_saver.py
   (Mac: the 'keyboard' library has limited support; see note at bottom.)
"""

import os
import time

import keyboard
import pyperclip

# Folder where the files will be saved (created next to this script)
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saved_selections")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_selection(slot: int):
    """Copy the current mouse selection and write it to selection_<slot>.txt"""
    # Remember whatever was on the clipboard before, so we can tell if copy worked
    previous_clip = None
    try:
        previous_clip = pyperclip.paste()
    except Exception:
        pass

    # Simulate Ctrl+C to copy whatever is currently highlighted
    keyboard.send("ctrl+c")
    time.sleep(0.2)  # small delay so the OS has time to update the clipboard

    text = pyperclip.paste()

    if text == previous_clip:
        print(f"[!] Nothing new was copied. Make sure you actually have text "
              f"selected before pressing Ctrl+{slot}.")
        return

    filepath = os.path.join(OUTPUT_DIR, f"selection_{slot}.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"[OK] Ctrl+{slot} -> saved to {filepath}")


# Register hotkeys Ctrl+1 through Ctrl+5
for i in range(1, 6):
    keyboard.add_hotkey(f"ctrl+{i}", save_selection, args=[i])

print("Listening for Ctrl+1 .. Ctrl+5. Select text with your mouse, then press one of them.")
print(f"Files will be saved in: {OUTPUT_DIR}")
print("Press Esc to quit.")

keyboard.wait("esc")
print("Stopped.")