#!/usr/bin/python3
import pathlib
import pygubu
import tkinter as tk
import subprocess
import shlex
import os

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "power.ui"


class PowerApp:
    def exit(self):
        exit()

    def shutdown(self):
        subprocess.call(shlex.split('pkexec systemctl poweroff'))

    def restart(self):
        subprocess.call(shlex.split('pkexec reboot'))

    def __init__(self, master=None, translator=None):
        self.builder = builder = pygubu.Builder(translator)
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("frame1", master)
        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = PowerApp(root)
    app.run()
