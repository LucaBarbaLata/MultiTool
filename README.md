# 🧰 MultiTool Installer & Tweaker for Windows

MultiTool is a Windows desktop application built with `customtkinter` that allows you to **quickly install popular software**, apply **useful system tweaks**, and gather **system info** — all in a sleek and centralized interface.

---

## ✨ Features

### 📦 Software Installer
Easily install apps by category using [Winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/):

- **Browsers**: Chrome, Firefox, Opera, Brave
- **Compression Tools**: 7-Zip, WinRAR, PeaZip
- **Media Players**: VLC, Spotify, Audacity, etc.
- **Dev Tools**: Python, Notepad++, VS Code, etc.
- **Imaging Tools**: GIMP, Blender, Krita, ShareX, etc.
- **Utilities**: TeamViewer, AnyDesk, Revo, WinDirStat
- **Document Tools**: LibreOffice, Foxit, SumatraPDF
- **OS Images**: Download Windows 10/11 ISO

### 🛠 System Tweaks
Apply quick system tweaks like:
- Show file extensions
- Delete temporary files
- Update all installed apps
- Enable classic right-click context menu (Windows 11)

### 🖥 System Information
Generate a report with:
- CPU, RAM, and Disk usage
- Network statistics
- Boot time and system details

---

## 📸 Screenshots

> *You can add screenshots here using Markdown image syntax:*  
> `![Main UI](images/main_ui.png)`  
> *(Make sure to upload them to your repo folder or GitHub’s media manager.)*

---

## 📁 Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/multitool.git
    cd multitool
    ```

2. Make sure you have Python 3.10+ installed.
3. Install the required libraries:
    ```bash
    pip install customtkinter psutil pyglet
    ```

4. Run the application:
    ```bash
    python multitool.py
    ```

---

## ⚠️ Notes

- You must run MultiTool as an **Administrator** for installs/tweaks to work correctly.
- Windows must have [Winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/) installed (Windows 10/11).
- This app does **not collect personal data**. Only anonymous system info is used for optional logging.

---

## 📃 License

This project is released under the **MIT License** — free to use, modify, and distribute.

---

## 🤝 Credits

Created by [Luca](https://github.com/yourusername)  
Made with ❤️, caffeine, and some BAT magic.

