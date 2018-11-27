from NewsParser import *
import re
from urllib import parse


class NewsParser_NBC(NewsParser):
    """Custom Parser for 'NBC' news website. Inherits 'NewsParser' class."""

    # All the methods in here are similar to 'NewsParser_CNN' class methods. Hence, limiting the comments.
    def handle_data(self, data):
        if "body" in self.prev_tags:
            if self.tagcount < 3:
                return
            if self.source == "nbc":
                self.getheadlines(data)
            elif self.source == "nbc-politics":
                self.getheadlines(data)
            elif self.source == "nbc-business":
                self.getheadlines(data)
            elif self.source == "nbc-world":
                self.getheadlines(data)

    def getheadlines(self, data):
        if self.tagcount > 1 and self.prev_tags[-1] == "span" and self.prev_tags[-2] == "a":
            span_class = str(dict(self.prev_attrs[-1]).get("class"))
            if not span_class.startswith("headline"):
                return
            # print(data)
            attr_dict = dict(self.prev_attrs[-2])
            if "/video/" in str(attr_dict.get('href')):
                return
            self.content += data + "; nbc; "
            artcl_url = parse.urljoin(self.baseUrl, attr_dict.get('href'))
            artcl_flnm = "nbc_" + str(self.filename_counter) + ".txt"
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
        content1 = re.findall(r'<p class="">(.*?)</p>', htmlstring)
        #print(content1)
        for i in range(len(content1)):
            article_content += str(content1[i]) + "\n"
            if i==2:
                break
        p = re.compile('<(.*?)>')
        article_content = p.sub("", article_content)
        #print(article_content)
        fh = open("files/news_articles/nbc/" + filename, 'w')
        fh.write(article_content)
        fh.close()
        return

    def exec_articles(self):
        for i in range(0, len(self.article_urls)):
            url = self.article_urls[i]
            filename = self.article_filenames[i]
            self.get_article_data(url, filename)
        self.article_urls = []
        self.article_filenames=[]

    def execute(self):
        self.parseurl("https://www.nbcnews.com/us-news", "nbc")
        self.write_to_file("headlines.txt")
        self.reset_content()
        self.parseurl("https://www.nbcnews.com/politics", "nbc-politics")
        self.write_to_file("headlines_politics.txt")
        self.reset_content()
        self.parseurl("https://www.nbcnews.com/business", "nbc-business")
        self.write_to_file("headlines_business.txt")
        self.reset_content()
        self.parseurl("https://www.nbcnews.com/world", "nbc-world")
        self.write_to_file("headlines_world.txt")
        self.reset_content()

        self.exec_articles()