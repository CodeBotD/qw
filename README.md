# 📝 qw — Tiny Terminal Editor

**Quick Writer (qw)** — a short, fast, single-file terminal text editor written in Python using `prompt_toolkit`.  
Perfect for super quick edits in the terminal! ⚡

---

## ✨ Features

- 🐍 Single-file Python script, no extra config files  
- 🖱 Mouse / trackpad scrolling supported  
- 📊 Status bar always shows available shortcuts  
- 💨 Super fast, minimal finger movement  

### ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+S`  | 💾 Save (prompts if Untitled) |
| `Ctrl+W`  | 💾 Save & Exit |
| `Ctrl+D`  | ❌ Exit without saving |
| `Esc`     | ❌ Exit without saving (fast bail-out) |

---

## 🚀 Usage

### New untitled buffer
```bash


qw

```
Opens a new untitled file (e.g., Untitled1, Untitled2, …) 🆕
Open existing file

```
qw <filename>

```
If the file exists → opens it 📂

If the file doesn’t exist → prompts to create it ❓

Explicit open:

qw open <filename>

Same behavior as above ✅
Create a new file (explicit)

```
qw new <filename>

```
Prompts if the file already exists ⚠️

# 💻 Installation & 🔹 Dependencies

``
    Python 3.7+ 🐍

   `` prompt_toolkit Python module ✨

   `` Git (optional, for cloning repo) 🛠️

🪟 Windows (Git Bash)

   `` Install [Python 3] and [Git].

   `` Open Git Bash.

   `` Install prompt_toolkit:

```
python3 -m pip install --upgrade prompt_toolkit

```
Put qw somewhere in your PATH, for example:

```
mkdir -p /c/Users/<YourName>/bin
mv qw /c/Users/<YourName>/bin/qw
chmod +x /c/Users/<YourName>/bin/qw

```
Run:

```
qw

```
🍎 macOS

``    Install Python 3 (via Homebrew brew install python or python.org).

  ``  Install dependency:

```
python3 -m pip install --upgrade prompt_toolkit

```   
 Move qw into
    
    
    ~/.local/bin 
    
    ```
  (or another folder in PATH):

```
mv ~/Downloads/qw ~/.local/bin/qw
chmod +x ~/.local/bin/qw

```
 Ensure 
    

   ``` 
  ~/.local/bin is in PATH:

 export PATH="$HOME/.local/bin:$PATH"


```
Run:

```
qw

```
🐧 Linux (Debian/Ubuntu example)

   ``
    Install Python 3 if missing:

```
sudo apt update
sudo apt install -y python3 python3-pip

```
Install dependency:

```
python3 -m pip install --upgrade prompt_toolkit

```
Move qw into

```
~/.local/bin:

#--

mv ~/Downloads/qw ~/.local/bin/qw
chmod +x ~/.local/bin/qw
```
  Ensure 
    
```
  ~/.local/bin

```
is in PATH:

```
export PATH="$HOME/.local/bin:$PATH"

```
Run:

```
qw

```
📝 Notes & Tips

    ```
   Prompts like This file does not exist. Create it? (y/N) happen before opening the editor. Cancel with Ctrl+C.

  Inside the editor: Esc or Ctrl+D exits immediately without saving.

   Ctrl+S saves (asks for filename if untitled).

   Works on macOS, Linux, and Windows terminals.

  Single-file and portable — ideal for quick edits.

❤️ Contributing

PRs and issues welcome! If you want UX tweaks (in-editor prompts, unsaved * indicator, config options), open an issue or PR.
