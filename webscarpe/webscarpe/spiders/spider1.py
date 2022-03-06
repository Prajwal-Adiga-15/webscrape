import scrapy

class QuotesSpider(scrapy.Spider):
    name = "webscrape"
    start_urls = ['https://in.seamsfriendly.com/']
    
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'webscrape-%s.html'% page
        with open(filename, 'wb') as f:
            f.write(response.body)