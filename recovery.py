#!/usr/bin/python3
import pathlib
import pygubu
import tkinter as tk
import os

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "recovery.ui"


class RecoveryApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("frame1", master)
        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def gd(self):
        os.system("gnome-disks")

    def pm(self):
        os.system("gparted")

    def chromium(self):
        os.system("chromium")

    def exit(self):
        exit()


if __name__ == "__main__":
    root = tk.Tk()
    app = RecoveryApp(root)
    app.run()
