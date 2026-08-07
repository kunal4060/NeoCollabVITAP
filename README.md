<div align="center">

# ⚡ NeoCollabVITAP

**A lightweight typing automation tool for lab submissions**

*Made by Kunal Ugale*

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-informational?style=flat-square)
![License](https://img.shields.io/badge/Use-Educational-lightgrey?style=flat-square)

</div>

---

## 📖 Overview

**NeoCollabVITAP** is a simple typing automation tool that reads predefined answers from text files and automatically types them into the active text field. It's designed to save time while completing lab submissions.

---

## ✨ Features

- 📂 Automatically reads answer files from the selected lab folder
- ⌨️ Types content with a small delay between characters for smoother, natural-looking input
- ▶️ Start, stop, or exit typing using simple keyboard shortcuts
- ⏳ Includes a 3-second countdown before typing begins

---

## 🧰 Requirements

Make sure you have **Python 3** installed, then install the required packages:

```bash
pip install keyboard pyautogui
```

**On Windows:**

```bash
py -m pip install keyboard pyautogui
```

**On macOS:**

```bash
python3 -m pip install keyboard pyautogui
```

These scripts now work on both **Windows** and **macOS**. On macOS, use **Command** as the alternate modifier key; on Windows, use **Ctrl**.

---

## 🗂️ Project Structure

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

| File | Description |
|------|-------------|
| `neo.py` | The typing automation script |
| `Q1_Answer.txt` – `Q5_Answer.txt` | Predefined answers for each question |
| `Questions_Order.png` | Image showing the correct question order |

---

## 🚀 How to Run

Open a terminal in the project folder, then run:

```bash
python Lab_0/neo.py
```

**On Windows:**

```bash
py Lab_0/neo.py
```

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|:--------:|--------|
| `Shift + 1` or `Command/Ctrl + 1` | Type Program 1 |
| `Shift + 2` or `Command/Ctrl + 2` | Type Program 2 |
| `Shift + 3` or `Command/Ctrl + 3` | Type Program 3 |
| `Shift + 4` or `Command/Ctrl + 4` | Type Program 4 |
| `Shift + 5` or `Command/Ctrl + 5` | Type Program 5 |
| `Shift + S` or `Command/Ctrl + S` | Stop current typing |
| `Shift + Q` or `Command/Ctrl + Q` | Exit the program |

---

## 📋 Instructions

1. Open the required lab folder.
2. **Check the PNG image in that folder first** — it shows the correct order of the questions to help you select the right answer file.
3. Open the website or application where you want to type the answer.
4. Place your cursor inside the target text box.
5. Run the script.
6. Press the corresponding shortcut (`Shift + 1` to `Shift + 5`).
7. A **3-second countdown** will begin.
8. The tool will automatically type the selected answer.

---

## ⚠️ Important Notes

> **Always check the PNG image inside the lab folder before typing** — the question order may differ between labs.

- The program reads answers from `Q1_Answer.txt` through `Q5_Answer.txt`.
- Ensure the cursor is already placed in the correct text box before starting.
- **Once typing starts, do not move the mouse or switch windows** — doing so may cause the text to be typed in the wrong location.
- Stop typing anytime with `Shift + S` or `Command/Ctrl + S`.
- Exit the application with `Shift + Q` or `Command/Ctrl + Q`.

---

## 💡 Example

To automatically type the contents of **Q1_Answer.txt**:

1. Open the target text field.
2. Place the cursor where you want the answer.
3. Press `Shift + 1`.
4. Wait for the 3-second countdown.
5. The answer is typed automatically.

---

## 📜 Disclaimer

This tool is intended for **educational purposes and personal productivity**. Please use it responsibly and follow your institution's academic policies.

---

<div align="center">

**Made with AI ❤️ **

</div>
