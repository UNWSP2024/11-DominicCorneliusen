#Title: Information
#Author: Dominic Corneliusen
#Date last modified: 4/13/2026

#Start
import tkinter
import tkinter.messagebox

class Window:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Information")

        self.button = tkinter.Button(self.window, text = "Click for information",
                                     command = self.display_info)
        self.button2 = tkinter.Button(self.window, text = "Quit",
                                      command = self.window.quit)

        self.button.pack()
        self.button2.pack()

        tkinter.mainloop()
    def display_info(self):
        tkinter.messagebox.showinfo("Information", "309 Minnesota Ave NE Warroad, MN 56763")
if __name__ == "__main__":
    window = Window()