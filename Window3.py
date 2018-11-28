from tkinter import *
from Readfile import Readfile

#class to open news story(paragraph) in new GUI window.
class Window3:
    def __init__(self, file):
        #opening file to read data (news story).
        self.rf1 = Readfile()
        self.rf1.openfile(file)
        self.paragraph = ''.join(self.rf1.get())    #storing data to string.

        #new GUI window to display news data.
        self.root3 = Tk()
        self.root3.title("STORY")
        self.root3.geometry("561x363")
        self.root3.resizable(0, 0)

        #adding text widget, button onto the window.
        self.text = Text(self.root3, width=62, height=20, bg="light grey", bd=0, wrap=WORD, cursor="arrow", font="Arial 12")
        self.text.place(x=0, y=0)

        self.text.insert(INSERT, "STORY\n\n")
        self.text.insert(END, self.paragraph)

        #indentation of data in GUI.
        self.text.tag_configure("center", justify='center')
        self.text.tag_add("center", "1.0", "1.5")

        self.text.tag_configure("left", justify='left')
        self.text.tag_add("left", "3.0", "end")

        #font for data.
        self.text.tag_configure("bold", font="Times 14 bold")
        self.text.tag_add("bold", "1.0", "1.5")

        #exit button.
        self.button = Button(self.root3, cursor="dot", bd=3, bg="grey70", font="Verdana 10 bold italic", text="Exit", relief=GROOVE, command=self.out)
        self.button.place(x=263, y=330)

        self.root3.mainloop()

    def out(self):
        #closing window usin button.
        self.root3.destroy()
