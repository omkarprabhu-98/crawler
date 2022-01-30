from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item, Field
from scrapy.exceptions import CloseSpider
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import json
import sqlite3

class MySpider(CrawlSpider):
    name = "test-crawler"
    max_links = 20
    target_domains = ["gatech.edu"] # list of domains that will be allowed to be crawled
    start_urls = ["https://cc.gatech.edu/"] # list of starting urls for the crawler
    handle_httpstatus_list = [404,410,301,500] # only 200 by default. you can add more status to list
    linkExtractor = LinkExtractor( allow_domains=target_domains, deny=('patterToBeExcluded'), unique=('Yes'))
    rules = [
        Rule(
            linkExtractor, 
            callback='parse_my_url', # method that will be called for each request
            follow=True),
        # crawl external links but don't follow them
        Rule(
            linkExtractor,
            callback='parse_my_url',
            follow=False)
    ]

    def __init__(self, *a, **kw):
        super(MySpider, self).__init__(*a, **kw)
        self.con = sqlite3.connect('crawl.db')
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS keywords
                    (url text, keywords text)''')
        self.con.commit()

    def parse_my_url(self, response):
        self.crawler.stats.inc_value('visited', 1)
        self.crawler.stats.inc_value('to_visit', len(self.linkExtractor.extract_links(response)))

        # get text from the page body
        soup = BeautifulSoup(response.body)
        res_list = [p.get_text().strip() for p in soup.find_all('p')]
        # tokenize into list
        res = list(map(str.split, res_list))
        # remove stop words
        filtered_words = [word for word in res if word not in stopwords.words('english')]
        self.crawler.stats.inc_value('keywords', len(filtered_words))

        cur = self.con.cursor()
        cur.execute("INSERT INTO keywords VALUES (?, ?)", (response.request.url, json.dumps(filtered_words)))
        self.con.commit()

        if self.crawler.stats.get_value('visited') > self.max_links:
            # save some stats to file for plotting
            # details = dict({'visited': self.crawler.stats.get_value('visited'), 
            #     'to_visit': self.crawler.stats.get_value('to_visit'),
            #     'keywords': self.crawler.stats.get_value('keywords'),
            #     'elapsed_time_seconds': self.crawler.stats.get_value('elapsed_time_seconds'),
            #     'downloader/response_bytes': self.crawler.stats.get_value('downloader/response_bytes')})
            # with open('data_{0}.json'.format(self.max_links), 'w') as convert_file:
            #     convert_file.write(json.dumps(details))
            raise CloseSpider("Sufficient urls visited")
