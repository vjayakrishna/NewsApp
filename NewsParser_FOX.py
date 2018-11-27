from NewsParser import *
import re
from urllib import parse


class NewsParser_FOX(NewsParser):
    """Custom Parser for 'Fox news' website. Inherits 'NewsParser' class."""
    #All the methods in here are similar to 'NewsParser_CNN' class methods. Hence, limiting the comments.
    def handle_data(self, data):
        if "body" in self.prev_tags:
            if self.tagcount < 3:
                return
            if self.source == "fox":
                self.getheadlines(data)
            elif self.source == "fox-politics":
                self.getheadlines(data)
            elif self.source == "fox-business":
                self.getheadlines_business(data)
            elif self.source == "fox-world":
                self.getheadlines(data)
            elif self.source == "fox-entertainment":
                self.getheadlines(data)

    def getheadlines(self, data):
        if self.tagcount > 7 and self.prev_tags[-1] == "a" and self.prev_tags[-2] == "h4" and self.prev_tags[-7]=="section":
            section_class = str(dict(self.prev_attrs[-7]).get("class"))
            if not section_class.startswith("collection collection-article-list"):
                return
            h4_class = str(dict(self.prev_attrs[-2]).get("class"))
            if h4_class != "title":
                return
            attr_dict = dict(self.prev_attrs[-1])
            if "/v/" in str(attr_dict.get('href')):
                return
            #print(data)
            self.content += data + "; fox; "
            artcl_url = parse.urljoin(self.baseUrl, attr_dict.get('href'))
            artcl_flnm = "fox_" + str(self.filename_counter) + ".txt"
            self.content += artcl_url + "; "
            self.content += artcl_flnm
            self.content += "\n"

            self.newscount += 1
            self.filename_counter += 1
            self.article_urls.append(artcl_url)
            self.article_filenames.append(artcl_flnm)
            if self.newscount > self.maxcount-1:
                raise DataParsedException(data)
        return

    def getheadlines_business(self, data):
        if self.tagcount > 1 and self.prev_tags[-1] == "a" and self.prev_tags[-2] == "h3":
            attr_dict = dict(self.prev_attrs[-1])
            if "/v/" in str(attr_dict.get('href')):
                return
            #print(data)
            self.content += data + "; fox; "
            artcl_url = parse.urljoin(self.baseUrl, attr_dict.get('href'))
            artcl_flnm = "fox_" + str(self.filename_counter) + ".txt"
            self.content += artcl_url + "; "
            self.content += artcl_flnm
            self.content += "\n"

            self.newscount += 1
            self.filename_counter += 1
            self.article_urls.append(artcl_url)
            self.article_filenames.append(artcl_flnm)
            if self.newscount > self.maxcount-1:
                raise DataParsedException(data)
        return

    def get_article_data(self, url, filename):
        article_content = ""
        response = urlopen(url)
        htmlstring = response.read().decode('utf-8')
        content1 = re.findall(r'<p class="speakable">(.*?)</p>', htmlstring)
        content2 = re.findall(r'<p>(.*?)</p>', htmlstring)
        content1.extend(content2)
        #print(content1)
        for i in range(len(content1)):
            article_content += str(content1[i]) + "\n"
            if i==2:
                break
        p = re.compile('<(.*?)>')
        article_content = p.sub("", article_content)
        p = re.compile('&apos;')
        article_content = p.sub("\'", article_content)
        p = re.compile('&#xA0;')
        article_content = p.sub(" ", article_content)
        p = re.compile('&quot;')
        article_content = p.sub("\"", article_content)
        #article_content.replace('&apos;', "")
        #print(article_content)
        fh = open("files/news_articles/fox/" + filename, 'w')
        fh.write(article_content)
        fh.close()
        return

    def exec_articles(self):
        print("Extracting articles content...")
        for i in range(0, len(self.article_urls)):
            url = self.article_urls[i]
            filename = self.article_filenames[i]
            self.get_article_data(url, filename)
        self.article_urls = []
        self.article_filenames=[]
        print("Success...\n")

    def execute(self):
        self.parseurl("https://www.foxnews.com/us", "fox")
        self.write_to_file("headlines.txt")
        self.reset_content()
        self.parseurl("https://www.foxnews.com/politics", "fox-politics")
        self.write_to_file("headlines_politics.txt")
        self.reset_content()
        self.parseurl("https://www.foxbusiness.com", "fox-business")
        self.write_to_file("headlines_business.txt")
        self.reset_content()
        self.parseurl("https://www.foxnews.com/world", "fox-world")
        self.write_to_file("headlines_world.txt")
        self.reset_content()
        self.parseurl("https://www.foxnews.com/entertainment", "fox-entertainment")
        self.write_to_file("headlines_entertainment.txt")
        self.reset_content()

        self.exec_articles()