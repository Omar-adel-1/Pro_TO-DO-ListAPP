# ☑️ Pro To-Do List-APP

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Release-v1.0-success?style=for-the-badge)

A professional, desktop-based Task Management application built with **Python** and **Tkinter**. This project features a modern **Cyberpunk/Dark UI**, persistent **JSON storage**, and advanced **UX interactions** (shortcuts & context menus) for maximum productivity.

---

## 🚀 Key Features

* **🎨 Modern UI/UX:**
    * **Dark Theme:** A sleek interface using Charcoal & Cyan colors (VS Code style).
    * **Custom Styling:** Features a custom-themed Scrollbar using `ttk` library.
    * **Responsive Design:** Window is fully resizable with a fluid layout.
* **💾 Smart Persistence:**
    * **JSON Engine:** Tasks are stored in `tasks.json` instead of text files for better structure and speed.
    * **Auto-Save:** Data is saved instantly upon any change (Add, Delete, Edit).
 * **🧠 Developer Friendly:**
    * **Well-Documented:** The code is fully commented (Arabic/English) to explain complex logic, making it perfect for students and beginners to understand.
* **⚡ Interaction Efficiency:**
    * **Context Menu:** Right-click support for quick actions (Delete / Toggle Status).
    * **Keyboard Shortcuts:** Full support for keyboard navigation (Enter to add, Delete to remove).
    * **Smart Filtering:** Toggle button to view "All Tasks" or "Completed Only".

---

## 🛠️ Project Structure

| File | Type | Description |
| :--- | :--- | :--- |
| `main.py` | GUI (Frontend) | The main entry point. Handles window, events, and user interactions. |
| `task_manager.py` | Logic (Backend) | Manages data persistence, reading/writing to `tasks.json`. |
| `settings.py` | Config | Centralized configuration for Colors, Dimensions, and Constants. |
| `tasks.json` | Database | Auto-generated file storing tasks in a structured format. |

---

## 🎮 Controls & Shortcuts

The application is designed for speed. You can manage tasks without leaving the keyboard.

| Action | Input / Shortcut |
| :--- | :--- |
| **Add Task** | Type text + Press `Enter` |
| **Delete Task** | Select task + Press `Delete` Key |
| **Toggle Status** | `Double Click` on task |
| **Context Menu** | `Right Click` on any task |

---
## 🏃‍♂️ How to Run

Follow these simple steps to get the application running on your machine:

**1. Prerequisites:**
* Ensure you have **Python 3.x** installed.
* Tkinter is usually included with Python, but on Linux (Ubuntu), you might need to install it:
 ```bash
 sudo apt-get install python3-tk
 ```
  
**2. Clone the Repository:**
   ```bash
   git clone https://github.com/Omar-adel-1/Pro_TO-DO-ListAPP.git
   ```
**3. Run the App:**
  ```bash
  python main.py
  ```
---
## 📸 Screenshots
 <img width="1920" height="1200" alt="Screenshot from 2025-12-25 00-13-21" src="https://github.com/user-attachments/assets/4d9bc032-d2e3-448c-a26c-61489b2d529d" />

<img width="1920" height="1200" alt="Screenshot from 2025-12-25 00-13-33" src="https://github.com/user-attachments/assets/b1b45ea9-6891-4afb-b32f-9347b1525173" />


---

## 🔮 Future Improvements

- [ ] **Priority Levels:** Add a feature to flag tasks as High, Medium, or Low priority with color coding.
- [ ] **Due Dates:** Integrate a calendar picker to set deadlines for specific tasks.
- [ ] **Categories/Tags:** Allow users to group tasks (e.g., Work, Personal, Study).
- [ ] **Sound Effects:** Add satisfying sound feedback when completing a task.
- [ ] **Executable Build:** Convert the project to a standalone `.exe` or `.app` file using PyInstaller.

---

## 👤 Author
* **📌 Omar Adel Abouzeid**

