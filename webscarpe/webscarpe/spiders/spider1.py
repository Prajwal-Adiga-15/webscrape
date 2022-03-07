import scrapy
#from items import GfgItem


class QuotesSpider(scrapy.Spider):
    name = "webscrape"
    #def start_requests(self):
    start_urls = ['https://in.seamsfriendly.com/collections/shorts']
        #for url in urls:
            #yield scrapy.Request(url = url, callback=self.parse)
    
    def parse(self, response):
        title: response.css("#shopify-section-collection-template a::text").extract()
        price: response.css("#shopify-section-collection-template .Text--subdued::text").extract()
        img_url: response.css('img::attr(src)').extract()

        for item in zip(title,price,img_url):
            scrap_info = {
                'title' : item[0],
                'price' : item[1],
                'img_url' : item[2]
            }
            yield scrap_info

