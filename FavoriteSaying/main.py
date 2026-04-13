#Title: Favorite saying
#Author: Dominic Corneliusen
#Date last modified: 4/13/2026

#Start
import tkinter
from tkinter import *

class window:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Favorite Saying')
        self.label = tkinter.Label(self.main_window, text = "Have no fear of perfection, you'll never reach it.")
        self.label.pack(side = "left")
        tkinter.mainloop()
if __name__ == '__main__':
    myGui = window()