#!/usr/bin/python3
import pathlib
import pygubu
import tkinter as tk
import os

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "nanode.ui"


class NanodeApp:
    def cmd(self):
        os.system("xfce4-terminal")

    def recovery(self):
        os.system("python recovery.py")

    def power(self):
        os.system("python power.py")

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
    root.title("NanoDE")
    app = NanodeApp(root)
    app.run()
