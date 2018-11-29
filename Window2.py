import webbrowser
from tkinter import ttk
from Window3 import Window3
from tkHyperlinkManager import *


#class to display data on main GUI window.
class Window2:
    def __init__(self, root, data):
        self.counter = 0    #counter for the control flow of data.
        self.value = self.value1 = self.value2 = self.value3 = []   #lists to store data from files.

        #initialize root to main window.
        self.root2 = root
        self.headlines = data   #reading data from file.

        ttk.Separator(self.root2, orient=HORIZONTAL).place(x=0, y=90, relwidth=1)#line separator on GUI.
        self.org_out()

    def org_out(self):
        #method to display data onto GUI.
        if self.counter <= len(self.headlines)-1:
            del self.value[:]
            self.value = self.headlines[self.counter].split(';')    #spliting the data from file to list.

            #Adding text widget to main window, to display data from files.
            text1 = Text(self.root2, bg="light grey", width=93, bd=0, wrap=WORD, cursor="arrow", font="Times 15 bold")
            text1.place(x=0, y=100)
            hyperlink = HyperlinkManager(text1) #hyperlink to open story window and web browser(for opening url).

            #inserting news data to text widget.
            text1.insert(INSERT, "Headline: "+self.value[0])
            text1.insert(END, "\nSource: "+self.value[1])
            text1.insert(END, "\nFor story, ")

            #link to open new GUI window.
            text1.insert(END, "click here", hyperlink.add(lambda: self.story(self.value)))

            #setting font to diaplay data.
            text1.tag_configure("arial", font="Arial 11")
            text1.tag_add("arial", "2.0", "end")

            #link to open url in web browser.
            text1.insert(END, "\nLink: ")
            text1.insert(END, self.value[2], hyperlink.add(lambda: self.callback(self.value[2])))

            #setting font to diaplay data.
            text1.tag_configure("verdana", font="Verdana 8 italic")
            text1.tag_add("verdana", "4.0", "end")

            #line separator to main window.
            ttk.Separator(self.root2, orient=HORIZONTAL).place(x=0, y=205, relwidth=1)

        if self.counter+1 <= len(self.headlines)-1:
            del self.value1[:]
            self.value1 = self.headlines[self.counter+1].split(';')

            #Adding text widget to main window, to display data from files.
            text2 = Text(self.root2, bg="light grey", width=93, bd=0, wrap=WORD, cursor="arrow", font="Times 15 bold")
            text2.place(x=0, y=210)
            hyperlink = HyperlinkManager(text2) #hyperlink to open story window and web browser(for opening url).

            #inserting news data to text widget.
            text2.insert(INSERT, "Headline: "+self.value1[0])
            text2.insert(END, "\nSource: "+self.value1[1])
            text2.insert(END, "\nFor story, ")

            #link to open new GUI window.
            text2.insert(END, "click here", hyperlink.add(lambda: self.story(self.value1)))

            #setting font to diaplay data.
            text2.tag_configure("arial", font="Arial 11")
            text2.tag_add("arial", "2.0", "end")

            #link to open url in web browser.
            text2.insert(END, "\nLink: ")
            text2.insert(END, self.value1[2], hyperlink.add(lambda: self.callback(self.value1[2])))

            #setting font to diaplay data.
            text2.tag_configure("verdana", font="Verdana 8 italic")
            text2.tag_add("verdana", "4.0", "end")

            #line separator to main window.
            ttk.Separator(self.root2, orient=HORIZONTAL).place(x=0, y=315, relwidth=1)

        if self.counter+2 <= len(self.headlines)-1:
            del self.value2[:]
            self.value2 = self.headlines[self.counter+2].split(';')

            #Adding text widget to main window, to display data from files.
            text3 = Text(self.root2, bg="light grey", width=93, bd=0, wrap=WORD, cursor="arrow", font="Times 15 bold")
            text3.place(x=0, y=320)
            hyperlink = HyperlinkManager(text3) #hyperlink to open story window and web browser(for opening url).

            #inserting news data to text widget.
            text3.insert(INSERT, "Headline: "+self.value2[0])
            text3.insert(END, "\nSource: "+self.value2[1])
            text3.insert(END, "\nFor story, ")

            #link to open new GUI window.
            text3.insert(END, "click here", hyperlink.add(lambda: self.story(self.value2)))

            #setting font to diaplay data.
            text3.tag_configure("arial", font="Arial 11")
            text3.tag_add("arial", "2.0", "end")

            #link to open url in web browser.
            text3.insert(INSERT, "\nLink: ")
            text3.insert(END, self.value2[2], hyperlink.add(lambda: self.callback(self.value2[2])))

            #setting font to diaplay data.
            text3.tag_configure("verdana", font="Verdana 8 italic")
            text3.tag_add("verdana", "4.0", "end")

            #line separator to main window.
            ttk.Separator(self.root2, orient=HORIZONTAL).place(x=0, y=425, relwidth=1)

        if self.counter+3 <= len(self.headlines)-1:
            del self.value3[:]
            self.value3 = self.headlines[self.counter+3].split(';')

            #Adding text widget to main window, to display data from files.
            text4 = Text(self.root2, bg="light grey", width=93, bd=0, wrap=WORD, cursor="arrow", font="Times 15 bold")
            text4.place(x=0, y=430)
            hyperlink = HyperlinkManager(text4) #hyperlink to open story window and web browser(for opening url).

            #inserting news data to text widget.
            text4.insert(INSERT, "Headline: "+self.value3[0])
            text4.insert(END, "\nSource: "+self.value3[1])
            text4.insert(END, "\nFor story, ")

            #link to open new GUI window.
            text4.insert(END, "click here", hyperlink.add(lambda: self.story(self.value3)))

            #setting font to diaplay data.
            text4.tag_configure("arial", font="Arial 11")
            text4.tag_add("arial", "2.0", "end")

            #link to open url in web browser.
            text4.insert(END, "\nLink: ")
            text4.insert(END, self.value3[2], hyperlink.add(lambda: self.callback(self.value3[2])))

            #setting font to diaplay data.
            text4.tag_configure("verdana", font="Verdana 8 italic")
            text4.tag_add("verdana", "4.0", "end")

            #line separator to main window.
            ttk.Separator(self.root2, orient=HORIZONTAL).place(x=0, y=535, relwidth=1)

        #adding buttons to main window to contol data movement.
        button_prev = Button(self.root2, bd=3, bg="grey70", font="Verdana 11 italic", text="Prev", relief=GROOVE, command=self.prev)
        button_prev.place(x=400, y=560)

        button_next = Button(self.root2, bd=3, bg="grey70", font="Verdana 11 italic", text="Next", relief=GROOVE, command=self.next)
        button_next.place(x=465, y=560)

    def prev(self):
        #method to implement functionality for previous button using counter.
        if len(self.headlines) > 0:
            if self.counter <= 0:
                pass
            else:
                self.counter -= 4
                self.org_out()

    def next(self):
        #method to implement functionality for next button using counter.
        if len(self.headlines) > 0:
            if self.counter < len(self.headlines)-4:
                self.counter += 4
                self.org_out()

    def callback(self, url):
        #method to open url in web browser.
        webbrowser.open(url.strip())

    def story(self, news):
        #method to open news story in new window(GUI).
        window = Window3(news)


if __name__ == "__main__":
    print("Try to run GUI.py")

