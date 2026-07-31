# NeoCollabVITAP

**Made by Kunal Ugale**

NeoCollabVITAP is a simple typing automation tool that reads predefined answers from text files and automatically types them into the active text field. It is designed to save time while completing lab submissions.

## Features

- Automatically reads answer files from the selected lab folder.
- Types the contents with a small delay between characters for smoother input.
- Start, stop, or exit the typing process using keyboard shortcuts.
- Includes a 3-second countdown before typing begins.

---

## Requirements

Make sure you have **Python 3** installed.

Install the required packages:

```bash
pip install keyboard pyautogui
```

or on Windows:

```bash
py -m pip install keyboard pyautogui
```

---

## Project Structure

```
NeoCollabVITAP/
│
├── Lab_0/
│   ├── neo.py
│   ├── Q1_Answer.txt
│   ├── Q2_Answer.txt
│   ├── Q3_Answer.txt
│   ├── Q4_Answer.txt
│   ├── Q5_Answer.txt
│   └── Questions_Order.png
│
├── Lab_1/
│   └── ...
│
└── README.md
```

Each lab folder contains:

- `neo.py` (or the typing script)
- `Q1_Answer.txt` to `Q5_Answer.txt`
- **A PNG image showing the question order**

---

## How to Run

Open a terminal in the project folder.

Run:

```bash
python Lab_0/neo.py
```

or on Windows:

```bash
py Lab_0/neo.py
```

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| **Shift + 1** | Type Program 1 |
| **Shift + 2** | Type Program 2 |
| **Shift + 3** | Type Program 3 |
| **Shift + 4** | Type Program 4 |
| **Shift + 5** | Type Program 5 |
| **Shift + S** | Stop current typing |
| **Shift + Q** | Exit the program |

---

## Instructions

1. Open the required lab folder.
2. **Check the PNG image in that folder first.** It shows the correct order of the questions to help you select the correct answer file.
3. Open the website or application where you want to type the answer.
4. Place your cursor inside the target text box.
5. Run the script.
6. Press the corresponding shortcut (`Shift + 1` to `Shift + 5`).
7. A **3-second countdown** will begin.
8. The tool will automatically type the selected answer.

---

## ⚠️ Important Notes

- The program reads answers from:
  - `Q1_Answer.txt`
  - `Q2_Answer.txt`
  - `Q3_Answer.txt`
  - `Q4_Answer.txt`
  - `Q5_Answer.txt`
- **Always check the PNG image inside the lab folder before typing.** The question order may differ between labs.
- Ensure the cursor is already placed in the correct text box before starting.
- **Once typing starts, DO NOT move the mouse or switch windows.** Doing so may cause the text to be typed in the wrong location.
- You can stop the typing process anytime using **Shift + S**.
- Exit the application using **Shift + Q**.

---

## Example

To automatically type the contents of **Q1_Answer.txt**:

1. Open the target text field.
2. Place the cursor where you want the answer.
3. Press **Shift + 1**.
4. Wait for the 3-second countdown.
5. The answer will be typed automatically.

---

## Disclaimer

This tool is intended for educational purposes and personal productivity. Please use it responsibly and follow your institution's academic policies.

---

**Made with ❤️ by Kunal Ugale**
