from html.parser import HTMLParser
from urllib.request import urlopen
import random

class DataParsedException(Exception):
    """Custom exception designed to stop the execution of NewsParsers.
    Raised after parsing a news website and extracting the required data from the html content of the website."""
    def __init__(self, data):
        self.data = data


class NewsParser(HTMLParser):
    """Base class with all the common functionality needed to parse a news website.
    Inherits 'HTMLParser' class from python's library.
    'HTMLParser' is a basic web crawler that comes default with Python-3,
    and do not require any other installations."""

    def __init__(self):
        """Init the required attributes for parsing and storing the data."""
        super().__init__()

        self.newscount = 0 #stores the count of news headlines extracted from html.
        self.prev_tags = [] #has all the tags encountered while parsing the html content.
        # (If html is '<div><a href="...">data</a></data>', then 'prev_tags' = ['div', 'a'], while data is being extracted.)

        self.prev_attrs=[] #has all the attributes of the corresponding tags in 'prev_tags'
        # In the above html, 'prev_attrs' = [{}, {'href': '...'}].
        #Here, prev_attrs is a list of dictionaries. In the example, first dictionary is empty as 'div' tag has no attributes.
        #Second dictionary has one (key, value) pair since 'a' tag has 'href' attribute with some value.

        self.tagcount = 0 #count of tags present in 'prev_tags'
        self.content = "" #stores the headlines content extracted from html page.
        self.maxcount = 5 #number of headlines to be exracted from each news website. Can be customized.
        # Better to have <15, else performance can be drastically affected.

        self.article_urls = [] #list of article urls for all the news headlines extracted from news website.
        self.article_filenames = [] #list of file names to save article paragraphs for all headlines.
        # Has one item for each url in 'self.article_urls'

        self.filename_counter = random.randint(100000, 1000000) #random int for filenames.

    def handle_starttag(self, tag, attrs):
        """Triggered when encountering the start tags, while parsing html content.
        'tag': value of the current start tag,
        'attrs': attribute dictionary of the current tag."""

        # Here, we are only interested in html content present in <body> tag.
        if tag == "html" or tag == "body" or "body" in self.prev_tags: #if inside <body> tag, proceed furthur. Else, return.
            self.prev_tags.append(tag) #append the current tag
            self.prev_attrs.append(attrs) #append the 'attrs' dictionary.
            self.tagcount += 1


    def handle_endtag(self, tag):
        """Triggered when encountering the end tags, while parsing html content.
        'tag': value of the current end tag"""

        if  tag == "html" or tag == "body" or "body" in self.prev_tags: #if inside <body> tag, proceed furthur. Else, return.
            #Have to remove tag from 'prev_tags' as this is endtag.
            if self.tagcount>0 and self.prev_tags[-1] == tag: #if last tag in 'prev_tags' equals tag,
                # remove the tag and the attrs
                self.prev_tags.pop()
                self.prev_attrs.pop()
                self.tagcount -= 1
            else: #Else, 'tag' has to be somewhere before the last tag.
                # Find that index, remove the tags starting from 'index' from the list 'prev_tags'.
                index = 2
                for i in range(2,self.tagcount):  #Loop through all the tags from the end of 'prev_tags' list,
                    # and find the matching 'index'.
                    if self.prev_tags[-i] == tag: #If match found, remove tags and their attrs from index to the end.
                        index = i
                        self.prev_tags = self.prev_tags[:-index] #slicing to remove tags starting from 'index'.
                        self.tagcount -= index
                        self.prev_attrs = self.prev_attrs[:-index] #slicing to remove corresponding attrs.
                        break

    def parseurl(self, url, source):
        """Parsers url, extracts html content from it, and feeds it to HTMLParser"""

        self.baseUrl = url #store in instance variables
        self.source = source
        response = urlopen(url) #Opens the url and returns web content present in it.
        #print(response.getheader("Content-Type"))
        htmlstring = response.read().decode('utf-8') #Decode the html content
        #print(htmlstring)
        try:
            print("Visiting... ", self.baseUrl)
            self.feed(htmlstring) #feeds the html string to the HTMLParser which triggers 'handle' methods one by one (as per the tags and data).

            # While parsing, somewhere along the way, the parser has to raise 'DataParsedException' to let us know that Required data has been extracted successfully.
            # If exception not raised, then something went wrong, as it lets us know that the data has been parsed.
            print("Failed. Something went wrong.\n")
        except DataParsedException as excp:
            #If exception raised, the data has parsed successfully.
            print("Success...")
            return
        finally:
            #Reset the parser.
            response = None
            self.reset()
            self.reset_var()

    def reset_var(self):
        """Resets all the variables"""
        self.newscount = 0
        self.prev_tags = []
        self.prev_attrs = []
        self.tagcount = 0

    def write_to_file(self, filename):
        """Writes the extracted headlines present in 'self.content' to file. """
        fh = open("files/headlines/"+filename, 'a')
        fh.write(self.content)
        fh.close()

    def reset_content(self):
        """Resets 'self.content' variable"""
        self.content = ""
