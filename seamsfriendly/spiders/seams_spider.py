import scrapy
#from ..items import SeamsfriendlyItem

class SeamsSpider(scrapy.Spider):
    name = 'seams'
    start_urls = [
        'https://in.seamsfriendly.com/collections/shorts'
        ]

    def parse(self, response):

        #items = SeamsfriendlyItem()


        #all_div_shorts = response.css('div.Grid__Cell 1/2--phone 1/2--tablet-and-up 1/3--desk')
        title : response.css("#shopify-section-collection-template a::text").extract()
        price : response.css(".Price::text").extract()
        url : response.css("img::attr(data-src)").extract()

        #items['title'] = title
        #items['url'] = url

        yield {
            'title' : title,
            'price' : price,
            'url' : url
        }
