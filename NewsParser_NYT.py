from NewsParser import *
import re
from urllib import parse


class NewsParser_NYT(NewsParser):
    """Custom Parser for 'NYtimes' news website. Inherits 'NewsParser' class."""

    # All the methods in here are similar to 'NewsParser_CNN' class methods. Hence, limiting the comments.
    def handle_data(self, data):
        if "body" in self.prev_tags:
            if self.tagcount < 3:
                return
            if self.source == "nytimes":
                self.getheadlines(data)
            elif self.source == "nytimes-politics":
                self.getheadlines(data)
            elif self.source == "nytimes-business":
                self.getheadlines(data)
            elif self.source == "nytimes-world":
                self.getheadlines_world(data)

    def getheadlines(self, data):
        if self.tagcount>1 and self.prev_tags[-1] == "a" and self.prev_tags[-2] == "h2":
            #print(data)
            attr_dict = dict(self.prev_attrs[-1])
            self.extract_content(data, attr_dict)
        elif self.tagcount>1 and self.prev_tags[-1] == "h2" and self.prev_tags[-2] == "a":
            # print(data)
            attr_dict = dict(self.prev_attrs[-2])
            self.extract_content(data, attr_dict)
        return

    def getheadlines_world(self, data):
        if self.tagcount>1 and self.prev_tags[-1] == "a" and self.prev_tags[-2] == "h2":
            h2_class = dict(self.prev_attrs[-2]).get("class")
            if h2_class != "headline":
                return
            #print(data)
            attr_dict = dict(self.prev_attrs[-1])
            self.extract_content(data, attr_dict)
        return

    def extract_content(self, data, attr_dict):
        """Has common execution content for all 'get_headlines" methods."""
        self.content += data + "; nytimes; "
        # print(attr_dict)
        artcl_url = parse.urljoin(self.baseUrl, attr_dict.get('href'))
        artcl_flnm = "nytimes_" + str(self.filename_counter) + ".txt"
        self.content += artcl_url + "; "
        self.content += artcl_flnm
        self.content += "\n"

        self.newscount += 1
        self.filename_counter += 1
        self.article_urls.append(artcl_url)
        self.article_filenames.append(artcl_flnm)
        if self.newscount > self.maxcount - 1:
            raise DataParsedException(data)
        return

    def get_article_data(self, url, filename):
        article_content = ""
        response = urlopen(url)
        htmlstring = response.read().decode('utf-8')

        content1 = re.findall(r'<p class="css-1ebnwsw e2kc3sl0">(.*?)</p>', htmlstring)
        for i in range(len(content1)):
            article_content += str(content1[i]) + "\n"
            if i==2:
                break
        p = re.compile('<(.*?)>')
        article_content = p.sub("", article_content)
        #print(article_content)
        fh = open("files/news_articles/nytimes/" + filename, 'w')
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
        self.parseurl("https://www.nytimes.com/section/us", "nytimes")
        self.write_to_file("headlines.txt")
        self.reset_content()
        self.parseurl("https://www.nytimes.com/section/politics", "nytimes-politics")
        self.write_to_file("headlines_politics.txt")
        self.reset_content()
        self.parseurl("https://www.nytimes.com/section/business", "nytimes-business")
        self.write_to_file("headlines_business.txt")
        self.reset_content()
        self.parseurl("https://www.nytimes.com/section/world", "nytimes-world")
        self.write_to_file("headlines_world.txt")
        self.reset_content()
        self.exec_articles()
