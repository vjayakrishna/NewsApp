import webbrowser
from Readfile import Readfile
from tkHyperlinkManager import *


#class to open news story(paragraph) in new GUI window.
class Window3:
    def __init__(self, list_news):
        #path of directory to read story from files.
        self.location = "./files/news_articles/"

        #opening file to read data (news story).
        self.rf1 = Readfile()
        self.rf1.openfile(self.location+list_news[1].strip()+"/"+list_news[3].strip())
        self.paragraph = ''.join(self.rf1.get())    #storing data to string.
        self.paragraph = self.paragraph.strip()
        self.paragraph = self.paragraph.replace('\n', "\n\n\t")

        #new GUI window to display news data.
        self.root3 = Tk()
        self.root3.title("STORY")
        self.root3.geometry("563x507")
        self.root3.resizable(0, 0)

        #adding text widget, button onto the window.
        self.text = Text(self.root3, bg="light grey", bd=0, wrap=WORD, cursor="arrow", font="Arial 12")

        hyperlink = HyperlinkManager(self.text)

        self.text.insert(INSERT, "Headline:  ")
        self.text.insert(END, list_news[0]+"\n\n")

        self.text.insert(END, "STORY\n\n")
        self.text.insert(END, self.paragraph)

        self.text.insert(END, "\n\nsee full story", hyperlink.add(lambda: self.callback(list_news[2])))


        #indentation of data in GUI.
        self.text.tag_configure("left", justify='left')
        self.text.tag_add("left", "1.0", "end")

        self.text.tag_configure("center", justify='center')
        self.text.tag_add("center", "3.0", "3.5")

        #font for data.
        self.text.tag_configure("bold", font="Times 14 bold")
        self.text.tag_add("bold", "1.8", "2.0")

        self.text.tag_configure("underline", font="Times 14 bold underline")
        self.text.tag_add("underline", "1.0", "1.8")
        self.text.tag_add("underline", "3.0", "3.5")

        #scroll bar for the window.
        scrollbar = Scrollbar(self.root3, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=self.text.yview)
        self.text.pack(side="top")

        #exit button.
        self.button = Button(self.root3, bd=3, bg="grey70", font="Verdana 10 italic", text="Exit", relief=GROOVE, command=self.out)
        self.button.pack(side="bottom")

        self.root3.config(bg="light grey")
        self.root3.mainloop()

    def callback(self, url):
        #method to open url in web browser.
        webbrowser.open(url.strip())

    def out(self):
        #closing window usin button.
        self.root3.destroy()

