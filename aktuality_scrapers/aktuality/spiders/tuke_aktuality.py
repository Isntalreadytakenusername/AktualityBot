import scrapy


class TukeAktualitySpider(scrapy.Spider):
    name = 'tuke_aktuality'
    allowed_domains = ['www.tuke.sk']
    start_urls = ['http://www.tuke.sk/']

    def parse(self, response):
        pass
