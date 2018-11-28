from tkinter import *
from Readfile import Readfile
from Window2 import Window2
import tkinter.messagebox

#class for implementing GUI
class GUI:
    def __init__(self):
        self.file = ""
        self.headlines = []
        self.location = "./files/headlines/" #path of directory to read files.
        self.rf = Readfile()    #object of readfiles class to read data from files.

        #creating main window.
        self.root1 = Tk()
        self.root1.title("NEWS APP")
        self.root1.geometry("932x600")
        self.root1.resizable(0, 0)

        #welcome screen in GUI.
        self.var = StringVar()
        self.var.set("WELCOME, TO NEWS APP")

        #label and button to get started.
        self.label2 = Label(self.root1, textvariable=self.var, bg="grey", fg="white", font="Verdana 19 bold italic")
        self.label2.place(x=450, y=300, anchor=CENTER)

        self.button9 = Button(self.root1, cursor="dot", bd=3, bg="grey", fg="white", font="Verdana 13 bold italic", text="Get started", relief=GROOVE, command=self.start)
        self.button9.place(x=450, y=350, anchor=CENTER)

        self.root1.config(bg="grey")
        self.root1.mainloop()

    def start(self):
        #adding label, entry buttons to root window.
        label = Label(self.root1, bg="light grey", fg="grey50", font="Verdana 19 bold", text="NEWS")
        label.place(x=0, y=0)

        self.entry = Entry(self.root1, relief=GROOVE, bd=3, font="Arial 12", width=75)
        self.entry.place(x=95, y=6)

        button1 = Button(self.root1, cursor="dot", bd=3, bg="grey70", font="Verdana 12 bold", text="Search", relief=GROOVE, command=self.search)
        button1.place(x=785, y=0)

        button2 = Button(self.root1, cursor="dot", bd=3, bg="grey70", font="Verdana 12 bold", text="Exit", relief=GROOVE, command=self.root1.destroy)
        button2.place(x=880, y=0)

        button = Button(self.root1, cursor="watch", bd=3, bg="grey70", font="Verdana 13 bold italic", text="Menu", relief=GROOVE, command=self.menu)
        button.place(x=10, y=50)

        self.root1.config(bg="light grey")
        self.home()

    def menu(self):
        #Adding buttons to menu.
        button3 = Button(self.root1, cursor="watch", bd=3, bg="grey70", font="Verdana 13 bold italic", text="Home", relief=GROOVE, command=self.home)
        button3.place(x=10, y=50)

        button4 = Button(self.root1, cursor="watch", bd=3, bg="grey70", font="Verdana 13 bold italic", text="World", relief=GROOVE, command=self.world)
        button4.place(x=150, y=50)

        button5 = Button(self.root1, cursor="watch", bd=3, bg="grey70", font="Verdana 13 bold italic", text="Business", relief=GROOVE, command=self.business)
        button5.place(x=300, y=50)

        button6 = Button(self.root1, cursor="watch", bd=3, bg="grey70", font="Verdana 13 bold italic", text="Politics", relief=GROOVE, command=self.politics)
        button6.place(x=475, y=50)

        button7 = Button(self.root1, cursor="watch", bd=3, bg="grey70", font="Verdana 13 bold italic", text="Entertainment", relief=GROOVE, command=self.entertainment)
        button7.place(x=630, y=50)

        button8 = Button(self.root1, cursor="watch", bd=3, bg="grey70", font="Verdana 13 bold italic", text="Refresh", relief=GROOVE, command=self.root1.destroy)
        button8.place(x=840, y=50)

        self.root1.config(bg="light grey")

    def home(self):
        #method to display news in home window.
        self.root1.title("HOME")
        self.file = self.location+"headlines.txt"

        self.rf.openfile(self.file)
        self.headlines = self.rf.get()

        #calling Window to class to display data onto root window.
        win1 = Window2(self.root1, self.headlines)

    def business(self):
        #method to read, display bussiness news.
        self.root1.title("BUSINESS NEWS")
        self.file = self.location+"headlines_business.txt"

        self.rf.openfile(self.file)
        self.headlines = self.rf.get()

        win2 = Window2(self.root1, self.headlines)

    def politics(self):
        #methos to read, display political news.
        self.root1.title("POLITICAL NEWS")
        self.file = self.location+"headlines_politics.txt"

        self.rf.openfile(self.file)
        self.headlines = self.rf.get()

        win3 = Window2(self.root1, self.headlines)

    def world(self):
        #method to read, display world news.
        self.root1.title("WORLD NEWS")
        self.file = self.location+"headlines_world.txt"

        self.rf.openfile(self.file)
        self.headlines = self.rf.get()

        win4 = Window2(self.root1, self.headlines)

    def entertainment(self):
        #method to read, display entertainment news.
        self.root1.title("ENTERTAINMENT NEWS")
        self.file = self.location+"headlines_entertainment.txt"

        self.rf.openfile(self.file)
        self.headlines = self.rf.get()

        win5 = Window2(self.root1, self.headlines)

    def search(self):
        #method to implement search bar, for searching data in files.
        temp = self.entry.get().strip()

        self.rf.search_item(temp)
        self.headlines = self.rf.search_get()
        self.entry.delete(0, 'end')

        #message box if search is inapropriate.
        if not temp:
            tkinter.messagebox.showinfo("SEARCH", "Empty string")
        elif not self.headlines:
            tkinter.messagebox.showinfo("SEARCH", "No results found")
        else:
            win6 = Window2(self.root1, self.headlines)


if __name__ == "__main__":
    GUI()


