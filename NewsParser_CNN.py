from NewsParser import *
import re
from urllib import parse


class NewsParser_CNN(NewsParser):
    """Custom Parser for 'CNN' news website. Inherits 'NewsParser' class."""

    def handle_data(self, data):
        """Triggered when encountering data, while parsing the html content.
            'data': data present inside html tags. e.g. <div><a>data</a></div>"""
        if "body" in self.prev_tags: #Only interested in data present inside <body> tags.
            # i.e., 'body' should be one of the 'prev_tags'.
            if self.tagcount < 3: #Based on observation, 'headlines' data will be inside atleast 3 tags.
                return #if has less than 3 tags, return, as we are not interested in this data.

            #In 'CNN' website, different sections('politics', 'business', etc. ) have different html data formats. Hence, we will have source values accordingly.
            #Redirecting 'data' to different methods according to the source value.
            if self.source == "cnn":
                self.getheadlines(data)
            elif self.source == "cnn-politics":
                self.getheadlines_politics(data)
            elif self.source == "cnn-entertainment":
                self.getheadlines_entertainment(data)
            elif self.source == "cnn-business":
                self.getheadlines(data)
            elif self.source == "cnn-world":
                self.getheadlines(data)

    def getheadlines(self, data):
        """Extracts headlines from data and stores in 'self.content'"""

        #Based on observation, headlines data is present inside span, a, h3 tags for this 'CNN' site. i.e., in this format '<h3 ...><a ...><span ...> data </span></a></h3>'
        #Hence, matching the specific tags. If matched, proceed furthur.
        if self.tagcount>2 and self.prev_tags[-1] == "span" and self.prev_tags[-2] == "a" and self.prev_tags[-3]=="h3":
            span_class = dict(self.prev_attrs[-1]).get("class") #get the attributes dictionary for <span> tag.
            if span_class!="cd__headline-text": #check for class attribute in <span> tag.
                return
            #print(data)
            self.content += data + "; cnn; " #Here, 'data' has one news headline. adding, 'cnn' as source at the end.
            attr_dict = dict(self.prev_attrs[-2]) #get the attributes dictionary for <a> tag.
            artcl_url = parse.urljoin(self.baseUrl, attr_dict.get('href')) #get the url for the news headline using 'href' attribute in <a> tag and joining it with website's base url.
            artcl_flnm = "cnn_" + str(self.filename_counter) + ".txt" #generate a filename that stores the paragraph content of the current headline.
            self.content += artcl_url + "; " #add the above url and filename to the content
            self.content += artcl_flnm
            self.content += "\n" #newline to be able to store next headline in a newline.

            self.newscount += 1 #update the news counter.
            self.filename_counter += 1 #update the filenames counter
            self.article_urls.append(artcl_url) #store the above article url and filename in the instance variables.
            self.article_filenames.append(artcl_flnm)
            if self.newscount > self.maxcount-1: #When the count headlines reach specified max value, stop the parser exec. by raising 'DataParsedException.'
                raise DataParsedException(data)

    def getheadlines_politics(self, data):
        """Extracts headlines from data for 'politics' url and stores in 'self.content'"""
        # Based on observation, headlines data is present inside script, body, html tags for this 'CNN' site. i.e., in this format '<html ...><body ...><script ...> data </script></body></html>'
        # Hence, matching the specific tags. If matched, proceed furthur.
        if self.tagcount>2 and self.prev_tags[-1] == "script" and self.prev_tags[-2] == "body" and self.prev_tags[-3]=="html":
            if '"articleList":' in data: #Here, data in a script format with a different format from usual. It has "articleList": in it.
                #The url and headline are in two (key,value) pairs like ("uri", "...") and ("headline", "..."). So, extracting them using regex pattern matching and 're'.
                urls = re.findall(r'{"uri":"(.*?)","headline"', data)
                #print(urls)
                headlines = re.findall(r'","headline":"(.*?)","thumbnail":', data)
                for i in range(0, self.maxcount): #Looping through the headlines extracted above and storing them in 'self.content'
                    self.content += headlines[i] + "; cnn; " #Adding source 'cnn'
                    artcl_url = parse.urljoin(self.baseUrl, urls[i]) #Get 'url'
                    artcl_flnm = "cnn_" + str(self.filename_counter) + ".txt" #Get filename to store article paragraph content.
                    self.content += artcl_url + "; " #Adding article 'url' and 'filename'
                    self.content += artcl_flnm
                    self.content += "\n"

                    self.filename_counter += 1 #Updating filenames counter
                    self.article_urls.append(artcl_url) #Adding article url and filename to instance vars.
                    self.article_filenames.append(artcl_flnm)
                raise DataParsedException("") #Raise exception to stop parsing the current html page.
        return

    def getheadlines_entertainment(self, data):
        """Extracts headlines from data for 'entertainment' url and stores in 'self.content'"""
        # Based on observation, headlines data is present inside span, a, h3 tags for this 'CNN' site. i.e., in this format '<h3 ...><a ...><span ...> data </span></a></h3>'
        # Hence, matching the specific tags. If matched, proceed furthur.
        if self.tagcount>2 and self.prev_tags[-1] == "span" and self.prev_tags[-2] == "a" and self.prev_tags[-3]=="h3":
            span_class = dict(self.prev_attrs[-1]).get("class") #get the attributes dictionary for <span> tag.
            if span_class!="cd__headline-text":#check for class attribute in <span> tag.
                return
            #print(data)
            self.content += data + "; cnn; " #Here, 'data' has one news headline. adding, 'cnn' as source at the end.
            attr_dict = dict(self.prev_attrs[-2]) #get the attributes dictionary for <a> tag.
            artcl_url = parse.urljoin(self.baseUrl, attr_dict.get('href')) #get the url for the news headline using 'href' attribute in <a> tag and joining it with website's base url.
            artcl_flnm = "cnn_" + str(self.filename_counter) + ".txt" #generate a filename that stores the paragraph content of the current headline.
            self.content += artcl_url + "; " #add the above url and filename to the content
            self.content += artcl_flnm
            self.content += "\n" #newline to be able to store next headline in a newline.

            self.newscount += 1 #update the news counter.
            self.filename_counter += 1 #update the filenames counter
            self.article_urls.append(artcl_url) #store the above article url and filename in the instance variables.
            self.article_filenames.append(artcl_flnm)
            if self.newscount > self.maxcount+5: #When the count headlines reach specified max value +5, stop the parser exec. by raising 'DataParsedException.'
                raise DataParsedException(data)

    def get_article_data(self, url, filename):
        """Extracts article paragraph data by parsing the url and writes to given filename"""
        article_content = ""
        response = urlopen(url) #Open url and get html response from it.
        htmlstring = response.read().decode('utf-8') #read and decode html content from response
        if "/videos/" not in url: #Handles the html data depending on whether it is a video or an article.
            #If normal article, use pattern matching to match the data accordingly as below to retrieve paragraphs from the html data.
            content1 = re.findall(r'<p class="zn-body__paragraph speakable">(.*?)</p>', htmlstring) #pattern matching for the first paragraph.
            if len(content1) >0: #if successful in matching, remove <cite> tags from the content(, if they exist.)
                if "</cite>" in content1[0]:
                    article_content +=  str(content1[0]).split('</cite>')[1] + "\n"
                else:
                    article_content += str(content1[0]) + "\n" #adding newline to allow next paragraph to start from a newline.
            content1 = re.findall(r'<div class="zn-body__paragraph speakable">(.*?)</div>', htmlstring) #pattern matching for next paragraphs.
            if len(content1) > 0:
                article_content += str(content1[0]) + "\n"
        else: #If dealing with video content page.
            content1 = re.findall(r'class="media__video-description media__video-description--inline">(.*?)</div>',
                                  htmlstring) #pattern matching for retrieving first paragraph. Here, there is only one paragraph for video based articles.
            if len(content1) > 0:
                article_content += str(content1[0]) + "\n" #adding the paragraph to variable.
        p = re.compile('<(.*?)>') #matching any tags present in the article paragraphs content.
        article_content = p.sub("", article_content) #removing any tags present, by replacing them with empty string.
        #print(article_content)
        fh = open("files/news_articles/cnn/"+filename, 'w')
        fh.write(article_content) #writing the paragraphs to the given file.
        fh.close()
        return

    def exec_articles(self):
        """Loops through all the saved article urls and calls 'get_article_data' method to retrieve paragraph content for each url."""
        print("Extracting articles content...")
        for i in range(0, len(self.article_urls)):
            url = self.article_urls[i]
            filename = self.article_filenames[i]
            self.get_article_data(url, filename) #method call
        self.article_urls = [] #reset vars.
        self.article_filenames=[]
        print("Success...\n")

    def execute(self):
        """Main method for this class. Visits different cnn website urls by calling class methods."""
        self.parseurl("https://www.cnn.com/us", "cnn")
        self.write_to_file("headlines.txt") #saving the content retrieved from 'parseurl' call above to a file.
        self.reset_content() #Resetting class content for next operation.
        self.parseurl("https://www.cnn.com/politics", "cnn-politics")
        self.write_to_file("headlines_politics.txt")
        self.reset_content()
        self.parseurl("https://www.cnn.com/entertainment", "cnn-entertainment")
        self.write_to_file("headlines_entertainment.txt")
        self.reset_content()
        self.parseurl("https://www.cnn.com/business", "cnn-business")
        self.write_to_file("headlines_business.txt")
        self.reset_content()
        self.parseurl("https://www.cnn.com/world", "cnn-world")
        self.write_to_file("headlines_world.txt")
        self.reset_content()
        #After getting all headlines, extract all the article's paragraph content by calling 'exec_articles' method.
        self.exec_articles()
