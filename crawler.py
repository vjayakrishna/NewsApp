import os
import NewsParser_CNN
import NewsParser_NYT
import NewsParser_NBC
import NewsParser_FOX


def clearallfiledata():
    """Clears the content present in 'headlines' files.
    ('headlines.txt', 'headlines_politics.txt', 'headlines_entertainment.txt',
    'headlines_business.txt', 'headlines_world.txt')"""
    fh = open("files/headlines/headlines.txt", 'w')
    fh.close()
    fh = open("files/headlines/headlines_politics.txt", 'w')
    fh.close()
    fh = open("files/headlines/headlines_entertainment.txt", 'w')
    fh.close()
    fh = open("files/headlines/headlines_business.txt", 'w')
    fh.close()
    fh = open("files/headlines/headlines_world.txt", 'w')
    fh.close()


def remove_existing_files():
    """Removes all the files in 'files/news_articles' directory"""
    curr_dir = os.getcwd()
    dir_paths = ["files/news_articles/cnn", "files/news_articles/nytimes", "files/news_articles/nbc", "files/news_articles/fox"] #List of directories containing news article files.
    for path in dir_paths: #for each news articles directory, remove all the files present in it.
        file_path = os.path.join(curr_dir, path) #set the complete file path.
        file_list = os.listdir(file_path) #get the list of all file names present in the file_path
        #print(file_list)
        for file in file_list: #remove all the files
            os.remove(os.path.join(file_path, file))
    return

def execute():
    #Reset all the file data and article files before executing the program.
    remove_existing_files()
    clearallfiledata()

    #Init all the news parsers and execute them...
    NP1 = NewsParser_CNN.NewsParser_CNN()
    NP1.execute()

    NP2 = NewsParser_NYT.NewsParser_NYT()
    NP2.execute()

    NP3 = NewsParser_NBC.NewsParser_NBC()
    NP3.execute()

    NP4 = NewsParser_FOX.NewsParser_FOX()
    NP4.execute()

#execute()
