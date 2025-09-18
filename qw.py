#!/usr/bin/env python3
"""
qw — tiny terminal editor (single-file, prompt_toolkit v3)
Short name, one script, no external state files.

Features:
 - Run:  qw                -> opens a new unique UntitledN file
 - Run:  qw <filename>     -> open or prompt to create
 - Run:  qw open <filename>
 - Run:  qw new <filename>
 - Ctrl+S : Save (prompts for filename if Untitled)
 - Ctrl+W : Save & Exit
 - Ctrl+D : Exit without saving
 - Esc    : Exit without saving (same as Ctrl+D; fast bail)
 - Mouse / trackpad scroll works
 - Bottom status bar shows shortcuts
Notes:
 - Filename prompts shown before the editor use standard input(). Cancel with Ctrl+C.
"""

import sys
import os
from prompt_toolkit import Application
from prompt_toolkit.widgets import TextArea, Frame, Label
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.key_binding import KeyBindings

def prompt_yes_no(question: str) -> bool:
    try:
        ans = input(f"{question} (y/N): ").strip().lower()
    except (KeyboardInterrupt, EOFError):
        return False
    return ans in {"y", "yes"}

def prompt_filename(prompt_text: str) -> str:
    try:
        return input(prompt_text).strip()
    except (KeyboardInterrupt, EOFError):
        return ""

def generate_untitled():
    counter = 1
    while True:
        name = f"Untitled{counter}"
        if not os.path.exists(name):
            return name
        counter += 1

def parse_args(argv):
    # Returns (mode, filename)
    # mode in {"implicit", "open", "new", "untitled"}
    if len(argv) == 1:
        return ("untitled", None)
    if len(argv) >= 2:
        if argv[1] in ("open", "new") and len(argv) >= 3:
            return (argv[1], argv[2])
        # else treat argv[1] as filename
        return ("implicit", argv[1])
    return ("untitled", None)

def main():
    mode, fn = parse_args(sys.argv)

    # determine filename and initial text
    if mode == "untitled":
        filename = generate_untitled()
        text = ""
    else:
        filename = fn
        exists = os.path.exists(filename)
        if mode == "open":
            if not exists:
                if not prompt_yes_no("This file does not exist. Create it?"):
                    print("Aborted.")
                    sys.exit(0)
                text = ""
            else:
                with open(filename, "r", encoding="utf-8") as f:
                    text = f.read()
        elif mode == "new":
            if exists:
                if not prompt_yes_no("That file already exists. Open it?"):
                    print("Aborted.")
                    sys.exit(0)
                with open(filename, "r", encoding="utf-8") as f:
                    text = f.read()
            else:
                text = ""
        else:  # implicit
            if not exists:
                if not prompt_yes_no("This file does not exist. Create it?"):
                    print("Aborted.")
                    sys.exit(0)
                text = ""
            else:
                with open(filename, "r", encoding="utf-8") as f:
                    text = f.read()

    original_text = text

    # --- build UI ---
    text_area = TextArea(
        text=text,
        scrollbar=True,
        line_numbers=True,
        focus_on_click=True,
    )

    status_bar = Label(
        "Ctrl+S: Save | Ctrl+W: Save & Exit | Ctrl+D: Exit Without Saving | Esc: Exit Without Saving",
        style="reverse"
    )

    root_container = HSplit([
        Frame(text_area, title=f"qw - {filename}"),
        status_bar
    ])

    kb = KeyBindings()

    def write_file(path, content):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    @kb.add("c-s")
    def _(event):
        nonlocal filename, original_text
        if filename.startswith("Untitled") and not os.path.exists(filename):
            new_name = prompt_filename("Enter filename to save as: ")
            if not new_name:
                return
            filename = new_name
            root_container.children[0].title = f"qw - {filename}"
        write_file(filename, text_area.text)
        original_text = text_area.text

    @kb.add("c-w")
    def _(event):
        nonlocal filename, original_text
        if filename.startswith("Untitled") and not os.path.exists(filename):
            new_name = prompt_filename("Enter filename to save as: ")
            if new_name:
                filename = new_name
                root_container.children[0].title = f"qw - {filename}"
        write_file(filename, text_area.text)
        original_text = text_area.text
        event.app.exit(result=text_area.text)

    @kb.add("c-d")
    def _(event):
        event.app.exit(result=None)

    @kb.add("escape", eager=True)
    def _(event):
        event.app.exit(result=None)

    # Build & run
    app = Application(
        layout=Layout(root_container),
        key_bindings=kb,
        full_screen=True,
        mouse_support=True,
    )
    app.run()

if __name__ == "__main__":
    main()
