import os
import re

#class to perform file operations.
class Readfile:
    def __init__(self):
        #initializing list variables to store data from files.
        self.headlines = []
        self.search_word = []

    def openfile(self, file):
        #opening file, reading data and closing them.
        handle = open(file, 'r')
        self.headlines = handle.readlines()
        handle.close()

    def search_item(self, words):
        #method for implementing search functionality, for search bar in the app.
        location = "./NewsApp-master/files/headlines/"  #file path.
        files = os.listdir(location)    #reading all files from path directory.
        self.search_word = []
        word = words.lower().split()    #list for search keywords.

        for file in files:
            #opening all the headline files for searching.
            if "headlines" in file:
                handle = open(location+file, 'r')
                content = handle.readlines()    #converting file data to list.
                for item in content:
                    sentence = item.split(';')
                    #considering main part of data in file.
                    searching = sentence[0].lower().split()
                    searching.append(sentence[1].lower().strip())

                    #searching begins.
                    for i in range(len(searching)):
                        #eliminating all the special characters.
                        searching[i] = re.sub(r'\'s', '', searching[i])
                        searching[i] = re.sub('[()!?,.:\']', '', searching[i])
                        if '-' in searching[i]:
                            temp = searching[i].split('-')
                            searching[i] = temp[0]
                            searching[i+1] = temp[1]

                    #matching the search bar input to file data.
                    result = all(elem in searching for elem in word)
                    #if data is matched, storing it.
                    if result:
                        self.search_word.append(item)
                handle.close()

        self.search_word = list(set(self.search_word))

    def get(self):
        #returning the data that is read from files.
        return self.headlines

    def search_get(self):
        #returning the data that matches to searching data.
        return self.search_word


if __name__ == "__main__":
    print("Try to run GUI.py")
