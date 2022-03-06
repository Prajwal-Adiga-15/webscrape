import scrapy
#from items import GfgItem

class QuotesSpider(scrapy.Spider):
    name = "webscrape"
    def start_requests(self):
        urls = ['https://in.seamsfriendly.com/collections/shorts']
        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)
    
    def parse(self, response):
                title: response.css("#shopify-section-collection-template a::text").extract()
                price: response.css("#shopify-section-collection-template .Text--subdued::text").extract()
                img_url: response.css(".ProductItem__Image lazyautosizes Image--lazyLoaded::text").extract()


