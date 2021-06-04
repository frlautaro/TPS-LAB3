import scrapy

class QuoteSpider(scrapy.Spider):
    name='titulo'
    start_urls =[
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response, ):
        title=response.css('title').extract()
        yield {'titletext':title}
