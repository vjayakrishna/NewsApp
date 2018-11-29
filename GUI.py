from tkinter import *
import tkinter.messagebox
from Window2 import Window2
from Readfile import Readfile
import crawler
import NewsParser_CNN
import NewsParser_NYT
import NewsParser_NBC
import NewsParser_FOX


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
        self.label = Label(self.root1, textvariable=self.var, bg="grey", fg="white", font="Verdana 20 bold italic")
        self.label.place(x=450, y=300, anchor=CENTER)

        self.button9 = Button(self.root1, bd=3, bg="grey", fg="white", font="Verdana 13 bold italic", text="Get started", relief=GROOVE, command=self.start)
        self.button9.place(x=450, y=350, anchor=CENTER)

        self.root1.config(bg="grey")
        self.root1.mainloop()

    def start(self):
        #adding label, entry buttons to root window.
        label1 = Label(self.root1, bg="light grey", fg="grey50", font="Verdana 20 bold", text="NEWS:")
        label1.place(x=0, y=0)

        button1 = Button(self.root1, bd=3, bg="grey70", font="Verdana 12 bold", text="Home", relief=GROOVE, command=self.home)
        button1.place(x=130, y=4)

        button2 = Button(self.root1, bd=3, bg="grey70", font="Verdana 12 bold", text="World", relief=GROOVE, command=self.world)
        button2.place(x=270, y=4)

        button3 = Button(self.root1, bd=3, bg="grey70", font="Verdana 12 bold", text="Business", relief=GROOVE, command=self.business)
        button3.place(x=410, y=4)

        button4 = Button(self.root1, bd=3, bg="grey70", font="Verdana 12 bold", text="Politics", relief=GROOVE, command=self.politics)
        button4.place(x=575, y=4)

        button5 = Button(self.root1, bd=3, bg="grey70", font="Verdana 12 bold", text="Entertainment", relief=GROOVE, command=self.entertainment)
        button5.place(x=725, y=4)

        button6 = Button(self.root1, cursor="watch", bd=3, bg="grey70", font="Verdana 11 italic", text="Refresh", relief=GROOVE, command=self.refresh)
        button6.place(x=15, y=50)

        self.entry = Entry(self.root1, relief=GROOVE, bd=3, font="Arial 12", width=75)
        self.entry.place(x=110, y=54)

        button7 = Button(self.root1, bd=3, bg="grey70", font="Verdana 11 italic", text="Search", relief=GROOVE, command=self.search)
        button7.place(x=805, y=50)

        button8 = Button(self.root1, bd=3, bg="grey70", fg="red", font="Verdana 11 italic", text="Exit", relief=GROOVE, command=self.root1.destroy)
        button8.place(x=885, y=50)

        self.root1.config(bg="light grey")
        self.home()

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

        #message box if search is inappropriate.
        if not temp:
            tkinter.messagebox.showinfo("SEARCH", "Empty string")
        elif not self.headlines:
            tkinter.messagebox.showinfo("SEARCH", "No results found")
        else:
            win6 = Window2(self.root1, self.headlines)

    def refresh(self):
        #method to run the crawler again, to update latest news.
        self.entry.delete(0, "end")

        #message box to get user opinion.
        msgbox = tkinter.messagebox.askquestion("REFRESH", "Loading app data, it may take some time.\nDo you want to continue?", icon='warning')

        if msgbox == 'yes':
            crawler.execute()
            tkinter.messagebox.showinfo("REFRESH", "Process completed.")

            #To start displaying new data from files.
            self.home()


if __name__ == "__main__":
    GUI()

